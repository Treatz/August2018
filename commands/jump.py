from evennia import default_cmds
from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.rooms import Room
class CmdJump(default_cmds.MuxCommand):
    """
       +jump - Teleport to a room.

       Usage:
        +jump <args>

       Travel to another locaion.

    """
    key = "+jump"
    locks = "cmd:all()"
    help_category = "Magic"
    auto_help = True
    maxdepth = 4

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

        if not self.caller.db.correspondence:
            self.caller.msg("This spell requires knowledge of the correspondence sphere.")
            return
        wins = 0
        bonus = 0
        if(self.caller.db.sign == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.zodiac == self.caller.db.starsign):
            self.caller.db.magic_fuel += 1
            bonus += 1
        if(self.caller.db.alignment == "Jupiter"):
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
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.correspondence, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.correspondence, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.correspondence):
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
        self.target = self.caller.search(self.args, global_search=True, typeclass=Room)

        # initialize a list to store rooms we've visited
        self.visited = []
        if not self.args:
            self.caller.msg("You must search for something.")
            return
        # now start the search, passing in depth=0
        if not self._searcher(self.caller.location, 0):
            # give the 'not found' message
            self.caller.msg("You are unable to determine which way to go.")

    def _searcher(self, room, depth):
        """Searches surrounding rooms recursively for an object"""

        # first, record that we've been here
        self.visited.append(room)

        # our end condition is either when the item is found...
        if self.target == room:
            self.caller.move_to(room)
            self.caller.msg("You teleport!")
            return True

        # or we have traveled `maxdepth` rooms away
        if depth > self.maxdepth:
            return False

        # it's not in the current room, so loop through the exits and check them,
        # skipping rooms we've already visited
        exits = [exit for exit in room.exits if exit.destination not in self.visited]
        for next in exits:
            if depth == 0:  # we only want to return the exit out of the current room
                self.direction = next.key
            if self._searcher(next.destination, depth + 1):  # if we found the object, stop searching
                return True

        # we've checked all the exits, so return false
        return False
