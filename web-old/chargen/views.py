# file mygame/web/chargen/views.py

from django.shortcuts import render
from web.chargen.models import CharApp
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from evennia.commands.default import unloggedin
from django import forms
from evennia import search_object
from django.shortcuts import redirect


def trans(varnum):
    if(varnum == "One"):
        return 1
    if(varnum == "Two"):
        return 2
    if(varnum == "Three"):
        return 3
    if(varnum == "Four"):
        return 4
    if(varnum == "Five"):
        return 5
    if (varnum == "Six"):
        return 6


def index(request):
    current_user = request.user # current user logged in
    myobj = request.user
    context = {'myobj': myobj}
    return render(request, 'chargen/index.html', context)

def detail(request):
    current_user = request.user # current user logged in
    myobj = request.user
    context = {'myobj': myobj}
    return render(request, 'chargen/readme.txt', context)

def creating(request):
    user = request.user
    #foobar = create.create_account("TestAccount42", email="test@test.com", password="testpassword", typeclass=settings.BASE_ACCOUNT_TYPECLASS)
    #foobar.db.FIRST_LOGIN = True
    #unloggedin._create_character(self, foobar, settings.BASE_CHARACTER_TYPECLASS, settings.DEFAULT_HOME, settings.PERMISSION_ACCOUNT_DEFAULT)
    if request.method == 'POST':
        myform = request.POST
        print(request.POST)
        print(myform)
        fields = myform['name']
        pwd = myform['password']
        circuit = create.create_account(fields, email="test@test.com", password=pwd, typeclass=settings.BASE_ACCOUNT_TYPECLASS)
        unloggedin._create_character(user, circuit, settings.BASE_CHARACTER_TYPECLASS, settings.DEFAULT_HOME, settings.PERMISSION_ACCOUNT_DEFAULT)
        newchar = circuit.db._last_puppet
        newchar.db.tradition = myform['tradition']
        newchar.db.desc =  myform['description']
        newchar.db.image = myform['image']
        newchar.db.essence = myform['testinput']
        newchar.db.concept = myform['concept']
        newchar.db.strength = trans(myform['Strength'])
        newchar.db.dexterity = trans(myform['Dexterity'])
        newchar.db.stamina = trans(myform['Stamina'])
        newchar.db.charisma = trans(myform['Charisma'])
        newchar.db.manipulation = trans(myform['Manipulation'])
        newchar.db.appearance = trans(myform['Appearance'])
        newchar.db.perception = trans(myform['Perception'])
        newchar.db.intelligence = trans(myform['Intelligence'])
        newchar.db.wits = trans(myform['Wits'])
        newchar.db.alertness = trans(myform['testA'])-1
        newchar.db.athletics = trans(myform['testA1'])-1
        newchar.db.awareness = trans(myform['testA2'])-1
        newchar.db.brawl = trans(myform['testA3'])-1
        newchar.db.intimidation = trans(myform['testA4'])-1
        newchar.db.streetwise = trans(myform['testA5'])-1
        newchar.db.drive = trans(myform['testB'])-1
        newchar.db.firearms = trans(myform['testB1'])-1
        newchar.db.martialarts = trans(myform['testB2'])-1
        newchar.db.melee = trans(myform['testB3'])-1
        newchar.db.meditation = trans(myform['testB4'])-1
        newchar.db.stealth = trans(myform['testB5'])-1
        newchar.db.astrology = trans(myform['testC'])-1
        newchar.db.computer = trans(myform['testC1'])-1
        newchar.db.language = trans(myform['testC2'])-1
        newchar.db.medicine = trans(myform['testC3'])-1
        newchar.db.occult = trans(myform['testC4'])-1
        newchar.db.rituals = trans(myform['testC5'])-1

        newchar.db.melee = trans(myform['testB3'])-1
        newchar.db.meditation = trans(myform['testB4'])-1
        newchar.db.stealth = trans(myform['testB5'])-1
        newchar.db.astrology = trans(myform['testC'])-1
        newchar.db.computer = trans(myform['testC1'])-1
        newchar.db.language = trans(myform['testC2'])-1
        newchar.db.medicine = trans(myform['testC3'])-1
        newchar.db.occult = trans(myform['testC4'])-1
        newchar.db.rituals = trans(myform['testC5'])-1
        newchar.db.correspondence = trans(myform["Correspondence"])-1
        newchar.db.entropy = trans(myform["Entropy"])-1
        newchar.db.life = trans(myform["Life"])-1
        newchar.db.forces = trans(myform["Forces"])-1
        newchar.db.matter = trans(myform["Matter"])-1
        newchar.db.mind = trans(myform["Mind"])-1
        newchar.db.prime = trans(myform["Prime"])-1
        newchar.db.spirit = trans(myform["Spirit"])-1
        newchar.db.time = trans(myform["Time"])-1

        newchar.db.quintessence = trans(myform["Quintessence"])-1
        newchar.db.arete = trans(myform["Arete"])-1
        newchar.db.willpower = trans(myform["Willpower"])-1
        newchar.db.arcane = trans(myform["Arcane"])-1
        newchar.db.belief = trans(myform["Belief"])-1
        newchar.db.luck = trans(myform["Luck"])-1
        newchar.db.avatar = trans(myform["Avatar"])-1
        newchar.db.familiar = trans(myform["Familiar"])-1
        newchar.db.resources = trans(myform["Resources"])-1
        urlz = '/character/sheet/'
        nchr = str(newchar.id);
        urlz = urlz + nchr + '/'
        return redirect(urlz)
        

  