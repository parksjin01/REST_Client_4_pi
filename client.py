import requests
import json

"""
Header
    - Mutable Header
        * Accept
        * Parameter         (Optional)
        * Accept-Encoding   (Optional)
        * Extra             (Optional)
        
    - Immutable Header
        * Host
        * User-Agent        (Optional)
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

class RestClient(requests.Request):
    def __init__(self):
        super(RestClient, self).__init__()
        self.headers = {}
        self.immutable_header_list = ["host", "user-agent", "access-token", "cache-control", "content-type",
                                      "content-length", "date"]

    def set_header(self, key, value):
        if key.lower() in self.immutable_header_list:
            print("[Warning] {} can't be setted with this funtion".format(key))
        else:
            try:
                self.headers[key]
                self.change_header(key, value)
            except:
                self.headers[key] = value

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

    # def add_header(self, key, value):
    #     self.header[key] = value
    #
    # def add_params(self, key, value):
    #     self.params[key] = value
    #
    # def add_cookies(self, key, value):
    #     self.cookies[key] = value
    #
    # def set_timeout(self, timeout):
    #     self.timeout = timeout
    #
    # def set_redirection_following(self, allowing):
    #     self.allow_redirection = allowing
    #
    # def set_json(self, json_data):
    #     self.json = json_data
    #
    # def base64(self, msg):
    #     return str(base64.urlsafe_b64encode(msg.encode("utf-8")), "utf-8")
    #
    # def send(self, url, method="GET"):
    #     ret = 0
    #
    #     try:
    #         if method.lower() == "get":
    #             self.response = requests.get(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
    #         elif method.lower() == "post":
    #             self.response = requests.post(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies, json=self.json)
    #         elif method.lower() == "delete":
    #             self.response = requests.delete(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
    #         elif method.lower() == "patch":
    #             self.response = requests.patch(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
    #         elif method.lower() == "put":
    #             self.response = requests.put(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
    #
    #         self.response.raise_for_status()
    #
    #     except requests.exceptions.Timeout:
    #         ret = 1
    #
    #     except requests.exceptions.HTTPError as err:
    #         print(err)
    #
    # def check_redirection(self):
    #     return len(self.response.history) > 1
    #
    # def get_redirection_list(self):
    #     return self.response.history
    #
    # def print_header(self):
    #     pprint.pprint(self.response.headers)
    #
    # def print_response(self):
    #     if "/json" in self.response.headers["Content-Type"]:
    #         pprint.pprint(self.response.json())
    #         return self.response.json()
    #     else:
    #         pprint.pprint(self.response.content)
    #         return self.response.content