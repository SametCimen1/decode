import operator
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def getOutput(url):
    output_string = StringIO()
    with open(url, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        return output_string
def setObj(output_string):
    for word in output_string.getvalue():
        if word in list:
            index = list.index(word)
            char = list[index] # a
            obj[char] = obj[char] + 1



list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc =  ["w", "h", "m", "k", "z", "o", "q", "r", "p", "l", "a", "t", "c", "e", "n", "g", "b", "i", "d", "f", "s", "v", "u", "j", "x", "y"]
combined = list + enc
obj = {
 'a': 0, 
 'b': 0, 
 'c': 0, 
 'd': 0, 
 'e': 0, 
 'f': 0, 
 'g': 0,
 'h': 0,
 'i': 0, 
 'j': 0, 
 'k': 0, 
 'l': 0, 
 'm': 0, 
 'n': 0, 
 'o': 0, 
 'p': 0, 
 'q': 0, 
 'r': 0, 
 's': 0,
 't': 0, 
 'u': 0, 
 'v': 0, 
 'w': 0, 
 'x': 0, 
 'y': 0,
 'z': 0,
}

print("getting output 1")
output_string = getOutput("articles/0.pdf")

print("got first article setting obj")
setObj(output_string)
print(obj)


print("getting output 2")
output_string = getOutput("articles/1.pdf")

print("got second article setting obj")
setObj(output_string)




print("getting output 3")
output_string = getOutput("articles/2.pdf")

print("got second article setting obj")
setObj(output_string)




print("getting output 4")
output_string = getOutput("articles/3.pdf")

print("got second article setting obj")
setObj(output_string)



print("getting output 5")
output_string = getOutput("articles/4.pdf")

print("got second article setting obj")
setObj(output_string)



print("getting output 6")
output_string = getOutput("articles/5.pdf")

print("got second article setting obj")
setObj(output_string)



print("sorting outputs")

sortedObj = dict( sorted(obj.items(), key=operator.itemgetter(1),reverse=True))



secret = "i am zodiac today is saturday i went to new york if you dont post this message i will kill people hahahha kill"

def enc(letter):
   secretLetter = ""
   for word in letter:
     if word == ' ':
       secretLetter += " "
     else:
      letterIndex = list.index(word)
      secretIndex = (letterIndex + 26)
      secretLetter += combined[secretIndex]
   return secretLetter
      
secretObj = {
 'a': 0, 
 'b': 0, 
 'c': 0, 
 'd': 0, 
 'e': 0, 
 'f': 0, 
 'g': 0,
 'h': 0,
 'i': 0, 
 'j': 0, 
 'k': 0, 
 'l': 0, 
 'm': 0, 
 'n': 0, 
 'o': 0, 
 'p': 0, 
 'q': 0, 
 'r': 0, 
 's': 0,
 't': 0, 
 'u': 0, 
 'v': 0, 
 'w': 0, 
 'x': 0, 
 'y': 0,
 'z': 0,
}
def getSecretCount(secret):
    for letter in list:
        for secretLetter in secret:
            if letter == secretLetter:
                print("found", letter)
                secretObj[secretLetter] += 1

encSecret = enc(secret);
getSecretCount(encSecret)

sortedSecretObj = dict( sorted(secretObj.items(), key=operator.itemgetter(1),reverse=True))
print(sortedObj)
print(sortedSecretObj)

"""
i am zodiac today is saturday i went to new york if you dont post this message i will kill people hahahha kill
{'e': 84338, 't': 66936, 'a': 53695, 'i': 52907, 'n': 52186, 'o': 51235, 'r': 43971, 's': 41453, 'h': 39072, 'l': 32587, 
'd':  'f': 14907, 'g': 14464, 'w': 13957, 'p': 12699, 'y': 12476, 'b': 10148, 'v': 8150, 'k': 6182, 'x': 1329, 'j': 841, 
'z': 558, 'q': 525}

{'p': 10, 'w': 9, 'n': 8, 'f': 7, 't': 7, 'd': 6, 'z': 6, 'r': 5, 'k': 4, 'x': 4, 'a': 3, 'e': 3, 'g': 3, 'u': 3, 'c': 2,
 'i': 2, 's': 2, 'm': 1, 'o': 1, 'q': 1, 'y': 1, 'b': 0, 'h': 0, 'j': 0, 'l': 0, 'v': 0}

p wc ynkpwm fnkwx pd dwfsikwx p uzef fn ezu xnia po xns knef gndf frpd czddwqz p uptt aptt gzngtz rwrwrrw aptt
e tp nahetv
p = e
w = t
n = a
f = i
y n
d o
z r
r s
k h
x l
a d
e f
g g
u w
c p
i y
s b
m v 
o k
q x
y j
b z
h q
j
l
v

'y': 12476, 'b': 10148, 'v': 8150, 'k': 6182, 'x': 1329, 'j': 841, 
'z': 558, 'q': 525}


"""