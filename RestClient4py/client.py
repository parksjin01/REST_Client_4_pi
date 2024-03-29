import requests
import json
import xml.etree.ElementTree as ElementTree

"""
Header
    - Mutable Header
        * Accept
        * Accept-Encoding   (Optional)
        * Extra             (Optional)
        
    - Immutable Header
        * Host
        * User-Agent        (Optional)
        * Parameter         (Optional)
        * Data              (Optional)
        * Access Token      (Optional & Auto Gen)
        * Cache-Control     (Optional & Auto Gen)
        * Content-Type      (Optional & Auto Gen)
        * Content-Length    (Optional & Auto Gen)
        * Date              (Optional & Auto Gen)
"""
ERROR_NAME = {
    "JSON_DECODE": 1
}

ERROR_CODE = {
    1: json.JSONDecodeError
}

def printJsonStructure(data, indent=0):

    if type(data) not in [list, dict]:
        return

    if type(data) == list:
        if len(data) > 0:
            printJsonStructure(data[0], indent)

    else:
        for k in data.keys():
            print(" |\t" * indent, k)
            printJsonStructure(data[k], indent + 1)

class RestClient(requests.Request):
    def __init__(self):
        super(RestClient, self).__init__()
        self.immutable_header_list = ["host", "user-agent", "access-token", "cache-control",
                                      "date", "parameter", "param", "params", "data"]
        self.session = requests.Session()
        self.response = None
        self.params = {}
        self.data = {}
        self.json = None
        self.session_send_kwargs = {"timeout": 3, "allow_redirects": True}

    def set_header(self, key, value):
        if key.lower() in self.immutable_header_list:
            print("[Warning] {} can't be setted with this funtion".format(key))
        else:
            self.headers[key] = value if type(value) == str else str(value)

    def set_headers_with_dict(self, dictionary):
        for key, value in dictionary.items():
            self.set_header(key, value)

    def set_headers_with_json(self, json_data):
        try:
            self.set_headers_with_dict(json.loads(json_data))
        except json.JSONDecodeError as e:
            print("[Warning] Your configuration file is not json or invalid json")
            return ERROR_NAME["JSON_DECODE"]

    def set_headers_with_file(self, filename):
        with open(filename, "r") as f:
            config = f.read()
            self.set_headers_with_json(config)

    def change_header(self, key, value):
        self.set_header(key, value)

    def change_header_with_dict(self, dictionary):
        self.set_headers_with_dict(dictionary)

    def change_header_with_json(self, json):
        self.set_headers_with_json(json)

    def clear_header(self, header_name):
        try:
            del self.headers[header_name]
        except:
            print("[ERROR] {} is not in header".format(header_name))

    def clear_all_header(self):
        self.headers = {}

    # Only for testing
    def get_header(self):
        return self.headers

    def set_timeout(self, limit=3):
        self.session_send_kwargs["timeout"] = limit

    def set_redirection(self, redirection_availability):
        self.session_send_kwargs["allow_redirects"] = redirection_availability

    def __parsing_from_json(self):
        return self.response.json()

    def __parsing_from_xml(self):
        return ElementTree.fromstring(self.response.text())

    def return_data(self):
        if self.response.status_code // 100 == 2:
            if "json" in self.response.headers["content-type"]:
                try:
                    return self.__parsing_from_json()
                except:
                    body = self.response.content
                    try:
                        return body.decode("utf-8")
                    except:
                        return body

            elif "xml" in self.response.headers["content-type"]:
                return self.__parsing_from_xml()

            else:
                body = self.response.content
                try:
                    return body.decode("utf-8")
                except:
                    return body

        else:
            self.response.raise_for_status()

    def get(self, url=None, params={}):
        self.method = "GET"
        self.url = url
        self.params = params
        self.response = self.session.send(self.prepare(), **self.session_send_kwargs)
        return self.return_data()

    def post(self, url="", data={}, json=""):
        self.method = "POST"
        self.url = url
        self.data = data
        self.json = json
        self.response = self.session.send(self.prepare(), **self.session_send_kwargs)
        return self.return_data()

    def put(self, url="", data={}, json=""):
        self.method = "PUT"
        self.url = url
        self.data = data
        self.json
        self.response = self.session.send(self.prepare(), **self.session_send_kwargs)
        return self.return_data()

    def patch(self, url="", data={}, json=""):
        self.method = "PATCH"
        self.url = url
        self.data = data
        self.json = json
        self.response = self.session.send(self.prepare(), **self.session_send_kwargs)
        return self.return_data()

    def delete(self, url="", data={}, json=""):
        self.method = "PATCH"
        self.url = url
        self.data = data
        self.json = json
        self.response = self.session.send(self.prepare(), **self.session_send_kwargs)
        return self.return_data()

    def __str__(self):
        template = """Method: {}\n""" + "-" * 72 + "\nHeaders\n\n{}\n" + "-" * 72 + "\nBody\n\n{}"
        header = ""
        header_template = "{}: {}\n"

        for k, v in self.headers.items():
            header += header_template.format(k, v)

        return template.format(self.method, header.strip("\n"), json.dumps(self.params) + "\n" + json.dumps(self.data) + "\n" + (self.json or ""))