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


@app.route('/retrieve_dog_info', methods=['GET'])
def retrieve_dog_info():
    try:
        data = request.json
        print("Received JSON:", data)
        user_id = data.get('user_id')
        print("User data", user_id)

        if user_id is None:
            return jsonify({'error': 'Missing user_id parameter'})

        with establish_db_connection() as connection:
            cursor = connection.cursor()

            query = "SELECT dogID, dogName, dogSize, dogAge, homeZip, playTimes FROM Dogs WHERE userID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if result:
                dog_data = {
                    'dogID': result[0],
                    'dogName': result[1],
                    'dogSize': result[2],
                    'dogAge': result[3],
                    'homeZip': result[4],
                    'playTimes': result[5]
                }
                print("Dog data:", dog_data)
                return jsonify({'dog_data': dog_data})
            else:
                return jsonify({'error': 'User not found'})

    except mysql.connector.Error as e:
        print("check 4")
        return jsonify({'error': f"Database error: {e}"})


if __name__ == '__main__':
    app.run(port=5004)
