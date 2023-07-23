Rhombus = int(input("ٌWrite your number for the diameter: "))

for i in range(Rhombus ):
    print((Rhombus  - i) * " ", end=' ')
    print((i * 2 - 1) * '◊')

for i in range(Rhombus , 0, -1):
    print((Rhombus  - i) * " ", end=' ')
    print((i * 2 - 1) * '◊')