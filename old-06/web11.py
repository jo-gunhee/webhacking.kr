import base64
import sys


eni = "admin"
enp = "nimda"

eni = eni.encode('utf-8')
enp = enp.encode('utf-8')

i=0
for i in range(20):
    eni = base64.b64encode(eni)
j=0
for j in range(20):
    enp = base64.b64encode(enp)

eni = eni.decode()
enp = enp.decode()

eni.replace("1","!")
eni.replace("2","@")
eni.replace("3","$")
eni.replace("4","^")
eni.replace("5","&")
eni.replace("6","*")
eni.replace("7","(")
eni.replace("8",")")

enp.replace("1","!")
enp.replace("2","@")
enp.replace("3","$")
enp.replace("4","^")
enp.replace("5","&")
enp.replace("6","*")
enp.replace("7","(")
enp.replace("8",")")

print(eni,"\n\n",enp)

