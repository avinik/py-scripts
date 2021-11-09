import json
import uuid

import requests


def populate_work_order(work_orders_to_populate):
    url = "http://fms.dev.captainfresh.in:80/api/areas"
    work_orders = []
    for work_order in work_orders_to_populate:
        creator_id = str(uuid.uuid1())
        payload = json.dumps({
            "createdAt": "2021-07-26T01:17:24.648Z",
            "createdBy": creator_id,
            "name": work_order["name"],
            "facility": {
                "id": work_order["facility_id"]
            },
            "type": work_order["type"],
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
