"""
CP1404 Practical
Hex colours
"""
colour_to_code = {"acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "amaranth": "	#e52b50", "apricot": "#fbceb1",
                  "black": "#000000", "blue1": "#0000ff", "brass": "#b5a642", "corn": "#fbec5d",
                  "gold1": "#ffd700", "white": "#ffffff"}

print("Colours to pick from.")
for colour in colour_to_code.keys():
    print(colour.title(), end=", ")
print("")

choice = input("Colour: ").lower()
while choice != "":
    try:
        print(colour_to_code[choice])
    except KeyError:
        print("Invalid")
    choice = input("Colour: ").lower()

print("Farewell")
