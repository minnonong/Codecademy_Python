#  07_19 Review:Built-In Functions

def distance_from_zero(val):
    val_type = type(val)
    if(val_type == int or val_type == float):
        return abs(val)
    else:
        return 'Not an integer or float!'
