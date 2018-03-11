from flask import Flask, render_template, send_from_directory
from os.path import join
import sys

app = Flask(__name__, static_url_path='',
            static_folder=join('templates', 'dist'))

REMINDERS_ON = False
ON_SCREEN = False


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
    global ON_SCREEN
    ON_SCREEN = False
    log_msg(leave.__name__, ON_SCREEN)
    return ('', 204)


@app.route("/")
def index():
    global ON_SCREEN
    ON_SCREEN = True
    log_msg(index.__name__, ON_SCREEN)
    return render_template(join('dist', 'index.html'))
