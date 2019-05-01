#	Script Created by ElliotGamer3
#	
#	This file contains wiimote to xoutput definitions
#	Created by Elliot Imhoff
#	Credit where due to creators of XOutputPlugin and FreePIE
#	XOutputPlugin: https://github.com/dschu012/XOutputPlugin
#	FreePie: https://github.com/AndersMalmgren/FreePIE
#	
# Uses XOutputPlugin to map multiple wiimotes to xbox virtual remotes
# Detects accessory changes to wiimotes and updates mappings accordingly
# Currently detects and has maps for:
#	Wii Guitar
#	Wii Remote (no accessories)
#
# If MAX_PLAYERS is increased, update definitons listed below must be made for added players
# update_wiimote
# update_wiimote_Guitar
# update_player_<PLAYERNUMBER>
# Once this is done update_player_<PLAYERNUMBER>() must be called after
# update_player_<PLAYERNUMBER - 1>()
#
# List for keeping track of players current accessories
# Definition for updating the player_type list
# Guitar = 3
# Nunchuck = 2
# No Accessories = 1
# Other = -1


#############
# Constants #
#############

POLLING_PERIOD 	= 1
MAX_PLAYERS = 4

GUITAR_EXTENSION = 3
NUNCHUCK_EXTENSION = 2
NO_EXTENSION = 1
OTHER_EXTENSION = -1

#####################
# Accessory updater #
#####################

player_type = list((0,0,0,0))

def update_player_type():
	for player in range(MAX_PLAYERS-1):
		print(" Player: ", player, "\n")
		
		try:
			wiimote[player].status.request()
		except:
			print(" Player ", player, " not connected\n")
			continue
			
		if wiimote[player].capabilities.has_extension(WiimoteExtensions.None):
			player_type[player] = NO_EXTENSION #None
		elif wiimote[player].capabilities.has_extension(WiimoteExtensions.Nunchuck):
			player_type[player] = NUNCHUCK_EXTENSION #Nunchuck
		elif wiimote[player].capabilities.has_extension(WiimoteExtensions.GuitarHeroGuitar):
			player_type[player] = GUITAR_EXTENSION #Guitar
		else:
			player_type[player] = OTHER_EXTENSION #disconnected

##############
# Led Toggle #
##############

def led_toggle(player_number, led_number):
	wiimote[player_number].status.setLEDState(led_number, not(wiimote[player_number].status.getLEDState(led_number)))

#########################
# Wiimote Button Binder #
#########################

def wButton_xButton(wiimote_num, xoutput_num, wButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].buttons.button_down(wButton))

def wButton_xButton(remote_num, wButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].buttons.button_down(wButton))

##########################
# Nunchuck Button Binder #
##########################

def nButton_xButton(wiimote_num, xoutput_num, nButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].nunchuck.buttons.button_down(nButton))

def nButton_xButton(remote_num, nButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].nunchuck.buttons.button_down(nButton))

########################
# Guitar Button Binder #
########################

def gButton_xButton(wiimote_num, xoutput_num, gButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].guitar.buttons.button_down(gButton))

def gButton_xButton(remote_num, gButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].guitar.buttons.button_down(gButton))

####################
# Wiimote mappings #
####################

def map_wiimote(n):	
	wButton_xButton(n, WiimoteButtons.A, XOutputButton.A)
	wButton_xButton(n, WiimoteButtons.B, XOutputButton.B)
	wButton_xButton(n, WiimoteButtons.One, XOutputButton.X)
	wButton_xButton(n, WiimoteButtons.Two, XOutputButton.Y)
	
	wButton_xButton(n, WiimoteButtons.Plus, XOutputButton.Back)
	wButton_xButton(n, WiimoteButtons.Minus, XOutputButton.Start)
	
	wButton_xButton(n, WiimoteButtons.DPadUp, XOutputButton.Up)
	wButton_xButton(n, WiimoteButtons.DPadRight, XOutputButton.Right)
	wButton_xButton(n, WiimoteButtons.DPadDown, XOutputButton.Down)
	wButton_xButton(n, WiimoteButtons.DPadLeft, XOutputButton.Left)

#####################
# Nunchuck mappings #
#####################

#TODO::Test mapping for nunchuck stick
def map_wiimote_nunchuck(n):
	nButton_xButton(n, NunchuckButtons.C, XOutputButton.L1)
	nButton_xButton(n, NunchuckButtons.Z, XOutputButton.R1)
	xoutput[n].lx = wiimote[n].nunchuck.stick.x
	xoutput[n].ly = wiimote[n].nunchuck.stick.y

###################
# Guitar mappings #
###################

#TODO::Test mapping for guitars
def map_wiimote_Guitar(n):
	gButton_xButton(n, GuitarButtons.Green, XOutputButton.A)
	gButton_xButton(n, GuitarButtons.Red, XOutputButton.B)
	gButton_xButton(n, GuitarButtons.Yellow, XOutputButton.X)
	gButton_xButton(n, GuitarButtons.Blue, XOutputButton.Y)
	gButton_xButton(n, GuitarButtons.Orange, XOutputButton.R1)
	
	gButton_xButton(n, GuitarButtons.Minus, XOutputButton.Back)
	gButton_xButton(n, GuitarButtons.Plus, XOutputButton.Start)
	
	gButton_xButton(n, GuitarButtons.StrumUp, XOutputButton.Up)
	gButton_xButton(n, GuitarButtons.StrumDown, XOutputButton.Down)

###################
# Wiimote updates #
###################

def update_wiimote1():
	map_wiimote(0)

def update_wiimote2():
	map_wiimote(1)

def update_wiimote3():
	map_wiimote(2)

def update_wiimote4():
	map_wiimote(3)

####################
# Nunchuck updates #
####################

def update_nunchuck_wiimote1():
	map_nunchuck_wiimote(0)

def update_nunchuck_wiimote2():
	map_nunchuck_wiimote(1)

def update_nunchuck_wiimote3():
	map_nunchuck_wiimote(2)

def update_nunchuck_wiimote4():
	map_nunchuck_wiimote(3)

##################
# Guitar updates #
##################

def update_wiimote_Guitar1():
	map_wiimote_Guitar(0)

def update_wiimote_Guitar2():
	map_wiimote_Guitar(1)

def update_wiimote_Guitar3():
	map_wiimote_Guitar(2)

def update_wiimote_Guitar4():
	map_wiimote_Guitar(3)

##################
# Player updates #
##################

def update_player_one():
	player_number = 0
	if player_type[player_number] == OTHER_EXTENSION:
		return False
	elif player_type[player_number] == NO_EXTENSION:		
		wiimote[player_number].buttons.update += update_wiimote1
	elif player_type[player_number] == NUNCHUCK_EXTENSION:
		wiimote[player_number].buttons.update += update_wiimote1
		wiimote[player_number].nunchuck.update += update_nunchuck_wiimote1
	elif player_type[player_number] == GUITAR_EXTENSION:
		wiimote[player_number].guitar.update += update_wiimote_Guitar1
	else:
		print("Wiimote ", player_number, " not updated\n")
		print("Unknown extension: ", player_type[player_number], "\n")

def update_player_two():
	player_number = 1
	if player_type[player_number] == OTHER_EXTENSION:
		return False
	elif player_type[player_number] == NO_EXTENSION:		
		wiimote[player_number].buttons.update += update_wiimote2
	elif player_type[player_number] == NUNCHUCK_EXTENSION:
		wiimote[player_number].buttons.update += update_wiimote2
		wiimote[player_number].nunchuck.update += update_nunchuck_wiimote2
	elif player_type[player_number] == GUITAR_EXTENSION:
		wiimote[player_number].guitar.update += update_wiimote_Guitar2
	else:
		print("Wiimote ", player_number, " not updated\n")
		print("Unknown extension: ", player_type[player_number], "\n")

def update_player_three():
	player_number = 2
	if player_type[player_number] == OTHER_EXTENSION:
		return False
	elif player_type[player_number] == NO_EXTENSION:		
		wiimote[player_number].buttons.update += update_wiimote3
	elif player_type[player_number] == NUNCHUCK_EXTENSION:
		wiimote[player_number].buttons.update += update_wiimote3
		wiimote[player_number].nunchuck.update += update_nunchuck_wiimote3
	elif player_type[player_number] == GUITAR_EXTENSION:
		wiimote[player_number].guitar.update += update_wiimote_Guitar3
	else:
		print("Wiimote ", player_number, " not updated\n")
		print("Unknown extension: ", player_type[player_number], "\n")
		
def update_player_four():
	player_number = 3
	if player_type[player_number] == OTHER_EXTENSION:
		return False
	elif player_type[player_number] == NO_EXTENSION:		
		wiimote[player_number].buttons.update += update_wiimote4
	elif player_type[player_number] == NUNCHUCK_EXTENSION:
		wiimote[player_number].buttons.update += update_wiimote4
		wiimote[player_number].nunchuck.update += update_nunchuck_wiimote4
	elif player_type[player_number] == GUITAR_EXTENSION:
		wiimote[player_number].guitar.update += update_wiimote_Guitar4
	else:
		print("Wiimote ", player_number, " not updated\n")
		print("Unknown extension: ", player_type[player_number], "\n")

###############
# Main Thingy #
###############

if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	
	update_player_type()
	
	update_player_one()
	update_player_two()
	update_player_three()
	update_player_four()
	
	