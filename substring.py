s = "abcbbbaa"
s_list = list(s)

conjuntos = []

def find_substring(l, start_at):
    letras = []
    band = True
    i = start_at
    while band :
        if i == start_at: 
            letras.append(l[i])
            print("añadido el primer carácter a letras")
        else:
            if l[i] not in letras:
                letras.append(l[i])
                print("letra añadida")
            else:
                band = False
                conjuntos.append(letras)
                print("Encontrada una coincidencia")
                print("---------")
        print(letras, " letras")
        i += 1
        if i == len(l): 
            conjuntos.append(letras)
            break

def busca_mas_larga(c):
    valores = []
    print(c, " c")
    for i in range(len(c)):
        valores.append(len(c[i]))
    print(valores, " valores")
    highest = 0
    for i in range(len(valores)):
        if valores[i] > highest: highest = valores[i]
    return highest
        

for i in range(len(s_list)):
    print(f"Ciclo {i}")
    find_substring(s_list, i)

valor = busca_mas_larga(conjuntos)
print(valor)