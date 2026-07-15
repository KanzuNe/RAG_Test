import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="TestRag")
collection.add(
    ids = ["1","2","3"],
    documents = ["The cat looking good", "The Dog is better", "The car is meh" ]
)

res = collection.query(
    query_texts=["This is not about an animal"],
    n_results=2
)
print(res)

