import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infoclub.settings')

import django
django.setup()

import random
from signup.models import SignUp
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        name = fakegen.name().split()
        fake_fname = name[0]
        fake_lname = name[1]
        fake_email = fakegen.email()

        fake_entry = SignUp.objects.get_or_create(first_name = fake_fname, last_name = fake_lname, email = fake_email)[0] 
    return

if __name__ == '__main__':
    print("[*] Populating script running.....")
    populate(20)        #Generate 20 records
    print("[+] Population Successful!")
