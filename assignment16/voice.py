from gtts import gTTS
from playsound import playsound

sen1 = input("Please write your sentence: ")
sen2 = input("Please write your sentence: ")
sen3 = input("Please write your sentence: ")
#Display the longest_sentence 
longest_sen = max([sen1, sen2, sen3], key=len)

name = input("Enter file name: ")

tts = gTTS(longest_sen)
##and now time to Place it
tts.save(f"{name}.mp3")

playsound(f"{name}.mp3")



