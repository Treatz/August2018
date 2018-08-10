from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.characters import Character
import datetime

class CmdCast(MuxCommand):
    """
       +cast - Use ritual magic.

       Usage:
         +cast <entry>

       Define your ritual spell.

    """
    key = "+cast"
    locks = "cmd:all()"
    help_category = "Magic"
    auto_help = True
    def func(self):

        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        Wiz = Character.objects.get(id=1)
        today = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        save = self.args
        if not Wiz.db.rituals:
            Wiz.db.rituals = []
        Wiz.db.rituals.append((self.caller,today, save))
        cnt = -1
        for entry in Wiz.db.rituals:
            cnt += 1

        Wiz.msg("|/(%i) %s|/%s|/%s|/" % (cnt, self.caller,today, save))
        self.caller.msg("|/Your spell is being cast!|/")
