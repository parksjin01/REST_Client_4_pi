import json
import client

def data_lab():
    with open("secret_key.json", "r") as f:
        key = json.load(f)

    url = "https://openapi.naver.com/v1/datalab/search"

    parameter = {
        "startDate": "2019-01-01",
        "endDate": "2019-06-30",
        "timeUnit": "date",
        "keywordGroups": [
            {
                "groupName": "날씨",
                "keywords": ["기온", "바람", "태풍"],
            }
        ],

        "ages": ["3", "4", "5", "6"]
    }

    request = client.Reqeust()

    request.add_header("Accept", "*/*")
    request.add_header("X-Naver-Client-Id", key["naver_client_id"])
    request.add_header("X-Naver-Client-Secret", key["naver_client_secret"])

    request.set_json(parameter)

    request.send(url, "POST")

    request.print_header()
    request.print_response()

if __name__ == '__main__':
    data_lab()