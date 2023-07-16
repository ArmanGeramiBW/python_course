#add = add something to our set
SET1 = {"Blue , Black , White"}
SET1.add("Pink")
print(SET1)

#Remove = REmove something from our set
SET2 = {"Blue" , "orange" , "White"}
SET2.remove("Blue")
print(SET2)

#copy = Copy something from our set.
SET3 = {"Blue", "Black", "White"}
a = SET3.copy()
print(a)

#clear = Remove all things in a set

SET4 = {"Blue", "Black", "White"}
SET4.clear()
print(SET4)

#discard = Remove something that we want to remove it
SET5= {"Blue", "Black", "White"}
SET5.discard("Black")
print(SET5)

#update = 
SET6 = {"Blue", "Black", "White"}
tropical = {"Pink" , "Green" , "Gray"}
SET6.update(tropical)
print(SET6)