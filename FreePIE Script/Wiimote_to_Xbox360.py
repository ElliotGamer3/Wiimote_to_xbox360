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
UNSUPPORTED_EXTENSION = 0
UNKNOWN_EXTENSION = -1

##############
# Led Toggle #
##############

def toggle_LED(wiimote_num, led_number):
	wiimote[wiimote_num].status.setLEDState(led_number, not(wiimote[wiimote_num].status.getLEDState(led_number)))

##################################
# Button to Mouse Button Binders #
##################################

def wButton_mButton(remote_num, wButton, mButton):
	if wiimote[remote_num].buttons.button_down(wButton):
		mouse.setButton(mButton, True)
	else:
		mouse.setButton(mButton, False)

def gButton_mButton(remote_num, gButton, mButton):
	if wiimote[remote_num].guitar.buttons.button_down(gButton):
		mouse.setButton(mButton, True)
	else:
		mouse.setButton(mButton, False)
		
def nButton_mButton(remote_num, nButton, mButton):
	if wiimote[remote_num].nunchuck.buttons.button_down(nButton):
		mouse.setButton(mButton, True)
	else:
		mouse.setButton(mButton, False)

#########################
# Button to Key Binders #
#########################

def wButton_kButton(remote_num, wButton, kButton):
	if wiimote[remote_num].buttons.button_down(wButton):
		keyboard.setKeyDown(kButton)
	else:
		keyboard.setKeyUp(kButton)

def gButton_kButton(remote_num, gButton, kButton):
	if wiimote[remote_num].guitar.buttons.button_down(wButton):
		keyboard.setKeyDown(kButton)
	else:
		keyboard.setKeyUp(kButton)
      
def nButton_kButton(remote_num, nButton, kButton):
	if wiimote[remote_num].nunchuck.buttons.button_down(wButton):
		keyboard.setKeyDown(kButton)
	else:
		keyboard.setKeyUp(kButton)

##########################
# Wiimote Button Binders #
##########################

def wButton_xButton(wiimote_num, xoutput_num, wButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].buttons.button_down(wButton))

def wButton_xButton(remote_num, wButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].buttons.button_down(wButton))

###########################
# Nunchuck Button Binders #
###########################

def nButton_xButton(wiimote_num, xoutput_num, nButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].nunchuck.buttons.button_down(nButton))

def nButton_xButton(remote_num, nButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].nunchuck.buttons.button_down(nButton))

#########################
# Guitar Button Binders #
#########################

def gButton_xButton(wiimote_num, xoutput_num, gButton, xButton):
	xoutput[xoutput_num].setButton(xButton, wiimote[wiimote_num].guitar.buttons.button_down(gButton))

def gButton_xButton(remote_num, gButton, xButton):
	xoutput[remote_num].setButton(xButton, wiimote[remote_num].guitar.buttons.button_down(gButton))

####################
# Wiimote Mappings #
####################

diagnostics.watch(wiimote[0].buttons)

def map_wiimote(wiimote_num):	
	wButton_xButton(wiimote_num, WiimoteButtons.A, XOutputButton.A)
	wButton_xButton(wiimote_num, WiimoteButtons.B, XOutputButton.B)
	wButton_xButton(wiimote_num, WiimoteButtons.One, XOutputButton.X)
	wButton_xButton(wiimote_num, WiimoteButtons.Two, XOutputButton.Y)
	
	wButton_xButton(wiimote_num, WiimoteButtons.Plus, XOutputButton.Back)
	wButton_xButton(wiimote_num, WiimoteButtons.Minus, XOutputButton.Start)
	
	wButton_xButton(wiimote_num, WiimoteButtons.DPadUp, XOutputButton.Up)
	wButton_xButton(wiimote_num, WiimoteButtons.DPadRight, XOutputButton.Right)
	wButton_xButton(wiimote_num, WiimoteButtons.DPadDown, XOutputButton.Down)
	wButton_xButton(wiimote_num, WiimoteButtons.DPadLeft, XOutputButton.Left)
	toggle_button_press(wiimote_num)
	
def map_wiimote_KB(wiimote_num):
	wButton_kButton(wiimote_num, WiimoteButtons.A, Key.LeftShift)
	wButton_kButton(wiimote_num, WiimoteButtons.B, Key.LeftAlt)
	wButton_mButton(wiimote_num, WiimoteButtons.One, mouse.leftButton)
	wButton_kButton(wiimote_num, WiimoteButtons.Two, Key.Space)
	
	wButton_kButton(wiimote_num, WiimoteButtons.Plus, Key.Escape)
	wButton_kButton(wiimote_num, WiimoteButtons.Minus, Key.E)
	
	wButton_kButton(wiimote_num, WiimoteButtons.DPadUp, Key.A)
	wButton_kButton(wiimote_num, WiimoteButtons.DPadRight, Key.W)
	wButton_kButton(wiimote_num, WiimoteButtons.DPadDown, Key.D)
	wButton_kButton(wiimote_num, WiimoteButtons.DPadLeft, Key.S)
	toggle_button_press(wiimote_num)

#####################
# Nunchuck Mappings #
#####################

#TODO::Test mapping for nunchuck stick
def map_wiimote_Nunchuck(remote_num):
	nButton_xButton(remote_num, NunchuckButtons.C, XOutputButton.L1)
	nButton_xButton(remote_num, NunchuckButtons.Z, XOutputButton.R1)
	xoutput[remote_num].lx = wiimote[remote_num].nunchuck.stick.x
	xoutput[remote_num].ly = wiimote[remote_num].nunchuck.stick.y

###################
# Guitar Mappings #
###################

def map_wiimote_Guitar(wiimote_num):
	gButton_xButton(wiimote_num, GuitarButtons.Green, XOutputButton.A)
	gButton_xButton(wiimote_num, GuitarButtons.Red, XOutputButton.B)
	gButton_xButton(wiimote_num, GuitarButtons.Yellow, XOutputButton.X)
	gButton_xButton(wiimote_num, GuitarButtons.Blue, XOutputButton.Y)
	gButton_xButton(wiimote_num, GuitarButtons.Orange, XOutputButton.R1)
	
	gButton_xButton(wiimote_num, GuitarButtons.Minus, XOutputButton.Back)
	gButton_xButton(wiimote_num, GuitarButtons.Plus, XOutputButton.Start)
	
	gButton_xButton(wiimote_num, GuitarButtons.StrumUp, XOutputButton.Up)
	gButton_xButton(wiimote_num, GuitarButtons.StrumDown, XOutputButton.Down)

###################
# Wiimote Updates #
###################

def update_wiimote1():
	map_wiimote(0)

def update_wiimote2():
	map_wiimote(1)

def update_wiimote3():
	map_wiimote(2)

def update_wiimote4():
	map_wiimote(3)
	
def update_wiimote1_KB():
	map_wiimote_KB(0)

####################
# Nunchuck Updates #
####################

def update_wiimote_Nunchuck1():
	map_wiimote_Nunchuck(0)

def update_wiimote_Nunchuck2():
	map_wiimote_Nunchuck(1)

def update_wiimote_Nunchuck3():
	map_wiimote_Nunchuck(2)

def update_wiimote_Nunchuck4():
	map_wiimote_Nunchuck(3)
	
#ADD MAPPING	
def update_wiimote_Nunchuck1_KB():
	return
	
##################
# Guitar Updates #
##################

def update_wiimote_Guitar1():
	map_wiimote_Guitar(0)

def update_wiimote_Guitar2():
	map_wiimote_Guitar(1)

def update_wiimote_Guitar3():
	map_wiimote_Guitar(2)

def update_wiimote_Guitar4():
	map_wiimote_Guitar(3)

#ADD MAPPING
def update_wiimote_Guitar1_KB():
	return
	
##############################
# Player One Keyboard Update #
##############################

def update_player_one_KB():
	update_wiimote1_KB()
	update_wiimote_Nunchuck1_KB()
	update_wiimote_Guitar1_KB()

##################
# Player Updates #
##################

def update_player_one():
	update_wiimote1()
	update_wiimote_Nunchuck1()
	update_wiimote_Guitar1()

def update_player_two():
	update_wiimote2()
	update_wiimote_Nunchuck2()
	update_wiimote_Guitar2()
	
def update_player_three():
	update_wiimote3()
	update_wiimote_Nunchuck3()
	update_wiimote_Guitar3()
	
def update_player_four():
	update_wiimote4()
	update_wiimote_Nunchuck4()
	update_wiimote_Guitar4()

########################
# Capabilities Enabler #
########################

def enable_extensions(wiimote_num):
	wiimote[wiimote_num].enable(WiimoteCapabilities.Extension)

####################
# Debug Definition #
####################

def toggle_button_press(wiimote_num):
	if wiimote[wiimote_num].buttons.button_pressed(WiimoteButtons.Home):
		toggle_LED(wiimote_num, wiimote_num)
		
###############
# Main Thingy #
###############

if wiimote[0].status.getLEDState(0):
	update_player_one_KB()
else:
	update_player_one()
	
if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD

	update_player_two()
	update_player_three()
	update_player_four()
	
	