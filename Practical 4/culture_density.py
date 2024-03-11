cell_density = 5 
#starting cell density at 5%
days_passed = 0  
#initialize the number of days
while cell_density <= 90:
    days_passed += 1
    cell_density *= 2
print("The cell density exceeds 90% on day " + str(days_passed) + ".")
