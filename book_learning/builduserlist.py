#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman

def create_user_list():
    '''
    Build a custom list of non-negative integers specified by the user
    '''
    u_list = []
    u_input = 0
    while u_input >= 0:
        u_input = int(input("Enter an integer (-1 quits): "))
        if u_input >= 0:
            u_list += [u_input]
    return u_list


# Define a main() 
def main():
    input_list = create_user_list()
    print(input_list)
    n = len(input_list)
    print("Number of entries:", n)
    print("Average: ", float(sum(input_list)/n))
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
