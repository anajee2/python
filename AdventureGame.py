def AdventureGame():
    first = input("You are in a creepy house! Would you like to go 'upstairs' or into the 'kitchen'? ")
    if first == "kitchen":
        second = input("There is a long countertop with dirt dishes everywhere. Off to one side there is, as you'd expect, a refrigerator. You may open the refrigerator or look in a cabinet")
        if second == 'refrigerator':
            third = input("Inside the refrigerator you see food and stuff. It looks pretty nasty. Would you like to eat some of the food?('Yes or No')")
            if third == 'yes':
                print("Good Choice, you will survive for another day!")
            if third == 'no':
                print("You die of starvation...eventually!")
        elif fourth == "cabinet":
            fifth = input("Inside the cabinet you find cereal and bowls, do you 'eat' the cereal or keep 'exploring'? ")
            if fifth == 'eat':
                print("That cereal poisoned and killed you, RIP!")
            if fifth == 'exploring':
                print("While exploring you were killed and eaten by a creepy monster")
    if first == 'upstairs':
        seventh = input("Upstairs you see a hallway, At the end of the hallway is the master 'bedroom'. There is also a 'bathroom' off the hallway. Where would you like to go? ")
        if seventh == 'bedroom':
            eighth = input("You are in a plush bedroom, with expensive-looking hardwood furniture. The bed is unmade. In the back of the room, the closet door is ajar. Would you like to open the door? ('yes' or 'no') ")
            if eighth == 'yes':
                print("You fell into a deep black hole and can never be found...oof")
            if eighth == 'no':
                print("Well, then I guess you'll never know what was in there. Thanks for playing!")
        elif seventh == 'bathroom':
            ninth = input("The bathroom is old and moldy, however, you find a shiny object hidden inside a swarm of spiders. Do you 'pick' up the shiny object between the swarm of spiders or 'leave' the bathroom? ")
            if ninth == 'pick':
                print("Congrats, the shiny object was a rare diamond, You are now a millionaire!!")
            if ninth == 'leave':
                print("You have lucked out of becoming a millionaire, sad, but thanks for playing the game!")

AdventureGame()
        
            
            
        
            
        
