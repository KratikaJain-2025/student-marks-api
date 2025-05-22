import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    names = request.query.getall("name", [])
    path = os.path.join(os.path.dirname(__file__), "marks.json")

    with open(path) as f:
        marks_data = json.load(f)

    result = [marks_data.get(name, None) for name in names]
    return response.json({ "marks": result })
