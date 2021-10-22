from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def zyte():
    zyterequest = requests.get('https://api.github.com/orgs/scrapinghub/repos')
    zytedata = json.loads(zyterequest.content)

    return render_template('index.html', data=zytedata)

if __name__ == "__main__":
    app.run(host='0.0.0.0')