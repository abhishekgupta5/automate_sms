from flask import Flask, Response, request
from twilio import twiml

app = Flask(__name__)

@app.route("/")
def check_app():
    return Response("App working!"), 200


