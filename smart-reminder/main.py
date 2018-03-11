from flask import Flask, render_template, send_from_directory, request
from os.path import join
import sys
import json
import base64

from .utils import decode
from .model import Model

app = Flask(__name__, static_url_path='',
            static_folder=join('templates', 'dist'))

REMINDERS_ON = True
MODEL = Model()


def log_msg(func, msg):
    print("[{}]: {}".format(func, msg), file=sys.stderr)


@app.route("/reminders_off")
def reminders_off():
    global REMINDERS_ON
    REMINDERS_ON = False
    log_msg(reminders_off.__name__, REMINDERS_ON)
    return ('', 204)


@app.route("/reminders_on")
def reminders_on():
    global REMINDERS_ON
    REMINDERS_ON = True
    log_msg(reminders_on.__name__, REMINDERS_ON)
    return ('', 204)


@app.route("/leave")
def leave():
    return ('', 204)


@app.route("/get_state", methods=["POST", ])
def get_state():
    img = request.form['current']
    img = base64.b64decode(img)
    img = decode(img)

    return json.dumps({
        "on_seat": MODEL.is_person(img),
        "stop": not REMINDERS_ON
    })


@app.route("/")
def index():
    return render_template(join('dist', 'index.html'))
