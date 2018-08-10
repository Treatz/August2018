# -*- coding: utf-8 -*-
 
#HEADER
from evennia import TICKER_HANDLER as tickerhandler 
from evennia.objects.models import ObjectDB
 
#CODE
 
#for each in ObjectDB.objects.all():
#    if each.is_typeclass('typeclasses.objects.Object'):
#        each.db.invis = 0

for each in ObjectDB.objects.all():
    if each.is_typeclass('typeclasses.characters.Character'):
        tickerhandler.add(60, each.heal, persistent=True)
        tickerhandler.add(120, each.heal_lethal, persistent = True)
        tickerhandler.add(180, each.spells, persistent = True)
        tickerhandler.add(15, each.ban, persistent = True)
        tickerhandler.add(360, each.death, persistent = True)
