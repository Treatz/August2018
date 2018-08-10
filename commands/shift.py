from evennia.commands.default.muxcommand import MuxCommand


class CmdShift(MuxCommand):

    """
       +Shift - Changes you into an animal.

       Usage:
         +shift <form>

       Changes your appearance but not your stats.

    """

    key = "+shift"
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
            self.caller.msg("You must suply a form to change to.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.life:
            self.caller.msg("This spell requires knowledge of the life sphere.")
            return
        bonus = 0
        if(self.caller.db.sign == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.zodiac == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.alignment == "Venus"):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(bonus > 0):
            if bonus == 1:
                self.caller.msg("The stars are aligned with you!")
            if bonus == 2:
                self.caller.msg("You are channeling cosmic energies!")
            if bonus == 3:
                self.caller.msg("Your magic is fueld by the planets!")
        wins = 0
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.life, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.life, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.life):
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
        if self.args == "cat":
            self.caller.ndb.nameSave = self.caller.key
            self.caller.key = "A black cat"
            self.caller.ndb.descSave = self.caller.db.desc
            self.caller.db.desc = "A good kitty."
            self.caller.ndb.imageSave = self.caller.db.image
            self.caller.db.image = "http://www.germantownvet.com/wp-content/uploads/2016/11/Cat-Dandruff-300x223.jpg"
            self.caller.msg("You now appear as %s." % self.caller.key)
            self.caller.db.form = "cat"

        if self.args == "dog":
            self.caller.ndb.nameSave = self.caller.key
            self.caller.key = "A dog"
            self.caller.ndb.descSave = self.caller.db.desc
            self.caller.db.desc = "A good doggy."
            self.caller.ndb.imageSave = self.caller.db.image
            self.caller.db.image = "https://s-media-cache-ak0.pinimg.com/236x/ef/ed/c1/efedc1948b3902ace1a16b2127672cd7--white-photography-sled-dogs.jpg"
            self.caller.msg("You now appear as %s." % self.caller.key)
            self.caller.db.form = "dog"
