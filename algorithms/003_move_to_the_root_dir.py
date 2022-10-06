def minimumSteps(loggedMoves):
    # Write your code here
    parent_folder = "../"
    same_folder = "./"
    child_folder = "[a-zA-Z]//"
    counter = 0
    for s in loggedMoves:
        if s == parent_folder:
            counter -= 1
        elif s == same_folder:
            counter + 0
        else:
            counter += 1
    return counter
