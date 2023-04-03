side_a = 20

side_b = 15

def calculate_hypotenuse():
    hypotenuse = ((side_a ** 2) + (side_b ** 2)) ** (1/2)
    print("The hypotenuse of a right-angled triangle is " + str(hypotenuse)
          + " if one of the two sides is " + str(side_a) + " and the other side is "
          + str(side_b))

calculate_hypotenuse()