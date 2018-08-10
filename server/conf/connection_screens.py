# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
""" |wWelcome to|n 
 |w%s Online|n
 ===================================

 If you have an existing account, 
 connect to it by typing:
 |wconnect <username> <password>|n

 If you need to create an account,|n
 use the character generator:
 |whttp://mud.streetwitch.com/chargen/|n

 To generate a character for you,|n 
 type:
 |wcreate <username> <password>|n

 If you have spaces in your name, 
 enclose it in quotes.
 
 Enter |whelp|n for more info. 
 |wlook|n will re-show this screen.
""" \
 % (settings.SERVERNAME)
