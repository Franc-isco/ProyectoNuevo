import http.client
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auxiliares.url_servicio import url_base_serper as url_serper

def buscar_en_api(query):
    conn = http.client.HTTPSConnection(url_serper)
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': '2c1d43077dc16528462e8efea576a79356941fbe',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))



