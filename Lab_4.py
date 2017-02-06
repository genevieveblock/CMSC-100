import random



#printing directions
def main():

    print("Ahoy Captain! You and your crew have just stolen a ship and are now racing to cross the pacific ocean and out-sail the authorities.")
    print("You must choose to either manually row, use the sail, let the crew rest, patch up the boat, and/or abandon ship.")

    done = False
    miles_traveled = 125
    crew_tiredness = 1
    authorities_distance = -10
    ship = 5

    print(" ")
#printing choices 
    while done == False:
        print(" A. Manually row")
        print(" B. Use the sail")
        print(" C. Let the crew rest")
        print(" D. Patch up the ship")
        print(" E. Status Check")
        print(" Q. Quit")


        print(" ")

        user_input = input("What is your choice? ")
        if user_input.upper() == " ":
            done = True

    #Q
        elif user_input.upper() == "Q":
            print("Thankyou for playing")
            done = True

        elif user_input.upper() == "E":
            print("Status Check")
            print("Miles Traveled: ", miles_traveled)
            print("Ship Status: ", ship)
            if ship > 5:
                print("NEEDS REPAIRS")
            print("Crew Status: ", crew_tiredness)
            if crew_tiredness > 5:
                print("CREW NEEDS REST")
            print("Authorities Distance: ", authorities_distance)
    #D
        elif user_input.upper() == "D":
            print("You have patched up the ship")
            print("Authorities Distance: ", miles_traveled - authorities_distance)
            ship = ship * 0
            if ship < 0:
                print("Sadly, you and your crew died in a sinking the sinking ship. Game Over")
                done = True


    #C
        elif user_input.upper() == "C":
            print("The crew is well rested")
            print("Authrorities Distance: ", miles_traveled - authorities_distance)
            crew_tiredness = crew_tiredness * 0
            if crew_tiredness < -1:
                print("Sadly, you and your crew died from overexertion. Game Over")
                done = True


   #B
        elif user_input.upper() == "B":

            ship += random.randrange(1, 4)
            crew_tiredness = crew_tiredness + random.randrange(1,5)
            authorities_distance = authorities_distance + random.randrange(80,100)
            print("Miles Traveled: ", miles_traveled)
            miles_traveled += random.randrange(100,200)
            if random.randrange(1,20) == 1:
                print("You have found a pod of Mermaids that fixed your ship!")
                ship = ship * 0
                crew_tiredness = crew_tiredness * 0


    #A
        elif user_input.upper() == "A":

            ship += random.randrange(1,4)
            crew_tiredness = crew_tiredness + random.randrange(1,4)
            authorities_distance = authorities_distance + random.randrange(100,150)
            print("Miles Traveled: ", miles_traveled)
            miles_traveled += random.randrange(200, 300)
            if random.randrange(1,100) == 1:
                print("You have found a pod of Mermaids that fixed your ship!")
                ship = ship * 0
                crew_tiredness = crew_tiredness * 0

        if crew_tiredness > 10:
            print("Your crew is tired.")
        elif crew_tiredness > 20:
            print("Sadly you and your crew have died from overexertion. Game Over")
            done = True
        if ship > 10:
            print("Your ship needs repairs")
        if ship > 15:
            print("Sadly, you and your crew died in a sinking ship. Game Over")
            done = True
        elif miles_traveled - authorities_distance < 5:
            print("Oh no! The authorities are close!")
        elif miles_traveled - authorities_distance == 0:
            print("You and your crew were caught by the authorities. Game Over")
            done = True

        elif miles_traveled > 1000:
            print("Arr Matey You've won!")
            done = True

main()

