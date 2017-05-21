# trip fuel calculator

vehicle_avg = 15
fuel_cost = 65
trip_kms = 700

total_cost = (trip_kms / vehicle_avg) * fuel_cost
total_cost_2 = (trip_kms / vehicle_avg+2) * fuel_cost

print("Total cost: %0.2f" % (total_cost))
print("You could save: %0.2f (i.e. %0.2f%%) if the avg is increased by 2" % (total_cost_2 - total_cost))
