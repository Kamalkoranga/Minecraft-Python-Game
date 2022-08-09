from ursina import *

class Test_Cube(Entity):
	def __init__(self):
		super().__init__(
				model='cube',
				color=color.white,
				texture='white_cube',
				rotation=Vec3(45,45,45)
			)

class Test_Button(Button):
	def __init__(self):
		super().__init__(
			parent=scene,
			model='cube',
			texture='brick',
			color=color.blue,
			highlight_color=color.red,
			pressed_color=color.lime
		)

	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				print("Left pressed")

def update():
	if held_keys['a']:
		test_square.x -= 3 * time.dt

app = Ursina()

test_square = Entity(model='quad', color=color.red, scale=(4,4), position=(5,1))

sans_texture = load_texture('assets/Sans.png')
sans = Entity(model='quad', texture=sans_texture)
test_cube = Test_Button()

app.run()