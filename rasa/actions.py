from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from helper import (
    getUserFromSlackId,
    createNewObjective,
    createNewKeyResult,
    listObjectives,
    deleteObjective
)

# tracker.sender_id gives slack user's ID


def unexpectedError(dispatcher, tracker, message=None):
    if message:
        dispatcher.utter_message(message)
    else:
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
                    SlotSet("selected_objective", objective['id'])
                ]
        return unexpectedError(dispatcher, tracker)


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
        else:  # reset conversation
            return unexpectedError(dispatcher, tracker)


class ActionListObjectives(Action):
    def name(self) -> Text:
        return "action_list_objectives"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        (status, user) = getUserFromSlackId(tracker.sender_id)
        if status:
            (status, objectives, string) = listObjectives(user['id'])
            if status:
                dispatcher.utter_message(string)
                return [
                    AllSlotsReset(), SlotSet('objectives_list', objectives)]
        return unexpectedError(dispatcher, tracker)


class SelectObjectiveForm(FormAction):

    def name(self) -> Text:
        return "select_objective_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        objectives_list = tracker.get_slot("objectives_list")
        if objectives_list:
            return ["selected_objective_number"]
        else:
            return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "selected_objective_number": [self.from_text()],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        objectives_list = tracker.get_slot("objectives_list")
        if objectives_list:
            number = tracker.get_slot("selected_objective_number")
            try:
                number = int(number)
                index = number - 1
                nObjectives = len(objectives_list)
                if index >= 0 and index < nObjectives:
                    objective = objectives_list[index]
                    return [
                        AllSlotsReset(),
                        SlotSet("selected_objective", objective['id'])
                    ]
            except ValueError:
                pass
        return unexpectedError(dispatcher, tracker, "Invalid choice")


class NewKeyResultForm(FormAction):

    def name(self) -> Text:
        return "new_key_result_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        objective = tracker.get_slot("selected_objective")
        if objective:
            return [
                "kr_title", "kr_start_value",
                "kr_goal_value"
            ]
        else:  # skip this form if objective is not selected
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
        selected_objective = tracker.get_slot("selected_objective")
        if selected_objective:  # check if objective set otherwise skip
            (status, user) = getUserFromSlackId(tracker.sender_id)
            if status:
                kr_title = tracker.get_slot("kr_title")
                kr_start_value = tracker.get_slot("kr_start_value")
                kr_goal_value = tracker.get_slot("kr_goal_value")
                (status, kr) = createNewKeyResult(
                    kr_title, kr_start_value, kr_goal_value,
                    selected_objective, user['id']
                )
                if status:
                    dispatcher.utter_template(
                        "utter_key_result_created", tracker)
                    return [
                        AllSlotsReset(),
                    ]
            return unexpectedError(dispatcher, tracker)
        return []


class ActionDeleteObjective(Action):
    def name(self) -> Text:
        return "action_delete_objective"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        selected_objective = tracker.get_slot("selected_objective")
        if selected_objective:  # check if objective set otherwise skip
            (status, user) = getUserFromSlackId(tracker.sender_id)
            if status:
                status = deleteObjective(selected_objective, user['id'])
                if status:
                    dispatcher.utter_template('utter_okr_deleted', tracker)
                    return [AllSlotsReset()]
        return unexpectedError(dispatcher, tracker)
