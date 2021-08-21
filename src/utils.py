import random
from os import path
from time import localtime, strftime

import face_recognition

from src.constants import PHOTOS_PATH

PEOPLE = [
    # Tenant
    "john-01.jpg",
    "john-02.jpg",
    "john-03.jpg",

    # Visitor
    "grace-01.jpeg",
    "grace-02.jpeg",
    "grace-03.jpeg",

    # Tenant
    "mary-01.jpg",
    "mary-02.jpg",
    "mary-03.jpg",

    # Visitor
    "phillip-01.jpeg",
    "phillip-02.jpeg",
    "phillip-03.jpeg",

    # Tenant
    "joseph-01.jpg",
    "joseph-02.jpg",
    "joseph-03.jpg",
]

# PEOPLE = [
#     # Tenant
#     "john-01.jpg",
#     "john-02.jpg",
#     "john-03.jpg",
#
#     # Visitor
#     "paul-01.jpg",
#     "paul-02.jpg",
#     "paul-03.jpg",
#
#     # Visitor
#     "grace-01.jpg",
#     "grace-02.jpg",
#     "grace-03.jpg",
#
#     # Tenant
#     "mary-01.jpg",
#     "mary-02.jpg",
#     "mary-03.jpg",
#
#     # Visitor
#     "phillip-01.jpg",
#     "phillip-02.jpg",
#     "phillip-03.jpg",
#
#     # Visitor
#     "jane-01.jpg",
#     "jane-02.jpg",
#     "jane-03.jpg",
#
#     # Visitor
#     "matheo-01.jpg",
#     "matheo-02.jpg",
#     "matheo-03.jpg",
#
#     # Tenant
#     "joseph-01.jpg",
#     "joseph-02.jpg",
#     "joseph-03.jpg",
#
#     # Visitor
#     "claire-01.jpg",
#     "claire-02.jpg",
#     "claire-03.jpg"
# ]


def generate_log_filename():
    current_date = strftime("%d-%m-%Y_%H-%M", localtime())
    return f'log-{current_date}.txt'


def get_encoded_photo_by_name(filename):
    full_path = path.join(PHOTOS_PATH, filename)
    photo = face_recognition.load_image_file(full_path)
    return face_recognition.face_encodings(photo)[0]


def get_random_encoded_photo():
    random_photo = random.choice(PEOPLE)
    return get_encoded_photo_by_name(random_photo)
