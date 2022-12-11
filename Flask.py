"""
By Shaima'a Khashan
"""

import requests
import json
from flask import Flask, render_template, url_for

exportAll_api = "http://staging.bldt.ca/api/method/build_it.test.get_students"
app = Flask(__name__)


@app.route("/template.html")
def home():
    result = requests.get(exportAll_api)
    data = result.text
    data = json.loads(data)
    context = {}
    print(data)
    context['title'] = 'GSG Task 4'
    context['details'] = data['data']
    return render_template("template.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
