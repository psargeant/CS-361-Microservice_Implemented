import pymysql
from tkinter import messagebox

class UserManager:
    user_id = None

    @classmethod
    def get_user_id(cls):
        return user_id


    def handle_login(self, username, password, login_window):
        db_host = "localhost"
        db_port = 3306
        db_user = "root"
        db_password = "root"
        db_name = "dogdatabase"

        connection = None
        cursor = None

        try:
            connection = pymysql.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            cursor = connection.cursor()

            query = "SELECT * FROM users WHERE email = %s AND passwordHash = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Login Successful", f"Welcome to PupDate, {username}!")
                login_window.destroy()  # Close the login window
                UserManager.user_id = user['userID']  # Set the class variable
                return UserManager.user_id

            else:
                messagebox.showerror("Login Failed", "Incorrect username or password. Please try again.")
                return None

        except pymysql.err.MySQLError as error:
            messagebox.showerror("Database Error", f"MySQL Error: {error}")
            return None

        except pymysql.err.IntegrityError as integrity_error:
            messagebox.showerror("Integrity Error", f"Integrity Error: {integrity_error}")
            return None

        finally:
            if cursor:
                cursor.close()
            if connection and connection.open:
                connection.close()

# Create an instance of UserManager
user_manager = UserManager()

# Example usage for testing
if __name__ == "__main__":
    result = user_manager.handle_login("example", "password", None)
    if result is not None:
        print("Login Successful. UserID:", result)

    # Now you can access the userID without calling handle_login again
    user_id = user_manager.get_user_id()
    print("User ID:", user_id)
