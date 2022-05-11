# checks input is a number more than a given value 
def num_check(question, low):
    valid = False
    while not valid:
        error = "Please enter an integer that is more than (or equal to {}) ".format(low)
        
        try:    
            
            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response  

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)



# finds # of bits for 24 bit colour

    print()
    # get image height
    image_height = input("Enter Image Height: ")
    
    # get image width
    image_width = input("Enter image width: ")

    # Output answer with working
    print()
    