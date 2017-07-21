#  07_17 Review:Functions

def shut_down(s):
    ch = s.lower()
    if (ch == "yes"):
        return "Shutting down..."
    elif (ch == "no"):
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."
