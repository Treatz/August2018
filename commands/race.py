from evennia.commands.default.muxcommand import MuxCommand


class CmdRace(MuxCommand):

    """
       +rush - Increase your speed using forces.

       Usage:
         +rush

       Speeds up your movement with forces.

    """

    key = "+rush"
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

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.forces:
            self.caller.msg("This spell requires knowledge of the forces sphere.")
            return
        wins = 0
        bonus = 0
        if(self.caller.db.sign == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.zodiac == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.alignment == "Mars"):
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
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.forces, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.forces, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.forces):
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
        if(self.caller.db.rush >= 0 and self.caller.db.rush <= 6):
            self.caller.db.rush = self.caller.db.rush + 1
            if self.caller.db.move_speed == "stroll":
                self.caller.db.move_speed = "walk"
            elif self.caller.db.move_speed == "walk":
                self.caller.db.move_speed = "run"
            elif self.caller.db.move_speed == "run":
                self.caller.db.move_speed = "sprint"
            elif self.caller.db.move_speed == "sprint":
                self.caller.db.move_speed = "zoom"
            self.caller.msg("You are moving faster!")
