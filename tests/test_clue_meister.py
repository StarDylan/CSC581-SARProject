import pytest
from sar_project.agents.clue_meister import ClueMeisterAgent
from sar_project.knowledge import KnowledgeBase

class TestClueMeisterAgent:
    @pytest.fixture
    def agent(self):
        self.kb = KnowledgeBase()

        self.kb.add_clue(1, "Test clue 1")
        self.kb.add_clue(2, "Test clue 2")

        return ClueMeisterAgent(self.kb)

    def test_initialization(self, agent):
        assert agent.name == "clue_meister"
        assert agent.role == "Clue Meister"
        assert agent.mission_status == "standby"

    def test_get_clues(self, agent):
        message = {
            "get_clues": True
        }
        response = agent.process_request(message)
        assert "clue_text" in response
        assert "Test clue 1" in response["clue_text"]
        assert "Test clue 2" in response["clue_text"]

    def test_flag_clue(self, agent):
        message = {
            "flag_clue": 1
        }
        response = agent.process_request(message)
        assert "clue_id" in response
        assert response["clue_id"] == 1

        message = {
            "get_clues": True
        }
        response = agent.process_request(message)
        assert "clue_text" in response
        assert "Test clue 1 (Already Flagged)" in response["clue_text"]

    def test_ask_human_query(self, agent):
        message = {
            "ask_human_query": "What does this clue mean?"
        }
        response = agent.process_request(message)
        assert "response" in response
        assert response["response"] == "Added Query"

        assert self.kb.query_queue == ["What does this clue mean?"]

    def test_status_update(self, agent):
        response = agent.update_status("active")
        assert response["new_status"] == "active"
        assert agent.get_status() == "active"

    def test_unknown_request(self, agent):
        message = {
            "random_message_that_is_invalid": True
        }
        response = agent.process_request(message)
        assert "error" in response