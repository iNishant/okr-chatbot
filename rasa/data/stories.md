## create objective path
* create_objective
  - new_objective_form
  - form{"name": "new_objective_form"}
  - form{"name": null}
  - action_ask_add_key_result
* affirm
  - new_key_result_form
  - form{"name": "new_key_result_form"}
  - form{"name": null}

## create key result path
* create_key_result
  - action_list_objectives
  - select_objective_form
  - form{"name": "select_objective_form"}
  - form{"name": null}
  - new_key_result_form
  - form{"name": "new_key_result_form"}
  - form{"name": null}


## list okrs path
* list_okrs
  - action_list_objectives


## delete objective path
* delete_objective
  - action_list_objectives
  - select_objective_form
  - form{"name": "select_objective_form"}
  - form{"name": null}
  - action_delete_objective


## chitchat path
* affirm OR deny
  - action_deactivate_form
  - form{"name": null}