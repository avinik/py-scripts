import requests
import json
import random
import uuid
from typing import List
import string


sku_list = [
    {
        "sku_code": "Sku_1",
        "name": "Rohu",
        "grade": "A",
        "type": "Fresh",
        "species": None,
        "form": "frozen",
        "processing_level": "whole",
        "unit_of_measurement": "kg"
    },
    {
        "sku_code": "Sku_2",
        "name": "Katla",
        "grade": "B",
        "type": "Fresh",
        "species": None,
        "form": "frozen",
        "processing_level": "whole",
        "unit_of_measurement": "quantity"
    },
    {
        "sku_code": "Sku_3",
        "name": "Prawns",
        "grade": "A",
        "type": "Fresh",
        "species": None,
        "form": "frozen",
        "processing_level": "whole",
        "unit_of_measurement": "kg"
    },

    {
        "sku_code": "Sku_4",
        "name": "Salmon",
        "grade": "A",
        "type": "Fresh",
        "species": None,
        "form": "frozen",
        "processing_level": "whole",
        "unit_of_measurement": "kg"
    }
]


def random_str(length: int) -> str:
    """
    Generate random Alphanumeric String of given length
    :param length: required length of string
    :return: random alphanumeric string of given size
    """
    return "".join(
        [random.choice(string.ascii_letters + string.digits)
         for _ in range(length)]
    )


def populate_sku(sku_list):
    url = "http://cms.dev.captainfresh.in:80/api/skus"

    skus = []
    for sku in sku_list:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "skuCode": sku["sku_code"],
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": sku["name"],
            "grade": sku["grade"],
            "type": sku["type"],
            "species": sku["species"],
            "form": sku["form"],
            "processingLevel": sku["processing_level"],
            "unitOfMeasurement": sku["unit_of_measurement"],
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        skus.append(json_reponse)
    return skus


def populate_manaufacturing_order(order_list):
    url = "http://slash.dev.captainfresh.in:80/api/manufacturing-orders"
    print("here")

    mfg_orders = []
    for mfg_order in order_list:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "addressId": str(uuid.uuid1()),
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "facilityId": mfg_order['facility_id'],
            "skuId": mfg_order['sku_id'],
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id,
            "customerSegment": mfg_order.get('customer_segement'),
            "eta": mfg_order.get("eta"),
            "qty": mfg_order.get("qty")
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        mfg_orders.append(json_reponse)
        print(payload)
        print(json_reponse)

    return mfg_orders


def populate_facility(facility_names: List[str]):
    url = "http://fms.dev.captainfresh.in:80/api/facilities"

    facilities = {}
    for facility in facility_names:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "addressId": str(uuid.uuid1()),
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": facility,
            "type": "PROCESSING_UNIT",
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        facilities[json_reponse["id"]] = json_reponse["name"]

    return facilities


def populate_area(areas_to_add):
    url = "http://fms.dev.captainfresh.in:80/api/areas"
    areas = []
    for area in areas_to_add:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": area["name"],
            "facility": {
                "id": area["facility_id"]
            },
            "type": area["type"],
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        areas.append(json_reponse)

    return areas


def populate_workstation(workstation_to_add):
    url = "http://fms.dev.captainfresh.in:80/api/workstations"
    workstations = []
    for workstation in workstation_to_add:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": workstation["name"],
            "facilityId": workstation["facility_id"],
            "area": {
                "id": workstation["area_id"]
            },
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        workstations.append(json_reponse)

    return workstations


def populate_task(tasks_to_add):
    url = "http://tasker-service.dev.captainfresh.in:80/api/tasks"
    tasks = []
    for task in tasks_to_add:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "taskName": task["task_name"],
            "facilityId": task["facility_id"],
            "entityType": task["entity_type"],
            "entityId": task["entity_id"],
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id,
            "status": task["status"]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        tasks.append(json_reponse)
    return tasks


def populate_activity(activities_to_add):
    url = "http://central-workflow.dev.captainfresh.in:80/api/activities"
    activities = []
    for activity in activities_to_add:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": activity,
            "isManual": True,
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id,
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        activities.append(json_reponse)

    return activities


def populate_activity_workstation_mapping(activities_workstation_mapping_to_add):
    url = "http://fms.dev.captainfresh.in:80/api/activity-worksation-mappings"
    activity_workstation_mappings = []
    for mapping in activities_workstation_mapping_to_add:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "activityId": mapping["activity_id"],
            "workstation": {
                "id": mapping["workstation_id"]
            },
            "updatedAt": "2021-04-20T21:14:32.391Z",
            "updatedBy": creator_id,
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_reponse = response.json()
        activity_workstation_mappings.append(json_reponse)

    return activity_workstation_mappings


def main():

    # Populate Skus
    skus_populated = populate_sku(sku_list)

    print("here")

    # Populate facility
    facility_names = ["Banglore Bommasandra", "Manglore", "Banglore Rampura"]
    facilities = populate_facility(facility_names)
    # for facility in facilities.keys():
    #     print(facility)

    mfg_order_to_add = []
    for sku in skus_populated:
        for facility_id in facilities.keys():
            mfg_order = {
                "facility_id": facility_id,
                "sku_id": sku["id"],
                "customer_segment": "Prime",
                "eta": "2021-10-30T21:14:32.391Z",
                "qty": "10"
            }
            mfg_order_to_add.append(mfg_order)

    populate_manaufacturing_order(mfg_order_to_add)

    areas_to_add = []
    area_types = ["CLEANING_AREA", "CUTTING_AREA",
                  "INWARD_AREA", "STORAGE_AREA"]
    for facility_id in facilities.keys():
        for area_type in area_types:
            areas_to_add.append({
                "name": area_type + "_1",
                "facility_id": facility_id,
                "type": area_type
            })
    areas = populate_area(areas_to_add)

    # for area in areas:
    #     print(area)

    workstation_to_add = []
    for area in areas:
        for i in range(1, random.randint(1, 4)):
            workstation_to_add.append({
                "name": f"Workstation_{i}",
                "area_id": area["id"],
                "facility_id": area["facility"]["id"]
            })

    workstations = populate_workstation(workstation_to_add)
    # for workstation in workstations:
    #     print(workstation)

    tasks_to_add = []
    task_types = ["PICKING", "CLEANING", "CUTTING", "PACKING", "PRINTING"]
    task_statuses = ["PENDING", "STARTED", "ENDED", "CANCELLED", "ON_HOLD"]
    for workstation in workstations:
        for task_type in task_types:
            for task_status in task_statuses:
                tasks_to_add.append({
                    "facility_id": workstation["facilityId"],
                    "entity_type": "workstation",
                    "entity_id": workstation["id"],
                    "task_name": task_type,
                    "status": task_status,
                    "workflow_instance_id": random_str(8),
                    "etc": "2021-10-30T21:14:32.391Z",
                })
    for task in tasks_to_add:
        print(task)
    tasks = populate_task(tasks_to_add)
    # for task in tasks:
    #     print(task)

    activities_to_add = ["PICKING", "CUTTING",
                         "CUTTING", "PACKING", "PRINTING"]
    activities = populate_activity(activities_to_add)
    # for activity in activities:
    #     print(activity)

    activities_workstation_mapping_to_add = []
    for activity in activities:
        for workstation in workstations:
            activities_workstation_mapping_to_add.append({
                "activity_id": activity["id"],
                "workstation_id": workstation["id"]
            })

    activities_workstation_mappings = populate_activity_workstation_mapping(
        activities_workstation_mapping_to_add)

    # for mapping in activities_workstation_mappings:
    #     print(mapping)


if __name__ == "__main__":
    main()
