from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from helper import (
    getUserFromSlackId,
    createNewObjective,
    createNewKeyResult
)

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


class NewObjectiveForm(FormAction):

    def name(self) -> Text:
        return "new_objective_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["objective_title"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "objective_title": [self.from_text()],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        (status, user) = getUserFromSlackId(tracker.sender_id)
        if status:
            (status, objective) = createNewObjective(
                tracker.get_slot("objective_title"),
                user['id']
            )
            if status:
                dispatcher.utter_template("utter_objective_created", tracker)
                # set selected okr for adding KRs
                return [
                    AllSlotsReset(),
                    SlotSet("selected_objective", objective)
                ]
        return unexpectedError(self, dispatcher, tracker)

    class ActionAskAddKeyResult(Action):
        def name(self) -> Text:
            return "action_ask_add_key_result"

        def run(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            objective = tracker.get_slot("selected_objective")
            if objective:  # if objective was set (successful creation)
                dispatcher.utter_template("utter_ask_add_key_result", tracker)
            return []

    class NewKeyResultForm(FormAction):

        def name(self) -> Text:
            return "new_key_result_form"

        @staticmethod
        def required_slots(tracker: Tracker) -> List[Text]:
            objective = tracker.get_slot("selected_objective")
            if objective:
                return ["kr_title", "kr_start_value", "kr_goal_value"]
            else:  # skip this form if objective is not set
                return []

        def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
            return {
                "kr_title": [self.from_text()],
                "kr_start_value": [self.from_text()],
                "kr_goal_value": [self.from_text()],
            }

        def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
            objective = tracker.get_slot("selected_objective")
            if objective:  # check if objective set otherwise skip
                (status, user) = getUserFromSlackId(tracker.sender_id)
                if status:
                    kr_title = tracker.get_slot("kr_title")
                    kr_start_value = tracker.get_slot("kr_start_value")
                    kr_goal_value = tracker.get_slot("kr_goal_value")
                    (status, kr) = createNewKeyResult(
                        kr_title, kr_start_value, kr_goal_value,
                        objective['id'], user['id']
                    )
                    if status:
                        dispatcher.utter_template("utter_key_result_created", tracker)
                        return [
                            AllSlotsReset(),
                        ]
                return unexpectedError(self, dispatcher, tracker)
            return []
