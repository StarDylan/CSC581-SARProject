from typing import TypedDict
from sar_project.knowledge.knowledge_base import KnowledgeBase
import os
import google.generativeai as genai
import dotenv


from sar_project.agents.base_agent import SARBaseAgent

dotenv.load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class ClueMessage(TypedDict):
    flag_clue: int
    get_clues: bool
    get_status: bool
    ask_human_query: str

    

from sar_project.agents.base_agent import SARBaseAgent
class ClueMeisterAgent(SARBaseAgent):
    def __init__(self,  kb: KnowledgeBase, name="clue_meister"):
        super().__init__(
            name=name,
            role="Clue Meister",
            system_message="""You are a clue meister for SAR operations. Your role is to:
            1. Sort clues by criteria
            2. Identify patterns in clue sets
            3. initiate further inquiries""",
            knowledge_base=kb
        )

    
    def process_request(self, message: ClueMessage):
        """Process clue-related requests

        Input:
        - message: dict containing one of the following keys:
            - flag_clue: int
            - get_clues: bool
            - get_status: bool
            - ask_human_query: str
        
        Output (All Optional):
        - clue_id: int
        - clue_text: str
        - response: str
        - error: str
        """
        try:
            # Example processing logic
            if "flag_clue" in message:
                assert "flag_clue" in message
                assert isinstance(message["flag_clue"], int)

                self.kb.add_clue_tag(message["flag_clue"], "ai_flagged")
                return {"clue_id": message["flag_clue"]}

            elif "get_clues" in message:
                return self.clues_to_text()
            
            elif "get_status" in message:
                return self.get_status()
            
            elif "ask_human_query" in message:
                self.kb.add_query(message["ask_human_query"])
                return {"response": "Added Query"}

            else:
                return {"error": "Unknown request type"}
        except Exception as e:
            return {"error": str(e)}
    
    def extract_clue(self, raw_text: str):
        """Extract clue from text"""
        
        prompt = f"""You are a clue meister for SAR operations. Your role is to extract clues from the text below.
        
        Please surround your proposed clue with the tags <clue> and </clue>.
        
        {raw_text}"""

        response = genai.text_generation(prompt)

        after_first_tag = response.split("<clue>")[1]
        before_second_tag = after_first_tag.split("</clue>")[0]

        return {"clue_text": before_second_tag}
    

    def flag_clues(self):
        
        clues = self.clues_to_text()

        clue_text = clues["clue_text"]

        prompt = f"""You are a clue meister for SAR operations. 
        
        Your role is to flag any clues that might be related to each other and require further investigation.

        You can flag a clue by providing the clue ID surrounded by exclaimation marks.

        For example: Clue !1! and !2! are related.

        {clue_text}"""

        response = genai.text_generation(prompt)

        if "!" not in response:
            return {"info": "Found nothing"}
        
    

        import re
        print(response)
        matches = re.findall(r"!(\d+)!", response)

        print(matches)
        for match in matches:
            self.kb.add_clue_tag(int(match), "ai_flagged")



        return {"info": f"Flagged {len(matches)} Clues"}

    
    def clues_to_text(self):
        """Convert clues to text"""
        clues = self.kb.get_clues()

        text = "Clues:\n"

        for (id, clue) in clues.items():
            if id in self.kb.clue_tags.get("ai_flagged", []):
                text += f"Clue ID #{id}: {clue} (Already Flagged)\n\n"
            else:
                text += f"Clue ID #{id}: {clue}\n\n"

        return {"clue_text": text}

    def update_status(self, status):
        """Update the agent's status"""
        self.status = status
        return {"status": "updated", "new_status": status}

    def get_status(self):
        """Get the agent's current status"""
        return getattr(self, "status", "unknown")
