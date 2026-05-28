from math import inf

import numpy as np 

from sentence_transformers import SentenceTransformer


semantic_model = SentenceTransformer('all-MiniLM-L6-v2')


class Vector:
    def __init__(self, text):
        self.text = text
        vec = semantic_model.encode(text)
        self.vec = vec
    
    def __str__(self):
        return f'{self.text} | Vec {self.vec.shape}'
    

class VectorStorage:
    vectors = []
    
    def add_vector(self, vector: Vector):
        self.vectors.append(vector)
        
    def search(self, query):
        v_query = semantic_model.encode(query)
        
        max_similarity = -inf
        best_v = None
        
        for v in self.vectors:
            similarity_rate = cos_sim(v_query, v)
            
            if max_similarity < similarity_rate:
                max_similarity = similarity_rate
                best_v = v
                
        return best_v, max_similarity
        
        
def rescale(n):
    return n / 50 - 1

def l2_norm(v):
    return np.sqrt(sum([np.square(i) for i in v]))

def cos_sim(v1, v2):
    up = np.dot(v1, v2)
    v1_l2norm = l2_norm(v1)
    v2_l2norm = l2_norm(v2)
    
    return up / (v1_l2norm * v2_l2norm)

# size energy hairness aggression
# haski_input = np.array([65, 95, 85, 5])
# malamut_input = np.array([95, 80, 95, 10])
# mops_input = np.array([15, 20, 25, 2])

# haski = list(map(rescale, haski_input))
# malamut = list(map(rescale, malamut_input))
# mops = list(map(rescale, mops_input))

# print(cos_sim(haski, malamut))
# print(cos_sim(haski, mops))

def main():
    
    vectors = VectorStorage()
    
    vectors_texts = ['king', 'dog', 'England']
    
    vectors.add_vector(Vector('king'))
    vectors.add_vector(Vector('dog'))
    
    for i in vector_texts:
        vectors.add_vector(Vector(i))


if __name__ == '__main__':
    main()