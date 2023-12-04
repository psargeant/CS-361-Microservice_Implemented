import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)


def save_registration_to_db(first_name, last_name, email, password):
    try:
        connection = mysql.connector.connect(
            host="classmysql.engr.oregonstate.edu",
            user="cs361_bowlinst",
            password="SsxGXiv1TpPP",
            database="cs361_bowlinst"
        )

        cursor = connection.cursor()

        insert_user_data = "INSERT INTO Users(firstName, lastName, email, passwordHash) VALUES (%s, %s, %s, %s)"
        user_data = (first_name, last_name, email, password)
        cursor.execute(insert_user_data, user_data)

        user_id = cursor.lastrowid

        connection.commit()

        cursor.close()
        connection.close()

        print(f"Data saved to the database. User ID: {user_id}")
        return user_id

    except mysql.connector.Error as err:
        print(f"Error: {err}")


@app.route('/save_registration_route', methods=['POST'])
def save_registration_route():
    data = request.json
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

    user_id = save_registration_to_db(first_name, last_name, email, password)

    if user_id is not None:
        return jsonify({'user_id': user_id})
    else:
        return jsonify({'error': 'Failed to save registration'}), 500


if __name__ == '__main__':
    app.run(port=5000)
