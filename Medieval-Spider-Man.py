	#Medieval Spider-man.py
	
	
import time
	
a=0
b=0
c=0
d=0	
	
def introduction():
	print("Welcome to Medieval Spider-Man")
	print("Once upon a time, Green Goblin created a time machine to get Spider-Man out of the way of his takeover on New York.")
	print("His plan was successful and he was able to leave Spider-Man stuck in the seventeenth century. Help Spider-man get back to the twenty first century.")
	time.sleep(.8)
	print("...")
	time.sleep(.8)
	print("...")
	print("Mordred: Intruder! Intruder! There is an intruder in the castle!")
	time.sleep(.5)
	print("Spider-Man: Wait!... I'm not... there is a mis...")
	time.sleep(.5)
	print("Mordred: Save the excuse for the dungeons you criminal!")
	mordred()
	
def mordred():
	global a
	global b
	global c
	global d
	d = d + 1
	time.sleep(.5)
	print("Morded draws his sword and Spider-Man must decide what to do. Help Spider-Man decide what to do to get back.")
	answer = int(input("1. Knock him out! \n 2. Run Away \n 3. Try to reason \n"))
	if answer==1:
		a = a + 1
		print("Spider-Man does a back flip and kicks him in the face to knock him out")
		KingArthur()
	elif answer == 2:
		print("Mordred chases after the fleeting Spider-Man")
		KingArthur()
		b=b+1
	if b>=3:
		capture()
	elif answer ==3:
		c=c+1
		print("Spider-Man: I am not a criminal! I am a superhero from the future, I live in New York, and I save people.")
		time.sleep(.5)
		print("Morded: Where the hell is New York? Did you really think I would be gullible enough to believe your lies.")
		time.sleep(.5)
		print("Spider-Man fails to reason and flees the scene.")
		KingArthur()
		
		
	
	
def KingArthur():
	global a
	global b
	global c 
	global d 
	d = d + 1
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("After Spider-Man's encounter with Mordred he comes across King Arthur.")
	time.sleep(.5)
	print("King Artur: HALT, intruder! What are you doing trampling inside my castle in such an insulting costume. Did you come to assassinate me?")
	time.sleep(.5)
	print("Spider-Man: I don't want to assassinate you. I don't want to kill people. I don't even know you...")
	time.sleep(.5)
	print("King Arthur: ...")
	time.sleep(.5)
	print("King Arthur: I am King Arthur! What is a peasant like you doing in my castle?")
	time.sleep(.5)
	print("...")
	answer = int(input("1. Knock him out! \n 2. Run away \n 3. Try to reason \n"))
	if answer == 1:
		a = a + 1
		print("Spider-Man attaches himself to the ceiling and launches himself at the king knocking him out.")
	elif answer == 2:
		b = b + 1
		if b>=1:
			capture()
			print("Spider-Man flees and the king gives order for the knights to chase him down.")

	elif answer == 3:
		c = c + 1
		print("Spider-Man: I am not a killer I am just lost.")
		time.sleep(.5)
		print("King Arthur: Lost?")
		time.sleep(.5)
		print("Spider-Man explains his situation.")
		time.sleep(.5)
		print("The king is suspicious but he chooses to believe Spider-Man.")
		time.sleep(.5)
		print("King Arthur: I shall choose to believe you but if I find out you do anything I will have you executed. Let us find Gauis, the Court physician, I think he may be able to help you.")
		gaius()
		
		
def gaius():
	global a 
	global b 
	global c
	global d 
	d = d + 1
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("Gaius: King Arthur! Is there anything you need? And this person is...?")
	print("King Arthur: This is...")
	print("Spider-Man: Spider-Man.")
	time.sleep(.5)
	print("Gaius: Pleased to meet you Spider-Man.")
	print("Spider-Man: You as well...")
	time.sleep(.5)
	print("King Arthur: He claims to be from the future. Do you have any way of confirming this?")
	time.sleep(.5)
	print("Gaius: The future? Um yes. A simple truth potion should confirm this.")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("Gaius: My goodness, he really is from the future. How on earth did you travel to the past?")
	time.sleep(.5)
	print("Spider-Man: Haha ha. I would ask if you had any way to travel me back to the future?")
	time.sleep(.5)
	print("Gaius: Can I? Of course, it will take me a few months to get the right ingredients for the right potion but I can get you home.")
	time.sleep(.5)
	print("Spider-Man spends the next 6 months helping Gaius brew the required potion to get home. But eventually he does the skyscrapers of New York City.")
	print("GAMEOVER" + "Spider-Man met" + str(d) + "people.")
	

		
		
		
		
		
def capture():
		print("Too many people are chasing Spider-Man and he is eventually captured.")
		if (a+b)>c:
			print("Spider-Man tries to reason with the people and they do not believe him he will be thrown into the dungeons and will be executed.")
		else:
			print("Using his negotiation skills the people believe him and try to help him get back home.")
	
		
		
		
introduction()	
