from evennia import EvForm, EvTable
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evform

class Sheet(MuxCommand):

    key = "+sheet"
    lock = "cmd:all()"
    def func(self):


        form = evform.EvForm("world/charactersheetform.py")
        form.map(cells={1: self.caller.name,
                        2: self.caller.db.tradition,
                        3: self.caller.db.essence,
                        4: self.caller.db.concept,
                        5: self.caller.db.desc,
                        6: self.caller.db.strength,
                        7: self.caller.db.dexterity,
                        8: self.caller.db.stamina,
                        9: self.caller.db.charisma,
                        10: self.caller.db.manipulation,
                        11: self.caller.db.appearance,
                        12: self.caller.db.perception,
                        13: self.caller.db.intelligence,
                        14: self.caller.db.wits,
                        15: self.caller.db.alertness,
                        16: self.caller.db.athletics,
                        17: self.caller.db.awareness,
                        18: self.caller.db.brawl,
                        19: self.caller.db.intimidation,
                        20: self.caller.db.starsign,
                        22: self.caller.db.firearms,
                        23: self.caller.db.martialarts,
                        24: self.caller.db.melee,
                        25: self.caller.db.meditation,
                        26: self.caller.db.stealth,
                        27: self.caller.db.astrology,
                        28: self.caller.db.computer,
                        29: self.caller.db.language,
                        30: self.caller.db.medicine,
                        31: self.caller.db.occult,
                        32: self.caller.db.rituals,
                        33: self.caller.db.correspondence,
                        34: self.caller.db.entropy,
                        35: self.caller.db.forces,
                        36: self.caller.db.life,
                        37: self.caller.db.matter,
                        38: self.caller.db.mind,
                        39: self.caller.db.prime,
                        40: self.caller.db.spirit,
                        41: self.caller.db.time,
                        42: self.caller.db.arete,
                        43: self.caller.db.avatar,
                        44: self.caller.db.willpower,
                        45: self.caller.db.belief,
                        46: self.caller.db.quintessence,
                        47: self.caller.db.luck})

        self.caller.msg(unicode(form))
