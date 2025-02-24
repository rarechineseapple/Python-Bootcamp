#hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() is False:
    if is_facing_north():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_left()
        

#hurdle 2