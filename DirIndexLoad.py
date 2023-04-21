import json
from os import walk

try:
	File = open("Data.json", "r")
	LastDirUsed = json.load(File) #Loads the json file into a dictionary
	File.close()
except:
	LastDirUsed = {}

Data = {}

def DirIndexLoad():
	Results = []
	CurrentSet = ""
	dirPath = ""
	#input(LastDirUsed)
	
	while True:
		try:
			UserInput = input("Please enter the path to a folder with your JSON sets.\nYour last used folder was located at " + LastDirUsed["RecentDirPath"] + "\nIf you would like to use this folder, press enter")
		except:
			UserInput = input("Please enter the path to a folder with your JSON sets.")
		if UserInput == "":
			DirPath = LastDirUsed["RecentDirPath"]
		else:
			DirPath = UserInput

		#Saving the recently used directory path
		Data["RecentDirPath"] = DirPath
		File = open("Data.json", "w")
		json.dump(Data,File)
		File.close()
				

		for (DirPath, DirNames, FileNames) in walk(DirPath):
			Results.extend(FileNames)
		
		Count = 0
		IndexedResults = {}
		for x in Results:
			Count += 1			
			print(str(Count) + ". " + x + "\n")
			IndexedResults[Count] = x

		UserInput = input("Type the number of the set you would like to load")

		try:
			File = open(DirPath + "\\" + IndexedResults[int(UserInput)], "r")
			InputDict = json.load(File) #Loads the json file into a dictionary
			File.close()
		except:
			print("Sorry, that file does not exist")
			continue
		else:
			break
		
	CurrentSet = IndexedResults[int(UserInput)]
	return (InputDict, CurrentSet, DirPath)

