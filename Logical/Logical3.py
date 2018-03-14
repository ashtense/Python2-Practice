print "You enter a dark room with two doors. Do you choose #1 or #2?"

door_selected = int(raw_input("> "))


if door_selected == 1:
    print "There's a giant bear here. What do you do now?"
    print "1.) Do you take scream?"
    print "2.) Do you go back the door?"

    bear_option = int(raw_input("> "))
    if bear_option == 1:
        print "Bear now notices you. Go back."
    elif bear_option == 2:
        print "Smart option to select. Take care."

elif door_selected == 2:
    print "There's a witch in this room. Do you want to play with her?"
    print "1.) To play with the witch"
    print "2.) Do you go back the door?"

    witch_option = int(raw_input("> "))

    if witch_option == 1:
        print "Witch will trick you and take your soul. Good luck"
    elif witch_option == 2:
        print "Smart option to select. Take care" 

else:
    print "Are you nuts? I just told you there are only two doors."
