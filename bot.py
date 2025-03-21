import google.generativeai as ai
from flask import Flask,jsonify,request
from flask_cors import CORS
# from jsonify import jsonify
my_key= "AIzaSyCykKtAvqohdiRMIRvSWip_IldrmlHODUY"
ai.configure(api_key=my_key)
model =ai.GenerativeModel("gemini-1.5-pro")

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route("/chat", methods=['GET'])
def Chat():
    msg=request.args.get("message")
    if not msg:
        return jsonify({'error':"there is a error"})
    
    chat = model.start_chat()
    result = chat.send_message(msg)
    answer= result.text
    return jsonify({'message':answer})

if __name__ == "__main__":
    app.run(debug=True)

