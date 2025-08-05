from gtts import gTTS
import os
s=input("enter your text:")
c=gTTS(s)
c.save("test_audio.mp3")
os.system("start text_audio.mp3")
