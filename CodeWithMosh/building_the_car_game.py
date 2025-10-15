# User types "help" to see a list of commands
# If user types an unknown command, print "I don't understand that..."
# User types "quit" to exit the game
# User types "start" to start the car
# Print "Car started...Ready to go!"
# User types "stop" to stop the car
# Print "Car stopped.".."
# If user types "start" when the car is already started, print "Car is already started!"
# If user types "stop" when the car is already stopped, print "Car is already stopped!"

command = ""
started = False
stopped = True

while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            stopped = False
            print("Car started...Ready to go!")
    elif command == "stop":
        if stopped:
            print("Car is already stopped!")
        else:
            stopped = True
            started = False
            print("Car stopped.")
    elif command == "quit":
        print("Exiting the game...")
    else:
        print("I don't understand that...")
# The game continues until the user types "quit"
