from sentence_transformers import util
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "The cat is really small and lovely",
    "The dog, in the other hand, is big and strong",
    "But the car is the most unique thing among all of them"
]

embeddings_thing = model.encode(sentences)
vector_cat = embeddings_thing[0]
vector_dog = embeddings_thing[1]
vector_car = embeddings_thing[2]



similarity_vector1 = util.cos_sim(vector_cat, vector_dog)
similarity_vector2 = util.cos_sim(vector_car, vector_cat)
print(similarity_vector1)
print(similarity_vector2)