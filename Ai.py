from requests import post
from flask import Flask, jsonify, jsonify

app = Flask(__name__)

headers = { "X-API-KEY": "Your real api key from mothadev", "User-Agent": "Mozilla/5.0", "referer": "your website link Not facebook" }

message = "Hello Ai, HowreYou ?"

system = "Your Name is Cris st. You are an ai assistance Developed by Cris"

@app.route("/", methods=["POST", "GET"])
def ai():
    data = { "user_id": "Chris", "messages": { "system": system, "user": user }
    req = post("https://api.motadev.xyz/api/chat", json=data, headers=headers)
    print(req.json())
    return req.json()
  
app.run()
