# File Name : OllieMcLellan_FinalProject
# Student Name: Leah Radcliffe, Alisha Siddiqui, Daquan Daniels
# email:  radclilr@mail.uc.edu, siddiqas@mail.uc.edu, danialdu@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 5/1/25
# Course #/Section:  IS401001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: decrypts a hidden team location and a movie title using data from files, then displays a team photo.

from cryptography.fernet import Fernet
import json
import os

def display_photo():
    os.startfile("team_photo.jpg")  



def decrypt_team_location():
    with open('UCEnglish.txt', 'r') as f:
        words = f.readlines()

    with open('EncryptedGroupHints Spring 2025.json', 'r') as f:
        data = json.load(f)

    indices = data["Ollie McLellan"]
    location = ' '.join([words[int(i)].strip() for i in indices])
    print(" Decrypted Location:\n", location)

def decrypt_movie():
    encrypted = "gAAAAABn9tC14lyaNa1eJI9cjNKQBGgtcxk5KgiBzqWuhjGKKu-NgQ7h11XgLDwy5O9j0sAeC-2AE6Z7Luikzy1yX4M7L0dd9Mu17a7ZzC5Q2NGmdAuSA8E="
    key = b"zM3D9i6IrhRGyBDOgB25TwXk371iZpnAmG6EbmbDRik="
    f = Fernet(key)
    movie = f.decrypt(encrypted.encode()).decode()
    print(" Decrypted Movie Title:\n", movie)



if __name__ == "__main__":
    decrypt_team_location()
    decrypt_movie()
    display_photo()



