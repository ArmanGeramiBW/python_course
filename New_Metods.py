#copy = yek matn ra copy mikonad ba tamami gosiatash
Books = ['Asimof_in_first', 'metro2033', 'evil_son', 'my_war']
a = Books.copy()
print(a)
#insert = be oon yek shomare midahim va str ya inty ke moshakhas kardim jaigozin mishan
Books.insert(0, "Golestan")
print(Books)
#index = baraye ma on chizi ke behesh dadim ra peyda mikonad va tabaghesh ra migooiad
z = Books.index("metro2033")
print(z)
#extend = 2 list ra ba ham makhloot mikonad
Food = ['Pizza', 'Pasta', 'Ghormesabzi']
Books.extend(Food)
print(Books)