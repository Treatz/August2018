from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.characters import Character
import datetime

class CmdSlog(MuxCommand):
    """
       +slog - List spells ready to be cast.

       Usage:
         +slog
       List spells in que..

    """
    key = "+slog"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.rituals:
            self.caller.msg("No spells in buffer")
        cnt = 0
        for entry in self.caller.db.rituals:
            self.caller.msg("|/(%i) %s |/%s|/%s|/" % (cnt, entry[0], entry[1], entry[2]) )
            cnt += 1

