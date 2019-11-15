import unittest
from RestClient4py.client import RestClient
import json
import random
import copy

class Header_Testcase(unittest.TestCase):

    def test_set_single_mutable_header(self):
        self.client = RestClient()

        header = [
            ("accept", "text/html"), ("accept_encoding", "br"), ("accept_encoding", "gzip"),
            ("gid", 1), ("uid", "test"), ("category", "amenity")
        ]

        for header_name, header_value in header:
            self.client.set_header(header_name, header_value)
            self.assertDictEqual(self.client.get_header(), {header_name: header_value})
            self.client.clear_header(header_name)
            self.assertDictEqual(self.client.get_header(), {})

    def test_set_single_immutable_header(self):
        self.client = RestClient()

        header = [
            ("host", "192.168.0.1"), ("host", "10.21.102.210"), ("host", "25.77.118.55"), ("host", "156.128.71.243"),
            ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"),
            ("User-agent", "Mozilla/5.0 (Windows NT 10.0.15063.674; osmeta 10.3.2535) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/9.0 Safari/602.1.1 osmeta/10.3.2535 Build/2535 [FBAN/FBW;FBAV/140.0.0.205.179;FBBV/74431143;FBDV/WindowsDevice;FBMD/UX360CAK;FBSN/Windows;FBSV/10.0.15063.674;FBSS/2;FBCR/;FBID/desktop;FBLC/pl_PL;FBOP/45;FBRV/0]"),
            ("user-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"),
            ("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)	"),
            ("Access-Token", "mvQ31rWIk3"), ("access-Token", "1eJ4wSLpfr"), ("Access-token", "79r3ccVIe6"), ("access-token", "OQKV4j7vQk"),
            ("Content-Type", "audio/aac"), ("content-Type", "text/css"),
            ("Content-type", "text/html"), ("content-type", "application/java-archive"),
            ("Content-Length", 12031), ("content-Length", 21), ("Content-length", 21445), ("content-length", 2134),
            ("Date", "2013-01-01"), ("Date", "2019-12-11"), ("Date", "2019-11-13"), ("Date", "2018-12-31"),
        ]

        for header_name, header_value in header:
            self.client.set_header(header_name, header_value)
            self.assertDictEqual(self.client.get_header(), {})
            self.client.clear_header(header_name)
            self.assertDictEqual(self.client.get_header(), {})

    def test_set_headers_with_dict(self):
        self.client = RestClient()

        header = [
            (
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "content-Length": 21,
                    "Date": "2019-11-13"
                },
                {}
            ),
            (
                {
                    "accept": "text/html",
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "content-Length": 21,
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "Date": "2019-11-13"
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "accept": "image/jpeg",
                    "host": "192.168.0.1",
                    "accept_encoding": "deflate",
                    "content-type": "application/java-archive",
                    "Content-length": 21445,
                    "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)	",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "access-Token": "1eJ4wSLpfr",
                    "category": "Car",
                    "Date": "2019-11-12",
                },
                {
                    "accept": "image/jpeg",
                    "accept_encoding": "deflate",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "category": "Car",
                }
            )
        ]

        for header_value, header_result in header:
            self.client.set_headers_with_dict(header_value)
            self.assertDictEqual(self.client.get_header(), header_result)
            self.client.clear_all_header()
            self.assertDictEqual(self.client.get_header(), {})

    def test_set_headers_with_json(self):
        self.client = RestClient()

        header = [
            (
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "content-Length": 21,
                    "Date": "2019-11-13"
                },
                {}
            ),
            (
                {
                    "accept": "text/html",
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "content-Length": 21,
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "Date": "2019-11-13"
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "accept": "image/jpeg",
                    "host": "192.168.0.1",
                    "accept_encoding": "deflate",
                    "content-type": "application/java-archive",
                    "Content-length": 21445,
                    "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)	",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "access-Token": "1eJ4wSLpfr",
                    "category": "Car",
                    "Date": "2019-11-12",
                },
                {
                    "accept": "image/jpeg",
                    "accept_encoding": "deflate",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "category": "Car",
                }
            )
        ]

        for header_value, header_result in header:
            json_header = json.dumps(header_value)

            self.client.set_headers_with_json(json_header)
            self.assertDictEqual(self.client.get_header(), header_result)
            self.client.clear_all_header()
            self.assertDictEqual(self.client.get_header(), {})

            self.assertEqual(1, self.client.set_headers_with_json(json_header[:15]))
            self.client.clear_all_header()

    def test_change_header(self):
        self.client = RestClient()

        header = [
            ("accept", "text/html"), ("accept_encoding", "br"), ("accept_encoding", "gzip"),
            ("gid", 1), ("uid", "test"), ("category", "amenity")
        ]

        header_length = len(header)

        for header_name, header_value in header:
            result = {header_name: header_value}
            random_idx = random.randrange(header_length)
            result[header[random_idx][0]] = header[random_idx][1]

            self.client.set_header(header_name, header_value)
            self.client.change_header(header[random_idx][0], header[random_idx][1])
            self.assertDictEqual(self.client.get_header(), result)
            self.client.clear_all_header()
            self.assertDictEqual(self.client.get_header(), {})

    def test_change_header_with_dict(self):
        self.client = RestClient()

        header = [
            (
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "content-Length": 21,
                    "Date": "2019-11-13"
                },
                {}
            ),
            (
                {
                    "accept": "text/html",
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "content-Length": 21,
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "Date": "2019-11-13"
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "accept": "image/jpeg",
                    "host": "192.168.0.1",
                    "accept_encoding": "deflate",
                    "content-type": "application/java-archive",
                    "Content-length": 21445,
                    "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)	",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "access-Token": "1eJ4wSLpfr",
                    "category": "Car",
                    "Date": "2019-11-12",
                },
                {
                    "accept": "image/jpeg",
                    "accept_encoding": "deflate",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "category": "Car",
                }
            )
        ]
        header_length = len(header)

        for header_value, header_result in header:
            result = copy.deepcopy(header_result)
            random_idx = random.randrange(header_length)
            for k, v in header[random_idx][1].items():
                result[k] = v

            self.client.set_headers_with_dict(header_value)
            self.client.change_header_with_dict(header[random_idx][0])
            self.assertDictEqual(self.client.get_header(), result)
            self.client.clear_all_header()
            self.assertDictEqual(self.client.get_header(), {})

    def test_change_header_with_json(self):
        self.client = RestClient()

        header = [
            (
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "content-Length": 21,
                    "Date": "2019-11-13"
                },
                {}
            ),
            (
                {
                    "accept": "text/html",
                    "host": "25.77.118.55",
                    "user-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "content-Length": 21,
                    "accept_encoding": "bz",
                    "parameter": "200OK",
                    "Access-Token": "mvQ31rWIk3",
                    "Content-Type": "audio/aac",
                    "Date": "2019-11-13"
                },
                {
                    "accept": "text/html",
                    "accept_encoding": "bz",
                }
            ),
            (
                {
                    "accept": "image/jpeg",
                    "host": "192.168.0.1",
                    "accept_encoding": "deflate",
                    "content-type": "application/java-archive",
                    "Content-length": 21445,
                    "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)	",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "access-Token": "1eJ4wSLpfr",
                    "category": "Car",
                    "Date": "2019-11-12",
                },
                {
                    "accept": "image/jpeg",
                    "accept_encoding": "deflate",
                    "gid": 10982,
                    "uid": "CA2019374102-39184992831",
                    "category": "Car",
                }
            )
        ]
        header_length = len(header)

        for header_value, header_result in header:
            result = copy.deepcopy(header_result)
            random_idx = random.randrange(header_length)
            for k, v in header[random_idx][1].items():
                result[k] = v

            self.client.set_headers_with_dict(header_value)
            self.client.change_header_with_json(json.dumps(header[random_idx][0]))
            self.assertDictEqual(self.client.get_header(), result)
            self.client.clear_all_header()
            self.assertDictEqual(self.client.get_header(), {})


if __name__ == '__main__':
    # testcase = Header_Testcase()
    unittest.main()
