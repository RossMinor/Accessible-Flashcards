import json
import random
import pyperclip as Pc
import textwrap

Card = {}
File = ""
CurrentSet = ""

def editCard(back):
	if back == False:
		back = ""
	if back == True:
		back = ""
	
	

print("Welcome to Accessible Flashcards.\nTo stay up to date on updates and bug fixes, be sure to check the Github repo at:\nhttps://github.com/RossMinor/Accessible-Flashcards or follow me on Twitter:\n@Ross_Minor.")

while True: #stop forgetting that true is caps
	UserInput = input("What would you like to do?\n1 = Create new set\n2 = Study set\n3 = Add cards to a set\n0 = exit")
	if UserInput == "1":
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
			UserInput = input("Please name your set")
			if UserInput == "":
				print("Please enter a value")
				continue
			else:
				File = open(UserInput+".json", "w")
				json.dump(Card,File)
				File.close()
				break


	if UserInput == "2":
		#Asks the user for a json file name and loads the json file. The set is shuffled and then iterated through, first front and then back of card. 
		while True:
			UserInput = input("Please enter the path to a JSON set.")
			CurrentSet = UserInput
			if UserInput == "":
				print("Please enter a value")
				continue

			#If the file can not be found, print the error message.
			try:
				File = open(UserInput+".json", "r")
				InputDict = json.load(File) #Loads the json file into a dictionary
				File.close()
			except:
				print("Sorry, that file does not exist")
				continue
			else:
				break

		WorkingDict = InputDict.copy()
		
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
				File = open(CurrentSet+".json", "w")
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
				File = open(CurrentSet+".json", "w")
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
				File = open(CurrentSet+".json", "w")
				json.dump(InputDict,File)
				File.close()
				continue
			elif UserInput == "edit":
				Pc.copy(InputDict[RandomKey]) #Copies the back of the card to the clipboard so it can be pasted and edited in the console.
				UserInput = input("Editing")
				InputDict.update({RandomKey: UserInput}) #Adds the unchanged dictionary key and its new dictionary value to the InputDict dictionary.
				WorkingDict.pop(RandomKey)

				#Saves the JSON file.
				File = open(CurrentSet+".json", "w")
				json.dump(InputDict,File)
				File.close()
				continue #Restarts the loop so the updated dictionary (InputDict) can be used.
			
			WorkingDict.pop(RandomKey) #Deletes the original dictionary item so it isn't pulled again.
		
		
	if UserInput == "3":
		while True:
			UserInput = input("Please put the set you would like to open in the directory of this program, then type the file name")
			CurrentSet = UserInput
			if UserInput == "":
				print("Please enter a value")
				continue

			#If the file can not be found, print the error message.
			try:
				File = open(UserInput+".json", "r")
				InputDict = json.load(File) #Loads the json file into a dictionary
				File.close()
			except:
				print("Sorry, that file does not exist")
				continue
			else:
				break
	
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

		File = open(CurrentSet+".json", "w")
		json.dump(InputDict,File)
		File.close()
		print("cards saved.")
	
	
	if UserInput == "4":
		while True:
			UserInput = input("Please enter the path to a JSON set.")
			CurrentSet = UserInput
			if UserInput == "":
				print("Please enter a value")
				continue

		#If the file can not be found, print the error message.
			try:
				File = open(UserInput+".json", "r")
				InputDict = json.load(File) #Loads the json file into a dictionary
				File.close()
			except:
				print("Sorry, that file does not exist")
				continue
			else:
				break

		UserInput = input("Type the text you would like to search for.")
		
		#for key, value in InputDict.items:
			#print("balls")
			
			
	if UserInput == "0":
		break #Breaks the main loop