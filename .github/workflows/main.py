# workflow_decider.py
import os

def determine_workflows():
    layers_changed = os.getenv("LAYER_CHANGED", "false") == "true"
    other_changed = os.getenv("OTHER_CHANGED", "false") == "true"

    if layers_changed and not other_changed:
        print("Trigger: light_client.yml → deploy.yml")
    elif not layers_changed and other_changed:
        print("Trigger: deploy.yml only")
    elif layers_changed and other_changed:
        print("Trigger: light_client.yml → deploy.yml")
    else:
        print("No relevant changes — do not trigger any workflow.")

if __name__ == "__main__":
    determine_workflows()
