import requests
from typing import Any

zones_header: [str] = ["ID", "Name", "Status", "Plan"]
records_header: [str] = ["ID", "Name", "Type", "Content", "Proxiable", "Proxied"]


class Record:
    id: str = None
    name: str = None
    type: str = None
    content: str = None
    proxiable: bool = None
    proxied: bool = None
    record: dict = None

    def __init__(self, record: dict) -> None:
        self.record = record
        self.id = dict_value(self.record, "id")
        self.name = dict_value(self.record, "name")
        self.type = dict_value(self.record, "type")
        self.content = dict_value(self.record, "content")
        self.proxiable = dict_value(self.record, "proxiable")
        self.proxied = dict_value(self.record, "proxied")

    def __str__(self) -> str:
        return "id: %s, name: %s, type: %s, content: %s, proxiable: %s, proxied: %s" % (
            self.id, self.name, self.type, self.content, self.proxiable, self.proxied
        )

    def row(self) -> []:
        return [self.id, self.name, self.type, self.content, self.proxiable, self.proxied]


class Zone:
    id: str = None
    name: str = None
    status: str = None
    plan: str = None
    zone: dict = None
    records: [Record] = None

    def __init__(self, zone: dict) -> None:
        self.zone = zone
        self.id = dict_value(self.zone, "id")
        self.name = dict_value(self.zone, "name")
        self.status = dict_value(self.zone, "status")
        self.plan = dict_value(self.zone, "plan.name")

    def __str__(self) -> str:
        return "id: %s, name: %s, status: %s, plan: %s" % (self.id, self.name, self.status, self.plan)

    def row(self) -> []:
        return [self.id, self.name, self.status, self.plan]


def zones(auth_token: str) -> [Zone]:
    collection = []

    for zone in send("zones", auth_token):
        collection.append(Zone(zone))

    return collection


def records(auth_token: str, zone: Zone) -> [Record]:
    collection = []

    for record in send("zones/%s/dns_records" % zone.id, auth_token):
        collection.append(Record(record))

    return collection


def send(request_uri: str, auth_token: str, page: int = 1) -> dict:
    try:
        response = requests.request(
            method="GET",
            url="https://api.cloudflare.com/client/v4/%s?page=%d&per_page=%d" % (request_uri, page, 10),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer %s" % auth_token
            }
        )

        # Check status code
        if response.status_code == 200:
            response_content = response.json()

            # Check if response body has required items
            if "result" in response_content and "result_info" in response_content and "success" in response_content:
                result = response_content["result"]
                result_info = response_content["result_info"]
                success = response_content["success"]

                # Success should be True
                if success:
                    final_result = result

                    # Build result recursively
                    if result_info["page"] < result_info["total_pages"]:
                        page += 1
                        final_result += send(request_uri, auth_token, page)

                    return final_result

        return {}
    except (requests.RequestException, requests.ConnectionError, requests.Timeout):
        return {}


def dict_value(dictionary: dict, variable: str) -> Any:
    response = dictionary
    steps: [str] = variable.split(".")

    for step in steps:
        if step in response:
            response = response[step]
        else:
            return None

    return response
