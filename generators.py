from faker import Faker
import random
import string

fake = Faker()

def email_generator():
    return fake.email()

def password_generator():
    return fake.password()

def name_generator():
    return fake.first_name()