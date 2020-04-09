from flask import Flask, request
from multiprocessing import Process, Queue
from time import sleep
app = Flask(__name__)

if 0:
    import relay
    update_relays = relay.update_relays
else:
    def update_relays(buttons):
        print("UPDATE:",buttons)

DIRECTIONS = (
    "fl","f","fr",
    "bl","b","br"
)



def bg():
    i = 0
    buttons = {"f":False, "b":False, "l":False, "r":False}
    while True:
        print(i)
        if not queue.empty():
            direction, duration = queue.get()
            print(direction, duration)
        else:
            direction, duration = "", 100
        for k in buttons:
            buttons[k] = k in direction
        update_relays(buttons)
        sleep(duration/1000)
        i += 1

queue = Queue()
p = Process(target=bg)
p.start()

@app.route('/')
def hello_world():
    return app.send_static_file("index.html")

@app.route('/control', methods=["POST"])
def control():
    direction = request.form["direction"]
    duration = int(request.form["duration"])
    assert duration < 4000
    if direction in DIRECTIONS:
        res = "Received direction <code>{}</code> with duration {}.".format(
            direction, duration
        )
        app.logger.info(request.remote_addr + ": " + res)
        queue.put((direction, duration))
        return res
    else:
        res = "Received invalid direction <code>{}</code> with duration {}.".format(
            direction, duration
        )
        app.logger.info(request.remote_addr + ": " + res)
        return res, 400

