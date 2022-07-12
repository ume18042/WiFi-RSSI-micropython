# WiFi-RSSI-micropython
ESP32でWiFiのRSSIを取得
言語：micropython(version:1.18)

・AP.pyでは，使用するESP32をWi-Fiのアクセスポイントにするためのソースコードとなっています．
　IPのところにAP化するESP32のIPアドレスを追記してください．
 
　IPアドレスの確認は以下で確認可能

import network
ap_if = network.WLAN(network.AP_IF)
ap_if.ifconfig()
