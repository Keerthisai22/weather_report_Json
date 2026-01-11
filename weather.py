import json
with open("weather.json","r") as file:
    data=json.load(file)
    city=input("\nEnter the city=").lower()
    if city in data:
        print("Weather Report")
        print("city:",city.capitalize())
        print("Temperature:",data[city]["temp"],"°c")
        print("Condition:",data[city]["condition"])
    else:
        print("city not found")