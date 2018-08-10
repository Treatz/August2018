from evennia.contrib.dice import roll_dice
from evennia import EvForm, EvTable
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evform

class CmdContemplate(MuxCommand):

    key = "+contemplate"
    lock = "cmd:all()"
    def func(self):

        if not self.args:
            self.caller.msg("You must suply a target for this to work.")
            return
        form = evform.EvForm("world/charactersheetform.py")
        body = self.caller.search(self.args)
        form.map(cells={1: body,
                        2: body.db.tradition,
                        3: body.db.essence,
                        4: body.db.concept,
                        5: body.db.desc,
                        6: body.db.strength,
                        7: body.db.dexterity,
                        8: body.db.stamina,
                        9: body.db.charisma,
                        10: body.db.manipulation,
                        11: body.db.appearance,
                        12: body.db.perception,
                        13: body.db.intelligence,
                        14: body.db.wits,
                        15: body.db.alertness,
                        16: body.db.athletics,
                        17: body.db.awareness,
                        18: body.db.brawl,
                        19: body.db.intimidation,
                        20: body.db.starsign,
                        22: body.db.firearms,
                        23: body.db.martialarts,
                        24: body.db.melee,
                        25: body.db.meditation,
                        26: body.db.stealth,
                        27: body.db.astrology,
                        28: body.db.computer,
                        29: body.db.language,
                        30: body.db.medicine,
                        31: body.db.occult,
                        32: body.db.rituals,
                        33: body.db.correspondence,
                        34: body.db.entropy,
                        35: body.db.forces,
                        36: body.db.life,
                        37: body.db.matter,
                        38: body.db.mind,
                        39: body.db.prime,
                        40: body.db.spirit,
                        41: body.db.time,
                        42: body.db.arete,
                        43: body.db.avatar,
                        44: body.db.willpower,
                        45: body.db.belief,
                        46: body.db.quintessence,
                        47: body.db.luck})

        wins = 0
        for x in range(0, self.caller.db.arete + self.caller.db.occult):
            roll = roll_dice(1,10)
            if(roll > 5 - self.caller.db.magic_fuel):
                wins += 1
        wins = wins + self.caller.db.autopoint
        if(self.caller.db.autopoint):
            self.caller.msg("You have %s successes out of 4 needed, using a point of willpower and %s quintessence" % (wins, self.caller.db.magic_fuel))
        else:
            self.caller.msg("You have %s successes out of 4 needed, using %s points of quintessence." % (wins, self.caller.db.magic_fuel))
        self.caller.db.magic_fuel = 0
        self.caller.db.autopoint = 0
        if wins < 4:
            self.caller.msg("Your spell fizzles out and fails.")
            return
        else:
            self.caller.msg(unicode(form))
