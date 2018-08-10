from evennia import Command
from evennia.utils.evmenu import EvMenu
from evennia.contrib.dice import roll_dice

class CmdAttack(Command):
    """
    initiates combat

    Usage:
      attack <target>

    This will initiate combat with <target>. If <target is
    already in combat, you will recieve an error.
    """
    key = "attack"
    help_category = "General"

    def func(self):
        if self.caller.search(self.args.strip()).db.npc:
           if not self.caller.search(self.args).sessions.all():
               self.caller.msg("Please wait for a story teller...")
               checktest = self.caller.search("Corey", global_search=True)
               checktest.msg("%s is attacking %s." % (self.caller.name, self.caller.search(self.args).name))
               return
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        self.caller.db.target = self.caller.search(self.args)
        self.caller.db.target.db.target = self.caller
        if(self.caller.db.present == 0 or self.caller.db.target.db.present == 0):
            self.caller.msg("You can't do that while time has stopped.")
            return
        if self.caller.db.invis:
            self.caller.msg("You have become visibile.")
            self.caller.db.invis = 0
        if self.caller.db.target.db.invis:
            self.caller.msg("You have become visibile.")
            self.caller.db.target.db.invis = 0
        if not self.caller.db.target.ndb.end_combat and self.caller.db.target.db.alive and self.caller.db.alive:
            self.caller.ndb.end_combat = 1
            self.caller.db.target.ndb.end_combat = 1
            if(self.caller.db.conscious == 1):
                self.caller.msg("|/|rYou try to attack %s" % (self.caller.db.target))
                self.caller.db.target.msg("|/|r%s tries to attack you" % (self.caller))
                self.caller.location.log_action("%s tries to attack %s." % (self.caller, self.caller.db.target))
                init_a = self.caller.db.dexterity + self.caller.db.wits+self.caller.db.alertness
                init_b = self.caller.db.target.db.dexterity + self.caller.db.target.db.wits + self.caller.db.target.db.alertness
                init_a = init_a + roll_dice(1,10) + 2
                init_b = init_b + roll_dice(1,10)
                if(init_a > init_b):
                    self.caller.db.attacking = 1
                    self.caller.db.target.db.attacking = 0
                    self.caller.msg("|/|yYou get the jump on %s."% (self.caller.db.target))
                    self.caller.db.target.msg("|/|y%s gets the jump on you." % (self.caller))
                    EvMenu(self.caller, "typeclasses.menu", startnode="attack_node", cmd_on_exit=None)
                else:
                    self.caller.db.attacking = 0
                    self.caller.db.target.db.attacking = 1
                    self.caller.db.target.msg("|/|yYou get the jump on %s." % (self.caller))
                    self.caller.msg("|/|y%s gets the jump on you." % (self.caller.db.target))
                    EvMenu(self.caller.db.target, "typeclasses.menu", startnode="attack_node", cmd_on_exit=None)
            else:
                self.caller.msg("You can't do that while unconscious.")
        else:
             if self.caller.db.target.ndb.end_combat:
                 self.caller.msg("They are already in a fight.")
             if self.caller.db.target.db.alive == 0:
                 self.caller.msg("They are already dead.")
             if self.caller.db.alive == 0:
                 self.caller.msg("You have to be alive to do that.")
             return
