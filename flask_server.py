from flask import Flask, request, jsonify

app = Flask(__name__)

latest_message = ""

@app.route('/send', methods=['GET','POST'])
def receive_message():
    global latest_message
    
    if request.method == "POST":    
        data = request.get_json()
        latest_message = data.get("message","")
        print("Message received:", latest_message)
        return "Message received"
    
    if request.method == "GET":
        return latest_message

app.run(host="0.0.0.0", port=5000)