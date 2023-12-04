from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def establish_db_connection():
    return mysql.connector.connect(
        host="classmysql.engr.oregonstate.edu",
        user="cs361_bowlinst",
        password="SsxGXiv1TpPP",
        database="cs361_bowlinst"
    )


print("check 1")


@app.route('/validate_login', methods=['POST'])
def validate_login():
    try:
        data = request.json
        username = data['username']
        password = data['password']

        connection = establish_db_connection()
        try:
            cursor = connection.cursor()

            query = "SELECT userID, passwordHash FROM Users WHERE email = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                stored_password_hash = result[1]
                if password == stored_password_hash:
                    print("check 5")
                    return jsonify({'success': True, 'user_id': user_id})
                else:
                    print("check 6")
                    return jsonify({'error': 'Incorrect password'})
            else:
                return jsonify({'error': "Username not found"})
        finally:
            connection.close()

    except mysql.connector.Error as e:
        print("check 4")
        return jsonify({'error': f"Database error: {e}"})


if __name__ == '__main__':
    app.run(port=5002)
