# RSA
# para comenzar se programa el calculo de potencias modulo un numero usando cuadrados sucesivos y
# representacion de exponentes en forma binaria

import sympy.ntheory as nt
from sympy.core.numbers import igcd



def binario(k):
    """
    input: un entero k
    output: un string de la representacion binaria de k.
    se pone el final [2:] dado que los dos primeros caracteres de bin(k) son irrelevantes
    """
    return bin(k)[2:]

def pow_select(k):
    """
    input: un entero k
    output: lista que contiene las potencias 2**j necesarias para expresar k en binario, es decir
    los 1's de la representacion binaria
    """
    b = binario(k)
    l = len(b)
    list_pow_select = []
    for j in range(l):
        if b[l-1-j] == '1':
            list_pow_select.append(2**j)
    return list_pow_select

def pows_a_modn(a,n,l): # base, modulo, cantidad de potencias de la base a
    # retorna una lista de las l potencias de a modulo n
    list_powa = [a%n]
    for i in range(1,l):
        list_powa.append(((list_powa[-1])**2)%n)
    return list_powa

def pow_a_mod(a,k,n): #esta es la funcion realmente importante para calcular potencias
    """
    input: tres datos tipo int:   a;base    k;exponente   n;modulo
    output: un valor tipo int: (a**k) % n, es decir, eleve a ala k y luego saca residuo modulo n
    """
    b = binario(k)
    l = len(b)
    lista_todas = pows_a_modn(a,n,l)
    lista_algunas = []
    for i in range(l):
        if b[l-1-i] == '1':
            lista_algunas.append(lista_todas[i])
    prod = 1
    for i in range(len(lista_algunas)):
        prod = prod*lista_algunas[i]

    return prod % n

# todo lo anterior era solo para calcular potencias modulo n

#tener en cuanta para el siguiente alfabeto que se debe incluir la ñ, pero indagar lo que se debe poner en preambulo para que python reconozca dicha letra
alfabeto={'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,'x':34,'y':35,'z':36, ' ':99}
invalfabeto={11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',17:'g',18:'h',19:'i',20:'j',21:'k',22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',29:'s',30:'t',31:'u',32:'v',33:'w',34:'x',35:'y',36:'z', 99:' '}


def texto_a_num(texto):
    """
    input: string texto o mensaje
    output: string numero grande, que sera usado para construir bloques
    """
    numeros = []
    for letra in texto:
        numeros.append(alfabeto[letra])
    numero_string = ''
    for numero in numeros:
        numero_string += str(numero)

    return numero_string

def particion(numero, L=10): # por defecto bloques de longitud 10
    """
    input: string numero: que se quiere separar en bloques, int L; que sera cantidad de digitos por bloque (se busca que L sea menor que len(str(p*q)), asi todo bloque a, sera menor que m)
    output: lista de strings con los bloques a's
    """
    parti = []
    n = len(numero) // L
    for i in range(n):
        parti.append(numero[L*i:L*(i+1)])
    return parti


def are_coprimes(a,b):
    return igcd(a,b) == 1

def e_coprimo_minimo_con(n):
    contador = 2
    while True:
        if are_coprimes(contador, n):
            break
        else:
            contador += 1
    return contador

p = nt.prime(10000)
q = nt.prime(15000)
m = p*q
n = (p-1)*(q-1) # n es la funcion de Euler evaluada en m, es decir, nt.totient(m)=n
e = e_coprimo_minimo_con(n)
u = pow_a_mod(e,nt.totient(n)-1,n)

#print(binario(155555))
#print(pows_a_modn(2,5,len(binario(155555))))
#print(pow_a_mod(2,155555,5))

def encriptar():
    """
    input: None, pide al usuario escribir mensaje a encriptar
    output: lista de bloques a's
    """
    mensaje = input("Dame el mensaje que quieres encriptar: ")
    num = texto_a_num(mensaje)
    bloques = particion(num)
    new_bloques = []
    for bloque in bloques:
        new_bloques.append(pow_a_mod(int(bloque), e ,m))
    return new_bloques


def consigue_letras(lista_bloques_a):
    """
    input: lista de los bloques a, que son el mensaje encriptado
    output: lista de strings duodigitos que representan a las letras
    """
    numero_string = ''
    for bloque in lista_bloques_a:
        numero_string += str(bloque)
    lista_letras = particion(numero_string, 2)
    return lista_letras

def desencriptar(new_bloques):
    """
    input: lista de bloques b's encriptados
    output: lista de bloques a's del mensaje original
    """
    re_new_bloques = []
    for new_bloque in new_bloques:
        re_new_bloques.append(pow_a_mod(int(new_bloque), u, m))

    lista_letras = consigue_letras(re_new_bloques)
    mensaje_original = ''
    for duodigito in lista_letras:
        mensaje_original += invalfabeto[int(duodigito)]
    return mensaje_original

""" ++++++++++++++++++++++++++++++++++ habilitar cuando quiera encriptar y desencriptar
lista_bloques_b = encriptar()
print("____________________")
print(lista_bloques_b)

lista_bloques_a = desencriptar(lista_bloques_b)
print("____________________")
print(lista_bloques_a)
"""
