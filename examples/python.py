# Python Dictionary

body = {"user_id": "jbush", "text": "mesa 2"}
print(body["user_id"])
print(body["text"])

# split and len()

x = "mesa 2"

print(x.split(" "))
print(len(x.split(" ")))

# Python Arrays
y = ['mesa', '2']
print(y[0])
print(y[1])

z = ['tent', 'sleeping bag']
z.append('flashlight')
print(z)

# Check if a string contains an integer

"1".isdigit()
"a".isdigit()

# Casting: turn a string into an integer

"1" == 1
int("1") == 1

# Classes

class City:
    def __init__(self, key, name, state, country, latitude, longitude):
        self.key = key
        self.name = name
        self.state = state
        self.country = country
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f"{self.name}, {self.state} {self.country}"

    def __repr__(self):
        return f"{self.name}, {self.state} {self.country}"

city = City('X100', 'Mesa', 'AZ', 'US', '111.8315', '33.4152')
print(city.key)
print(city.name)
print(city)