import network
import time
import urequests
import ujson
import machine

machine.freq(240000000)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def send_db(name1,rssi1,name2,rssi2,name3,rssi3): #mongoに送るやつ
    url = 'http://iot-database.a910.tak-cslab.org:3000/iot'
    payload = {
        "db": "[db名]",
        "collection": "[コレクション名]",
        "data": {
            "name1": name1,
            "rssi1": rssi1,
            "name2": name2,
            "rssi2": rssi2,
            "name3": name3,
            "rssi3": rssi3,
        }
    }
    header = {'Content-Type' : 'application/json'}
    res = urequests.post(url, data = ujson.dumps(payload).encode("utf-8"), headers = header)
    res.close()
    
    
def wlan_scan():
    return network.WLAN(network.STA_IF).scan()

def rssi():
    try:
        w_scan = wlan_scan()
        if w_scan != []:
            for a in range(len(w_scan)):
                if w_scan[a][0] == [取得するESP32のssid]:
                    name1 = w_scan[a][0]
                    rssi1 = w_scan[a][3]
                elif w_scan[a][0] == [取得するESP32のssid]: 
                    name2 = w_scan[a][0]
                    rssi2 = w_scan[a][3]
                elif w_scan[a][0] == [取得するESP32のssid]:
                    name3 = w_scan[a][0]
                    rssi3 = w_scan[a][3]
        send_db(name1,rssi1,name2,rssi2,name3,rssi3)
    except Exception as e:
        print(e)


    
            
if __name__ == '__main__':
    print('start')
    while True:
        rssi()

    
print('end')








