roseColor = input("Enter a color for a Rose: ")
blueColor = input("Input any Object with blue color: ")
fruit = input("Enter any Fruit you can think of: ")

# Python 3
# output = f"""
# Roses are {roseColor},
# {blueColor} are blue,
# {fruit} is sweet,
# And so are you."""

# For compatibility issues with Python 2
output = "Roses are "+roseColor+",\n"+blueColor + \
    " are blue,\n"+fruit+" is sweet,\nAnd so are you."

print(output)
