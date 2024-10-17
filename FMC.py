binario= "110001001101"
w=1
x=5869
m=8051


for cada in binario:
  w= w*w
  if w>m:
     w= w%m
  if cada == "1":
     w=w*x
     if w>m:
       w= w%m

print ("El resultado de"+" "+ str(x) +"^"+ binario +" "+ "mod" +" "+ str(m)+ "  "+ "=" + str(w))


abc={
    'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,
 'n': 13,'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25}  

def encontrar_llave(num):
    llave=""
    for clave, valor in abc.items():
        if valor == num:
          llave = clave
          break
    return llave
a=11
b=15
mensaje="si la gente no cree que las matematicas son simples, es solo porque no se dan cuenta de lo complicado que es la vida"
cifrado=""
for cada in mensaje:
    if cada==" " or cada==",":
      cifrado+=cada
    else:
        m = abc[cada]
        num = (a*m)+b

        if num>25:
            num= num % 26    
        nuevo= encontrar_llave(num)
        cifrado+= nuevo
print (cifrado)
    
