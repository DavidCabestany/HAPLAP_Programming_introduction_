message = "hello world"

print("instead of o, Q")
print(message.replace("o","Q")) # 

print("instead of hello, bye")
print(message.replace("hello","bye")) #

print("previous replacements concatenated")
message = message.replace("hello","bye") #
message = message.replace("o","Q") # 
print(message)