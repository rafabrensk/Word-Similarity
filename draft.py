def SimilaridadedeCosseno(B):
    numerador = 0
    denominador = 0
    A = []

    for i in range(len(B)):
        A.append(1)

    for i in range(len(A)):
        numerador += A[i]*B[i]
    
    mod_A = 0
    mod_B = 0

    for i in range(len(A)):
        mod_A += A[i]*A[i]
    for i in range(len(B)):
        mod_B += B[i]*B[i]

    mod_A = mod_A ** (1/2)
    mod_B = mod_B ** (1/2)

    denominador = mod_A * mod_B

    return numerador/denominador
    
def IndiceJaccard(A, B):
    #A e B são listas de caracteres em letra minuscula. Ex: [a, m, o, r]
    n_intersecao = 0
    n_uniao = 0
    vetor_letrasA = []
    vetor_letrasB = []
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    alfabeto = list(alfabeto)

    for i in range(len(alfabeto)):
        for j in range(len(A)):
            if(alfabeto[i] == A[j]): 
                vetor_letrasA.append(A[j])
                break
    for i in range(len(alfabeto)):
        for j in range(len(B)):
            if(alfabeto[i] == B[j]): 
                vetor_letrasB.append(B[j])
                break

    if(len(vetor_letrasA)>=len(vetor_letrasB)):
        for i in range(len(vetor_letrasA)):
            for j in range(len(vetor_letrasB)):
                if (vetor_letrasA[i] == vetor_letrasB[j]): 
                    n_intersecao = n_intersecao + 1
                    n_uniao = n_uniao + 1
    if(len(vetor_letrasB)>len(vetor_letrasA)):
        for i in range(len(vetor_letrasB)):
            for j in range(len(vetor_letrasA)):
                if (vetor_letrasB[i] == vetor_letrasA[j]): 
                    n_intersecao = n_intersecao + 1
                    n_uniao = n_uniao + 1

    
    dx = abs(n_uniao-len(vetor_letrasA))
    dy = abs(n_uniao-len(vetor_letrasB))
    n_uniao += dx + dy
    
    return n_intersecao/n_uniao

def PalavraparaVetornaoBinario(A, B):
    #Char vazio: "⠀"
    vetorbinario_A = []
    vetorbinario_B = []

    vetor_letrasA = list(A.lower())
    vetor_letrasB = list(B.lower())

    desacentuacao = str.maketrans(
    "áàãâäéèêëíìîïóòõôöúùûüç",
    "aaaaaeeeeiiiiooooouuuuc"
    )

    texto = "ação é útil"
    texto = texto.translate(desacentuacao)

    if(len(vetor_letrasA) != len(vetor_letrasB)):
        if(len(vetor_letrasA) > len(vetor_letrasB)): 
            for i in range(len(vetor_letrasA)-len(vetor_letrasB)):
                vetor_letrasB.append("⠀")
        if(len(vetor_letrasA) < len(vetor_letrasB)): 
            for i in range(len(vetor_letrasB)-len(vetor_letrasA)):
                vetor_letrasA.append("⠀")
    
    for i in range(len(vetor_letrasA)):
        vetorbinario_A.append(1)
        if(vetor_letrasA[i] == vetor_letrasB[i]): vetorbinario_B.append(1)
        elif((vetor_letrasA[i]).translate(desacentuacao) == vetor_letrasB[i]): vetorbinario_B.append(0.8)
        elif((vetor_letrasB[i]).translate(desacentuacao) == vetor_letrasA[i]): vetorbinario_B.append(0.8)
        else: vetorbinario_B.append(0)
        
    return vetorbinario_B

def OrdenadorporParametro(A, B):
    listA = list(A)
    listB = list(B)
    movimentoBxA = []

    usadosA = [False] * len(listA)

    for j in range(len(listB)):
        encontrou = False
        for i in range(len(listA)):
            if not usadosA[i] and listB[j] == listA[i]:
                movimentoBxA.append(i - j)
                usadosA[i] = True
                encontrou = True
                break
        #if not encontrou:
        #    movimentoBxA.append('~')


    #O limite está entre 0 e (n²/2)

    soma = 0
    for i in range(len(movimentoBxA)):
        soma += abs(movimentoBxA[i])

    percentualerro = 1-(soma/((len(listA)**(2))/2))

    return percentualerro

def MediaFeatures(A, B):
    vetor_letrasA = list(A.lower())
    vetor_letrasB = list(B.lower())

    if(len(vetor_letrasA) != len(vetor_letrasB)):
        if(len(vetor_letrasA) > len(vetor_letrasB)): 
            for i in range(len(vetor_letrasA)-len(vetor_letrasB)):
                vetor_letrasB.append("⠀")
        if(len(vetor_letrasA) < len(vetor_letrasB)): 
            for i in range(len(vetor_letrasB)-len(vetor_letrasA)):
                vetor_letrasA.append("⠀")

    BB = PalavraparaVetornaoBinario(A,B)
    media = (IndiceJaccard(A,B) + SimilaridadedeCosseno(BB) + OrdenadorporParametro(A,B))/3

    print(f"Por Jaccard: {IndiceJaccard(A,B)}")
    print(f"Por Similaridade: {SimilaridadedeCosseno(BB)}")
    print(f"Por Posição: {OrdenadorporParametro(A,B)}")

    return media

print(MediaFeatures("Teste", "testo"))