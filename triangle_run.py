
def classify_triangle(side_one, side_two, side_three):
    if side_one > 200 or side_two > 200 or side_three > 200:
        return 'InvalidInput'
    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return 'InvalidInput'
    if not(isinstance(side_one, int) and isinstance(side_two, int) and isinstance(side_three, int)):
        return 'InvalidInput'
    if (side_one >= (side_two + side_three)) or (side_two >= (side_one + side_three)) or (side_three >= (side_one + side_two)):
        return 'NotATriangle'
    if((side_one ** 2) + (side_two ** 2) == (side_three ** 2)) or ((side_two ** 2) + (side_three ** 2) == (side_one ** 2)) or ((side_one ** 2) + (side_three ** 2) == (side_two ** 2)):
        return 'Right'
    elif side_one == side_two and side_two == side_three and side_one == side_three:
        return 'Equilateral'
    elif side_one != side_two and side_two != side_three and side_one != side_three:
        return 'Scalene'
    else:
        return 'Isoceles'