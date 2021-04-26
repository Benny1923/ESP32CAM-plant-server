import os, time
import json
from websocket import WebSocketApp
import requests

#default server_addr
defaddr = "127.0.0.1"

print("remote esp32 emulator by benny1923@2021-04-19")
print("this program emulate our custom api")
print("available command:\n1:send status\n2:send message\n3:upload image")
server_addr = input("enter server address(%s): "%defaddr)
if len(server_addr) == 0:
    server_addr = defaddr

def Msgfunc(ws, message):
    print(message)
    
def statusgen():
    status = {}
    status["type"] = "status"
    status["status"] = {}
    with open("sensor.txt", "r") as f:
        for line in f:
            if line[0] == '#' or len(line) < 1:
                continue
            temp = line.split('=', 1)
            temp[1] = temp[1].strip('\n')
            if temp[1].isdigit():
                status["status"][temp[0]] = int(temp[1])
    return(json.dumps(status))
    
def on_open(ws):
    print("server connected!")
    while (True):
        cmd = input("enter command(1-3): ")
        if not cmd.isdigit():
            continue
        else:
            cmd = int(cmd)

        if cmd == 1:
            ws.send(statusgen())
        elif cmd == 2:
            temp = {"type": "message"}
            temp["msg"] = input("enter message: ")
            ws.send(json.dumps(temp))
        elif cmd == 3:
            my_file = {"img": open("test.jpg", "rb")}
            r = requests.post("http://%s:8080/api/ESP32/saveimg"%server_addr, files = my_file)
            print(r.text)
        elif cmd == 4:
            t = eval(input("enter keep online sec: "))
            for i in range(t):
                ws.send("ping")
                time.sleep(1)
        elif cmd == 5:
            break

ws = WebSocketApp("ws://%s:8080/websocket"%server_addr,
                  on_message=Msgfunc,
                  on_open=on_open)

print("now connect to server(%s)..."%server_addr)
ws.run_forever()
print("exit emulator")
