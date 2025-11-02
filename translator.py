from deep_translator import GoogleTranslator

text = "我的名字是穆罕默德·纳维德·贾特"  //Chinise Language 
translated = GoogleTranslator(source='auto', target='en').translate(text)

print(translated)
