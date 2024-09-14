def determine_location(x, y):
    if x == 0 and y == 0:
        return "merupakan titik 0"
    elif x == 0:
        return f"({x}, {y}) berada di sumbu-y."
    elif y == 0:
        return f"({x}, {y}) berada di sumbu-x."
    elif x > 0 and y > 0:
        return f"({x}, {y}) berada di quadran I."
    elif x < 0 and y > 0:
        return f"({x}, {y}) berada di quadran II."
    elif x < 0 and y < 0:
        return f"({x}, {y}) berada di quadran III."
    elif x > 0 and y < 0:
        return f"({x}, {y}) berada di quadran IV."

# Example usage
x = float(input("masukkan koordinat x: "))
y = float(input("masukkan koordinat y: "))
location = determine_location(x, y)
print(location)
