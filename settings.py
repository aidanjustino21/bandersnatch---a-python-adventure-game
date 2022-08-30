# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}



# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'



# enemy
monster_data = {
	'squid': {'speed': 3,   'notice_radius': 360},
	'raccoon': {'speed': 2,   'notice_radius': 400},
	'spirit': { 'speed': 4,   'notice_radius': 350},
	'bamboo': { 'speed': 3,   'notice_radius': 300}}
