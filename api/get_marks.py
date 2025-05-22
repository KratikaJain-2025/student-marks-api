import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    names = request.query.getall("name", [])
    path = os.path.join(os.path.dirname(__file__), "marks.json")

    with open(path) as f:
        data = json.load(f)

    return response.json({ "marks": [data.get(name) for name in names] })
