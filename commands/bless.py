
from evennia.commands.default.muxcommand import MuxCommand

class CmdBless(MuxCommand):

    """
       +Bless - Increases your luck at everything.
       Usage:
         +bless <target>
       Can be increased if used again.
    """

    key = "+bless"
    locks = "cmd:all()"
    help_category = "Magic"
    auto_help = True
    def func(self):
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

        if not self.caller.db.entropy:
            self.caller.msg("This spell requires knowledge of the entropy sphere.")
            return
        wins = 0
        bonus = 0
        if(self.caller.db.sign == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.zodiac == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.alignment == "Mercury"):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(bonus > 0):
            if bonus == 1:
                self.caller.msg("The stars are aligned with you!")
            if bonus == 2:
                self.caller.msg("You are channeling cosmic energies!")
            if bonus == 3:
                self.caller.msg("Your magic is fueld by the planets!")
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.entropy, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.entropy, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.entropy):
            roll = roll_dice(1,10)
            if(roll > 5 - self.caller.db.magic_fuel):
                wins += 1
        wins = wins + self.caller.db.autopoint
        if(self.caller.db.autopoint):
            self.caller.msg("You have %s successes out of 4 needed, using a point of willpower" % wins)
        else:
            self.caller.msg("You have %s successes out of 4 needed." % wins)
        self.caller.db.magic_fuel = 0
        self.caller.db.autopoint = 0
        if wins < 4:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        hit =  self.caller.search(self.args)

        if hit == self.caller:
                if hit.db.blssed >= 0:
                   hit.db.blessed = hit.db.blessed +1
                   hit.msg("You are blessed")
                elif hit.db.blessed < 0:
                    hit.db.blessed = 0
                    hit.msg("You are no loner hexed")
        if not self.caller == hit:
               if hit.db.blessed >= 0:
                  hit.db.blessed = hit.db.blessed + 1
                  self.caller.msg("You bless %s." % hit)
                  hit.msg("You are blessed")
               elif hit.db.blessed < 0:
                   hit.db.blessed = 0
                   hit.msg("You are no longer hexed")
                   self.caller.msg("%s is no longer blessed." % hit)
        detect = hit.db.perception + hit.db.awareness
        see = 0
        for x in range(1,detect):
            l = roll_dice(1,10)
            if l >= 6:
                see += 1
        if(see >= 1 and not self.caller == hit):
            hit.msg("%s has cast a spell on you!" % self.caller)
        yield 60
        self.msg("Your luck has faded.")
        self.db.blessed = 0
