import mysql.connector
from flask import Flask, request, jsonify


app = Flask(__name__)


def save_dog_to_db(dog_name, dog_size, dog_age, home_zip, best_times, pref_contact_method, pref_contact_info,
                   dog_pic1, dog_pic2, dog_pic3, dog_pic4, dog_pic5, user_id):
    try:
        connection = mysql.connector.connect(
            host="classmysql.engr.oregonstate.edu",
            user="cs361_bowlinst",
            password="SsxGXiv1TpPP",
            database="cs361_bowlinst"
        )

        cursor = connection.cursor()

        insert_user_data = ("INSERT INTO Dogs(dogName, dogSize, dogAge, homeZip, playTimes, prefMethod, prefInfo, "
                            "picOne, picTwo, picThree, picFour, picFive, userID) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        user_data = (
            dog_name, dog_size, dog_age, home_zip, best_times, pref_contact_method, pref_contact_info, dog_pic1,
            dog_pic2, dog_pic3, dog_pic4, dog_pic5, user_id)

        cursor.execute(insert_user_data, user_data)

        dog_id = cursor.lastrowid

        connection.commit()

        cursor.close()
        connection.close()

        print(f"Data saved to the database. Dog ID: {dog_id}")
        return dog_id

    except mysql.connector.Error as err:
        print(f"Error: {err}")


@app.route('/save_dog_route', methods=['POST'])
def save_dog_route():
    data = request.json
    dog_name = data['dog_name']
    dog_size = data['dog_size']
    dog_age = data['dog_age']
    best_times = data['best_times']
    home_zip = data['home_zip']
    pref_contact_method = data['pref_contact_method']
    pref_contact_info = data['pref_contact_info']
    dog_pic1 = None
    dog_pic2 = None
    dog_pic3 = None
    dog_pic4 = None
    dog_pic5 = None
    user_id = data['user_id']

    if user_id is not None:

        dog_id = save_dog_to_db(dog_name, dog_size, dog_age, home_zip, best_times, pref_contact_method,
                                pref_contact_info, dog_pic1, dog_pic2, dog_pic3, dog_pic4, dog_pic5, user_id)

        if dog_id is not None:
            return jsonify({'dog_id': dog_id})
        else:
            return jsonify({'error': 'Failed to save registration'}), 500
    else:
        return jsonify({'error': 'Failed to retrieve user_id from the queue'}), 500


if __name__ == '__main__':
    app.run(port=5001)
