from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def zyte():
    zyterequest = requests.get('https://api.github.com/orgs/scrapinghub/repos?sort=name&direction=asc&per_page=10')
    data = json.loads(zyterequest.content)

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')