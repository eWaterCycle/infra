import random
import string
from passlib.hash import sha512_crypt 

def generate_password(length=16):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

def encrypt_password(password):
    return sha512_crypt.using(rounds=5000).hash(password)


def write_yml(users, filename='users.yml'):
    with open(filename, 'w') as f:
        for user in users:
            f.write(f"- name: {user['username']}\n")
            f.write(f"  # Unhashed password = {user['password']}\n")
            f.write(f"  password: {user['encrypted_password']}\n")

def write_md(users, filename='users.md'):
    with open(filename, 'w') as f:
        for user in users:
            f.write(f"* {user['username']}:{user['password']}\n")


def generate_user(username):
    password =  generate_password()
    encrypted_password = encrypt_password(password)
    return {
        'username': username,
        'password': password,
        'encrypted_password': encrypted_password,
    }

prefix = 'user'
nr_users = 30
users = []
for i in range(nr_users):
    users.append(generate_user(f'{prefix}{i}'))
users.append(generate_user('admin'))

write_yml(users)
write_md(users)
