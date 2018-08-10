from evennia import default_cmds


class CmdCommand(default_cmds.MuxCommand):
    """
       +command - Forces a character to do something.
    
       Usage: 
        +command <character> = <command>
    
       Forces someone else into doing an action.
    
    """
    key = "+Command"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        """confirms the target and initiates the search"""
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.mind:
            self.caller.msg("This spell requires knowledge of the mind sphere.")
            return
        wins = 0
        bonus = 0
        if(self.caller.db.sign == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.zodiac == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.alignment == "Neptune"):
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
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.mind, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.mind, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.mind):
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
        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.lhs, global_search=True)
        # initialize a list to store rooms we've visited
        detect = self.target.db.perception + self.target.hit.db.awareness
        see = 0
        for x in range(1,detect):
            l = roll_dice(1,10)
            if l >= 6:
                see += 1
        if(see >= 1 and not self.caller == self.target):
            self.target.msg("%s has cast a spell on you!" % self.caller)
            
        self.target.execute_cmd(self.rhs)
        
