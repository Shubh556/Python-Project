import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization": "2DJ3dPAwHXBoOCuIZvM7G9WsxrKVFj6cESpR5ql4k8b1zNemYfDToabAFnwKpu"
               "kPM9gGtz41sS56dYvN", "message": " Hi There :)\nThis Message is a test Message sent by a python interpreter\nRegards Shubh",
               "language":"english", "route": "q", "flash":"1","numbers":"1234587452"}

headers = {
    'cache-control': "no-cache"
}


response = requests.request("GET", url, headers=headers, params=querystring,)

print(response.text)
