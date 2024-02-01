from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.input_field import InputField
from ursina.prefabs.health_bar import HealthBar
import sys
import random
import time

app = Ursina(title="YaMinecraft 0.1.0 Standard",icon="icon.png")
tick=0
hb=HealthBar(max_value=100, roundness=.6, animation_duration=.5, show_text=True)
faller=[0]
item_list=["apple.png","diamond.png"]
icon_list=["empty","empty","empty","empty","empty","empty","empty","empty","empty"]
ground_perc=85
undground_perc=45
tree_create=5
invs_sel=1
player_hit=10
player_blood=100
invs=[]
sx = random.randint(-5,10)
sy = random.randint(-5,0)
sz = random.randint(-5,10)
for i in range(0,9):
	invs.append(Button(origin=(4.5-i,4),collider="box",scale=(0.1,0.1,0.1),icon="empty.png"))
class Mob(Entity):
	def __init__(self,texture,typ="mob_standard",model="cube",position=(0,1,0),scale=(1,1,1),hitting=5,blood=10,collider='box'):
		super().__init__(self,texture=texture,typ="mob_standard",model="cube",position=(0,1,0),scale=(1,1,1),hitting=5,blood=10,collider='box')
	def input(self, key):
		global player_hit,player_blood
		if distance(First, self) <= 4:
			if key == "left mouse down" and self.hovered:
				self.blood-=player_hit
	def update(self):
		global player_hit,player_blood,tick
		hb.value=round(player_blood)
		tick+=1
		faller.append(First.air_time)
		if faller[-1] == 0 and faller[-2] >= 0.125:
			player_blood-=faller[-2]*150
		if First.x > self.x:
			self.x+=0.05
		if First.x < self.x:
			self.x-=0.05
		if First.z > self.z:
			self.z+=0.05
		if First.z < self.z:
			self.z-=0.05
		if distance(First,self) <= 2 and tick % 8 == 0:
			player_blood-=self.hitting
		if player_blood <= 0:
			print("You are dead!")
			window.color=color.red
		if self.blood <= 0:
			destroy(self)
		if tick % 300 == 0:
			Mob(position=(random.randint(-10,6),1,random.randint(-10,6)),texture="mob/sinc.png")

class Items(Entity):
	def __init__(self,texture,model="cube",position=(0,1,3),scale=(0.003,0.2,0.2)):
		super().__init__(self,texture=texture,model="cube",position=(0,1,3),scale=(0.003,0.2,0.2),blood=100)
	def update(self):
		if distance(First, self) <= 1 and "empty" in icon_list:
			empty_space=0
			for i in range(0,9):
				if icon_list[i]=="empty":
					empty_space = i
			icon_list[empty_space] = self.texture
			destroy(self)
			print("Collected an apple.")

class Block(Entity):
	def __init__(self,typ,model="cube",position=(0,0,0),texture="cbs.png",collider='box',scale=(1,1,1)):
		super().__init__(position=position,
						typ=typ,
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
		if key == "v":
			First.speed=7.5
		if key == "l":
			First.speed=5
		if self.hovered:
			if key == "left mouse down" and self.typ != "bedrock" and distance(First,self)<=4:
				destroy(self)
				if "empty" in icon_list:
					if self.typ == "diamond_ore":
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = "item/diamond"
					elif self.typ == "leaf":
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = "item/apple"
					elif self.typ == "coal_ore":
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = "item/coal"
					elif self.typ == "iron_ore":
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = "item/iron"
					elif self.typ == "gold_ore":
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = "item/gold"
					else:
						empty_space=0
						for i in range(0,9):
							if icon_list[i] == "empty":
								empty_space = i
						icon_list[empty_space] = str(self.texture)[0:-4]

			elif key == "right mouse down" and icon_list[invs_sel] != "empty":
				Block(position=self.position+mouse.normal,texture=icon_list[invs_sel]+".png",collider="box",typ=icon_list[invs_sel])
				icon_list[invs_sel]="empty"
n=[]
def tree_planting(stl=(0,1,0)):
	for i in range(stl[1],stl[1]+6):
		loc = (stl[0],i,stl[2])
		Block(position=loc,texture="log.png",typ="log")
	Block(position=(stl[0],stl[1]+6,stl[2]),texture="leaf.png",typ="leaf")
	for i in range(4,6):
		Block(position=(stl[0]+1,stl[1]+i,stl[2]),texture="leaf.png",typ="leaf")
		Block(position=(stl[0]-1,stl[1]+i,stl[2]),texture="leaf.png",typ="leaf")
		Block(position=(stl[0],stl[1]+i,stl[2]+1),texture="leaf.png",typ="leaf")
		Block(position=(stl[0],stl[1]+i,stl[2]-1),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]+2,stl[1]+4,stl[2]),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]-2,stl[1]+4,stl[2]),texture="leaf.png",typ="leaf")
	Block(position=(stl[0],stl[1]+4,stl[2]+2),texture="leaf.png",typ="leaf")
	Block(position=(stl[0],stl[1]+4,stl[2]-2),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]+1,stl[1]+4,stl[2]+1),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]-1,stl[1]+4,stl[2]+1),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]+1,stl[1]+4,stl[2]-1),texture="leaf.png",typ="leaf")
	Block(position=(stl[0]-1,stl[1]+4,stl[2]-1),texture="leaf.png",typ="leaf")
gl=997
def wb(stx=-10,sty=-12,stz=-10):
	global iron_plus,gl
	for i in range(stx,stx+21):
		for j in range(stz,stz+21):
			for k in range(sty,0):
				if random.randint(0,101)<=undground_perc:
					adf = random.randint(0,1001)
					if adf<=940:
						pass
						Block(model="cube",texture="stone.png",position=(i,k,j),collider='box',typ="stone")
					elif adf >= 941 and adf <= 943:
						Block(model="cube",texture="gold_ore.png",position=(i,k,j),collider='box',typ="gold_ore")
					elif adf >= 944 and adf <= 975:
						Block(model="cube",texture="diorite.png",position=(i,k,j),collider='box',typ="diorite")
					elif adf >= 976 and adf <= 980:
						Block(model="cube",texture="iron_ore.png",position=(i,k,j),collider='box',typ="iron_ore")
					elif adf >= 981 and adf <= gl:
						Block(model="cube",texture="coal_ore.png",position=(i,k,j),collider='box',typ="coal_ore")
					else:
						Block(model="cube",texture="diamond_ore.png",position=(i,k,j),collider='box',typ="diamond_ore")
					if k >= -8:
						gl=999
					if k >= -4:
						gl == 1002

			if random.randint(0,101)<=ground_perc:
				for k in range(0,1):
					Block(model="cube",texture="grass.png",position=(i,k,j),collider='box',typ="grass")
	for i in range(stx,stx+21):
		for j in range(stz,stz+21):
			Block(model="cube",texture="bedrock.png",position=(i,-13,j),collider='box',typ="bedrock")

piv = Entity()
pivot = Entity()
pivo2t = Entity()


wb()

for i in range(-10,10):
	for j in range(-10,10):
		if random.randint(0,101)>=100-tree_create:
			tree_planting(stl=(i,0,j))

window.color=color.azure
clouds = []

def cloud_move():
	global clouds
	for i in clouds:
		i.x+=i.dx
		if i.x >= 450:
			i.dx=-random.uniform(0.01,0.03)
		if i.x <= -450:
			i.dx=random.uniform(0.01,0.03)
Text(text='YaMinecraft Standard 0.1.2 Preview', origin=(0,-18.5),font="mae.ttf")
cs=0
if random.randint(0,2) == 0:
	days="night"
else:
	days="day"

if days == "day":

	piv.update = cloud_move
	pivot.model="cube"
	pivot.texture="sun.png"
	pivot.scale=(30,30,30)
	pivot.position=(0,300,0)
	for i in range(-400,400,10):
		for j in range(-400,400,10):
			if random.randint(0,101)>=100-5:
				clouds.append(Entity(model='cube',texture="clouds.png",position=(i,random.randint(130,250),j),scale=(15,10,15),dx=random.uniform(0.01,0.03)))
else:
	piv.update = cloud_move
	for i in range(-400,400,10):
		for j in range(-400,400,10):
			if random.randint(0,101)>=100-5:
				clouds.append(Entity(model='cube',color=color.rgb(65,70,76),position=(i,random.randint(130,250),j),scale=(15,10,15),dx=random.uniform(0.01,0.03)))
	Entity(model="cube",texture="moon.png",scale=(30,30,30),position=(0,300,0))
	window.color=color.rgb(40,40,40)
	for i in range(-400,400,10):
		for j in range(-400,400,10):
			if random.randint(0,101)>=98:
				if random.randint(0,101) >= 20:
					Entity(model="cube",color=color.white,position=(i,600,j))
				else:
					Entity(model="cube",color=color.orange,position=(i,600,j))
def inven():
	for i in range(0,9):
		invs[i].icon = icon_list[i]+".png"
def shift_end(ws):
	First.height=ws
acti = False
can_compound=["glass","planks"]
cv=""
def input(key):
	global can_compound,acti,icon_list,cv,tick
	if key == "t":
		if not acti:
			cv = InputField()
			acti=True
	if key == "enter" and acti:
		cvt = cv.text.split(" ")
		if cvt[0] == "craft":
			if cvt[1] == "planks" and icon_list[0] == "log" and cvt[1] in can_compound :
				icon_list[0] = cvt[1]
		else:
			print("Player A says:"+cv.text)
		destroy(cv)
	if key == "r":
		First.position=(0,2,0)
		Block(model="cube",texture="cbs.png",position=(round(First.x),floor(First.y-1),round(First.z)),collider='box',typ="cbs")
	if key=="k":
		print("Player Position:x=",round(First.x),",y=",round(First.y),",z=",round(First.z))
	if key == "n":
		print(tick)
pivot.update=inven
First=FirstPersonController()
First.jump_height = 1.4
First.speed=5
First.position=(0,1.5,0)
Mob(texture="mob/sinc.png")
if __name__ == "__main__":
	app.run()