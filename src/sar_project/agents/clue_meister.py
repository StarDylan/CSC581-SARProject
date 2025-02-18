from typing import TypedDict
from sar_project.knowledge.knowledge_base import KnowledgeBase

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
        """Process clue-related requests"""
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
