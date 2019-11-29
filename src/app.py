from flask import Flask
import os
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    now = datetime.datetime.now()
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Current Date:</b> {currentdate}<br/>"
    return html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname(),
                       currentdate=str(now))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
