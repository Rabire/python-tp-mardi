import uuid
import hashlib
import getpass
import random
import string
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

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

