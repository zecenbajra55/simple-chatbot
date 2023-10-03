import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    knowledge = Path("data/account-number.txt").read_text().split("\n")

    def name(self) -> Text:
        return "utter_account_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'account_number':
                account_number = blob['value']
                if account_number in self.knowledge:
                    dispatcher.utter_message(text=f"Yes, {account_number} exists and has a balance of 1000")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {account_number}, are you sure it is correct")
        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/accounts.json")
        super().__init__(knowledge_base)