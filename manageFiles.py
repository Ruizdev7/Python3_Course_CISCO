'''
from io import open

file_text = open("file.txt", "w")

frase = "Estupendo dia para estudiar python \n el domingo"

file_text.write(frase)

file_text.close()'''

'''from io import open

file_text = open("file.txt", "r")

text = file_text.read()

file_text.close()

print(text)
'''
'''
from io import open

file_text = open("file.txt", "r")

lines = file_text.readlines()

file_text.close()

print(lines)
'''

from io import open

file_text = open("file.txt", "rt")

#file_text.write("\n siempre es bueno aprender algo nuevo de python \n")




