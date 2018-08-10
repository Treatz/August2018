from evennia.commands.default.muxcommand import MuxCommand

class CmdSpell(MuxCommand):

    """
       List of spells:
           Correspondence
               +Locate - Provides directions to an object or character.
               +Jump - Teleport to a room.
               +Peek - Look at what another character is holding.
               +Portal - Creates a portal that anyone can pass through.
               +Scry - Remote view other locations.
               +Source - locks a source location in place.
               +Take - Teleports an object from another account.
               +Teleport -Teleport through a list of directions
               +Where - Provides directions to a room.
           Entropy
               +Ban - Bans a character from a room with bad luck.
               +Bless - Increases your luck at everything.
               +Charm - blesses an object with luck.
               +Curse - Increases any damamge the target is hit by.
               +Deathtouch - Knock a subject unconscious.
               +Fate - View another persons luck / karma.
               +Hex - Ruins targets luck at everything.
           Forces
               +Kinetic - Changes unarmed attacks to lethal.
               +Push - Increase your strength using forces.
               +Rush - Increase your speed using forces.
               +Stop - Prevents attacks from hitting you.
               +Strike - Call lightning.
           Life
               +Clone - Cange your appearance into someone else.
               +Con - Examine character's physical state.
               +Heal - Restores a living being back to health.
               +Raise - Brings a corpse back to life.
               +Sap - Drains a person's physical atributes.
               +Shift - Changes you into an animal.
           Matter
               +Enchant - blesses a weapon with luck.
               +Make - Create objects.
           Mind
               +Bug - Listen to everything another character says.
               +Illusion - Fills the room with an illusion.
               +Command - Forces a character to do something.
               +Invis - Temporarily makes you invisible.
               +Project - Causes a character to see an illusion.
               +Send - Sends a message to another character with telepathy.
           Prime
               +Dispell - Stops target from using magic.
               +Drain - Drains quintessence from targets willpower.
               +Use - Use personal luck/quintessence/willpower, or from an object.
           Spirit
               +Exorcise - Send ghosts back to where they belong.
               +Lastbreath - Determine identity and cause of corpses.
               +Inflict - Causes harm to the living.
               +Sight - Temporarily see into the spirit world.
               +Summon - Opens the room to the spirit world.
               +Reach - Interact with the spirit world.
           Time
               +Freeze - Freezes time in a location.
               +Slowtime - Slows time around you
               +History - Reviews the history in a location
    """
    help_category = "Magic"
    auto_help = True

    key = "Spheres"
    locks = "cmd:all()"

    def func(self):
        return
