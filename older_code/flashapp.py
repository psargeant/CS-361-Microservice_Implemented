from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Replace these values with your actual database connection details
db_host = "localhost"
db_user = "root"
db_password = "root"
db_name = "dogdatabase"
user_id = 1

# Endpoint for saving dog profile
@app.route('/save_dog_profile', methods=['POST'])
def save_dog_profile():
    data = request.json
    dog_info = data.get('dogInfo', {})

    # Connect to the database
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = db.cursor()

        query = f"INSERT INTO Dogs (`dogName`, `dogSize`, `dogAge`, `homeZip`, `playSpace`, `userID`) " \
                f"VALUES ('{dog_info.get('name')}', " \
                f"'{dog_info.get('Weight')}', " \
                f"'{dog_info.get('age')}', " \
                f"'{dog_info.get('homeZip')}', " \
                f"'{dog_info.get('playSpace')}', " \
                f"'{user_id}')"

        cursor.execute(query)
        db.commit()

        return jsonify({'message': 'Dog profile saved successfully'}), 200

    except pymysql.Error as e:
        return jsonify({'error': f"Database Error: {e}"}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


# Endpoint for getting all dog profiles
@app.route('/get_all_dogs', methods=['GET'])
def get_all_dogs():
    # Connect to the database
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = db.cursor()

        query = "SELECT dogName, dogSize, dogAge, homeZip, playSpace FROM Dogs WHERE userID = %s"
        cursor.execute(query, (user_id,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Convert the rows to a list of dictionaries for JSON serialization
        dogs = [{'dogName': row[0], 'dogSize': row[1], 'dogAge': row[2], 'homeZip': row[3], 'playSpace': row[4]} for row in rows]

        return jsonify({'dogs': dogs}), 200

    except pymysql.Error as e:
        return jsonify({'error': f"Database Error: {e}"}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == '__main__':
    app.run(debug=True, port=5001)


