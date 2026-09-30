def cosine_similarity(B):
    numerator = 0
    denominator = 0

    lenght = len(B)

    for i in range(lenght):
        numerator += B[i]

    arA_norm = lenght
    arB_norm = 0

    for i in range(lenght):
        arB_norm += B[i]*B[i]

    denominator = (arA_norm * arB_norm) ** (1/2)

    return numerator/denominator

def jaccard_index(A, B):
    cardinality_intersection = 0
    cardinality_union = 0

    arA = []
    arB = []

    abc = "abcdefghijklmnopqrstuvwxyz"
    abc = process_word(abc)

    for i in range(len(abc)):
        for j in range(len(A)):
            if(abc[i] == A[j]): 
                arA.append(A[j])
                break
    for i in range(len(abc)):
        for j in range(len(B)):
            if(abc[i] == B[j]): 
                arB.append(B[j])
                break

    if(len(arA)>=len(arB)):
        for i in range(len(arA)):
            for j in range(len(arB)):
                if (arA[i] == arB[j]): 
                    cardinality_intersection = cardinality_intersection + 1
                    cardinality_union = cardinality_union + 1
    if(len(arB)>len(arA)):
        for i in range(len(arB)):
            for j in range(len(arA)):
                if (arB[i] == arA[j]): 
                    cardinality_intersection = cardinality_intersection + 1
                    cardinality_union = cardinality_union + 1

    
    dxA = abs(cardinality_union-len(arA))
    dxB = abs(cardinality_union-len(arB))

    cardinality_union += dxA + dxB
    
    return cardinality_intersection/cardinality_union

def word_to_approximation_vector(A,B):
    #Special char: "⠀"
    arA = process_word(A)
    arB = process_word(B)

    vA = []
    vB = []

    normalize = str.maketrans("áàãâäéèêëíìîïóòõôöúùûüç","aaaaaeeeeiiiiooooouuuuc")

    if(len(arA) != len(arB)):
        if(len(arA) > len(arB)): 
            for i in range(len(arA)-len(arB)):
                arB.append("⠀")
        if(len(arA) < len(arB)): 
            for i in range(len(arB)-len(arA)):
                arA.append("⠀")
    
    for i in range(len(arA)):
        vA.append(1)
        if(arA[i] == arB[i]): vB.append(1)
        elif((arA[i]).translate(normalize) == arB[i]): vB.append(0.8)
        elif((arB[i]).translate(normalize) == arA[i]): vB.append(0.8)
        else: vB.append(0)
        
    return vB

def calculate_position_displacement(A, B):
    arA = process_word(A)
    arB = process_word(B)
    
    sum_displacement = 0
    checkedA = [False] * len(arA)

    for j in range(len(arB)):
        for i in range(len(arA)):
            if ((checkedA[i] == False) and (arB[j] == arA[i])):
                sum_displacement += abs(i-j)
                checkedA[i] = True
                break

    return 1-(sum_displacement/((len(arA)**(2))/2))

def words_size(A,B):
    sizeA = len(process_word(A))
    sizeB = len(process_word(B))

    if (sizeA >= sizeB):
        return sizeB/sizeA
    if (sizeB > sizeA):
        return sizeA/sizeB

def process_word(X):
    return list(X.lower())

def average_features(A,B):
    average = (jaccard_index(A,B) + cosine_similarity(word_to_approximation_vector(A,B)) + calculate_position_displacement(A,B) + words_size(A,B))/4
    return average

def word_similarity(A,B):
    return average_features(A,B)

#Exemple: print(word_similarity("maçã", "mbac"))