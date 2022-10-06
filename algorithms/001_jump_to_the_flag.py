""""

"""


def jumps(flagHeight, bigJump):
    # Write your code here
    jumps = flagHeight // bigJump
    jumps += flagHeight % bigJump
    return jumps
