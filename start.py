import uuid
import hashlib
import getpass
import random
import string
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import smtplib
import ssl
import getpass
from email.mime.text import MIMEText


# Gererer un mdp (Yann)
def hash_password(password):
    # uuid is used to generate a random number of the specified password
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(8))

hashed_password = hash_password(password)

# Start un server FTP
username = "user"
authorizer = DummyAuthorizer()
authorizer.add_user(username, password, "./", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()

# Send un mail avec le mdp et le username

msg = MIMEText("Messages transmis")

context = ssl.create_default_context()

msg['Subject'] = 'Gros puant'
password = getpass.getpass(prompt='Password: ')
password = "pythonFormation"

with smtplib.SMTP_SSL("ssl0.ovh.net", 587, context=context) as server:
    server.connect('ssl0.ovh.net', 587)
    server.login("isitech@benke.fr", password)
    server.sendmail("yann.bonnaudo@ecole-isitech.fr",
                    ["rabire.hakim@ecole-isitech.fr"], {username, password})
    server.quit()
