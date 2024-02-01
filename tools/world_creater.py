import random
#0:empty;1:stone;2:diorite;3:coal_ore;4:iron_ore;5:diamond_ore;6:gold_ore;7:bedrock;8:grass
with open("world.json","w") as cr:
	cr.write("")
str_list=""
temp=""
def world_b():
	global temp,str_list
	temp = "8888888888\n"
	for i in range(0,10):
		str_list+=temp
	temp=""
	str_list+="-\n"
	for i in range(0,210):
		for j in range(0,10):
			if random.randint(0,101)<=40:
				adf = random.randint(0,1001)
				if adf<=940:
					temp+="1"
				elif adf >= 941 and adf <= 943:
					temp+="6"
				elif adf >= 944 and adf <= 970:
					temp+="2"
				elif adf >= 971 and adf <= 980:
					temp+="4"
				elif adf >= 981 and adf <= 1000:
					temp+="3"
				else:
					temp+="5"
			else:
				temp+="0"
		temp+="\n"
		if i % 10 == 0 and i != 0:
			temp+="-\n"
		str_list+=temp
		temp=""
	str_list+="0121134221\n-\n"
	temp = "7777777777\n"
	for i in range(0,10):
		str_list+=temp
	print(str_list)
	with open("world.json","w") as wd:
		wd.write(str_list)
world_b()