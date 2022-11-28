# WiFi-RSSI-micropython
ESP32でWiFiのRSSIを取得
言語：micropython(version:1.18)

・AP.pyは，使用するESP32をWi-Fiのアクセスポイントにするためのソースコードです．
IPのところをAP化するESP32のIPアドレスに修正してください．以下のコードはAPのIPアドレスを確認する際に使用してください．
 
 ``` 
import network
ap_if = network.WLAN(network.AP_IF)
ap_if.ifconfig()
```

・rssi.pyは，Wi-FiのRSSIを取得と取得したデータをMongodbへ送信するソースコードです．
　send_db()の「db名」と「コレクション名」を個人のものに修正してください．
  rssi()にてAP化した各ESP32のSSID名に修正してください．
  以下のコードはSSIDを確認する際に使用してください．
  
  ```
import network
ap_if = network.WLAN(network.AP_IF)
ap_if.ifconfig("essid")
```
