import requests
import pprint
import base64

class Reqeust():
    def __init__(self):
        self.header = {"accept": "application/json",}
        self.params = {}
        self.json = {}
        self.cookies = {}
        self.timeout = 3
        self.allow_redirection = False


    def add_header(self, key, value):
        self.header[key] = value

    def add_params(self, key, value):
        self.params[key] = value

    def add_cookies(self, key, value):
        self.cookies[key] = value

    def set_timeout(self, timeout):
        self.timeout = timeout

    def set_redirection_following(self, allowing):
        self.allow_redirection = allowing

    def set_json(self, json_data):
        self.json = json_data

    def base64(self, msg):
        return str(base64.urlsafe_b64encode(msg.encode("utf-8")), "utf-8")

    def send(self, url, method="GET"):
        ret = 0

        try:
            if method.lower() == "get":
                self.response = requests.get(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
            elif method.lower() == "post":
                self.response = requests.post(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies, json=self.json)
            elif method.lower() == "delete":
                self.response = requests.delete(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
            elif method.lower() == "patch":
                self.response = requests.patch(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)
            elif method.lower() == "put":
                self.response = requests.put(url, headers=self.header, params=self.params, timeout=self.timeout, allow_redirects=self.allow_redirection, cookies=self.cookies)

            self.response.raise_for_status()

        except requests.exceptions.Timeout:
            ret = 1

        except requests.exceptions.HTTPError as err:
            print(err)

    def check_redirection(self):
        return len(self.response.history) > 1

    def get_redirection_list(self):
        return self.response.history

    def print_header(self):
        pprint.pprint(self.response.headers)

    def print_response(self):
        if "/json" in self.response.headers["Content-Type"]:
            pprint.pprint(self.response.json())
            return self.response.json()
        else:
            pprint.pprint(self.response.content)
            return self.response.content