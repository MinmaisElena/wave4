def reverseLookup():
    userval = str(input("Enter a key : "))
    dictionary = {
        "python": "language",
        "dictionary" : "book",
        "computer" : "device",
        "school" : "St.Robert",
        "Year" : "2020",
        "Month" : "May"
    }
    if userval in dictionary:
        pt = dictionary.get(userval)
        print(pt)
    else:
        print("No keywords found in the dictionary")
reverseLookup()