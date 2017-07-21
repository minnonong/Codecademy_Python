#  08_03 Getting There

def hotel_cost(nights):
    result = nights * 140
    return result

def plane_ride_cost(city):
    if(city == "Charlotte"):
        return 183
    elif(city == "Tampa"):
        return 220
    elif(city == "Pittsburgh"):
        return 222
    elif(city == "Los Angeles"):
        return 475
