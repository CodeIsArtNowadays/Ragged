from sentence_transformers import SentenceTransformer

from calculations import cos_sim

semantic_model = SentenceTransformer('all-MiniLM-L6-v2')


class Vector:
    def __init__(self, text, metadata=None):
        self.text = text
        vec = semantic_model.encode(text)
        self.vec = vec
        self.metadata = metadata
    
    def __str__(self):
        return f'{self.text} | Vec {self.vec.shape}'
        
    def __repr__(self):
        return f'{self.text}'
    

class VectorStorage:
    
    def __init__(self):
        self.vectors = []
    
    def add_vector(self, vector: Vector):
        self.vectors.append(vector)
    
    def sort(self, query_vector):
        score = sorted(self.vectors, key=lambda x: cos_sim(query_vector, x.vec), reverse=True)
        return score
        
        
    def search(self, query, k=3):
        v_query = semantic_model.encode(query)
    
        return self.sort(v_query)[:k]


def main():
    
    vectors = VectorStorage()
    
    vectors_texts = ['king', 'dog', 'England', 'pink', 'rap']
    
    for i in vectors_texts:
        vectors.add_vector(Vector(i))
    
    print(vectors.search('London'))
    print(vectors.search('monarchy'))


if __name__ == '__main__':
    main()