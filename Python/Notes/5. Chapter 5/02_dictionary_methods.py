myDict = {
    "fast": "In a Quick Manner",
    "Miskatur": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Miskatur': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Miskatur": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Miskatur")) # Prints value associated with key "Miskatur"
print(myDict["Miskatur"]) # Prints value associated with key "Miskatur"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("Miskatur2")) # Returns None as Miskatur2 is not present in the dictionary
print(myDict["Miskatur2"]) # throws an error as Miskatur2 is not present in the dictionary