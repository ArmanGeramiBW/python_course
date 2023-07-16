# copy 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
x = Book.copy()
print(x)

# clear 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
Book.clear()
print(Book)

# update 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
Book.update({"papers": "seven hundred"})
print(Book)

# keys 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
x = Book.keys()
print(x)

# values 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
x = Book.values()
print(x)

# items 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
x = Book.items()
print(x)

# get 
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
x = Book.get("Model of Book")
print(x)

## pop
Book = {"The writer": "Demitry Glokhofsky", "Model of Book": "Zombies story" , "Birth Year": "2018"}
Book.pop("Model of Book")
print(Book)