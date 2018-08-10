from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdCharisma(MuxCommand):

    """
       +Charisma - Used to influence another character.

       Usage:
         +charisma <target> = <message>

       Requires some role playing on everyones part..

    """

    help_category = "Skills"
    auto_help = True

    key = "+charisma"
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
        hit =  self.caller.search(self.lhs)

        account = self.caller.db.manipulation + self.caller.db.charisma + self.caller.db.appearance
        target = hit.db.manipulation + hit.db.charisma + hit.db.appearance
        wins = 0
        wins2 = 0
        for x in range(0, account):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        for y in range(0, target):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins2 += 1
        if wins > wins2:
            hit.msg("|g[RP]:|W %s is very charming as he says, \"%s\"" % (self.caller, self.rhs))
            self.caller.msg("|g[RP]:|W You are charming when you say, \"%s\"" % self.rhs)
        if wins < wins2:
            hit.msg("%s says, \"%s\"" %(self.caller, self.rhs))
            self.caller.msg("You say,\"%s\"" % self.rhs)
        self.caller.location.msg_contents(("%s says, \"%s\"" % (self.caller, self.rhs)), exclude=(self.caller, hit))
