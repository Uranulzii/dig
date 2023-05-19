words="The rain in Spain falls mainly on the plain"
print(words.upper())
print(len(words))
print(words.lower())
print(words[0:18])
first=words[0:18]
later=words[18:44]
print(first + later.upper())
rain=words[4:8]
plain=words[38:44]
print("The "+(rain.upper() +" ")*3 +"on the " + (plain.upper()+" ")*2 +plain.upper())