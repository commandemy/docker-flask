from flask import Flask
import os
import socket
import datetime
import configparser

app = Flask(__name__)
configParser = configparser.ConfigParser()

@app.route("/")
def hello():

    now = datetime.datetime.now()
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Domainname: </b> {domainname}<br/>" \
           "<b>Port: </b> {port}<br/>" \
           "<b>Config Sections: </b> {sections}<br/>" \
           "<b>Current Date:</b> {currentdate}<br/>"
    return html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname(),
                       domainname=configParser.get('app', 'domainname'),
                       port=configParser.get('app','port'),
                       sections=', '.join(configParser.sections()),
                       currentdate=str(now))

if __name__ == "__main__":
    configParser.read('/app/etc/config.ini')
    app.run(host='0.0.0.0', port=configParser.get('app','port'))
