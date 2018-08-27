diction =  {
    "lol": "laugh out loud", 
    "ily": "i love you", 
    "omg": "oh my god",
}

while True:
    abr = input("Your term? ")
    if abr in diction:
        print(abr, "means", diction[abr])
    else:
        yn = input("Not found. Do you want to make a new definition? (Y/N)").upper()
    
        if yn == "Y":
            newvalue = input('Your explanation? ')
            diction[abr] = newvalue
            print("New definition was updated!")
        
        


    
    
    
    
    print()

