from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import random
import time

app = Ursina(title="YaMinecraft 0.0.1 Classic",icon="icon.png")

fh=100
cs=0
icon_list=["empty","empty","empty","empty","empty","empty","empty","empty","empty"]
ground_perc=85
undground_perc=55
day=True
tree_create=3
invs_sel=1
invs=[]
sx = random.randint(-5,10)
sy = random.randint(-5,0)
sz = random.randint(-5,10)
asd = Entity()

for i in range(0,9):
	invs.append(Button(origin=(4.5-i,4),collider="box",scale=(0.1,0.1,0.1),icon="empty.png"))


class Items(Entity):
	def __init__(self,model="cube",position=(0,0,0),texture="item/apple.png",scale=(0.5,0.1,0.5)):
		super().__init__(self,model="cube",position=(0,2,3),texture="item/apple.png",scale=(0.003,0.2,0.2))
	def update(self):
		if distance(First, self) <= 2:
			empty_space=0
			for i in range(0,9):
				if icon_list[i]=="empty":
					empty_space = i
			icon_list[empty_space] = self.texture
			destroy(self)
			print("Collected an apple.")

class Block(Entity):
	def __init__(self,model="cube",position=(0,0,0),texture="cbs.png",collider='box',scale=(1,1,1)):
		super().__init__(position=position,
						model="cube",
						texture=texture,
						collider='box',
						color=color.white,
						scale=(1,1,1))
	def input(self,key):
		global invs_sel
		if key == "escape":
			sys.exit()
		if key == "1":
			invs_sel=0
		if key == "2":
			invs_sel=1
		if key == "3":
			invs_sel=2
		if key == "4":
			invs_sel=3
		if key == "5":
			invs_sel=4
		if key == "6":
			invs_sel=5
		if key == "7":
			invs_sel=6
		if key == "8":
			invs_sel=7
		if key == "9":
			invs_sel=8
		if self.hovered:
			if key=="left mouse down":
				empty_space=0
				for i in range(0,9):
					if icon_list[i] == "empty":
						empty_space = i
				icon_list[empty_space] = self.texture
				destroy(self)
				print(icon_list)
			if key=="right mouse down" and icon_list[invs_sel]!="empty":
				Block(position=self.position+mouse.normal,texture=icon_list[invs_sel],collider="box")
				icon_list[invs_sel]="empty"
				print(icon_list)
n=[]
iron_plus=10
def tree_planting(stl=(0,1,0)):
	for i in range(stl[1],stl[1]+5):
		loc = (stl[0],i,stl[2])
		Block(position=loc,texture="log.png")
	Block(position=(stl[0],stl[1]+5,stl[2]),texture="leaf.png")
	for i in range(3,5):
		Block(position=(stl[0]+1,stl[1]+i,stl[2]),texture="leaf.png")
		Block(position=(stl[0]-1,stl[1]+i,stl[2]),texture="leaf.png")
		Block(position=(stl[0],stl[1]+i,stl[2]+1),texture="leaf.png")
		Block(position=(stl[0],stl[1]+i,stl[2]-1),texture="leaf.png")
	Block(position=(stl[0]+2,stl[1]+3,stl[2]),texture="leaf.png")
	Block(position=(stl[0]-2,stl[1]+3,stl[2]),texture="leaf.png")
	Block(position=(stl[0],stl[1]+3,stl[2]+2),texture="leaf.png")
	Block(position=(stl[0],stl[1]+3,stl[2]-2),texture="leaf.png")
	Block(position=(stl[0]+1,stl[1]+3,stl[2]+1),texture="leaf.png")
	Block(position=(stl[0]-1,stl[1]+3,stl[2]+1),texture="leaf.png")
	Block(position=(stl[0]+1,stl[1]+3,stl[2]-1),texture="leaf.png")
	Block(position=(stl[0]-1,stl[1]+3,stl[2]-1),texture="leaf.png")
def wb(stx=-10,sty=-12,stz=-10):
	global iron_plus
	for i in range(stx,stx+16):
		for j in range(stz,stz+16):
			for k in range(sty,0):
				if random.randint(0,101)<=undground_perc:
					adf = random.randint(0,1001)
					if adf<=850:
						Block(model="cube",texture="stone.png",position=(i,k,j),collider='box')
					elif adf >= 851 and adf <= 920:
						Block(model="cube",texture="diorite.png",position=(i,k,j),collider='box')
					elif adf >= 921 and adf <= 950:
						Block(model="cube",texture="iron_ore.png",position=(i,k,j),collider='box')
					elif adf >= 951 and adf <= 995:
						Block(model="cube",texture="coal.png",position=(i,k,j),collider='box')
					else:
						Block(model="cube",texture="diamond.png",position=(i,k,j),collider='box')

			if random.randint(0,101)<=ground_perc:
				for k in range(0,1):
					Block(model="cube",texture="grass.png",position=(i,k,j),collider='box')
	for i in range(stx,stx+16):
		for j in range(stz,stz+16):
			Block(model="cube",texture="bedrock.png",position=(i,-13,j),collider='box')




pivot = Entity(model="cube",color=color.yellow,scale=(30,30,30),position=(0,300,0))



wb()

for i in range(-10,5):
	for j in range(-10,5):
		if random.randint(0,101)>=100-tree_create:
			tree_planting(stl=(i,0,j))

if not day:
	DirectionalLight(parent=pivot, shadows=True)
	DirectionalLight(parent=pivot, shadows=True)
	DirectionalLight(parent=pivot, shadows=True)
	DirectionalLight(parent=pivot, shadows=True)
else:
	window.color=color.azure

def clouds(create):
	for i in range(-300,300,10):
		for j in range(-300,300,10):
			if random.randint(0,101)>=100-create:
				Entity(model='cube',texture="clouds.png",position=(i,200,j),scale=(10,1,10))

clouds(10)
Text(text='YaMinecraft Start-Edition 24w01a', origin=(0,-18.5),font="mae.ttf")
cs=0

def inven():
	for i in range(0,9):
		invs[i].icon = icon_list[i]
def shift_end(ws):
	First.height=ws
def input(key):
	if key == "r":
		First.position=(0,2,0)
		Block(model="cube",texture="cbs.png",position=(round(First.x),floor(First.y-1),round(First.z)),collider='box')
	if key=="k":
		print("Player Position:x=",round(First.x),",y=",round(First.y),",z=",round(First.z))
	if key=="right shift":
		First.gravity = 0
	if key == "left shift":
		First.gravity = 1
pivot.update=inven
First=FirstPersonController()
First.jump_height = 1.4
First.position=(0,100,0)
Items()
Items(position=(0,2,0))
if __name__ == "__main__":
	app.run()