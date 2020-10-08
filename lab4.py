import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3"  # Put your API Key here

def lab4():
    while True:
        group = "L3-T-7"
        cmail = ambarmendezjimenez@cmail.carleton.ca
        member_id = "a"

        params = urllib.urlencode({'field1': group, 'field2': cmail, 'field2': member_id 'key':key  }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
            lab4()
                