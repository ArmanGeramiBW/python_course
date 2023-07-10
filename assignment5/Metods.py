#istitle = barresi shorooe shodan kalamat ba horoof bozorg
Text = "Hello My Name Is Arman"
N = Text.istitle()
print(N)
#title = tamam horoof shorooe shode kalamat ro bozorg mikonad
Text2 = "hello my name is arman"
Z = Text2.title()
print(Z)
#find = har chizi ke be An bedahim peyda mikonad
Text3 = "My favoarite lessons are about physics and math and biology and a little history"
print(Text3.find("lessons"))
#replace = kalame mored nazar ra avaz mikonad
Text4 = "The hardest game for me is cuphead"
X = Text4.replace("cuphead", "Elden ring")
print(X)
#strip = az akhar mitavand ziad konad.
Text5 = "BW    "
B =  Text5.strip()
print(B , "is my best hero.")
#lstrip = az aval mitavand ziad konad.
Text6 = " Water"
C = Text6.lstrip()
print("Drink" , C)
#rjust = mitavanim be tedad addi ke be an midahim jabejash konim
Text7 = "Golestan"
S = Text7.rjust(30)
print(S, "is a favoarite book from Saedi.")
#zfill = brayeman aval kar sefr migozarad
Text8 = "1234.256458245"
L = Text8.zfill(22)
print(L)
