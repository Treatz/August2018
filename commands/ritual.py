from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdRitual(MuxCommand):

    """
       +Ritual - Used to start a ritual.

       Usage:
         +ritual

       Can be used before casting a spell.

    """
    help_category = "Skills"
    auto_help = True

    key = "+ritual"
    locks = "cmd:all()"

    def func(self):

        if self.caller.ndb.ritual:
            self.caller.msg("You are already in a ritual.")
            return
        if not self.caller.db.meritual or not self.caller.db.roomritual:
            self.caller.msg("Please use @setritual to describe your magic.")
            return

        if(self.caller.db.magic_fuel > self.caller.db.belief):
            self.caller.msg("You can't add anymore energy to this ritual.")
            return
        wins = 0
        if(not self.caller.ndb.ritual):
            for x in range(0, self.caller.db.rituals + self.caller.db.intelligence):
                roll = roll_dice(1,10)
                if(roll > 5):
                    wins += 1
            if(wins < 4):
                self.caller.msg("Your ritual fails.")
                return
            self.caller.ndb.ritual = 1
            self.caller.msg(self.caller.msg("You start the ritual."))
            self.caller.location.msg_contents("%s begins his ritual." % self.caller, exclude = self.caller, from_obj=self.caller)
            self.caller.location.msg_contents(self.caller.db.roomritual, from_obj=self.caller)
            yield 15
            if self.caller.ndb.ritual == 0:
                return
            self.caller.msg("You continue your ritual.")
            self.caller.location.msg_contents("%s continues the ritual." % self.caller, exclude=self.caller, from_obj=self.caller)
            yield 15
            if self.caller.ndb.ritual == 0:
                return
            self.caller.msg("You finish your ritual.")
            self.caller.location.msg_contents("%s closes the ritual." % self.caller, exclude=self.caller, from_obj=self.caller)
            self.caller.ndb.ritual = 0
            self.caller.db.magic_fuel += 1
