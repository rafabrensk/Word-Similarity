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

    if (denominator != 0):
        return numerator/denominator
    else: return 0

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

def features_explain(A,B):
    print(f"By jaccard: {jaccard_index(A,B)}")
    print(f"By cosseno: {cosine_similarity(word_to_approximation_vector(A,B))}")
    print(f"By posição: {calculate_position_displacement(A,B)}")
    print(f"By tamanho: {words_size(A,B)}")

def average_features(A,B):
    jac_Val = jaccard_index(A,B)
    cos_Val = cosine_similarity(word_to_approximation_vector(A,B))
    pos_Val = calculate_position_displacement(A,B)
    wsi_Val = words_size(A,B)
    array_values = [jac_Val,cos_Val,pos_Val,wsi_Val]

    jac_Imp = 10
    cos_Imp = 8
    pos_Imp = 7
    wsi_Imp = 10
    array_importance = [jac_Imp,cos_Imp,pos_Imp,wsi_Imp]

    totalIm = 0
    for i in range(len(array_importance)):
        totalIm += array_importance[i]

    average = 0
    for i in range(len(array_values)):
        average += array_values[i]*array_importance[i]
    average = average/totalIm

    low_index = 0
    for i in range(len(array_values)):
        if(array_values[i] <= 0.05): low_index += 1

    if (low_index > 0): return (average**(low_index*2))
    else: return average

def word_similarity(A,B):
    return average_features(A,B)

#Exemple: print(word_similarity("love", "lvoe"))