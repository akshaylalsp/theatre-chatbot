from flask import Flask, request, jsonify
from TheatreChatBot import TheatreChatBot

app = Flask(__name__)
chatbot_instance = None

@app.route('/initialize_chatbot', methods=['POST'])
def initialize_chatbot():
    global chatbot_instance
    data = request.get_json()
    location = data['location']
    chatbot_instance = TheatreChatBot(location)
    return jsonify(message="Chatbot initialized successfully!")

@app.route('/execute_result', methods=['POST'])
def execute_result():
    if chatbot_instance is None:
        return jsonify(error="Chatbot not initialized!")
    data = request.get_json()
    nl_question = data['nl_question']
    result = chatbot_instance.execute_result(nl_question)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)