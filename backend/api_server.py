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

def get_db_connection():
    conn = sqlite3.connect('modules/movie.db')  # Replace with your database name
    conn.row_factory = sqlite3.Row  # Allows fetching rows as dictionary-like objects
    return conn

# Define a route that returns all entries from the Movies table
@app.route('/movies', methods=['GET'])
def get_movies():
    # Connect to the database
    conn = get_db_connection()

    # Query to select all movies
    query = 'SELECT * FROM Movies'
    movies = conn.execute(query).fetchall()  # Fetch all rows

    # Convert the data to a list of dictionaries
    movies_list = [dict(movie) for movie in movies]

    # Close the database connection
    conn.close()

    # Return the data as a JSON response
    return jsonify(movies_list)


if __name__ == '__main__':
    app.run(debug=True)
