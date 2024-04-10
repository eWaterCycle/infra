"""Script to generate passwords for users.
    
```shell
cat usernames.txt
user1
user2
```

```
python3 create_student_passwords.py < usernames.txt > students.txt
```

"""

from secrets import token_urlsafe

password_length = 32

def main():
    usernames = []
    while True:
        try:
            line = input()
            if not line:
                break
            usernames.append(line.strip())
        except EOFError:
            break
    userpws = [':'.join([username, token_urlsafe(password_length)]) for username in usernames]
    print(','.join(userpws))

main()
