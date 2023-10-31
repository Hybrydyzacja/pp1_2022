
ICAO = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "X-ray",
    "y": "Yankee",
    "z": "Zulu"
}

# dict_str = str(ICAO)
# print(dict_str)
# print(type(dict_str))

with open("ICAO.txt", "w", encoding="utf-8") as file:
    for value, key in ICAO.items():
        x = value.upper(), key
        str = " ".join(x)
        print(str)
        file.write(str)
        file.write("\n")
    
