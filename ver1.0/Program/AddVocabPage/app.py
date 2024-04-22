from flask import Flask, request, jsonify
import sqlite3

# create Flask application
# __name__ is the name of Python script
app = Flask(__name__)

# create endpoint which is used for adding new flashcard
# POST method is only accepted
@app.route('/add_flashcard', methods=['POST'])

# define "add_flashcard" function 
def add_flashcard():
    try:
        # receive JSON(JavaScriot Object Notation/ file format) data from HTTP request
        data = request.get_json()
        # get the information from JSON data
        frontside = data['frontside']
        backside = data['backside']
        link = data['link']

        # CONNect to the 'flashcards.db'
        conn = sqlite3.connect('flashcards.db')
        # create cursor for query
        cursor = conn.cursor()

        # execute the query to insert new flashcard on database
        cursor.execute('INSERT INTO flashcards (frontside, backside, link) VALUES(?, ?, ?)', (frontside, backside, link))
        # finalize the changes
        conn.commit()
        # close the connection with databasse
        conn.close()

        # return the JSONresponse 
        return jsonify({'message': 'Flashcard added successfully'}), 200
    
    # exception handling
    except Exception as e:
        return jsonify({'error':str(e)}), 500

#execute the Flask application 
if __name__ == '__main__':
    app.run(debug=True)
    


