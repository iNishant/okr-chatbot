from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset
from slackapi import getUserEmailFromUserID

# tracker.sender_id gives slack user's ID

class NewOKRForm(FormAction):

    def name(self) -> Text:
        return "new_okr_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["new_okr"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"new_okr": [self.from_text()],
		}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_template("utter_okr_created", tracker)
        return [AllSlotsReset()]
        

class UpdateOKRForm(FormAction):

    def name(self) -> Text:
        return "update_okr_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["select_okr_query", "updated_okr"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"select_okr_query": [self.from_text()],
            "updated_okr": [self.from_text()],
		}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_template("utter_okr_updated", tracker)
        return [AllSlotsReset()]

        
class DeleteOKRForm(FormAction):

    def name(self) -> Text:
        return "delete_okr_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["select_okr_query"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"select_okr_query": [self.from_text()],
		}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_template("utter_okr_deleted", tracker)
        return [AllSlotsReset()]
