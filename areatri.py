side1 = float(input("Enter length of first side:"))
side2 = float(input("Enter length of second side:"))
side3 = float(input("Enter length of third side:"))

print("calculating...")
sp = (side1 + side2 + side3) / 2
area = (sp * (sp-side1) * sp * (sp-side2) * (sp-side3))
print("Area is.. %f", area)
