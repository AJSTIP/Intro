cities = {'NYC': 5000000, 'LA': 4000000, 
          'Chicago': 2700000, 'Houston': 2300000,
          'Phoenix': 1700000, 'Philadelphia': 1600000,}
print(f"The Cities Are -- {cities}")

largest = {k:v for k, v in cities.items() if v > 2000000}
print(f"The Largest Cities Are -- {largest}")

smallest = {k:v for k, v in cities.items() if v < 2000000}
print(f"The Smallest Cities Are -- {smallest}")