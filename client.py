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

class RestClient(requests.Request):
    def __init__(self):
        super(RestClient, self).__init__()
        self.headers = {"Cache-Control": "no-cache"}

    def set_headers(self, key, value):
        if key.lower() in ["host", "token", "user-agent", "agent", "cache-control"]:
            self.__set_immutable_headers(key, value)
        else:
            self.__set_mutable_headers(key, value)

    def set_headers_with_dict(self, dictionary):
        for key, value in dictionary.items():
            self.set_headers(key, value)

    def set_headers_with_json(self, json):
        json = json.loads(json)
        for key, value in json.items():
            self.set_headers(key, value)

    def read_header(self, config):
        with open(config, "r") as f:
            data = json.load(f)

        return data

    def change_header(self, key, value):
        if key.lower() not in ["host", "token", "user-agent", "agent", "cache-control"]:
            self.__set_mutable_headers(key, value)

    def change_header_with_dict(self, dictionary):
        for key, value in dictionary.items():
            self.change_header(key, value)
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