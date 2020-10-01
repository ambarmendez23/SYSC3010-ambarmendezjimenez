# Write your code here :-)
import httplib
import urllib
import time
key = "05KMLT9FYYFSUAPQ"  # Put your API Key here

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
TRIG = 4
ECHO = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance ():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = 0
    end = 0

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()
	
    sig_time = end - start
    distance = sig_time / 0.000058 #cm
    #distance = sig_time / 0.000148 #inches
    print('Distance: {} centimeters'.format(distance))
    
    params = urllib.urlencode({'field1': distance, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print temp
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    #break


def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.urlencode({'field1': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
        
if __name__ == "__main__":
        while True:
                distance()
                time.sleep(0.5)
                
GPIO.cleanup()



Reference: https://pythonprogramming.net/garage-stoplight-raspberry-pi-tutorials/?completed=/gpio-input-raspberry-pi-tutorials/
		
