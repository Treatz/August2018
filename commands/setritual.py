from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.characters import Character
from evennia.contrib.dice import roll_dice

class CmdSetRitual(MuxCommand):

    """
       @SetRitual - Used to set the description of the ritual.
    
       Usage: 
          @setritual me/room = description
   
       Sets either your personal messge and the message for the room.
    
    """   

    auto_help = False
   
    key = "@setritual"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
             self.caller.msg("You must suply descriptions for your ritual.")
             return
        Wiz = Character.objects.get(id=1)
        self.caller.db.roomritual = self.args
        self.caller.msg("You set your ritual message to %s." % self.args)
        Wiz.msg("%s sets his ritual room message to: %s" % (self.caller, self.args))
