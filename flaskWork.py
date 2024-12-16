from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-clinician/<>")
def get_clinician():
    return



if __name__ == "main":
    app.run(debug=True)
