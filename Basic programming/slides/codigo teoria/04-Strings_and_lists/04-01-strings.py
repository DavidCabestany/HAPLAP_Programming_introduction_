text = "Kaixo"
print("Text:",text)
print("Size of text:",len(text)) #

print("k character in text? ", "k" in text) # 
print("x character in text? ", "x" in text) # 

print("za srting in text?", "za" in text) # 
print("Ka string in text?", "Ka" in text) # 

print("Negations")
print("za string not in text?", "za" not in text) #
print("aixo string not in text?", "aixo" not in text) #

print("Case is important!!")
print("ka string in text?", "ka" in text) #

print("Kai at the beginning?", text.startswith("Kai")) #
print("xo at the end?", text.endswith("xo")) #