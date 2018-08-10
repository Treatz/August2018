from evennia import default_cmds
from evennia.contrib.dice import roll_dice
import time
import datetime

class CmdAstrology(default_cmds.MuxCommand):
    """
       +astrology Align your magick with your star sign to fuel the spheres.

       Usage:
        +astrology

       Astrology:  Spheres are more powerful when aligned with thier planets.
                   This chart shows which planets assist in which sphere's magick.

           Correspondence  Jupiter
           Entropy         Mercury
           Forces          Mars
           Life            Venus
           Matter          Uranus
           Mind            Neptune
           Prime           Moon
           Spirit          Pluto
           Time            Saturn
    """
    help_category = "Skills"
    key = "+astrology"
    locks = "cmd:all()"
    auto_help=True

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
        wins = 0
        for x in range(0, self.caller.db.astrology + self.caller.db.intelligence):
           roll = roll_dice(1,10)
           if(roll > 5):
               wins += 1
        if(wins < 4):
           self.caller.msg("You can't see the stars.")
           return

        if not self.caller.ndb.astro_timer:

            myDate = datetime.date.today()
            num = int (myDate.strftime("%j"))
            if(num >= 20 and num < 50):
                sign = "Aquarius"
            if(num >= 50 and num < 80):
                sign = "Pisces"
            if(num >= 80 and num < 110):
                sign  = "Aries"
            if(num >= 110 and  num < 141):
                sign = "Taurus"
            if(num >= 141 and num < 172):
                sign = "Gemini"
            if(num >= 172 and num < 204):
                sign = "Cancer"
            if(num >= 204 and num < 235):
                sign = "Leo"
            if(num >= 235 and num < 266):
                sign = "Virgo"
            if(num >=  266 and num < 296):
                sign = "Libra"
            if(num >= 296 and num < 326):
                sign = "Scorpio"
            if(num >= 326 and num < 356):
                sign = "Sagitarius"
            if(num >= 356 or num < 20):
                sign = "Capricorn"

            self.caller.db.sign = sign

            planet = roll_dice(1,9)
            if planet == 1:
                self.caller.db.alignment = "Mercury"
            if planet == 2:
                self.caller.db.alignment = "Venus"
            if planet == 3:
                self.caller.db.alignment = "Mars"
            if planet == 4:
                self.caller.db.alignment = "Jupiter"
            if planet == 5:
                self.caller.db.alignment = "Saturn"
            if planet == 6:
                self.caller.db.alignent = "Uranus"
            if planet == 7:
                self.caller.db.alignment = "Neptune"
            if planet == 8:
                self.caller.db.alignment = "Pluto"
            if planet == 9:
                self.caller.db.alignment = "Moon"

            sign = roll_dice(1,12)
            if sign == 1:
                self.caller.db.zodiac = "Aquarius"
            if sign == 2:
                self.caller.db.zodiac = "Pisces"
            if sign == 3:
                self.caller.db.zodiac = "Aries"
            if sign == 4:
                self.caller.db.zodiac = "Taurus"
            if sign == 5:
                self.caller.db.zodiac = "Gemini"
            if sign == 6:
                self.caller.db.zodiac = "Cancer"
            if sign == 7:
                self.caller.db.zodiac = "Leo"
            if sign == 8:
                self.caller.db.zodiac = "Virgo"
            if sign == 9:
                self.caller.db.zodiac = "Libra"
            if sign == 10:
                self.caller.db.zodiac = "Scorpio"
            if sign == 11:
                self.caller.db.zodiac = "Sagitarius"
            if sign == 12:
                self.caller.db.zodiac = "Capricorn"

            self.caller.msg("You are in the sign of %s, and %s is aligned with %s." % (self.caller.db.sign, self.caller.db.alignment, self.caller.db.zodiac))
            self.caller.ndb.astro_timer = 1
            yield  60
            self.caller.ndb.astro_timer = 0
            self.caller.db.sign = "none"
            self.caller.db.alignment = "none"
            self.caller.db.zodiac = "none"
        else:
            self.caller.msg("The stars are moving!")
