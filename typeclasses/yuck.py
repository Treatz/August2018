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
		caller.msg(prompt="test-1")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test0")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test1")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="test2")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="test3")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="test4")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="test5")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="test6")

	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test7")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test8")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test9")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="test10")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="test11")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="test12")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="test13")


	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test14")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test15")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test16")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="test17")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="test18")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="test19")

	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test20")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test21")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test22")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="test23")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="test24")

	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test25")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test26")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test27")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="test28")


	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test29")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test30")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="test31")

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test32")
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="test33")

	if((caller.db.lethal == 7 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="test34")

	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test35")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test36")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test37")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="test38")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="test39")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="test38")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="test39")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="test40")

	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test41")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test42")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test43")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="test44")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="test45")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="test46")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="test47")


	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test48")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test49")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test50")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="test51")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="test52")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="test53")

	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test54")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test55")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test56")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="test57")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="test58")

	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test59")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test60")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test61")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="test62")


	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test63")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test64")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="test65")

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="test66")
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="test67")
	if((caller.db.target.db.lethal == 7 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="")




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
		{"key": "|yskip",
		"desc": "Do nothing",
		"goto": "skip_attack"})

	for each in caller.contents:
		if each.db.weapon ==1:
			options += ({"key": "|y" + each.name,
				"desc": "An Axe",
				"goto": "wait",
				"exec": "axe"},) 

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
		caller.msg(prompt="68")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="69")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="70")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="71")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="72")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="73")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="74")
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="75")

	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="76")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="77")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="78")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="79")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="80")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="81")
	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="82")


	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="83")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="84")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="85")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="86")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="87")
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")

	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="88")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="89")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="90")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="91")
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="92")

	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="93")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="94")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="95")
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="96")


	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="97")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="98")
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="99")

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="100")
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="101")

	if((caller.db.lethal == 7 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="102")

	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="103")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="104")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="105")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="106")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="107")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="108")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="109")
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="110")

	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="111")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="112")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="113")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="114")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="115")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="116")
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="117")


	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="118")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="119")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="120")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="121")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="122")
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="123")

	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="124")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="125")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="126")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="127")
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="128")

	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="129")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="130")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="131")
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="132")


	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="133")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="134")
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="135")

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="136")
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="137")
	if((caller.db.target.db.lethal == 7 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="138")




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
		caller.db.target.msg("caller.db.target.msg")
		caller.msg("caller.msg")
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
		
		if(caller.db.testz == 0):
			caller.msg("|/|r caller.db.testz = 0")
		if(caller.db.testz == 1):
			caller.msg("|/|r caller.db.testz = 1")
		if(caller.db.target.db.testz == 0):
			caller.db.target.msg("|/|r caller.db.target.db.testz = 0")
		if(caller.db.target.db.testz == 1):
			caller.db.target.msg("|/|r caller.db.target.db.testz = 1")


		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|gYou dodge %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, reduced))
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
			caller.msg("|/|rTEST ONE")
			caller.db.target.msg("|/|rTEST TWO")
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
    attack_roll = roll_dice(3, 6)
    #caller.db.target.start_time = timer()
    caller.db.start_time = 99999999999999999999999
    if (attack_roll <= caller.db.dexterity):
        caller.msg("|/|gYou block %s's attack." % caller.db.target)
        caller.db.target.msg("|/|g%s blocks your attack." % caller)
    else:
        caller.msg("|/|rYou have been hit by %s." % caller.db.target)
        caller.db.target.msg("|/|r%s fails to block your attack." % caller)

    EvMenu(caller, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)
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
