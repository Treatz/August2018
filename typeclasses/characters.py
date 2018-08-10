"""
GO!
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from typeclasses.rooms import Room
from evennia import DefaultCharacter, TICKER_HANDLER
from evennia.contrib.dice import roll_dice
import random
import evennia
from evennia.utils.utils import (variable_from_module, lazy_property,
                                 make_iter, to_unicode, is_iter, to_str)

class Character(DefaultCharacter):
# [...]

    PHYSICAL_STATS = ('strength', 'dexterity', 'stamina')
    SOCIAL_STATS = ('charisma', 'manipulation', 'appearance')
    MENTAL_STATS = ('perception', 'intelligence', 'wits')
    ALL_STATS = PHYSICAL_STATS + SOCIAL_STATS + MENTAL_STATS

    TALENTS = ('alertness', 'athletics', 'awareness', 'brawl', 'intimidation')
    SKILLS = ('firearms', 'martialarts', 'melee', 'meditation', 'stealth')
    KNOWLEDGES = ('astrology', 'computer', 'medicine', 'occult', 'rituals')
    ALL_ABILL = TALENTS + SKILLS + KNOWLEDGES

    ADV = ('arete','avatar','belief','luck')
    SPHERES = ('correspondence','entropy','forces','life','matter','mind','prime','spirit','time')   
    def randomize_stats(self, stats, max):
        while max > 0:
            max -= 1
            stat = random.choice(stats)
            current_value = self.attributes.get(stat, 1)
            self.attributes.add(stat, current_value + 1)

    def randomize_spheres(self, stats, max):
        while max > 0:
            stat = random.choice(stats)
            current_value = self.attributes.get(stat, 0)
            if current_value < self.db.arete:
                self.attributes.add(stat, current_value + 1)
                max -= 1

    def at_say(self, message, msg_self=None, msg_location=None,
               receivers=None, msg_receivers=None, **kwargs):

        conscious = [obj for obj in self.location.contents if obj.db.conscious == 1 and obj is not self]
        self.msg(conscious)
       
        msg_type = 'say'
        if kwargs.get("whisper", False):
            # whisper mode
            msg_type = 'whisper'
            msg_self = '{self} whisper to {all_receivers}, "{speech}"' if msg_self is True else msg_self
            msg_receivers = msg_receivers or '{object} whispers: "{speech}"'
            msg_location = None
        else:
            msg_self = '{self} say, "{speech}"' if msg_self is True else msg_self
            msg_receivers = msg_receivers or '{object} says, "{speech}"'
            #msg_location = msg_location or '{object} says, "{speech}"'
            msg_location = None
        custom_mapping = kwargs.get('mapping', {})
        receivers = make_iter(conscious) if conscious else None
        location = self.location

        if msg_self:
            self_mapping = {"self": "You",
                            "object": self.get_display_name(self),
                            "location": location.get_display_name(self) if location else None,
                            "receiver": None,
                            "all_receivers": ", ".join(
                                recv.get_display_name(self)
                                for recv in receivers) if receivers else None,
                            "speech": message}
            self_mapping.update(custom_mapping)
            self.msg(text=(msg_self.format(**self_mapping), {"type": msg_type}), from_obj=self)

        if receivers and msg_receivers:
            receiver_mapping = {"self": "You",
                                "object": None,
                                "location": None,
                                "receiver": None,
                                "all_receivers": None,
                                "speech": message}
            for receiver in make_iter(receivers):
                individual_mapping = {"object": self.get_display_name(receiver),
                                      "location": location.get_display_name(receiver),
                                      "receiver": receiver.get_display_name(receiver),
                                      "all_receivers": ", ".join(
                                            recv.get_display_name(recv)
                                            for recv in receivers) if receivers else None}
                receiver_mapping.update(individual_mapping)
                receiver_mapping.update(custom_mapping)
                receiver.msg(text=(msg_receivers.format(**receiver_mapping),
                             {"type": msg_type}), from_obj=self)

        if self.location and msg_location:
            location_mapping = {"self": "You",
                                "object": self,
                                "location": location,
                                "all_receivers": ", ".join(str(recv) for recv in receivers) if receivers else None,
                                "receiver": None,
                                "speech": message}
            location_mapping.update(custom_mapping)
            self.location.msg_contents(text=(msg_location, {"type": msg_type}),
                                       from_obj=self,
                                       exclude=(self, ) if msg_self else None,
                                       mapping=location_mapping)



    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character
        generation step instead.
        """
        #set persistent attributes
        self.db.tradition = "Orphans"
        genum = random.randint(1,4)
        if genum == 1:
            self.db.essence = "Dynamic"
        if genum == 2:
            self.db.essence = "Pattern"
        if genum == 3:
            self.db.essence = "Primordial"
        if genum == 4:
            self.db.essence = "Questing"


        genum = random.randint(1,12)
        if genum == 1:
            self.db.starsign = "Aries"
        if genum == 2:
            self.db.starsign = "Taurus"
        if genum == 3:
            self.db.starsign = "Gemini"
        if genum == 4:
            self.db.starsign = "Cancer"
        if genum == 5:
            self.db.starsign = "Leo"
        if genum == 6:
            self.db.starsign = "Virgo"
        if genum == 7:
            self.db.starsign = "Libra"
        if genum == 8:
            self.db.starsign = "Scorpio"
        if genum == 9:
            self.db.starsign = "Sagitarius"
        if genum == 10:
            self.db.starsign = "Capricorn"
        if genum == 11:
            self.db.starsign = "Aquarius"
        if genum == 12:
            self.db.starsign = "Pisces"




        genum = random.randint(1,20)
        if genum == 1:
            self.db.concept = "Activist"
        if genum == 2:
            self.db.concept = "Artist"
        if genum == 3:
            self.db.concept = "Criminal"
        if genum == 4:
            self.db.concept = "Crusader"
        if genum == 5:
            self.db.concept = "Hacker"
        if genum == 6:
            self.db.concept = "Intellectual"
        if genum == 7:
            self.db.concept = "Kid"
        if genum ==8:
           self.db.concept = "Loner"
        if genum == 9:
           self.db.concept = "Mystic"
        if genum == 10:
           self.db.concept = "Night-Owl"
        if genum == 11:
           self.db.concept = "Official"
        if genum ==12:
           self.db.concept = "Prophet"
        if genum ==13:
           self.db.concept = "Rebel"
        if genum ==14:
           self.db.concept = "Rogue"
        if genum ==15:
           self.db.concept = "Scientist"
        if genum ==16:
           self.db.concept = "Survivor"
        if genum ==17:
           self.db.concept = "Techie"
        if genum == 18:
           self.db.concept = "Trickster"
        if genum == 19:
           self.db.concept = "Visionary"
        if genum == 20:
           self.db.concept = "Wage-Slave"

        self.db.form = "human"
        self.db.strength = 1
        self.db.dexterity = 1
        self.db.stamina = 1
        self.db.charisma = 1
        self.db.manipulation = 1
        self.db.appearance = 1
        self.db.perception = 1
        self.db.intelligence = 1
        self.db.wits = 1        

        for stat in self.ALL_STATS:
            self.attributes.add(stat, 1)        
 
        priorities = random.randint(1,6)

        if priorities == 1:
            self.randomize_stats(self.PHYSICAL_STATS, 7)
 
            self.randomize_stats(self.SOCIAL_STATS, 5)
 
            self.randomize_stats(self.MENTAL_STATS, 3)

        if priorities == 2:
            self.randomize_stats(self.PHYSICAL_STATS, 7)
 
            self.randomize_stats(self.SOCIAL_STATS, 3)
 
            self.randomize_stats(self.MENTAL_STATS, 5)

        if priorities == 3:
            self.randomize_stats(self.PHYSICAL_STATS, 5)
 
            self.randomize_stats(self.SOCIAL_STATS, 7)
 
            self.randomize_stats(self.MENTAL_STATS, 3)

        if priorities == 4:
            self.randomize_stats(self.PHYSICAL_STATS, 5)
 
            self.randomize_stats(self.SOCIAL_STATS, 3)
 
            self.randomize_stats(self.MENTAL_STATS, 7)
     
        if priorities == 5:
            self.randomize_stats(self.PHYSICAL_STATS, 3)
 
            self.randomize_stats(self.SOCIAL_STATS, 5)
 
            self.randomize_stats(self.MENTAL_STATS, 7)

        if priorities == 6:
            self.randomize_stats(self.PHYSICAL_STATS, 3)
 
            self.randomize_stats(self.SOCIAL_STATS, 7)
 
            self.randomize_stats(self.MENTAL_STATS, 5)


        for stat in self.ALL_ABILL:
            self.attributes.add(stat, 0)
 
        priorities = random.randint(1,6)

        if priorities == 1:
            self.randomize_stats(self.TALENTS, 10)
 
            self.randomize_stats(self.SKILLS, 8)
 
            self.randomize_stats(self.KNOWLEDGES, 6)
        if priorities == 2:
            self.randomize_stats(self.TALENTS, 10)
 
            self.randomize_stats(self.SKILLS, 6)
 
            self.randomize_stats(self.KNOWLEDGES, 8)
        if priorities == 3:
            self.randomize_stats(self.TALENTS, 8)
 
            self.randomize_stats(self.SKILLS, 10)
 
            self.randomize_stats(self.KNOWLEDGES, 6)
        if priorities == 4:
            self.randomize_stats(self.TALENTS, 8)
 
            self.randomize_stats(self.SKILLS, 6)
 
            self.randomize_stats(self.KNOWLEDGES, 10)
        if priorities == 5:
            self.randomize_stats(self.TALENTS, 6)
 
            self.randomize_stats(self.SKILLS, 8)
 
            self.randomize_stats(self.KNOWLEDGES, 10)
        if priorities == 6:
            self.randomize_stats(self.TALENTS, 6)
 
            self.randomize_stats(self.SKILLS, 10)
 
            self.randomize_stats(self.KNOWLEDGES, 8)


        self.db.conscious = 1
        self.db.alive = 1
        self.db.sight = 0

        for stat in self.ADV:
            self.attributes.add(stat, 0)
        self.randomize_stats(self.ADV, 12)

        for stat in self.SPHERES:
            self.attributes.add(stat,0)
        self.randomize_spheres(self.SPHERES, 7)

        self.db.quintessence = self.db.avatar
        self.db.willpower = 5
        self.db.arcane = 0
        self.db.familiar = 0
        self.db.resources = 0
        self.db.target = self
        self.db.attacker = self
        self.db.bashing = 0
        self.db.lethal = 0
        self.db.weapon = 0
        self.db.invis = 0
        self.db.blessed = 0
        self.db.cursed = 0
        self.db.burned = 0
        self.db.astro = 0
        self.db.attack_not = 1
        self.db.magic = 1
        self.db.touch = 0
        self.db.intimidated = 0
        self.db.present = 1
        self.db.magic_fuel = 1
        self.db.autopoint = 1
        TICKER_HANDLER.add(60, self.heal)
        #TICKER_HANDLER.add(120, self.heal_lethal)
        TICKER_HANDLER.add(180, self.spells)
        TICKER_HANDLER.add(15, self.ban)
        TICKER_HANDLER.add(360, self.death)
        return

    def death(self, *args, **kwards):
        if(self.db.alive == 0):
            self.msg("You're Avatar has reformed, and you come back to life!")
            self.db.lethal = 0
            self.db.bashing = 0
            self.db.alive = 1
            self.db.conscious = 1
            self.location = Room.objects.get(id=3)

    def ban(self, *args, **kwards):
        if(self.db.ban  == self.location):
            self.msg("This area does not want you here!.")
            self.db.cursed = self.db.cursed + 1

    def spells(self, *args, **kwards):
    
        self.db.attack_not = 1
            
        if(self.db.alive == 0 and self.db.conscious == 0):
            self.db.conscious = 1
            self.msg("You take a deep breath of astral air.")


    def heal_lethal(self, *args, **kwargs):
        if(self.db.lethal > 0 and self.db.alive == 1):
            self.msg("You heal 1 point of lethal damage.")
            self.db.lethal = self.db.lethal  - 1
            healthbar = "|/|X|[wHealth:"
            total = self.db.lethal + self.db.bashing

            diff = 8 - self.db.lethal

            if self.db.bashing > diff:
                self.db.lethal += self.db.bashing - diff
                self.db.bashing -= self.db.bashing - diff
            for i in range(0,8):
                if i < self.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"

            healthbar += "|/"
            self.msg(prompt=healthbar)

            if(total<8):
                self.db.conscious = 1
               
    def heal(self, *args, **kwargs):
        if self.db.alive:
           self.locks.add("view:attr(alive, 1)")
        else:
           self.locks.add("view:attr(alive, 0)")
        if(self.ndb.nameSave):
            self.db.form = "human"
            self.key = self.ndb.nameSave
            self.db.desc = self.ndb.descSave
            self.db.image = self.ndb.imageSave
            self.ndb.nameSave = None
            self.ndb.descSave = None
            self.ndb.imageSave = None
            self.msg("You have changed back.")

        if(self.db.bashing > 0 and self.db.alive == 1):
            self.msg("You heal 1 point of bashing damage.")
            self.db.bashing = self.db.bashing - 1

            healthbar = "|/|X|[wHealth:"
            total = self.db.lethal + self.db.bashing

            diff = 8 - self.db.lethal
            if self.db.bashing > diff:
                self.db.lethal += self.db.bashing - diff
                self.db.bashing -= self.db.bashing - diff
            for i in range(0,8):
                if i < self.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"
            healthbar += "|/"
            self.msg(prompt=healthbar)
            if(total<8):
                self.db.conscious = 1

    def get_abilities(self):
        """
        Simple access method to return ability
        scores as a tuple (str,agi,mag)
        """
        return self.db.strength, self.db.agility, self.db.magic

    def is_alive(self):
        return self.db.alive

    def at_post_puppet(self):
        if not self.db.npc:
            self.location = Room.objects.get(id=3)
        super(Character, self).at_post_puppet()
        healthbar = "|/|X|[wHealth:"
        total = self.db.lethal + self.db.bashing

        diff = 8 - self.db.lethal

        if self.db.bashing > diff:
            self.db.lethal += self.db.bashing - diff
            self.db.bashing -= self.db.bashing - diff
        for i in range(0,8):
            if i < self.db.lethal:
                healthbar += " X"
            elif i < total:
                healthbar += " /"
            else:
                healthbar += " 0"
        healthbar += "|/"
        self.msg(prompt=healthbar)

    def return_appearance(self, looker):
        looker.msg(image=[self.db.image, self.db.desc])

    def at_post_unpuppet(self, account, session=None):
        if not self.sessions.count():
           if self.location and not self.db.npc:
              self.db.prelogout_location = self.location
              self.location = Room.objects.get(id=3)


    def at_after_move(self, source_location):
        """
        We make sure to look around after a move.
        """
        if self.location.access(self, "view"):
            self.msg(self.at_look(self.location))

            healthbar = "|/|X|[wHealth:"
            total = self.db.lethal + self.db.bashing

            diff = 8 - self.db.lethal
            if self.db.bashing > diff:
                self.db.lethal += self.db.bashing - diff
                self.db.bashing -= self.db.bashing - diff
            for i in range(0,8):
                if i < self.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"
            healthbar += "|/"
            self.msg(prompt=healthbar)


    def announce_move_from(self, destination, msg=None, mapping=None):
        """
        Called if the move is to be announced. This is
        called while we are still standing in the old
        location.
        Args:
            destination (Object): The place we are going to.
            msg (str, optional): a replacement message.
            mapping (dict, optional): additional mapping objects.
        You can override this method and call its parent with a
        message to simply change the default message.  In the string,
        you can use the following as mappings (between braces):
            object: the object which is moving.
            exit: the exit from which the object is moving (if found).
            origin: the location of the object before the move.
            destination: the location of the object after moving.
        """
        if not self.location:
            return
        if msg:
            string = msg
        elif self.db.alive == 1 and self.db.invis == 0 and not self.ndb.sneak:
            string = "{object} is leaving {origin}, heading for {destination}."
            
        elif self.ndb.sneak:
            total = self.db.dexterity + self.db.stealth
            winz = 0
            for x in range(1, total):
                roll = roll_dice(1,10)
                if roll >=6:
                    winz += 1
            if winz < 3:
                string = "{object} is leaving {origin}, heading for {destination}."
            else:
                string = ""
        else:
            string =  "{object} is leaving {origin}, heading for {destination}."
            
        location = self.location
        exits = [o for o in location.contents if o.location is location and o.destination is destination]
        if not mapping:
            mapping = {}

        mapping.update({
                "object": self,
                "exit": exits[0] if exits else "somwhere",
                "origin": location or "nowhere",
                "destination": destination or "nowhere",
        })


        out = []
        for objects in self.location.contents:
            if(objects.db.conscious == 0 or objects.db.alive == 0) or (objects.db.freeze == 1 and self.caller.db.present == 0):
                out.append(objects)
        out.append(self)
        self.location.msg_contents(string, exclude=out, mapping=mapping)
        self.location.log_action("%s is leaving %s, heading for %s" % (self, location, destination))
      #  out = []
      #  for objects in self.location.contents:
      #      if objects.db.conscious == 0 or objects.db.alive == 0:
      #          out.append(objects)
      #  if(out):
      #      self.location.msg_contents(string, exclude=(self,out[0]), mapping=mapping)
      #  else:
      #      self.location.msg_contents(string, exclude=(self, ), mapping=mapping)

    def announce_move_to(self, source_location, msg=None, mapping=None):
        """
        Called after the move if the move was not quiet. At this point
        we are standing in the new location.
        Args:
            source_location (Object): The place we came from
            msg (str, optional): the replacement message if location.
            mapping (dict, optional): additional mapping objects.
        You can override this method and call its parent with a
        message to simply change the default message.  In the string,
        you can use the following as mappings (between braces):
            object: the object which is moving.
            exit: the exit from which the object is moving (if found).
            origin: the location of the object before the move.
            destination: the location of the object after moving.
        """

        if not source_location and self.location.has_account:
            # This was created from nowhere and added to an account's
            # inventory; it's probably the result of a create command.
            string = "You now have %s in your possession." % self.get_display_name(self.location)
            self.location.msg(string)
            return

        if source_location:
            if msg:
                string = msg
            elif self.db.alive == 1 and self.db.invis == 0 and not self.ndb.sneak:
                string = "{object} arrives to {destination} from {origin}."
                
            elif self.ndb.sneak:
                total = self.db.dexterity + self.db.stealth
                winz = 0
                for x in range(1, total):
                    roll = roll_dice(1,10)
                    if roll >=6:
                        winz += 1
                if winz < 3:
                    string = "{object} arrives to {destination} from {origin}."
                else:
                    string = ""
            else:
                string = "" 
        elif self.db.alive == 1 and self.db.invis ==0 and not self.ndb.sneak:
            string = "{object} arrives to {destination}."
            
        elif self.ndb.sneak:
            total = self.db.dexterity + self.db.stealth
            winz = 0
            for x in range(1, total):
                roll = roll_dice(1,10)
                if roll >=6:
                    winz += 1
            if winz < 3:
                string = "{object} arrives to {destination}."
            else:
                string = ""

        else:
            string = ""
        origin = source_location
        destination = self.location
        exits = []
        if origin:
            exits = [o for o in destination.contents if o.location is destination and o.destination is origin]

        if not mapping:
            mapping = {}

        mapping.update({
                "object": self,
                "exit": exits[0] if exits else "somewhere",
                "origin": origin or "nowhere",
                "destination": destination or "nowhere",
        })
        out = []
        for objects in self.location.contents:
            if(objects.db.conscious == 0 or objects.db.alive == 0) or (objects.db.freeze == 1 and self.caller.db.present == 0):
                out.append(objects)
        out.append(self)
        self.location.msg_contents(string, exclude=out, mapping=mapping)
        self.location.log_action("%s arrives at %s from the %s" % (self, destination, origin))
