from evennia.utils.evmenu import EvMenu
from evennia.contrib.dice import roll_dice
from evennia import create_script
from timeit import default_timer as timer

damage = 0

# Menu implementing the dialogue tree
def exit_combat(caller):
    caller.execute_cmd('Exit')

def attack_node(caller):
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: O O O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: / O O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: / / O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: / / / O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: / / / / O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: / / / / / O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: / / / / / / O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: / / / / / / /")

	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X O O O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X / O O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X / / O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X / / / O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X / / / / O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X / / / / /")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")


	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X O O O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X / O O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X / / O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X / / / O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X / / / / O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")

	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X O O O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X / O O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X / / O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X / / / O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")

	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X O O O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X / O O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X / / O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")


	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X O O")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X / O")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X O")
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")

	if((caller.db.lethal == 7 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")

	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: O O O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: / O O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: / / O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / /")

	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X O O O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X / O O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / /")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")


	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X O O O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / O O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /")

	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X O O O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / O O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")

	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X O O O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / O O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")


	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X O O")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / O")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X O")
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
	if((caller.db.target.db.lethal == 7 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")




	caller.db.start_time = timer()

	attack_script = create_script("typeclasses.attackwait.AttackTime", obj=caller)
	attack_script.attacker(caller)
	attack_script.target(caller.db.target)
	text = ""

	options = ({"key": "|ypunch",
		"desc": "Punch %s" % caller.db.target,
		"goto": "wait",
		"exec": "punch"},
		{"key": "|ykick",
		"desc": "Kick %s" % caller.db.target,
		"goto": "wait",
		"exec": "kick"},
		{"key": "|ywield",
		"desc": "Wield a weapon",
		"goto": "wield",
		"exec": "wield"},
		{"key": "|yskip",
		"desc": "Do nothing",
		"goto": "skip_attack"},)

	for each in caller.contents:
		if each == caller.ndb.selected_weapon:
			options += ({"key": "|y" + caller.ndb.selected_weapon.name,
				"desc": "item",
				"goto": "wait",
				"exec": "punch"},)

	return text, options

def wield(caller):
	text = ""
	options = ({"key": "|ytest",
		"desc": "testing",
		"goto": "wait",
		"exec": "punch"},)
	for each in caller.contents:
		options += ({"key": "|y" + each.name,
			"desc": "appearances",
			"goto": "wait",
			"exec": lambda caller=caller:caller.nattributes.add("selected_weapon", each)},) 

	return text, options

def punch(caller):
	caller.db.weapon = 0
	test = caller.db.dexterity + caller.db.brawl
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou punch %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to punch you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s punches, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	return text, options


def kick(caller):
	caller.db.weapon = 0
	test = caller.db.dexterity + caller.db.brawl
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 7):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength + 1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou kick %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to kick you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s kicks, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def axe(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 7):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+3
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def knife(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 4):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def bat(caller):
	caller.db.weapon = 0

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 5):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+2
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def staff(caller):
	caller.db.weapon = 0

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def katana(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+3
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def wait(caller):
    caller.db.start_time = 99999999999999999999999
    text = ""
    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def skip_attack(caller):
    caller.db.start_time = 99999999999999999999999
    EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)
    text = "|r You have skipped your turn!"
    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def skip_defend(caller):
    caller.db.start_time = 99999999999999999999999
    caller.msg("|/|rYou have been hit by %s.|/" % caller.db.target)
    caller.db.target.msg("|/|r%s has skipped his turn.|/" % caller)
    EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)
    text = "|r You have skipped your turn!"
    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def defend_node(caller):
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: O O O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: / O O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: / / O O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: / / / O O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: / / / / O O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: / / / / / O O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: / / / / / / O")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: / / / / / / /")

	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X O O O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X / O O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X / / O O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X / / / O O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X / / / / O O")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X / / / / /")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")


	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X O O O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X / O O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X / / O O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X / / / O O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X / / / / O")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")

	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X O O O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X / O O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X / / O O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X / / / O")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")

	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X O O O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X / O O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X / / O")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")


	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X O O")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X / O")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X O")
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")

	if((caller.db.lethal == 7 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")

	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: O O O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: / O O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: / / O O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / O O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / O O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / O O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / O")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / /")

	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X O O O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X / O O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / O O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / O O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / O O")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / /")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")


	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X O O O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / O O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / O O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / O O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / O")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /")

	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X O O O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / O O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / O O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / O")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")

	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X O O O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / O O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / O")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")


	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X O O")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / O")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X O")
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
	if((caller.db.target.db.lethal == 7 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")




	caller.db.target.start_time = timer()

	defend_script = create_script("typeclasses.defendwait.DefendTime", obj=caller)
	defend_script.attacker(caller)
	defend_script.target(caller.db.target)

	text = ""
	options = ({"key": "|ydodge",
		"desc": "Avoid the attack.",
		"goto": "wait",
		"exec": "dodge"},
		{"key": "|yblock",
		"desc": "Block the attack.",
		"goto": "wait",
		"exec": "block"},
		{"key": "|yflee",
		"desc": "Run away.",
		"goto": "wait",
		"exec": "flee"},
		{"key": "|yskip",
		"desc": "Do nothing.",
		"goto": "skip_defend"})

	return text, options

def dodge(caller):
	test = caller.db.dexterity + caller.db.athletics
	soak = caller.db.stamina
	counter = 0
	defendpoints = 0
	while (counter < test):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			defendpoints = defendpoints + 1

	counter = 0
	soakpoints = 0
	while (counter < soak):
		counter = counter + 1
		roll = roll_dice(1,10)
		if (roll >= 6):
			soakpoints = soakpoints + 1

	caller.db.start_time = 99999999999999999999999
	if (defendpoints > 0):
		tst = damage2
		dmg2 = damage
		dmg = damage
		cnt2 = 0
		while (cnt2 < tst):
			cnt2 = cnt2 + 1
			roll = roll_dice(1, 10)
			if (roll >= 6):
				dmg = dmg + 1

		reduced =  dmg - defendpoints
		if(reduced < 0):
			reduced = 0
		if(defendpoints >= dmg2):
			defendpoints = dmg2
			reduced = 0

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|gYou dodge %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, reduced))
			if (soakpoints > reduced):
				soakpoints = reduced
			if (soakpoints > 0):
				caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, reduced))
			if (reduced - soakpoints > 0):
				caller.msg("|/|gYou lose a total of %i health points." % (reduced - soakpoints))
				caller.db.bashing = caller.db.bashing + (reduced - soakpoints)
			caller.db.target.msg("|/|g%s dodges %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of damage with your punch." % (reduced))
	
			if(soakpoints>0):
				caller.db.target.msg("|/|g%s soaks %i points of damage from your punch." % (caller, soakpoints))
			if(reduced-soakpoints > 0):
				caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, reduced - soakpoints))

		if(caller.db.target.db.weapon == 1):
			caller.msg("|/|gYou dodge %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, reduced))
			caller.db.lethal = caller.db.lethal + reduced
			caller.db.target.msg("|/|g%s dodges %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of lethal damage." % (reduced))
			
	else:
		caller.msg("|/|rYou have been hit by %s." % caller.db.target)
		caller.db.target.msg("|/|r%s fails to dodge your attack." % caller)

	EvMenu(caller, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	return text, options


def block(caller):
	test = caller.db.dexterity + caller.db.brawl
	soak = caller.db.stamina
	counter = 0
	defendpoints = 0
	while (counter < test):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			defendpoints = defendpoints + 1

	counter = 0
	soakpoints = 0
	while (counter < soak):
		counter = counter + 1
		roll = roll_dice(1,10)
		if (roll >= 6):
			soakpoints = soakpoints + 1

	caller.db.start_time = 99999999999999999999999
	if (defendpoints > 0):
		tst = damage2
		dmg2 = damage
		dmg = damage
		cnt2 = 0
		while (cnt2 < tst):
			cnt2 = cnt2 + 1
			roll = roll_dice(1, 10)
			if (roll >= 6):
				dmg = dmg + 1

		reduced =  dmg - defendpoints
		if(reduced < 0):
			reduced = 0
		if(defendpoints >= dmg2):
			defendpoints = dmg2
			reduced = 0

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|gYou block %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, reduced))
			if (soakpoints > 0):
				caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, reduced))
			if (reduced - soakpoints > 0):
				caller.msg("|/|gYou lose a total of %i health points." % (reduced - soakpoints))
				caller.db.bashing = caller.db.bashing + (reduced - soakpoints)
			caller.db.target.msg("|/|g%s blocks %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of damage with your attack." % (reduced))
	
			if(soakpoints>0):
				caller.db.target.msg("|/|g%s soaks %i points of damage from your punch." % (caller, soakpoints))
			if(reduced-soakpoints > 0):
				caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, reduced - soakpoints))

		if(caller.db.target.db.weapon == 1):
			caller.msg("|/|gYou cannot block %s's attack points." % (caller.db.target))
			caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, dmg2))
			caller.db.lethal = caller.db.lethal + dmg2
			caller.db.target.msg("|/|g%s can't block your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of lethal damage." % (dmg2))
			
	else:
		caller.msg("|/|rYou have been hit by %s." % caller.db.target)
		caller.db.target.msg("|/|r%s fails to dodge your attack." % caller)

	EvMenu(caller, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	return text, options

def flee(caller):
    caller.db.start_time = 99999999999999999999999
    caller.msg("|/|rYou flee from combat!|/|/")
    caller.db.target.msg("|/|r%s flees from combat|/|/" % caller)
    caller.db.target.ndb._menutree.close_menu()
    caller.ndb._menutree.close_menu()
    caller.msg("TEST: %s" % caller.db.target)
    caller.execute_cmd('look')
    caller.db.target.execute_cmd('look')
    text = ""
    options = ()
    return text, options

def END(caller):
    caller.msg("EXIT COMBAT")
    caller.db.target.msg("EXIT COMBAT")
    caller.ndb._menutree.close_menu()
    caller.db.target.ndb._menutree.close_menu()

    text = ""
    options = ()
    return text, options
