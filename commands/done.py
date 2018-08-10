from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.characters import Character
from evennia import default_cmds
import datetime

class CmdDone(MuxCommand):
    """
       +done - Approve the spell.

       Usage:
         +done <entry>

       cast the accounts spell.

    """
    key = "+done"
    locks = "cmd:all()"
    auto_help=False
    def func(self):

        self.caller.db.rituals.pop(int(self.args))
        self.caller.msg("Spell completed!")
