## create okr path
* create_okr
  - utter_enter_okr
  - action_listen <!-- add custom action after this to get user input -->
  - utter_okr_created
  - action_restart

## update okr path
* update_okr
  - utter_select_okr_for_updating
  - action_listen <!-- add custom action after this -->
  - utter_okr_updated
  - action_restart

## delete okr path
* delete_okr
  - utter_select_okr_for_deleting
  - action_listen <!-- add custom action after this -->
  - utter_okr_deleted
  - action_restart

## list okr path
* list_okr
  - utter_okr_listed
  - action_restart