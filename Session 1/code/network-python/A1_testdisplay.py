
import time
import display

def main(): # called at the end of the file

    # Creates some stuff to display
    d = display.Display()

    # Put value 2 in second column
    d.add_value(10, 2)
    # Performs the sum and display line
    d.render()

    # Wait 2 seconds
    time.sleep(2)


    # Add the value 4 starting from the 6th column
    i = 6
    d.add_value(i, 4)
    d.render()

    time.sleep(1)
    # Begin iterations

    # Run this a 99 times
    for iteration in range(1, 100):
        # From the ith position, move 1 position the 4 to the right and it has to remain 6 in the sum, so if you put another number, you will only leave behind a number such that the sum is 6
        # It renders the same line
        d.move_value_right(i, 1, 4)
        i += 1
        d.render()
        time.sleep(0.010)

    print()
    d.add_value(5, 1)
    # Delete the zeros
    d.render_clean()
    d.render()
    d.render_clean()
    d.render()



if __name__== "__main__":
  main()
