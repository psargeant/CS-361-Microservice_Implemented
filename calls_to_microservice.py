# Calls from the registration window to the send_user_info micro, send_user_info.py
import requests
import tk

button_Save1 = tk.Button(
            save_button_frame,
            text="Save",
            font=("Century Gothic bold", 20),
            fg="black",
            bd=5,
            relief="solid",
            command=lambda: self.save_registration(
                first_name=self.fn_entry.get(),
                last_name=self.ln_entry.get(),
                email=self.email_entry.get(),
                password=self.createpw_entry.get())
        )
        button_Save1.pack(padx=110, side=tk.RIGHT)


def save_registration(self, first_name, last_name, email, password):
    try:
        url = "http://localhost:5000/save_registration_route"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password

        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            user_id = response.json()['user_id']
            print(f"Data saved to the microservice. User ID: {user_id}")
            show_save_message(self)
            return user_id
        else:
            print(f"Failed to save registration. Error: {response.json()['error']}")

    except Exception as e:
        print(f"Error: {e}")
        return None






# From the dog registration window to the send_dog_info microservice, send_dog_info.py

button_Save = tk.Button(
            frame_5,
            text="Save",
            font=("Century Gothic", 20),
            fg="black",
            bd=2,
            relief="solid",
            width=5,
            height=0,
            command=lambda: self.save_dog(
                dog_name=self.dogname_entry.get(),
                dog_size=self.size_dropdown.selected_value.get(),
                dog_age=self.age_dropdown.selected_value.get(),
                best_times=self.time_dropdown.selected_value.get(),
                home_zip=self.zipcode_entry.get(),
                pref_contact_method=self.contact_dropdown.selected_value.get(),
                pref_contact_info=self.contact_info_entry.get(),
                dog_pic1=None,
                dog_pic2=None,
                dog_pic3=None,
                dog_pic4=None,
                dog_pic5=None,
                user_id=self.user_id,
            )
        )
        button_Save.pack(padx=5, side=tk.LEFT)


def save_dog(self, dog_name, dog_size, dog_age, home_zip, best_times, pref_contact_method, pref_contact_info,
             dog_pic1, dog_pic2, dog_pic3, dog_pic4, dog_pic5, user_id):
    try:
        url = "http://localhost:5001/save_dog_route"
        data = {
            'dog_name': dog_name,
            'dog_size': dog_size,
            'dog_age': dog_age,
            'home_zip': home_zip,
            'best_times': best_times,
            'pref_contact_method': pref_contact_method,
            'pref_contact_info': pref_contact_info,
            'dog_pic1': dog_pic1,
            'dog_pic2': dog_pic2,
            'dog_pic3': dog_pic3,
            'dog_pic4': dog_pic4,
            'dog_pic5': dog_pic5,
            'user_id': user_id
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            dog_id = response.json()['dog_id']
            print(f"Data saved to the microservice. User ID: {user_id}")
            show_save_message(self)
            return dog_id
        else:
            print(f"Failed to save registration. Error: {response.json()['error']}")

    except Exception as e:
        print(f"Error: {e}")
        return None




# From the login window to the login veriification microservice login_ms.py
enter_button = tk.Button(button_frame,
                                 text="Enter",
                                 font=(Styles.FONT_FAMILY, Styles.FONT_LARGE),
                                 bd=2,
                                 relief="solid",
                                 width=5,
                                 bg="gray",
                                 command=lambda: self.validate_login(
                                     username=self.username_entry.get(),
                                     password=self.password_entry.get()
                                 ))
        enter_button.pack(side=tk.RIGHT, padx=60)


def validate_login(self, username, password):
    url = "http://localhost:5002/validate_login"

    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            user_id = result.get('user_id')
            self.handle_successful_login(user_id)
        else:
            messagebox.showerror("Error", "Incorrect username or password")
    else:
        messagebox.showerror("Error", "Microservice error")


def handle_successful_login(self, user_id):
    print(f"User logged in successfully. User ID: {user_id}")
    ProfileWindow(user_id)
    self.withdraw()

def fetch_user_data(self):
        url = "http://localhost:5003/retrieve_profile"
        data = {'user_id': self.user_id}
        response = requests.get(url, json=data)
        print("Response Content:", response.content)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            result = response.json()
            print("Response Content:", response.content)
            if 'error' in result:
                messagebox.showerror("Error", f"Microservice error: {result['error']}")
                print("Microservice error:", result['error'])
            else:
                user_data = result.get('user_data', {})
                print("Fetched User Data:", user_data)
                self.populate_user_fields(user_data)
        else:
            messagebox.showerror("Error", "Microservice error")

def populate_user_fields(self, user_data):
        # Populate entry fields with the retrieved data
        self.first_name_info.config(text=user_data.get('firstName', ''))
        self.last_name_info.config(text=user_data.get('lastName', ''))
        self.contact_info.config(text=user_data.get('email', ''))

def fetch_dog_data(self):
        url = "http://localhost:5004/retrieve_dog_info"
        data = {'user_id': self.user_id}
        response = requests.get(url, json=data)

        print("Response Content:", response.content)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            result = response.json()
            print("Response Content:", response.content)
            if 'error' in result:
                messagebox.showerror("Error", f"Microservice error: {result['error']}")
                print("Microservice error:", result['error'])
            else:
                dog_data = result.get('dog_data', {})
                print("Fetched Dog Data:", dog_data)
                self.populate_dog_fields(dog_data)
        else:
            messagebox.showerror("Error", "Microservice error")

def populate_dog_fields(self, dog_data):
        # Populate entry fields with the retrieved data
        self.dog_name_info.config(text=dog_data.get('dogName', ''))
        self.dog_size_info.config(text=dog_data.get('dogSize', ''))
        self.dog_age_info.config(text=dog_data.get('dogAge', ''))
        self.home_zip_info.config(text=dog_data.get('homeZip', ''))
        self.best_times_info.config(text=dog_data.get('playTimes', ''))