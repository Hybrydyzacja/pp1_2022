
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

entered_text = input("Enter_text:")

i = 0
for key, value in ICAO.items():
    while i < len(entered_text):
        print(ICAO[entered_text[i]], end=" ")
        i += 1 