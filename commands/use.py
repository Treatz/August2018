from evennia.commands.default.muxcommand import MuxCommand


class CmdUse(MuxCommand):

    """
       +Use - Use luck or the luck of a charmed object.

       Usage:
         +use <target>

       Can be increased if used again.

    """

    key = "+use"
    locks = "cmd:all()"
    help_category = "Magic"
    auto_help = True
    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.prime:
            self.caller.msg("This requires knowledge of the prime sphere.")
            return

        if(self.args == 'luck' or self.args == 'Luck'):
            if(self.caller.db.burned <= self.caller.db.luck):
                self.caller.msg("You sacrifice some of your natural luck.")
                self.caller.db.burned = self.caller.db.burned + 1
                self.caller.db.blessed = self.caller.db.blessed + 1
            else:
                self.caller.msg("You have burned up all of your natural luck.")
            return

        if(self.args == 'Willpower' or self.args == 'willpower'):
            if(self.caller.db.autopoint > 0):
                self.caller.msg("You can only spend one point of willpower at a time.")
                return
            if(self.caller.db.used_will <= self.caller.db.willpower):
                self.caller.msg("You add a point of willpower to your pool.")
                self.caller.db.used_will += 1
                self.caller.db.autopoint += 1
            else:
                self.caller.msg("You have used up all of your willpower.")
            return

        if(self.args == 'Quintessence' or self.args == 'quintessence'):
            if(self.caller.db.magic_fuel >= 3):
                self.caller.msg("You can't spend anymore quintessence at this time.")
                return
            if(self.caller.db.quintessence > 0):
                self.caller.msg("You add a point of your quintessence to your magic pool.")
                self.caller.db.quintessence -= 1
                self.caller.db.magic_fuel += 1
            else:
                self.caller.msg("You have used up all of your quintessence.")
            return

        hit =  self.caller.contents
        for item in hit:
            if item.key == self.args:
                if item.db.charm:
                    item.db.charm = item.db.charm - 1
                    self.caller.msg("You use some of the luck in %s." % item)
                    self.caller.db.blessed = self.caller.db.blessed + 1
                else:
                    self.caller.msg("There is no luck left in %s." % item)
            else:
                self.caller.msg("You don't have that.")
