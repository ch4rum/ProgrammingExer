#!/bin/python3
#
#   dBBBBBb .dBBBBP dBBBBBb  
#       dBP BP           BB  ~ ch4rum
#   dBBBBK' `BBBBb   dBP BB  ~ https://github.com/ch4rum/ProgrammingExer
#  dBP  BB     dBP  dBP  BB  ~ python3
# dBP  dB'dBBBBP'  dBBBBBBB                            

import sys, signal, string

def handler(sig, frame):
    print(f"\n\n[!] Saliendo ... \n")
    sys.exit(1)

# Ctrl + C 
signal.signal(signal.SIGINT, handler)

class DataOperations:
    # Funciones mas sencillas para hacer las operaciones basicas para hallar lo nesesario para
    # las llaves publicas y privadas
    
    @staticmethod
    def verify_number_prime(n):
        # Funcion Que Verifica si el numero ingresado es primo o no 
        count = 0 ; x = 2
        while x < n and count == 0:
            if n % x == 0:
                count += 1
            x += 1
        if count == 0: return True
        else: return False
    
    @staticmethod
    def generate_primes(n):
        # Genera una lista de numeros primos
        list=[]
        if n != 0:
            for x in range(1,n+1):
                if DataOperations.verify_number_prime(x) == True:
                    list.append(x)
            return list

    @staticmethod
    def mcd (e,phi):
        # Maximo como un divisor de dos numero utiliza el algoritmo Euclides
        mod = phi % e
        while mod != 0:
            phi = e
            e = mod
            mod = phi % e
        return e

    @staticmethod
    def gen_calculate(phi):
        # Calcula el mcd  para saber si es coprimo y genera una lista
        list = [] ; e = 2
        while e>1 and e<phi:
            if DataOperations.mcd(e,phi) == 1:
                list.append(e)
                e += 1
            else: e += 1
        return list

    @staticmethod
    def Inverse_Multiplicative(e,phi):
        # Calcula el inverso multiplicativo de e
        k = 1
        mod = (1+(k)*(phi))%(e)
        while mod != 0:
            k += 1
            mod = (1+(k)*(phi))%(e)
        return int(1+(k)*(phi)/(e))

class AskForvalues:
    # Pide los datos para llamar a las funciones nesesarias y retorna los resulados correspondientes

    @staticmethod
    def PorQPNPhi():
        # Pide al usuario los valores (p) y (q) y verifica si los datos son validos
        # que sean primos y no se repitan, calcula la n y retorna en una list los valores
        p = int(input("\tValor de (p): "))
        while DataOperations.verify_number_prime(p) == False:
            print(f"\t(p) Tiene que ser un numero primo !!!\n")
            p = int(input("\tValor de (p): "))

        q = int(input("\tValor de (q): "))
        while DataOperations.verify_number_prime(q) == False or q == p:
            print(f"\t(q) Tiene que ser un numero primo y/o diferente de (p) !!!\n")
            q = int(input("\tValor de (q): "))
        n = p * q
        phi = (p-1)*(q-1)
        listpqnphi = [q,p,n,phi]
        return listpqnphi

    @staticmethod
    def ValueE():
        # Pide el valor de (e) y verifica si se cumple el mcd
        e = int(input("\tValor para (e): "))
        while DataOperations.mcd(e, phi) != 1:
            print(f"\tElige un valor de la lista !!!")
            e = int(input("\tValor para (e): "))
        return e

    @staticmethod
    def Msj_Encrypt(key):
        # Pide el mensaje para encriptar,luego lo encripta y retorna el msj encriptado
        msj = input("\tMensaje: ").upper()#[::-1]
        msj = msj.split(" "); msjEncrypt = []; strmsj = ""
        for values in msj:
            msj1 = Msj_Encrypt_Decrypt.Encrypt_word(values, key)
            msjEncrypt.append(msj1)
        for i in msjEncrypt:
            strmsj = strmsj+str(i)+""
        return strmsj

    @staticmethod
    def Msj_Decrypt(key):
        # Pide el mensaje cifrado, lo desencripta y luego muestra el mensaje desencriptado
        msj = input("\tMensaje: ")#[::-1]
        msj = msj.split(" "); msjDecrypt = []; strmsj = ""
        for values in msj:
            msj1 = Msj_Encrypt_Decrypt.Decrypt_msj(values, key)
            msjDecrypt.append(msj1)
        for i in msjDecrypt:
            strmsj = strmsj+str(i)
        return strmsj

class Msj_Encrypt_Decrypt:
    # Encripta/desencripta las letras y palabras, funciones para desencriptar o encriptar

    @staticmethod
    def Encryps_or_Decrypt(msj,key):
        # Exponenciacion modular para sacar el resultado encritado o desencriptado
        n1,n2 = key; a = bin(n2)[2:]; x = 1
        poten = msj % n1
        for values in range(len(a)):
            if int(a[-1-values]) == 1:
                x = (x * poten) % n1
            poten = (poten * poten) % n1
        return x

    @staticmethod
    def Encrypt_word(msj,key):
        # Encripta una palabra, segun lo que nos da la exponenciacion modular de la letra segun
        # el valor que nos da en el abecedario donde A=00, B=01, C=02 .... Z=25, 
        # retorna la palabra cifrada
        abc = [] ; abc2 = [] ;abc3 = []; msjEncrypt = [] 
        for letter in msj:
            if letter.isalpha():
                position = string.ascii_uppercase.index(letter)
                abc.append(position)
        '''if len(abc) % 2 == 1:
            abc2.append(abc[0])
            for values in range(1,len(abc),2):
                if values == len(abc) -1:
                    abc2.append(abc[values])
                else:
                    abc2.append(int(str(abc[values]) + str(abc[values+1])))
        else:
            for values in range(0,len(abc),2):
                if values == len(abc) -1:
                    abc2.append(abc[values])
                else:
                    abc2.append(int(str(abc[values]) + str(abc[values+1])))
        for element in abc2:
            if isinstance(element, int):
                abc3.append(str(element))
            else:
                abc3.append(''.join(map(str,element)))
        result = list(map(int,abc3))'''
        for number in abc:
            msj = Msj_Encrypt_Decrypt.Encryps_or_Decrypt(number,key)
            msjEncrypt.append(msj)
        return msjEncrypt
        
    @staticmethod
    def Decrypt_msj(msj,key):
        # Desencripta el msj, segun el resultado que nos da la exponenciacion modular y luego
        # la compara los los digitos que valen en el abcedario, retorna msj desencriptado
        abc2 = [] ;abc3 = {}; abc4 = []; msjDecrypt = []
        msj = Msj_Encrypt_Decrypt.Encryps_or_Decrypt(int(msj),key)
        abc2.append(msj)
        for letter in string.ascii_uppercase:
            abc3[ord(letter)- 65] = letter
        '''for values in abc2:
            if values > 9:
                str_values = str(values)
                if len(str_values) == 2 and int(str_values) < 10:
                    abc4.append(values)
                else:
                    if len(str_values) == 2:
                        one_digit = int(str_values[:1])
                        two_digit = int(str_values[1:])
                    elif len(str_values) == 4:
                        one_digit = int(str_values[:2])
                        two_digit = int(str_values[2:])
                    else:
                        one_digit = int(str_values[0])
                        two_digit = int(str_values[1:])
                abc4.append(one_digit)
                abc4.append(two_digit)
            else:
                abc4.append(values)'''
        for values in abc2:
            if values in abc3:
                msjDecrypt.append(abc3[values])
            else:
                msjDecrypt.append("*")
        return "".join(msjDecrypt)

if __name__ == "__main__":
    listNumbers=DataOperations.generate_primes(500)
    print(f"\t\t\tRSA\n1) Valores (p) y (p)\n\n*Lista primos:> {listNumbers}\n")
    p,q,n,phi = AskForvalues.PorQPNPhi()
    print(f"\n2) Calculamos valor (n)\n\n\t(n) = (p) * (q)\n\t(n) = {p} * {q}\n\t(n) = {n}")
    print(f"\n3) Calculamos valor (ø)\n\t(ø) = (p-1) * (q-1)\n\t(ø) = {p-1} * {q-1}\n\t(ø) = {phi}")
    listE = DataOperations.gen_calculate(phi)
    print(f"\n4) Calculamos e\n\t(e) = 1<e<ø and mcd(e,ø) == 1\n\n*Lista para (e):> {listE}\n")
    e = AskForvalues.ValueE()
    d = DataOperations.Inverse_Multiplicative(e,phi) 
    print(f"\n5) Calculamos (d)\n\t(d) = (e) * (d) == congruente == (1) * (mod ø)\n\t(d) = {d}\n")
    key_public = [n,e] ; key_private = [n,d]
    print(f"\n6) Llaves de encriptado\n\tLlave publica = {key_public}\n\tLlave privada = {key_private}\n")
    print(f"\n7) Ahora vamos a cifrar el mensaje(RSA)")
    msj_Encrypt = AskForvalues.Msj_Encrypt(key_public)
    print(f"\tMensaje cifrado: {msj_Encrypt}")  
    print(f"\n8) Ahora vamos a descifrar el mensaje(RSA)")
    msj_Decrypt = AskForvalues.Msj_Decrypt(key_private)
    print(f"\tMensaje descifrado: {msj_Decrypt}") 
