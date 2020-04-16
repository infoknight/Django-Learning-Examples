import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackerscafe.settings')

import django
django.setup()

import random
from cafe.models import signupModel
from faker import Faker

fakegen = Faker()

def populate(N=5):
    count = 0
    for entry in range(N):
        name = fakegen.name().split()
        fake_fname = name[0]
        fake_lname = name[1]
        fake_email = fakegen.email()
        fake_vmail = fake_email         #Keep as same else will raise error
    
        fake_entry = signupModel.objects.get_or_create(first_name = fake_fname, last_name = fake_lname, email = fake_email, verify_email = fake_vmail)[0]
        count = count + 1
    return count

if __name__ == "__main__":
    print("[*] Populating the model with fake data...")
    count = populate(20)
    print("[+] Populating completed successfully!")
    print("[*] Populated " + str(count) + " fake records")
