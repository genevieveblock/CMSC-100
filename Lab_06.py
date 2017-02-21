
room_list=[]

room=[0,1,2,3,4]

room[0]= "Grand Staircase"
room[1]= "Rose's Cabin"
room[2]= "First-Class Lounge"
room[3]= "Dining Saloon"
room[4]= "Promenade Deck"

room=["Hello Rose, the Titanic is currently sinking." \
      "You are curently in located in the Grand Staircase of the Titanic, you can go to the passage N or E",1,None,3,None,None,None]

room_list.append(room)

room=["You are in Your cabin, The ship is sinking and you must get to higher floor. There is a passage N, E, and W.",2,None,4,None,None]

room_list.append(room)

room=["You are now in the Fisrt Class lounge. Hurry! get to higher floors, the water is rising! There is a passage N and W.",None,None,5,None]

room_list.append(room)

room=["You have reached the Dining Saloon, The water is still rising! There is a passage S and E.",4,None,None]

room_list.append(room)

room=["You are in north hall you must find your way out quick before the mad man catches you. There is a passage S, W, and E",5,None]

room_list.append(room)

room=["You have reached the Promenade Deck. There is a passage N, W, and S",6]

room_list.append(room)

room=["You are on the Grand Balcony, the highest floor on the Titanic. There is a passage S."]

room_list.append(room)

current_room = 0


done = False
while not done:
    print("")
    print(room_list[0])
    print("")
    user_choice = input("Which path do you want to take?  ")

    if user_choice.upper() == "N" or user_choice.upper() == "NORTH":
        next_room = room_list[1]
        print(next_room)
        if next_room == None:
            print("You have come across a locked room, choose another path.")
        else:
            current_room = next_room

    elif user_choice.upper() == "E" or user_choice.upper() == "EAST":
        next_room = room_list[3]
        print(next_room)
        if next_room == None:
            print("You have come across a locked room, choose another path.")
        else:
            current_room = next_room

    elif user_choice.upper() == "S" or user_choice.upper() == "SOUTH":
        next_room = room_list[2]
        print(next_room)
        if next_room == None:
            print("You have come across a locked room, choose another path.")
        else:
            current_room = next_room


    elif user_choice.upper() == "W" or user_choice.upper() == "WEST":
        next_room = room_list[current_room][4]
        print(next_room)
        if next_room == None:
            print("You have come across a locked room, choose another path.")
        else:
            current_room = next_room

    elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
        done = True
        print("")
        print("You have quit the stage")





