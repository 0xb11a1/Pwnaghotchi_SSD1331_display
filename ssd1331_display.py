import time
from demo_opts import get_device
from luma.core.render import canvas
import json
import requests
import base64 
import os


device = get_device()

total = -1
curr_run = -1
uptime = -1
face = "(@_!)	"
name = "pwni"
new_pwn ="Nothing :("

def get_curr():
	global face 
	global total
	global uptime
	global curr_run 
	global name
	global new_pwn
	
	# get the name of the newest handshakes
	path = '/root/handshakes/'
	os.chdir(path)
	files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
	new_pwn = files[-1].split("_")[0]

	# get status from the API
	response = requests.get('http://127.0.0.1:8666/api/v1/mesh/data')
	json_data = json.loads(response.text)
	try:
		face = json_data['face']
		total = json_data['pwnd_tot']
		curr_run = json_data['pwnd_run']
		uptime = json_data['uptime'] / 60.0 
		name = json_data['name']

	except:
		print("not running yet .....")
		return
	

	print("-----recevied face ")
	print(face)

	# convert the original face to simpler one
	if base64.b64encode(("(⇀‿‿↼)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "sleeping"
		face = "(-__-)"
		return
	if base64.b64encode(("(≖‿‿≖)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "awakening"
		face = "(=__=)"
		return
	if base64.b64encode(("(◕‿‿◕)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "awake"
		face = "(*__* )"
		return
	if base64.b64encode(("( ⚆_⚆)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")):
	 	face = "neutral mood"
	 	face = "( *__*)"
	 	return
	if base64.b64encode(("(☉_☉ )".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")):
	 	face = "neutral mood"
	 	face = "(*__* )"
	 	return
	if base64.b64encode(("( ◕‿◕)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
	 	face = "happy"
	 	face = "( *_*)"
	 	return
	if base64.b64encode(("(◕‿◕ )".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
	 	face = "happy"
	 	face = "(*_* )"
	 	return
	if base64.b64encode(("(°▃▃°)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "intense"
		face = "(*////*)"
		return
	if base64.b64encode(("(⌐■_■)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "cool"
		face = "( ,-#-#)"
		return
	if base64.b64encode(("(•‿‿•)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "happy"
		face = "(*..*)"
		return
	if base64.b64encode(("(^‿‿^)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "grateful"
		face = "(^__^)"
		return
	if base64.b64encode(("(ᵔ◡◡ᵔ)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "excited"
		face = "(^__^)"
		return
	if base64.b64encode(("(✜‿‿✜)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "smart"
		face = "(%__%)"
		return
	if base64.b64encode(("(♥‿‿♥)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "friendly"
		face = "(<3__<3)"
		return
	if base64.b64encode(("(☼‿‿☼)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "motivated"
		face = "(+__+)"
		return
	if base64.b64encode(("(≖__≖)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "demotivated"
		face = "(!__!)"
		return
	if base64.b64encode(("(-__-)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "bored"
		face = "(-___-)"
		return
	if base64.b64encode(("(╥☁╥ )".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "sad"
		face = "(~__~)"
		return
	if base64.b64encode(("(ب__ب)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "lonely"
		face = "(/__\\)"
		return
	if base64.b64encode(("(☓‿‿☓)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "broken"
		face = "(x__x)"
		return
	if base64.b64encode(("(#__#)".encode("utf-8"))) == base64.b64encode(face.encode("utf-8")): 
		face = "debugging"
		face = "(#__#)"
		return
	
	print("nothing match")
	
	face = "noooo"
	return  



while True:
	with canvas(device) as draw:
		get_curr()

		# for power consumption, I use a gray color (10,10,10)
		draw.text((0, 0),name, fill=(10,10,10))
		draw.text((50, 0),face, fill=(10,10,10))
		draw.line((0, 13, 96, 13), fill=(10,10,10))
		draw.text((0, 15),"uptime:  "+str(int(uptime)), fill=(10,10,10))
		draw.text((0, 25),"total :  "+str(total), fill=(10,10,10))
		draw.text((0, 35),"curr  :  "+str(curr_run), fill=(10,10,10))
		draw.text((0, 45),str(new_pwn), fill=(10,10,10))
		
		time.sleep(1)