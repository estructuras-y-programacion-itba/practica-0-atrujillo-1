# Tu implementacion va aqui
import random
def upper_custom(texto):
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            resultado += chr(ord(char) - 32)
        else:
            resultado += char
    return resultado
def dado():
    valor=random.randint(1,6)
    return valor
def hola_mundo():
    return "hola_mundo"

def turno1():
    finaliza = False
    
    dados_tirada = []
    nro_tirada = 0
    dados_a_tirar = 5
    while finaliza == False and nro_tirada < 3:
        dados_guardados = []
        nro_dado = 0
        for nro_dado in range(dados_a_tirar):  
            valor = dado()
            dados_tirada.append(valor)
            nro_dado +=1
        print(f'Tirada {dados_tirada}')
        finalizar= upper_custom(input("Desea finalizar su turno?: "))
        if finalizar=="SI":
            finaliza=True
            print(dados_tirada)
        else:
            for k in range(len(dados_tirada)):
                print(dados_tirada[k])
                guardar= upper_custom(input("Desea guardar este dado?: "))
                if guardar == "SI":
                    dados_guardados.append(dados_tirada[k])
            print(f'Dados guardados: {dados_guardados}')
            dados_tirada = dados_guardados
            dados_a_tirar = 5-len(dados_guardados)
            nro_tirada +=1
            

def turno():
    finaliza=False
    dados_guardados=[]
    i=0
    while finaliza==False and i<3:
        
            tirada=[]
            j=0
            
            while j<5:
                valor = dado()
                tirada.append(valor) 
                j+=1           
            print(f'Tirada {tirada}')
            
            finalizar= upper_custom(input("Desea finalizar su turno?: "))
            if finalizar=="SI":
                for k in range(len(tirada)):
                    dados_guardados.append(tirada[k])
                finaliza=True
            else:
                guardar= input("Que valores de dados guarda: ")
                for l in range(len(tirada)):
                    for n in range(len(guardar)):
                        caracter=guardar[n]
                        if caracter==str(tirada[l]):
                            dados_guardados.append(tirada[l])                        
                finaliza=False
            i+=1
    print(dados_guardados)
    
turno1()