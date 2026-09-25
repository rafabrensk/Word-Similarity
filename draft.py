def SimilaridadedeCosseno(A, B):
    #A e B são vetores binarios. Ex: [1,0,0,1]
    if (type(A) != type([1,0])): 
        print("Insira um vetor!")
        return false
    if (type(B) != type([1,0])): 
        print("Insira um vetor!")
        return false

    numerador = 0
    denominador = 0

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

print(IndiceJaccard(list("Amor"),list("Amro")))