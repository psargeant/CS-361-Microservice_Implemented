# copy SQL dog info needed
from flask import Flask, request, jsonify
import mysql.connector
from fuzzywuzzy import fuzz

app = Flask(__name__)

def establish_db_connection():
    return mysql.connector.connect(
        host="classmysql.engr.oregonstate.edu",
        user="cs361_bowlinst",
        password="SsxGXiv1TpPP",
        database="cs361_bowlinst"
    )

@app.route('/make_match', methods=['GET'])  # Change the method to POST since you are sending JSON data
def make_match():
    try:
        data = request.json
        print("Received JSON:", data)
        dog_name = data.get('dog_name')
        print("Dog Name:", dog_name)

        if dog_name is None:
            return jsonify({'error': 'Missing dog_name parameter'})

        connection = establish_db_connection()
        cursor = connection.cursor()

        query = "SELECT dogID, dogName, dogSize, dogAge, homeZip, playTimes FROM Dogs WHERE dogName != %s"
        cursor.execute(query, (dog_name,))
        other_dogs_result = cursor.fetchall()

        query2 = "SELECT dogID, dogName, dogSize, dogAge, homeZip, playTimes FROM Dogs WHERE dogName = %s"
        cursor.execute(query2, (dog_name,))
        user_dog_result = cursor.fetchall()

        dog_list = []
        for row in other_dogs_result:
            dog_data = {
                'dogID': row[0],
                'dogName': row[1],
                'dogSize': row[2],
                'dogAge': row[3],
                'homeZip': row[4],
                'playTimes': row[5]
            }
            dog_list.append(dog_data)

        user_dog = []
        for row in user_dog_result:
            dog_data = {
                'dogID': row[0],
                'dogName': row[1],
                'dogSize': row[2],
                'dogAge': row[3],
                'homeZip': row[4],
                'playTimes': row[5]
            }
            user_dog.append(dog_data)

        # Accessing the user dog values
        user_dog_age = user_dog[0]['dogAge']
        user_dog_size = user_dog[0]['dogSize']
        user_dog_play_time = user_dog[0]['playTimes']
        user_dog_zipcode = user_dog[0]['homeZip']

        # Initialize results list
        results = []

        for dog in range(len(dog_list)):
            # Accessing the compare dog values
            compare_dog_age = dog_list[dog]['dogAge']
            compare_dog_size = dog_list[dog]['dogSize']
            compare_dog_play_time = dog_list[dog]['playTimes']
            compare_dog_zipcode = dog_list[dog]['homeZip']

            # Calculate similarity scores for string attributes
            age_similarity = fuzz.ratio(compare_dog_age, user_dog_age)
            size_similarity = fuzz.ratio(compare_dog_size, user_dog_size)
            play_time_similarity = fuzz.ratio(compare_dog_play_time, user_dog_play_time)
            zipcode_similarity = fuzz.ratio(str(compare_dog_zipcode), str(user_dog_zipcode))

            # Calculate overall similarity score
            overall_similarity = (age_similarity + size_similarity + play_time_similarity + zipcode_similarity) / 4.0

            # Convert the similarity score to a percentage
            percent_match = round(overall_similarity, 2)

            # Append the result to the results list
            results.append({
                'compare_dog_name': dog_list[dog]['dogName'],
                'percent_match': percent_match
            })
        # Sort results based on the 'percent_match' key in descending order
        sorted_results = sorted(results, key=lambda x: x['percent_match'], reverse=True)

        # Print or use the results list as needed
        print(sorted_results)

        cursor.close()
        connection.close()

        return jsonify(sorted_results)

    except mysql.connector.Error as e:
        print("Database error:", e)
        return jsonify({'error': f"Database error: {e}"})


if __name__ == '__main__':
    app.run(port=5005)


# Perform calculation as function into mongoDB

# return % dog match
