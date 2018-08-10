from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdStealth(MuxCommand):

    """
       +Stealth - Move through exits unseen.

       Usage:
         +stealth

       Seperate from the invisibility spell.

    """

    help_category = "Skills"
    auto_help = True

    key = "+stealth"
    locks = "cmd:all()"

    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        self.caller.msg("You are now moving silently")
        self.caller.ndb.sneak = 1
        yield 60
        self.caller.msg("You have stopped sneaking")
        self.caller.ndb.sneak = 0
