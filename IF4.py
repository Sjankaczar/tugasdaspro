def get_cylinder_contents(color):
    first_letter = color[0].lower()
    if first_letter == 'o':
        return "ammonia"
    elif first_letter == 'b':
        return "carbon monoxide"
    elif first_letter == 'y':
        return "hydrogen"
    elif first_letter == 'g':
        return "oxygen"
    else:
        return "Contents unknown"

# Example usage
color = input("Enter the color of the cylinder: ")
contents = get_cylinder_contents(color)
print(contents)
