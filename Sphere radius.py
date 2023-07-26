# Denzel Coleman COP1000
# Program5_2.py
# Collaborators: None
# Create a program that takes the radius of a sphere as an argument.
# One function returns the surface area of the sphere, while the other
# print the volume.
# Utilize the math module to get the value of pi.

import math

def main():

    # Get the user to input the radius of a sphere
    radius = float(input('Enter the radius of a sphere '))

    # Get the surface area from the surface_area function
    total_surface = surface_area(radius)

    # Get the surface area from the volume function
    total_volume = volume(radius)

    # Display the surface area
    print(f'The surface area of a sphere with radius {radius} is {total_surface:.4f}')

    # Display the Volume
    print(f'The volume is {total_volume:.3f}')


# The surface_area function accepts the numeric argument and
# returns the calculation of the surface area of a sphere
# using the radius that was inputted by the user.
def surface_area(s):
    
    
    radius = s
    # Calculate the surface area of a sphere
    result = 4 * math.pi * radius ** 2
    return result


# The volume function accepts the numeric argument and
# returns the calculation of the volume of a sphere
# using the radius that was inputted by the user.
def volume(v):
    
    radius = v
    # Calculate the volume of a sphere
    result = (4.0/3.0) * math.pi * (radius ** 3)
    return result

# Call the main function
main()
