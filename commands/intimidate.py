from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdIntimidate(MuxCommand):

    """
       +Intimidate - Used to scare the target.

       Usage:
         +intimidate <target>

       Can be used before attacking.

    """

    help_category = "Skills"
    auto_help = True

    key = "+intimidate"
    locks = "cmd:all()"

    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        if not self.args:
            self.caller.msg("You must suply a target for this to work.")
            return
        hit =  self.caller.search(self.args)

        init_a = self.caller.db.manipulation + self.caller.db.intimidation
        init_b = hit.db.wits + hit.db.intimidation
        init_a = init_a + roll_dice(1,10)
        init_b = init_b + roll_dice(1,10)

        self.caller.msg("You move closer to %s, intimidating him with a cold expression." % hit)
        hit.msg("%s looks like he is planning to kill you." % self.caller)

        if(init_a > init_b):
            self.caller.db.attacking = 2
            hit.db.intimidated = 1
        else:
            self.caller.db.attacking = 0
            hit.db.intimidated = 0
