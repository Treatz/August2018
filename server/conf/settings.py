"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/coret/Desktop/mud-devel/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Mage: the Ascension"

#SLOW EXITS#
#BASE_EXIT_TYPECLASS = "evennia.contrib.slow_exit.SlowExit"

MULTISESSION_MODE=0

######################################################################
# Django web features
######################################################################
INSTALLED_APPS += ('web.chargen',
		'web.character',
                'web.ff',)
DEBUG = False
# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = 'Tg"%FpD1+Px_sy0eIobz*92H)S@,jOE6|R=Y;~Vc'

TELNET_PORTS = [4000]
# The webserver sits behind a Portal proxy. This is a list
# of tuples (proxyport,serverport) used. The proxyports are what
# the Portal proxy presents to the world. The serverports are
# the internal ports the proxy uses to forward data to the Server-side
# webserver (these should not be publicly open)
WEBSERVER_PORTS = [(80, 8808)]
# Ports to use for SSH
SSH_PORTS = [8028]
# Ports to use for SSL
SSL_PORTS = [4028]
# The game server opens an AMP port so that the portal can
# communicate with it. This is an internal functionality of Evennia, usually
# operating between two processes on the same machine. You usually don't need to
# change this unless you cannot use the default AMP port/host for
# whatever reason.
AMP_HOST = 'localhost'
AMP_PORT = 9999
AMP_INTERFACE = '127.0.0.1'
# Server-side websocket port to open for the webclient.
WEBSOCKET_CLIENT_PORT = 8308

######################################################################
# Contrib config
######################################################################
TIME_FACTOR = 4.0
TIME_GAME_EPOCH = 0
TIME_ZONE = "EST"

GAME_INDEX_LISTING = {
    'game_status': 'pre-alpha',
    # Optional, comment out or remove if N/A
    'game_website': 'http://www.streetwitch.com',
    'short_description': 'Graphical online rpg based on Mage: the Ascension.',
    # Optional but highly recommended. Markdown is supported.
    'long_description': (
        "People have said that Mage: the Ascension could never be a MUD..<br><br>"
        "Let's prove them wrong!<br><br>The server is always open through the webclient. "
        "But we only role play when all our schedules are free.<br>"
        "Before you login, make a character with the web chargen: <a href=\"http://mud.streetwitch.com/chargen/\">http://www.streetwitch.com/chargen</a>"    
        "<br>Without the web client graphics will not be vissible, but you still can telnet into the game as usual."),
    'listing_contact': 'adventmagic@gmail.com',
    # At minimum, specify this or the web_client_url options. Both is fine, too.
    'telnet_hostname': 'mud.streetwitch.com',
    'telnet_port': 4000,
    # At minimum, specify this or the telnet_* options. Both is fine, too.
    'web_client_url': 'http://www.streetwitch.com/webclient',
}

