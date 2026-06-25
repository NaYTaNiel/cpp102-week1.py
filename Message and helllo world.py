import sys
import time

def slow_type(text, delay=0.10):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Adds a newline at the end


slow_type("hello world how are you doing today")
slow_type("what Meals did you eat this afternoon?")
slow_type("is there any problem in your rotation")
slow_type("in what way can YOU bring someone back at a time where time and space don't exist?")
slow_type("drifting in a void where you can not see anything how scary it is? can sojmeone hold on that type of lonelinesss, alone drifting in the void alone")
slow_type("don't forget that i still hvae say something to you plss don't lose hope on your way back to solaris 3.")
slow_type("from -Rover(NaYTaNiel)im still will be waiting even if the world ends.................")
