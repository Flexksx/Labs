import random

def game():
	anascore=0
	danscore=0
	anaturn=1
	while(anascore<=25 and danscore<=25):
		while anaturn:
			x=random.uniform(0,1)
			if(x>=0.3):
				anascore+=1
			else:
				anaturn=0
				danscore+=1
			if anascore>=25:
				return 1
			
		while not anaturn:
			x=random.uniform(0,1)
			if(x>=0.5):
				danscore+=1
			else:
				anaturn=1
				anascore+=1
			if danscore>=25:
				return 0

tries=100000
anawins=0
for i in range(tries):
	anawins+=game()
print("Probability of Ana win:",anawins/tries)

