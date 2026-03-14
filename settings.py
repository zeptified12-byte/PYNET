import os

SERVER_IP = '0.0.0.0' # Listens on all interfaces
BIND_IP = '145.40.129.8' # IP for bots to connect to
BOT_PORT = 9099
COMMAND_PORT = 1337
WEB_PORT = 80
DB_URI = 'file:/storage/emulated/0/Android/data/com.termux/files/' # Location of database file, it will be created if it doesn't exist (change this)
PATH = os.path.dirname(__file__)
PUBLIC = os.path.join(PATH, 'public')
