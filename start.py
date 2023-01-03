from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Gererer un mdp (Yann)
password = "pass"

# Start un server FTP
username = "user"
authorizer = DummyAuthorizer()
authorizer.add_user(username, password, "./", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()

# Send un mail avec le mdp et le username

