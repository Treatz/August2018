from evennia.commands.default.muxcommand import MuxCommand


class CmdMeditate(MuxCommand):
    """
       +Meditate - Regenerates quintessence.

       Usage:
         +Meditates

       Can only be used on yourself..

    """
    auto_help = True
    key = "+meditate"
    locks = "cmd:all()"
    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are already meditating.")
            return

        if not self.caller.db.med:
            self.caller.db.med = 1
            self.caller.msg("You begin meditaing.")
            yield 30
            if self.caller.db.med == 0:
                return
            self.caller.db.med = 0
            if self.caller.db.avatar > self.caller.db.quintessence:
                self.caller.db.quintessence += 1
                self.caller.msg("You generate 1 point of quintessence.")
        else:
            self.caller.msg("You need to wait a while before you can do that again.")