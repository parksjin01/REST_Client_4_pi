import client

request = client.Reqeust()
request.set_redirection_following(True)
# request.add_params("sm", "top_hty")
# request.add_params("fbm", "1")
# request.add_params("ie", "utf8")
# request.add_params("query", "google")
request.add_cookies("cookie", "c1")
request.add_cookies("cookie2", "c2")
request.add_header("Accept-Language", "ko-kr")
request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15")
request.add_header("Accept-Encoding", "br, gzip, deflate")
# request.add_header("Accept", "image/jpeg")
# request.send("https://httpbin.org/post", "post")
# request.send("https://httpbin.org/base64/{}".format(request.base64("Hello World")))
# request.send("https://httpbin.org/image")
request.send("http://192.9.82.22:8000/start/tester/0/1", "post")
# print(request.response.headers)
# print(request.response.content)
request.print_header()
response = request.print_response()
request.add_header("X-Auth-Token", response["token"])

for _ in range(5):
    request.send("http://192.9.82.22:8000/oncalls")
    # response = response.decode("utf-8")
    request.print_response()
    request.send("http://192.9.82.22:8000/action", "POST")
    command = {
        "commands": [
            {
                "elevator_id": 0,
                "command": "UP",
            }
        ]
    }
    request.set_json(command)
    request.print_response()
