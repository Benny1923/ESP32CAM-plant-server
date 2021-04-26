from geventwebsocket import WebSocketServer, WebSocketError, WebSocketApplication, Resource
import time, json, datetime
from model import plant_status, plant_message
from _init_ import db

#esp32 last reponse time
lastresponse = time.time()
client = None

#寫入感測器資料至資料庫
def save_status(data):
    status = plant_status(datetime.datetime.now(), data["moisture"], data["tankfluid"], data["lux"])
    db.session.add(status)
    db.session.commit()

#寫入ESP32發送的訊息置資料庫
def save_msg(msg):
    message = plant_message(datetime.datetime.now(), msg)
    db.session.add(message)
    db.session.commit()

#ESP32控制
#呼叫前先確認裝置在線上
class Esp32cmd:
    #更新遠端設定
    def updatecfg(cfg):
        cmd = {"op":"update", "config":cfg}
        client.ws.send(json.dumps(cmd))
    #檢查裝置上線狀態
    def isonline():
        global lastresponse
        if ((time.time() - lastresponse) < 5):
            return True
        else:
            return False
    #手動控制
    def manual(device, sw):
        global client
        cmd = {"op":"manual", "device": {}}
        if device == "all":
            cmd["device"]["sprinklers"] = int(sw)
            cmd["device"]["light"] = int(sw)
        elif device == "sprinklers":
            cmd["device"]["sprinklers"] = int(sw)
        elif device == "light":
            cmd["device"]["light"] = int(sw)
        client.ws.send(json.dumps(cmd))

#ESP32 websocket及時通訊程式
class Esp32conns(WebSocketApplication):
    def on_open(self):
        global lastresponse
        print("client connected!")
        lastresponse = time.time()
        client = self
        self.ws.send("hi")
    def on_message(self, message):
        global lastresponse
        global client
        client = self
        if (len(message) > 4):
            print("message received!")
            print(message)
            data = json.loads(message)
            if data["type"] == "status":
                save_status(data["status"])
            elif data["type"] == "message":
                save_msg(data["msg"])
        lastresponse = time.time()
    def on_close(self, reason):
        print("Connection closed!")