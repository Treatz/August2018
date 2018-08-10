from evennia.contrib.slow_exit import CmdSetSpeed

class CmdFaster(CmdSetSpeed):

    key = "faster"

    def func(self):
        """
        Simply sets an Attribute used by the SlowExit above.
        """

        if self.caller.db.move_speed == "stroll":
            self.caller.db.move_speed = "walk"
        elif self.caller.db.move_speed == "walk":
            self.caller.db.move_speed = "run"
        elif self.caller.db.move_speed == "run":
            self.caller.db.move_speed = "sprint"

        self.caller.msg("You are now %sing." % self.caller.db.move_speed)

    pass

class CmdSlower(CmdSetSpeed):

    key = "slower"

    def func(self):
        """
        Simply sets an Attribute used by the SlowExit above.
        """

        if self.caller.db.move_speed == "sprint":
            self.caller.db.move_speed = "run"
        elif self.caller.db.move_speed == "run":
            self.caller.db.move_speed = "walk"
        elif self.caller.db.move_speed == "walk":
            self.caller.db.move_speed = "stroll"

        self.caller.msg("You are now %sing." % self.caller.db.move_speed)

    pass