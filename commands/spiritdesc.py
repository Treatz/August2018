from evennia.commands.default.muxcommand import MuxCommand

class SpiritDesc(MuxCommand):
    key = "@spiritdesc"
    lock = "cmd:all()"

    def func(self):
        if self.lhs:
            obj = self.caller.search(self.lhs)
            if self.rhs:
                sdesc = self.rhs
                obj.db.spiritdesc = sdesc
        if obj.db.desc:
            self.caller.msg("spiritdesc = %s" % obj.db.spiritdesc)