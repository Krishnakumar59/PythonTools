# Import the gTTS module for text to speech conversion  
from gtts import gTTS  
import os
# This module is imported so that we can  
# play the converted audio  
from playsound import playsound  
# It is a text value that we want to convert to audio  
text_val = "Google is a tech giant, known for its search engine and digital services. It revolutionized online search, advertising, and cloud computing. With its vast reach, Google impacts information access, online advertising, and data privacy. It offers popular products like Gmail, Google Maps, and YouTube. Google's innovations include self-driving cars, AI advancements, and projects like Google Glass. While it dominates the internet, controversies arise regarding privacy concerns and monopolistic practices. Google continues to shape our digital landscape, connecting people worldwide, and striving to enhance our online experiences through technology and innovation."
# Here are converting in English Language  
language = 'en-in'  
# All Language Suppport
# {'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'en-us': 'English (US)','gu': 'Gujarati', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'en-ca': 'English (Canada)', 'jw': 'Javanese', 'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mr', 'en-in': 'English (India)'}
# Passing the text and language to the engine,  
# here we have assign slow=False. Which denotes  
# the module that the transformed audio should  
# have a high speed  
obj = gTTS(text=text_val, lang=language, slow=False)  
#Here we are saving the transformed audio in a mp3 file named audio.mp3
obj.save("audio.mp3")  
# Play the exam.mp3 file  
playsound("audio.mp3")  
# Remove the temporary audio file
os.remove("audio.mp3")
