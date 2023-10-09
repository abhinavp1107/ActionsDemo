Actions Test - Github Actions Tutorials

![workflow status](https://github.com/abhinavp1107/ActionsDemo/actions/workflows/blank.yml/badge.svg)


| Type | Description | URL |
| -------------         |-------------| -----|

| Python Code      |Start Trialforce Load.| [start_process.py](service/start_process.py)|
| Python Code      |Prepares Workspace.| [prepare_workspace.py](service/prepare_workspace.py)|
| Python Code      |Load service start metrics.| [load_start_metrics.py](service/load_start_metrics.py)|
| Python Code      |Load Temporary Table in everest DB.| [load_temp_table.py](service/load_temp_table.py)|
| Python Code      |Load main table in everest DB if source table has positive non-zero row count else old data persists.| [load_main_table.py](service/load_main_table.py)|
| Python Code      |Update metrics table if subtask succeeds.| [update_success.py](service/update_success.py)|
| Python Code      |Update metrics table if subtask fails.| [update_failure.py](service/update_failure.py)|
| Python Code      |Checks if any subtask failed inside the MapState.| [check_for_error.py](service/check_for_error.py)|
| Python Code      |Load dnu_trialforce_investigators table using dqs_studies, dnu_trialforce, sitetrove_Investigator tables.| [load_dnu_tf_investigators.py](service/load_dnu_tf_investigators.py)|
| Python Code      |Send notification to users on successful completion of the process.| [notify_success.py](service/notify_success.py)|
| Python Code      |Send notification to the users on failure of the process.| [notify_failure.py](service/notify_failure.py)|
