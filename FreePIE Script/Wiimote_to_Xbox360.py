#Created by ElliotGamer3
#	
#	This file contains wiimote to xoutput definitions
#	Created by Elliot Imhoff
#	Credit where due to creators of XOutputPlugin
#
# Uses XOutputPlugin to map multiple wiimotes to xbox virtual remotes
# Detects accessory changes to wiimotes and updates mappings accordingly
# Currently detects and has maps for:
#	Wii Guitar
#	Wii Remote (no accessories)
#

POLLING_PERIOD 	= 1

# If MAX_PLAYERS is increased, update definitons listed below must be made for added players
# update_wiimote
# update_wiimote_Guitar
# update_player_<PLAYERNUMBER>
# Once this is done update_player_<PLAYERNUMBER>() must be called after
# update_player_<PLAYERNUMBER - 1>()
#
# List for keeping track of players current accessories
# Definition for updating the player_type list
# Guitar = 2
# No Accessories = 1
# Other = -1


MAX_PLAYERS = 4

GUITAR_EXTENSION = 3
NUNCHUCK_EXTENSION = 2
NO_EXTENSION = 1
OTHER_EXTENSION = -1

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


def led_toggle(player_number, led_number):
	wiimote[player_number].status.setLEDState(led_number, not(wiimote[player_number].status.getLEDState(led_number)))


def map_wiimote(n):
	xoutput[n].setButton(XOutputButton.A, wiimote[n].buttons.button_down(WiimoteButtons.A))
	xoutput[n].setButton(XOutputButton.B, wiimote[n].buttons.button_down(WiimoteButtons.B))
	xoutput[n].setButton(XOutputButton.X, wiimote[n].buttons.button_down(WiimoteButtons.One))
	xoutput[n].setButton(XOutputButton.Y, wiimote[n].buttons.button_down(WiimoteButtons.Two))

	xoutput[n].setButton(XOutputButton.Back, wiimote[n].buttons.button_down(WiimoteButtons.Plus))
	xoutput[n].setButton(XOutputButton.Start, wiimote[n].buttons.button_down(WiimoteButtons.Minus))
	
	xoutput[n].setButton(XOutputButton.Up, wiimote[n].buttons.button_down(WiimoteButtons.DPadUp))
	xoutput[n].setButton(XOutputButton.Right, wiimote[n].buttons.button_down(WiimoteButtons.DPadRight))
	xoutput[n].setButton(XOutputButton.Down, wiimote[n].buttons.button_down(WiimoteButtons.DPadDown))
	xoutput[n].setButton(XOutputButton.Left, wiimote[n].buttons.button_down(WiimoteButtons.DPadLeft))
	
def map_wiimote_Guitar(n):
	xoutput[n].setButton(XOutputButton.A, wiimote[n].guitar.buttons.button_down(GuitarButtons.Green))
	xoutput[n].setButton(XOutputButton.B, wiimote[n].guitar.buttons.button_down(GuitarButtons.Red))
	xoutput[n].setButton(XOutputButton.Y, wiimote[n].guitar.buttons.button_down(GuitarButtons.Yellow))
	xoutput[n].setButton(XOutputButton.X, wiimote[n].guitar.buttons.button_down(GuitarButtons.Blue))
	xoutput[n].setButton(XOutputButton.R1, wiimote[n].guitar.buttons.button_down(GuitarButtons.Orange))
	
	xoutput[n].setButton(XOutputButton.Back, wiimote[n].guitar.buttons.button_down(GuitarButtons.Minus))
	xoutput[n].setButton(XOutputButton.Start, wiimote[n].guitar.buttons.button_down(GuitarButtons.Plus))
	
	xoutput[n].setButton(XOutputButton.Up, wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumUp))
	xoutput[n].setButton(XOutputButton.Down, wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumDown))

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


def update_nunchuck_wiimote1():
	map_nunchuck_wiimote(0)

def update_nunchuck_wiimote2():
	map_nunchuck_wiimote(1)

def update_nunchuck_wiimote3():
	map_nunchuck_wiimote(2)

def update_nunchuck_wiimote4():
	map_nunchuck_wiimote(3)

def update_wiimote_Guitar1():
	map_wiimote_Guitar(0)

def update_wiimote_Guitar2():
	map_wiimote_Guitar(1)

def update_wiimote_Guitar3():
	map_wiimote_Guitar(2)

def update_wiimote_Guitar4():
	map_wiimote_Guitar(3)
	

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

if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	
	update_player_type()
	
	update_player_one()
	update_player_two()
	update_player_three()
	update_player_four()