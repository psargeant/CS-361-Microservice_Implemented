# CS361
Software project for CS361
Software to facilitate doggie play dates local to the user's zipcode

for my microservice from my partner, I need it to be able to gather and populate the dog data when the user, clicks on the option to view their dogs profile (this doesn't exist yet but it will next weekend) the code exists here that sends the original data to the table so hopefully that will help

Installs needed for the backend database communication microservices:
    RabbirMQ

imports to the GUI handler:
    tkinter as tk
    from tkinter import messagebox
    import requests

imports to send_dog_info_ms.py, send_user_info_ms.py, retrieve_dog_info_ms.py and retrieve_info_ms.py
    mysql.connector
    from flask import Flask, request, jsonify
    import pika

imports to the login verification login_ms.py (involves retrieval from the database)
    mysql.connector
    from flask import Flask, request, jsonify

I put all of the calls into single file so my partner won't have to scroll through the GUI looking for them to see what they look like. The call to retrieve information when the Enter button is clicked after entering login info will attach to the def handle_successful_login(self, user_id) and will base the SQL queries on the use_id that is returned by the login microservice. The calls_to_microservice.py file is NONFUNCTIONAL, it is just to show the current calls to the microservices and how they are attached to buttons in the GUI - The call to open the profile page with all of the info is linked to the def handle_successful_login method rather than specifically a command invoked by pressing a button. The button to create matches exists on the program page but it has not command attached to it at all. You can see what the commands look like attached to a button when you look at the enter_button in the calls_to_microservice.py file.

The five files that are currently handling data microservices are send_user_info_ms.py, send_dog_info_ms.py, retrieve_dog_info_ms.py, retrieve_info_ms.py and buttons_ms.py all files are current and files no longer being used have been removed. The buttons_ms.py file is not necessary for testing purposes. Each microservice that sends data runs through a different port to avoid collisions. 

I think that covers everything. I have noticed the retrieval is a little slow, probably becuase I have too many microservices for the simplicity of the project but I am not sure how to combine the send and retrieve microservices because every time I do, they seem to get the wrong messages sent. I will keep refining next week. 

