import tkinter as tk
from tkinter import ttk
import requests

class DogMatcherPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dog Matcher")

        self.server_url = "http://localhost:5000/calculate_match"  # Flask app URL

        self.create_widgets()

    def create_widgets(self):
        # Entry widgets for user input
        ttk.Label(self.root, text="age:").pack(pady=10)
        self.range_entry = ttk.Entry(self.root)
        self.range_entry.pack(pady=10)

        ttk.Label(self.root, text="Size:").pack(pady=10)
        self.dog_entry = ttk.Entry(self.root)
        self.dog_entry.pack(pady=10)

        ttk.Label(self.root, text="Play Space:").pack(pady=10)
        self.temperament_entry = ttk.Entry(self.root)
        self.temperament_entry.pack(pady=10)

        ttk.Label(self.root, text="zipcode:").pack(pady=10)
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.pack(pady=10)

        # Button to calculate match
        ttk.Button(self.root, text="Calculate Match", command=self.calculate_match).pack(pady=10)

        # Label to display the result
        self.label_result = ttk.Label(self.root, text="")
        self.label_result.pack(pady=10)

    def calculate_match(self):
        # Retrieve entered values
        entered_range = self.range_entry.get()
        entered_dog = self.dog_entry.get()
        entered_temperament = self.temperament_entry.get()
        entered_age = self.age_entry.get()
        entered_playspace = self.playspace_entry.get()

        # Prepare the data for the HTTP request
        data = {
            "range": entered_range,
            "dog_breed": entered_dog,
            "temperament": entered_temperament,
            "age": entered_age,
            "playspace": entered_playspace
        }

        try:
            # Send HTTP request to the Flask app
            response = requests.post(self.server_url, json=data)

            if response.status_code == 200:
                result = response.json()
                percent_match = result.get("percent_match", "N/A")
                self.label_result.config(text=f"Match: {percent_match}%")
            else:
                self.label_result.config(text="No match found.")

        except requests.RequestException as e:
            print(f"Error: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DogMatcherPage()
    app.run()


