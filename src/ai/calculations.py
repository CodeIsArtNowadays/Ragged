import numpy as np

# NORMALIZATION

def l2_norm(v):
    return np.sqrt(np.sum(np.square(v)))

def min_max_norm(v):
    return (v - min(v)) / (max(v) - min(v))

# COSINE SIMILARITY

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (l2_norm(v1) * l2_norm(v2))

# BM25

def calc_term_frequency(query, data):
    res = {}
    for word in query:
        total = 0
        for i, d in enumerate(data):
            index = (word, i)
            tokens = d.split()
            count = tokens.count(word)
            res[index] = count
            if count > 0:
                total += 1
        res[word] = total
    return res

def calc_inverse_document_frequency(query, data, tf):
    res = {}
    for word in query:
        numerator = len(data) - tf[word] + 0.5
        denominator = tf[word] + 0.5
        fraction = numerator / denominator
        res[word] = np.log(fraction + 1)
    return res

def calc_document_length_normalization(data):
    res = 0
    for d in data:
        res += len(d.split(' '))
    res /= len(data)
    return res


def bm25(query, data):
    query = query.split(' ')
    chunks = [chunk.chunk for chunk in data]

    tf = calc_term_frequency(query, chunks)
    idf = calc_inverse_document_frequency(query, chunks, tf)
    dln = calc_document_length_normalization(chunks)
    k1 = 1.2 
    b = 0.75
    res = {}
    for i, d in enumerate(chunks):
        score = 0
        
        for word in query:
            num = tf[(word, i)] * (k1 + 1)
            den = tf[(word, i)] + (k1 * (1 - b + b * (len(d.split(' ')) / dln)))
            
            frac = num / den 
            score += idf[word] * frac
    
        res[data[i].id] = score
    
    return res   
