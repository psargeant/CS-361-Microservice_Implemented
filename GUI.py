import tkinter as tk
from buttons import help_buttons, BackButton, NextButton
from tkinter import messagebox
from common_classes import (LabelDropdownMenu, Tooltip, Styles, create_label, create_entry, create_label_frame,
                            create_profile_label, create_profile_info_display_label, create_profile_info_frame)
import requests
import bcrypt
import base64


def hash_and_encode_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    encoded_password = base64.b64encode(hashed_password).decode('utf-8')
    return encoded_password


def show_save_message(parent):
    print("check 3")
    save_message = tk.Toplevel(parent)
    save_message.geometry("300x300")
    message_label = tk.Label(save_message, text="Your data \nhas been \nsaved!", font=("Century Gothic", 28))
    message_label.pack(expand=True)


class StartWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Start Window")
        self.user_id = None

        main_label_frame = tk.Frame(self, padx=20, pady=20)
        main_label_frame.pack()
        label1 = tk.Label(
            main_label_frame, text="PupDate, the (play)Dating App for your best friend!",
            font=("Century Gothic", 26),
            fg="black",
            justify=tk.CENTER
        )
        label1.pack(side=tk.TOP, pady=10)
        label2 = tk.Label(
            main_label_frame,
            text="An app for helping you and your beloved pet connect to \nother "
                 "owners for playdates. Great for pup socialization, \nexercise "
                 "and your connection to other owners to share \n "
                 "doggie insights, advice, etc.",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.CENTER
        )
        label2.pack(side=tk.TOP, pady=30)

        large_button_frame = tk.Frame(self, padx=200, pady=100)
        large_button_frame.pack()

        button_NU = tk.Button(
            large_button_frame,
            text="New \n User",
            bg="gray", fg="black",
            font=("Century Gothic", 30),
            relief="solid",
            width=5,
            height=2,
            command=self.open_registration_window
        )
        button_NU.pack(side=tk.LEFT, padx=60)

        button_Login = tk.Button(
            large_button_frame,
            text="Login",
            bg="gray",
            fg="black",
            font=("Century Gothic", 30),
            relief="solid",
            width=5,
            height=2,
            command=self.open_login_window
        )
        button_Login.pack(side=tk.RIGHT, padx=60)

        help_frame = tk.Frame(self, padx=10, pady=160)
        help_frame.pack()
        help_buttons(help_frame)

    def open_registration_window(self):  # This & similar functions are not in the tooltips, etc. file for 2 reasons;
        # it only saved one line of code each & it introduces circular imports into the system that I don't have a way
        # around
        RegistrationWindow(self)
        self.withdraw()

    def open_login_window(self):
        LoginWindow()
        self.withdraw()


class RegistrationWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.user_id = None
        self.geometry("1000x1000")
        self.title("Registration Window")

        welcome_label = tk.Label(
            self,
            text="Welcome! We are so happy you have \ndecided to become part of our community.\n"
                 "Please fill in the information below to start creating your account.",
            font=("Century Gothic", 20),
            fg="black",
            justify=tk.CENTER
        )
        welcome_label.pack(side=tk.TOP, pady=25)

        fn_frame = create_label_frame(self)
        fn_label = create_label(fn_frame, text="First Name")
        self.fn_entry = create_entry(fn_frame)

        ln_frame = create_label_frame(self)
        ln_label = create_label(ln_frame, text="Last Name")
        self.ln_entry = create_entry(ln_frame)

        email_frame = create_label_frame(self)
        email_label = create_label(email_frame, text="Email")
        self.email_entry = create_entry(email_frame)

        def show_pw_requirement():
            requirements = ("Password Requirements:\n"
                            "- Minimum length: 8 characters\n"
                            "- Maximum length: 10 characters\n"
                            "- At least one uppercase letter\n"
                            "- At least one lowercase letter\n"
                            "- At least one number\n"
                            "- At least one special character")
            messagebox.showinfo("Password requirements", requirements)

        password_var = tk.StringVar()
        pw_reentry_var = tk.StringVar()

        def on_password_change(*args):
            entered_password = password_var.get()
            if validate_password(entered_password):
                status_label.config(text="Password is valid", fg="green")
            else:
                status_label.config(text="Password requirements not met", fg="red")

        def validate_password(password):
            min_length = 8
            max_length = 20
            has_uppercase = any(c.isupper() for c in password)
            has_lowercase = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_spec_char = not all(c.isalnum() for c in password)
            return min_length <= len(
                password) <= max_length and has_uppercase and has_lowercase and has_digit and has_spec_char

        def on_password_reentry(*args):
            entered_password = password_var.get()
            reentry_password = pw_reentry_var.get()
            if entered_password and reentry_password:
                if entered_password == reentry_password:
                    status_label.config(text="Passwords match", fg="green")
                else:
                    status_label.config(text="Passwords do not match, try again", fg="red")

        def validate_reentry(reentry_password):
            return True

        createpw_frame = tk.Frame(self)
        createpw_frame.pack(pady=15)
        createpw_label = tk.Label(
            createpw_frame,
            text="Create Password",
            font=(Styles.FONT_FAMILY, Styles.FONT_LARGE),
            fg=Styles.FONT_COLOR
        )

        createpw_label.pack(side=tk.LEFT, padx=10)
        self.createpw_entry = tk.Entry(
            createpw_frame,
            width=30,
            bd=2,
            relief=tk.SOLID,
            font=(Styles.FONT_FAMILY, Styles.FONT_LARGE),
            textvariable=password_var, show='*',
            validatecommand=validate_password
        )
        self.createpw_entry.pack(side=tk.RIGHT, padx=10)

        requirements_button = tk.Button(
            createpw_frame,
            text="Show Password Requirements",
            font=(Styles.FONT_FAMILY, Styles.FONT_XSMALL),
            fg=Styles.FONT_COLOR,
            command=show_pw_requirement
        )
        requirements_button.pack(pady=10)

        status_label = tk.Label(
            createpw_frame,
            text="",
            fg="green"
        )
        status_label.pack()

        reenterpw_frame = tk.Frame(self)
        reenterpw_frame.pack(pady=10)
        reenterpw_label = tk.Label(
            reenterpw_frame,
            text="Confirm Password",
            font=(Styles.FONT_FAMILY, Styles.FONT_LARGE),
            fg=Styles.FONT_COLOR
        )
        reenterpw_label.pack(side=tk.LEFT, padx=10)

        self.reenterpw_entry = tk.Entry(
            reenterpw_frame,
            width=30,
            bd=2,
            relief=tk.SOLID,
            font=(Styles.FONT_FAMILY, Styles.FONT_LARGE),
            textvariable=pw_reentry_var, show='*',
            validate="all",
            validatecommand=(self.register(validate_reentry), '%P')
        )
        self.reenterpw_entry.pack(side=tk.RIGHT, padx=10)

        password_var.trace_add("write", on_password_change)
        pw_reentry_var.trace_add("write", on_password_reentry)

        save_button_frame = tk.Frame(self)
        save_button_frame.pack(pady=40)

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

        back_next_button_frame = tk.Frame(self)
        back_next_button_frame.pack(pady=30)

        back_button = BackButton(
            back_next_button_frame,
            command=self.open_start_window
        )
        back_button.pack()

        next_button = NextButton(
            back_next_button_frame,
            command=self.open_addlreg_window
        )
        next_button.pack()

        help_frame = tk.Frame(self, padx=10, pady=30)
        help_frame.pack()
        help_buttons(help_frame)

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

    def open_start_window(self):
        StartWindow()
        self.withdraw()

    def open_addlreg_window(self):
        AddRegistrationWindow(self.user_id)
        self.withdraw()


class AddRegistrationWindow(tk.Toplevel):

    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.RegistrationWindow = parent
        self.geometry("1000x1000")
        self.title("Dog Registration Window")

        welcome_label = tk.Label(
            self,
            text="Please fill in the fields below to create your pup's profile .",
            font=("Century Gothic", 20),
            fg="black",
            justify=tk.CENTER
        )
        welcome_label.pack(side=tk.TOP, pady=15)

        frame_1 = tk.Frame(self)
        frame_1.pack(pady=10)

        inner_frame_1a = tk.Frame(frame_1)
        inner_frame_1a.pack(pady=5, side=tk.LEFT)
        dogname_label = tk.Label(
            inner_frame_1a,
            text="Dog name",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.LEFT
        )
        dogname_label.pack(side=tk.LEFT, padx=10)
        self.dogname_entry = tk.Entry(
            inner_frame_1a,
            width=15,
            bd=2,
            relief=tk.SOLID,
            font=("Century Gothic", 18),
            justify=tk.LEFT
        )
        self.dogname_entry.pack(side=tk.RIGHT, padx=10)

        inner_frame_1b = tk.Frame(frame_1)
        inner_frame_1b.pack(padx=30, pady=5, side=tk.RIGHT)
        contact_options = ["", "Email", "Text"]
        self.contact_dropdown = LabelDropdownMenu(
            inner_frame_1b,
            "Preferred \ncontact \nmethod",
            contact_options,

        )
        self.contact_dropdown.pack(padx=10, pady=5, fill=tk.X)

        frame_2 = tk.Frame(self)
        frame_2.pack(pady=5)

        inner_frame_2a = tk.Frame(frame_2)
        inner_frame_2a.pack(pady=5, side=tk.LEFT)
        age_options = ["", "< 1 year", "1 - 3 years", "4 - 9 years", "> 9 years"]
        self.age_dropdown = LabelDropdownMenu(
            inner_frame_2a,
            "Dog age",
            age_options,

        )
        self.age_dropdown.pack(padx=10, pady=5, fill=tk.X)

        inner_frame_2b = tk.Frame(frame_2)
        inner_frame_2b.pack(padx=30, pady=5, side=tk.RIGHT)
        contact_info_label = tk.Label(
            inner_frame_2b,
            text="Preferred \ncontact \ninformation",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.LEFT
        )
        contact_info_label.pack(side=tk.LEFT, padx=10)
        self.contact_info_entry = tk.Entry(
            inner_frame_2b,
            width=15,
            bd=2,
            relief=tk.SOLID,
            font=("Century Gothic", 18),
            justify=tk.LEFT
        )
        self.contact_info_entry.pack(side=tk.RIGHT, padx=20)

        frame_3 = tk.Frame(self)
        frame_3.pack(pady=5)

        inner_frame_3a = tk.Frame(frame_3)
        inner_frame_3a.pack(pady=5, side=tk.LEFT)
        size_options = ["", "X-small (< 6 lbs)", "Small (6-20 lbs)", "Medium (21-45 lbs", "Large (46-80 lbs)",
                        "X-large (> 80 lbs"]
        self.size_dropdown = LabelDropdownMenu(
            inner_frame_3a,
            "Dog size",
            size_options,

        )
        self.size_dropdown.pack(padx=10, pady=5, fill=tk.X)

        inner_frame_3b = tk.Frame(frame_3)
        inner_frame_3b.pack(padx=30, pady=5, side=tk.RIGHT)
        time_options = ["", "Early AM (before 7)", "Morning (7 - noon)", "Afternoon (noon - 5)", "Evening (5 - 10)"]
        self.time_dropdown = LabelDropdownMenu(
            inner_frame_3b,
            "Best \nplaydate \ntimes",
            time_options,

        )
        self.time_dropdown.pack(padx=10, pady=5, fill=tk.X)

        image_path_upload = r"C:\Users\tresa\Downloads\upload_FILL0_wght400_GRAD0_opsz24.png"
        self.upload_button_image = tk.PhotoImage(file=image_path_upload)

        frame_4 = tk.Frame(self)
        frame_4.pack(pady=5)

        inner_frame_4a = tk.Frame(frame_4)
        inner_frame_4a.pack(pady=5, side=tk.LEFT)
        upload_label = tk.Label(
            inner_frame_4a,
            text="Upload photos of your dog",
            font=("Century Gothic", 18),
            justify=tk.LEFT
        )
        upload_label.pack(side=tk.LEFT, padx=0)

        upload_button = tk.Button(
            inner_frame_4a,
            image=self.upload_button_image
        )
        upload_button.image = self.upload_button_image
        upload_button.pack(side=tk.LEFT, padx=5)

        inner_frame_4b = tk.Frame(frame_4)
        inner_frame_4b.pack(padx=30, pady=5, side=tk.RIGHT)

        zipcode_label = tk.Label(
            inner_frame_4b,
            text="Your zipcode",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.LEFT
        )
        zipcode_label.pack(side=tk.LEFT, padx=10)
        self.zipcode_entry = tk.Entry(
            inner_frame_4b,
            width=15,
            bd=2,
            relief=tk.SOLID,
            font=("Century Gothic", 18),
            justify=tk.LEFT
        )
        self.zipcode_entry.pack(side=tk.RIGHT, padx=20)

        frame_5 = tk.Frame(self)
        frame_5.pack(pady=30)

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

        new_dog_label = tk.Label(
            frame_5,
            text="Would you like to add another dog?",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.LEFT
        )
        new_dog_label.pack(side=tk.LEFT, padx=60)

        yes_button = tk.Button(
            frame_5,
            text="Yes",
            font=("Century Gothic", 20),
            bd=2,
            relief="solid")
        yes_button.pack(padx=5, side=tk.LEFT)

        no_button = tk.Button(
            frame_5,
            text="No",
            font=("Century Gothic", 20),
            bd=2,
            relief="solid")
        no_button.pack(padx=5, side=tk.LEFT)

        back_button_frame = tk.Frame(self)
        back_button_frame.pack(pady=45)

        back_button = BackButton(back_button_frame, command=self.open_registration_window)
        back_button.pack(side=tk.LEFT, padx=100)

        tooltip_dogimage = Tooltip(
            upload_button,
            "You may upload \nup to 3 photos \nwith a max size of \n2MB each"
        )

        help_frame = tk.Frame(self, padx=10, pady=30)
        help_frame.pack()
        help_buttons(help_frame)

    def open_registration_window(self):
        RegistrationWindow(self)
        self.withdraw()

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


class LoginWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Login Window")

        main_label_frame = tk.Frame(self, padx=20, pady=40)
        main_label_frame.pack()
        label = tk.Label(main_label_frame,
                         text="Welcome back! \nPlease enter your username (your email address) \nand password "
                              "to access your account",
                         font=("Century Gothic", 20),
                         fg="black", justify=tk.CENTER)
        label.pack(side=tk.TOP, pady=10)

        login_frame = tk.Frame(self)
        login_frame.pack(pady=110)
        login_frame_a = tk.Frame(login_frame)
        login_frame_a.pack(pady=10, side=tk.LEFT)
        login_frame_b = tk.Frame(login_frame)
        login_frame_b.pack(pady=10, side=tk.RIGHT)

        username_label = tk.Label(
            login_frame_a,
            text="Enter your \nusername",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.CENTER
        )
        username_label.pack(side=tk.LEFT, padx=0)
        self.username_entry = tk.Entry(
            login_frame_a,
            width=30,
            bd=2,
            relief=tk.SOLID,
            font=("Century Gothic", 14),
            justify=tk.LEFT
        )
        self.username_entry.pack(side=tk.RIGHT, padx=10)

        password_var = tk.StringVar()

        password_label = tk.Label(
            login_frame_b,
            text="Enter your \npassword",
            font=("Century Gothic", 18),
            fg="black",
            justify=tk.LEFT
        )
        password_label.pack(side=tk.LEFT, padx=15)
        self.password_entry = tk.Entry(
            login_frame_b,
            width=18,
            bd=2,
            relief=tk.SOLID,
            font=("Century Gothic", 16),
            justify=tk.LEFT,
            textvariable=password_var, show='*', )
        self.password_entry.pack(side=tk.RIGHT, padx=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=30)

        back_button = BackButton(button_frame, command=self.open_start_window)
        back_button.pack(side=tk.LEFT, padx=60)

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

        help_frame = tk.Frame(self, padx=10, pady=165)
        help_frame.pack()
        help_buttons(help_frame)

    def validate_login(self, username, password):
        url = "http://localhost:5002/validate_login"

        data = {'username': username, 'password': password}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                user_id = result.get('user_id')
                self.handle_successful_login(user_id)
                return user_id
            else:
                messagebox.showerror("Error", "Incorrect username or password")
        else:
            messagebox.showerror("Error", "Microservice error")

    def handle_successful_login(self, user_id):
        print(f"User logged in successfully. User ID: {user_id}")
        ProfileWindow(user_id)
        self.withdraw()

    def open_start_window(self):
        StartWindow()
        self.withdraw()


class MatchResultsWindow(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.geometry("400x300")
        self.title("Match Results")

        self.match_results_text = tk.Text(self, height=10, width=50, wrap=tk.WORD)
        self.match_results_text.pack(pady=10)

        close_button = tk.Button(
            self,
            text="Close",
            font=("Century Gothic", 12),
            bd=2,
            relief="solid",
            command=self.destroy_and_return
        )
        close_button.pack(pady=10)

    def destroy_and_return(self):
        self.destroy()


class ProfileWindow(tk.Toplevel):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.LoginWindow = parent
        self.geometry("1000x1000")
        self.title("User & Dog Profile Window")
        print("userID:", user_id)

        welcome_label = tk.Label(
            self,
            text="User & Pup(s) profile information .",
            font=("Century Gothic", 20),
            fg="black",
            justify=tk.CENTER
        )
        welcome_label.pack(side=tk.TOP, pady=20)

        print(f"Data retrieved from the microservice. User ID: {user_id}")


        first_name_frame = create_profile_info_frame(self)
        first_name_label = create_profile_label(first_name_frame, text="First Name:")
        self.first_name_info = create_profile_info_display_label(first_name_frame)

        last_name_frame = create_profile_info_frame(self)
        last_name_label = create_profile_label(last_name_frame, text="Last Name:")
        self.last_name_info = create_profile_info_display_label(last_name_frame)

        contact_info_frame = create_profile_info_frame(self)
        contact_info_label = create_profile_label(contact_info_frame, text="Preferred contact information:")
        self.contact_info = create_profile_info_display_label(contact_info_frame)

        dog_name_frame = create_profile_info_frame(self)
        dog_name_label = create_profile_label(dog_name_frame, text="Pup name:")
        self.dog_name_info = create_profile_info_display_label(dog_name_frame)

        dog_size_frame = create_profile_info_frame(self)
        dog_size_label = create_profile_label(dog_size_frame, text="Pup size:")
        self.dog_size_info = create_profile_info_display_label(dog_size_frame)

        dog_age_frame = create_profile_info_frame(self)
        dog_age_label = create_profile_label(dog_age_frame, text="Pup age:")
        self.dog_age_info = create_profile_info_display_label(dog_age_frame)

        home_zip_frame = create_profile_info_frame(self)
        home_zip_label = create_profile_label(home_zip_frame, text="Home zipcode:")
        self.home_zip_info = create_profile_info_display_label(home_zip_frame)

        best_times_frame = create_profile_info_frame(self)
        best_times_label = create_profile_label(best_times_frame, text="Favorite play time:")
        self.best_times_info = create_profile_info_display_label(best_times_frame)

        view_pup_pics_frame = create_profile_info_frame(self)
        view_pup_pics_label = create_profile_label(view_pup_pics_frame, text="Photos of your pup:")
        self.view_pup_pics_info = create_profile_info_display_label(view_pup_pics_frame)

        # Entry Textbox
        entry_label = tk.Label(self, text="Enter Dog Name:")
        entry_label.pack(pady=10)

        self.entry_var = tk.StringVar(self)
        self.entry_textbox = tk.Entry(self, textvariable=self.entry_var, font=("Century Gothic", 16), bd=2,
                                      relief="solid")
        self.entry_textbox.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(self, text="", font=("Century Gothic", 16))
        self.result_label.pack(pady=10)

        # Match Button
        match_button_frame = tk.Frame(self)
        match_button_frame.pack(pady=20)
        match_button = tk.Button(
            match_button_frame,
            text="Let's make \na match!",
            font=("Century Gothic", 20),
            bd=2,
            relief="solid",
            command=self.make_match_button_click  # Removed lambda
        )
        match_button.pack(padx=5, side=tk.LEFT)

        self.fetch_user_data()
        self.fetch_dog_data()

    def make_match_button_click(self):
        entry = self.entry_var.get()  # Retrieve the text from the Entry widget
        url = "http://localhost:5005/make_match"
        data = {'dog_name': entry}
        response = requests.get(url, json=data)

        print("Response Content:", response.content)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            dog_matches = response.json()  # Assuming the response is a JSON array
            print("Fetched Dog Data:", dog_matches)

            # Open a new window to display match results
            match_results_window = MatchResultsWindow(self)
            match_results_window.match_results_text.insert(tk.END, "Match Results:\n")
            for match in dog_matches:
                compare_dog_name = match.get('compare_dog_name', '')
                percent_match = match.get('percent_match', 0.0)
                match_results_window.match_results_text.insert(tk.END, f"{compare_dog_name} - {percent_match}%\n")

        else:
            messagebox.showerror("Error", "Microservice error")

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


    # Code here to populate user and dog information


if __name__ == "__main__":
    start_window = StartWindow()
    start_window.mainloop()
