my_sentence="python is fun and powerful"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[10:23])
print(my_sentence.lower())
print(my_sentence.count("o"))
print(my_sentence.find("fun"))
new_sentence=my_sentence.replace("powerful", "amazing")
print(new_sentence)
new_message="learning python is exciting"
message= my_sentence + " "  + new_message
print(message)
message_format="{} {}".format(my_sentence, new_message)
print(message_format)
message_fstring=f"{my_sentence} {new_message}"
print(message_fstring)
print(dir(my_sentence))
print(help(str.replace))







