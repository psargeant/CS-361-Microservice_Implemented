import requests

def get_dogs_by_user_id(user_id):
    try:
        # Flask app URL
        flask_app_url = "http://localhost:5001"

        # Make a GET request to the Flask app endpoint
        response = requests.get(f"{flask_app_url}/get_all_dogs")

        if response.status_code == 200:
            return response.json().get('dogs', [])
        else:
            print("Error fetching dogs:", response.text)
            return []
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []
