travel_cost = float(input("Enter travel cost (flight/train): "))
hotel_per_day = float(input("Enter hotel cost per day: "))
food_per_day = float(input("Enter food cost per day: "))
local_travel_per_day = float(input("Enter local travel cost per day: "))
days = int(input("Enter number of days: "))

def trip_cost_cal(travel_cost, hotel_per_day, food_per_day, local_travel_per_day, days):
 hotel_total = hotel_per_day * days
 food_total = food_per_day * days
 local_travel_total = local_travel_per_day * days
 total_cost = travel_cost + hotel_total + food_total + local_travel_total
 return total_cost
 
hotel_total = hotel_per_day * days
food_total = food_per_day * days
local_travel_total = local_travel_per_day * days
total_cost = travel_cost + hotel_total + food_total + local_travel_total
# Example usage of the function
"""trip1 = trip_cost_cal(
    travel_cost=12000,
    hotel_per_day=2000,
    food_per_day=800,
    local_travel_per_day=500,
    days=5
)
trip2 = trip_cost_cal(
    travel_cost=10000,
    hotel_per_day=1800,
    food_per_day=700,
    local_travel_per_day=400,
    days=5
)"""
print(" Trip Cost Summary ")
print("Travel Cost:", travel_cost)
print("Hotel Cost:", hotel_total)
print("Food Cost:", food_total)
print("Local Travel Cost:", local_travel_total)
print("Total Trip Cost:", total_cost)
