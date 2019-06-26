from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from slack_utils import getUserEmailFromUserID
from firebase_utils import createNewOKR, updateExistingOKR, deleteExistingOKR, listOKRs

# tracker.sender_id gives slack user's ID

def okrsListString(okrs):
    message = ''
    for i in range(len(okrs)):
        message += (str(i+1) + '. ' + okrs[i]['body'] + '\n')
    return message


def formSuccessful(self, dispatcher, tracker):
    return [AllSlotsReset()]


def unexpectedError(self, dispatcher, tracker):
    dispatcher.utter_template("utter_error_occurred", tracker)
    return [AllSlotsReset(), Restarted()]


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
        (status, userEmail) = getUserEmailFromUserID(tracker.sender_id)
        if status:
            okrBody = tracker.get_slot("new_okr")
            createNewOKR(okrBody, userEmail)
            dispatcher.utter_template("utter_okr_created", tracker)
            return formSuccessful(self, dispatcher, tracker)
        else:
            return unexpectedError(self, dispatcher, tracker)
        

class UpdateOKRForm(FormAction):

    def name(self) -> Text:
        return "update_okr_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["selected_okr", "updated_okr"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"selected_okr": [self.from_text()],
            "updated_okr": [self.from_text()],
		}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        (status, userEmail) = getUserEmailFromUserID(tracker.sender_id)
        if status:
            okrList = tracker.get_slot("okrs_list")
            okrSelectedIndex = None
            try:
                okrSelectedIndex = int(tracker.get_slot("selected_okr")) - 1
            except ValueError:
                return unexpectedError(self, dispatcher, tracker)
            okrId = okrList[okrSelectedIndex]['id']
            newOkrBody = tracker.get_slot("updated_okr")
            updateExistingOKR(okrId, newOkrBody, userEmail)
            dispatcher.utter_template("utter_okr_updated", tracker)
            return formSuccessful(self, dispatcher, tracker)
        else:
            return unexpectedError(self, dispatcher, tracker)

        
class DeleteOKRForm(FormAction):

    def name(self) -> Text:
        return "delete_okr_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["selected_okr"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"selected_okr": [self.from_text()],
		}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        (status, userEmail) = getUserEmailFromUserID(tracker.sender_id)
        if status:
            okrList = tracker.get_slot("okrs_list")
            okrSelectedIndex = None
            try:
                okrSelectedIndex = int(tracker.get_slot("selected_okr")) - 1
            except ValueError:
                return unexpectedError(self, dispatcher, tracker)
            okrId = okrList[okrSelectedIndex]['id']
            deleteExistingOKR(okrId, userEmail)
            dispatcher.utter_template("utter_okr_deleted", tracker)
            return formSuccessful(self, dispatcher, tracker)
        else:
            return unexpectedError(self, dispatcher, tracker)


class ListOKRs(Action):
    def name(self) -> Text:
        return "action_list_okrs"
    
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        (status, userEmail) = getUserEmailFromUserID(tracker.sender_id)
        if status:
            okrs = listOKRs(userEmail)
            nokrs = len(okrs)
            message = ''
            if nokrs:
                message = 'Here are your OKRs \n' + okrsListString(okrs)
            else:
                message = 'No OKRs found'
            dispatcher.utter_message(message)
            return formSuccessful(self, dispatcher, tracker)
        else:
            return unexpectedError(self, dispatcher, tracker)


class ListOKRsForSelection(Action):
    def name(self) -> Text:
        return "action_list_okrs_for_selection"
    
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        (status, userEmail) = getUserEmailFromUserID(tracker.sender_id)
        if status:
            okrs = listOKRs(userEmail)
            nokrs = len(okrs)
            if nokrs:
                dispatcher.utter_message('List of OKRs \n' + okrsListString(okrs))
                return [SlotSet('okrs_list', okrs)]
            else:
                dispatcher.utter_message('No OKRs found')
                return [Restarted()]
        else:
            return unexpectedError(self, dispatcher, tracker)