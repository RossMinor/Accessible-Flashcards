import json
import random
import pyperclip as Pc
import textwrap
from DirIndexLoad import *

Card = {}
UserInput = ""

print("Welcome to Accessible Flashcards!\nTo stay up to date on updates and bug fixes, be sure to check the Github repo at:\nhttps://github.com/RossMinor/Accessible-Flashcards\nor follow me on Twitter:\n@Ross_Minor")	

while True: #stop forgetting that true is caps
	UserInput = input("What would you like to do?\n1 = Create new set\n2 = Study set\n3 = Add cards to a set\n4 = Search a set\n0 = exit")
	if UserInput == "1":
		print("Type \"Done\" at any point to finish.")
		#Asks for card front and back. Card front and back are then added to the card dictionary. Typing done breaks the loop.
		while True:
			
			UserInputFront = input("Enter card front")
			if UserInputFront == "done":
				break
			if UserInputFront == "":
				print("Please enter a value")
				continue
			UserInputBack = input("Enter card back")
			if UserInputBack == "done":
				break
			if UserInputBack == "":
				print("Please enter  a value")
				continue
			Card.update({UserInputFront: UserInputBack})

		#Asks the user to name their set and creates a json file with the specified name. Dumps the card dictionary into the json file.
		while True:
			UserInput = input("Please type where you would like to save your set." + "\n if you would like to use the directory you have been working in, simply type the name of your set.")
			if UserInput == "":
				print("Please enter a value")
				continue
			elif "\\" in UserInput:
				File = open(UserInput+".json", "w")
				json.dump(Card,File)
				File.close()
				break
			else:
				File = open(LastDirUsed["RecentDirPath"] + "\\" + UserInput + ".json", "w")
				json.dump(Card,File)
				File.close()
				break
		print("Set saved!")

	if UserInput == "2":
		Returns = DirIndexLoad(); InputDict = Returns[0].copy(); CurrentSet = Returns[1]; DirPath = Returns[2]
		WorkingDict = InputDict.copy() #Copies the dictionary
		
		TempList = list(WorkingDict.keys()) #Creates a list out of the dictionary so it can be iterated through.
		input("Your set will be shuffled.\nPress enter to flip each card.\nYou may type done at any time to end your study session.\nTo edit a card, simply type edit on the side of the card you would like to edit. The text will be copied to your clipboard, where you can make any changes and paste it back into the console.")
		#Loops through the list and randomly grabs a value from the json file dictionary. Then prints the front and back of the card.
		for key in TempList:
			RandomKey = random.choice(list(WorkingDict.keys())) #Chooses a random key out of the original dictionary and converts it to a list.
			print("\n".join(textwrap.wrap(RandomKey, 80)))
			UserInput = input()
			if UserInput == "Done":
				break
			elif UserInput == "delete":
				InputDict.pop(RandomKey)
				WorkingDict.pop(RandomKey)
				File = open(DirPath + "\\" + CurrentSet + ".json", "w")
				json.dump(InputDict,File)
				File.close()
				continue
			elif UserInput == "edit":
				Pc.copy(RandomKey) #Copies the front of the card to the clipboard so it can be pasted and edited in the console.
				UserInput = input("Editing. ")
				InputDict.update({UserInput: InputDict[RandomKey]}) 
				InputDict.pop(RandomKey)
				WorkingDict.pop(RandomKey)
				
				#Saves the new dictionary in the same JSON file.
				File = open(DirPath + "\\" + CurrentSet + ".json", "w")
				json.dump(InputDict,File)
				File.close()
				continue
			
			print("\n".join(textwrap.wrap(InputDict[RandomKey], 80)))
			UserInput = input()
			if UserInput == "done":
				break
			elif UserInput == "delete":
				InputDict.pop(RandomKey)
				WorkingDict.pop(RandomKey)
				File = open(DirPath + "\\" + CurrentSet, "w")
				json.dump(InputDict,File)
				File.close()
				continue
			elif UserInput == "edit":
				Pc.copy(InputDict[RandomKey]) #Copies the back of the card to the clipboard so it can be pasted and edited in the console.
				UserInput = input("Editing")
				InputDict.update({RandomKey: UserInput}) #Adds the unchanged dictionary key and its new dictionary value to the InputDict dictionary.
				WorkingDict.pop(RandomKey)

				#Saves the JSON file.
				File = open(DirPath + "\\" + CurrentSet, "w")
				json.dump(InputDict,File)
				File.close()
				continue #Restarts the loop so the updated dictionary (InputDict) can be used.
			
			WorkingDict.pop(RandomKey) #Deletes the original dictionary item so it isn't pulled again.
		
		
	if UserInput == "3":
		Returns = DirIndexLoad(); InputDict = Returns[0].copy(); CurrentSet = Returns[1]; DirPath = Returns[2]
		input("Adding cards to " + CurrentSet + ".")

		while True:
			UserInputFront = input("Enter card front")
			if UserInputFront == "done":
				break
			if UserInputFront == "":
				print("Please enter a value")
				continue
			UserInputBack = input("Enter card back")
			if UserInputBack == "done":
				break
			if UserInputBack == "":
				print("Please enter  a value")
				continue
			InputDict[UserInputFront] = UserInputBack

		File = open(DirPath + "\\" + CurrentSet, "w")
		json.dump(InputDict,File)
		File.close()
		print("cards saved.")
	
	
	if UserInput == "4":
		Returns = DirIndexLoad(); InputDict = Returns[0].copy(); CurrentSet = Returns[1]; DirPath = Returns[2]		
		UserInput = input("Type the text you would like to search for.")
		
		
		SearchResults = {}
		for x in InputDict:
			if UserInput in x:
				SearchResults[x] = InputDict[x]
			if UserInput in InputDict[x]:
				SearchResults[x] = InputDict[x]
		if SearchResults:		
			print("Search results:")
		else:
			print("Sorry, nothing was found. Make sure your spelling is correct, otherwise try to simplify your search.")
		Count = 0
		for x in SearchResults:
			Count += 1
			print(str(Count) + ". " + x + ":\n   " + SearchResults[x])
		input()
	
	
	if UserInput == "0":
		break #Breaks the main loop
