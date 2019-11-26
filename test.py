from RestClient4py.client import RestClient

client = RestClient()
client.set_header("Accept", "*/*")
client.set_header("Content-Type", "application/json")
print(client)