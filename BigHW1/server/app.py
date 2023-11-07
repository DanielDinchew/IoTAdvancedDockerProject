from flask import Flask, request, jsonify
from pysondb import db
import json

app = Flask(__name__)
database = db.getDb("static/database.json")

@app.route("/")
def returnLinks():
    return 0

@app.route("/data", methods=['POST'])
def addData():
    data = request.get_json()

    database.add(data)

    filePath = database.filename
    with open(filePath, "r") as json_file:
        fileData = json.load(json_file)
    

    fileData["data"] = sorted(fileData["data"], key=lambda record: record["timestamp"], reverse=True)

    with open(filePath, "w") as json_file:
        json.dump(fileData, json_file, indent=4)

@app.route("/stats")
def getStats():
    return 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)