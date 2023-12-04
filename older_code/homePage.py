import tkinter as tk
from tkinter import ttk
import requests
from dog_profile_page import DogProfilePage
from dog_matches import DogMatcherPage
from dogs import get_dogs_by_user_id


# Flask app URL
flask_app_url = "http://localhost:5001"

def open_view_dog_profile():
    # Assume user ID is 1, replace with actual user ID if needed
    user_id = 1

    # Fetch dog profile data from the get_dogs_by_user_id function
    dog_profiles = get_dogs_by_user_id(user_id)

    # Call the display_dog_profiles function with the fetched data
    display_dog_profiles(dog_profiles)

# Example implementation of display_dog_profiles
def display_dog_profiles(dog_profiles):
    # Create a new window for displaying dog profiles in a table
    view_dogs_window = tk.Toplevel()
    view_dogs_window.title("View Dogs")

    # Create a treeview for displaying the dog profiles in a table
    tree = ttk.Treeview(view_dogs_window)
    tree["columns"] = ("Name", "Size", "Age", "Home Zip", "Play Space")

    # Configure column headings
    tree.heading("Name", text="Name")
    tree.heading("Size", text="Size")
    tree.heading("Age", text="Age")
    tree.heading("Home Zip", text="Home Zip")
    tree.heading("Play Space", text="Play Space")

    # Insert dog profiles into the treeview
    print(dog_profiles)
    for dog_profile in dog_profiles:
        tree.insert("", "end", values=(
            dog_profile.get("dogName", ""),  # Use .get() to handle missing keys
            dog_profile.get("dogSize", ""),
            dog_profile.get("dogAge", ""),
            dog_profile.get("homeZip", ""),
            dog_profile.get("playSpace", "")
        ))

    # Pack the treeview to display it
    tree.pack(expand=tk.YES, fill=tk.BOTH)


def open_create_dog_window():
    dog_profile_page = DogProfilePage()
    dog_profile_page.open_create_dog_window()


def create_home_page():
    home_window = tk.Toplevel()
    home_window.title("Home Page")

    # Add content to the home window
    label_welcome = tk.Label(home_window, text="Welcome to PupDate!", font=("Century Gothic", 20))
    label_welcome.pack(pady=10)

    # Buttons for different actions
    button_create_dog = tk.Button(home_window, text="Create Dog", command=open_create_dog_window)
    button_create_dog.pack(pady=10)

    button_view_dog_profile = tk.Button(home_window, text="View Dog Profile", command=open_view_dog_profile)
    button_view_dog_profile.pack(pady=10)

    button_view_matches = tk.Button(home_window, text="View Dog Matches", command=open_view_matches_window)
    button_view_matches.pack(pady=10)


def open_view_matches_window():
    # Open the DogMatcherPage from dog_matches.py
    dog_matcher_page = DogMatcherPage()
    dog_matcher_page.run()


if __name__ == "__main__":
    create_home_page()
    tk.mainloop()


create_home_page()
tk.mainloop()
