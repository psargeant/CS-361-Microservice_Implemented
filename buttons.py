import tkinter as tk
from common_classes import Tooltip, Styles
import pika

# File that holds all the buttons for the GUI and their commands/interactions/etc.


class BackButton(tk.Button):
    def __init__(self, parent, command, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(text="Back",
                            font=(Styles.FONT_FAMILY, Styles.FONT_MEDIUM),
                            fg=Styles.FONT_COLOR,
                            bg="gray",
                            relief="solid",
                            width=5,
                            height=1,
                            compound="left",
                            padx=0,
                            anchor="center",
                            command=command)
        self.pack(padx=10, side=tk.LEFT)


class NextButton(tk.Button):
    def __init__(self, parent, command, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(text="Next",
                            font=(Styles.FONT_FAMILY, Styles.FONT_MEDIUM),
                            fg=Styles.FONT_COLOR,
                            bg="gray",
                            relief="solid",
                            width=5,
                            height=1,
                            compound="right",
                            padx=0,
                            anchor="center",
                            command=command)
        self.pack(padx=10, side=tk.RIGHT)


def send_open_mp4_message(file_path):
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='messages')

        message = f'open_mp4_Intro_Video:{file_path}'
        channel.basic_publish(exchange='', routing_key='messages', body=message.encode())

        print(f"Sent message: {message}")

    if connection.is_open:
        connection.close()


def send_open_pdf_message(file_path):
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='messages')

        message = f'open_pdf:{file_path}'
        channel.basic_publish(exchange='', routing_key='messages', body=message.encode())

        print(f"Sent message: {message}")
        print("I have made it this far")

    if connection.is_open:
        connection.close()
        # print("Connection closed")


def open_Intro_Vid():
    intro_Vid_file_path = r"C:\Users\tresa\PycharmProjects\mainProject361\Intro Video.mp4"
    send_open_mp4_message(intro_Vid_file_path)


def open_FAQ():
    faq_file_path = r"C:\Users\tresa\PycharmProjects\mainProject361\FAQ document.pdf"
    send_open_pdf_message(faq_file_path)


def open_Help():
    help_file_path = r"C:\Users\tresa\PycharmProjects\mainProject361\Help document.pdf"
    send_open_pdf_message(help_file_path)


def help_buttons(frame):

    def create_video_button():
        button_Video = tk.Button(frame, text="Intro Video",
                                 bg="gray",
                                 font=(Styles.FONT_FAMILY, Styles.FONT_SMALL),
                                 fg=Styles.FONT_COLOR,
                                 relief="solid",
                                 command=open_Intro_Vid,
                                 width=10,
                                 height=1)
        button_Video.pack(side=tk.LEFT, padx=50)
        tooltip_Video = Tooltip(button_Video, "Quick overview video of \ninitial account \nset-up process and "
                                              "\nfeatures available.")

    def create_FAQ_button():
        button_FAQ = tk.Button(frame, text="FAQ",
                               bg="gray",
                               font=(Styles.FONT_FAMILY, Styles.FONT_SMALL),
                               fg=Styles.FONT_COLOR,
                               relief="solid",
                               command=open_FAQ,
                               width=10,
                               height=1)
        button_FAQ.pack(side=tk.LEFT, padx=50)
        tooltip_FAQ = Tooltip(button_FAQ, "Answers to our most \nfrequently asked \nquestions.")

    def create_help_button():
        button_Help = tk.Button(frame, text="Help",
                                bg="gray",
                                font=(Styles.FONT_FAMILY, Styles.FONT_SMALL),
                                fg=Styles.FONT_COLOR,
                                relief="solid",
                                command=open_Help,
                                width=10,
                                height=1)
        button_Help.pack(side=tk.LEFT, padx=50)
        tooltip_Help = Tooltip(button_Help, "Search our \nknowledge base.")

    def create_contact_button():
        button_Contact = tk.Button(frame,
                                   text="Contact",
                                   bg="gray",
                                   font=(Styles.FONT_FAMILY, Styles.FONT_SMALL),
                                   fg=Styles.FONT_COLOR,
                                   relief="solid",
                                   width=10,
                                   height=1)
        button_Contact.pack(side=tk.LEFT, padx=50)
        tooltip_Contact = Tooltip(button_Contact, "Not finding what \nyou need? \nSend us a message")

    create_video_button()
    create_FAQ_button()
    create_help_button()
    create_contact_button()


if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    help_buttons(frame)

    root.mainloop()
