import requests
import json
import random
import uuid
from typing import List
import string

FMS_BASE_URL = "http://fms.dev.captainfresh.in:80/api"
CENTRAL_WORKFLOW_BASE_URL = "http://central-workflow.dev.captainfresh.in:80/api"


def main():

    workflows = requests.get(CENTRAL_WORKFLOW_BASE_URL + "/workflows").json()
    activities = requests.get(CENTRAL_WORKFLOW_BASE_URL + "/activities").json()

    creator_id = str(uuid.uuid1())

    for workflow in workflows:
        level = 0
        for activity in activities:
            level += 1
            url = CENTRAL_WORKFLOW_BASE_URL + "/workflow-activity-mappings"
            activity_workflow_mapping = json.dumps({
                "workflow": workflow,
                "activity": activity,
                "level": str(level),
                "createdAt": "2021-07-26T01:17:24.648Z",
                "createdBy": creator_id,
                "updatedAt": "2021-04-20T21:14:32.391Z",
                "updatedBy": creator_id,
            }
            )
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(
                url, headers=headers, data=activity_workflow_mapping)

            print(response.json())

    workstations = requests.get(FMS_BASE_URL + "/workstations").json()
    for workstation in workstations:
        for activity in activities:
            url = FMS_BASE_URL + "/activity-workstation-mappings"
            activity_workstation_mapping = json.dumps({
                "workstation": workstation,
                "activityId": activity.get("id"),
                "createdAt": "2021-07-26T01:17:24.648Z",
                "createdBy": creator_id,
                "updatedAt": "2021-04-20T21:14:32.391Z",
                "updatedBy": creator_id,
            })
            print("\n")
            print(activity_workstation_mapping)
            print()
            headers = {
                'Content-Type': 'application/json'
            }
            # response = requests.post(
            #     url, headers=headers, data=activity_workstation_mapping)

            # print(response.json())


if __name__ == "__main__":
    main()
