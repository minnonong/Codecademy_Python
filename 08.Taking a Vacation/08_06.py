#  08_06 Hey, You Never Know!

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

def rental_car_cost(days):
    cost = 40
    if(days >= 3 and days < 7):
        result = (days * cost) - 20
        return result
    elif(days >= 7):
        result = (days * cost) - 50
        return result
    else:
        result = (days * cost)
        return result

def trip_cost(city, days, spending_money):
    total = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return total
