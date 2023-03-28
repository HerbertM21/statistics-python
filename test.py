from googlesearch import search

query = "hello world"
results = search(query, num_results=5)

for result in results:
    print(result)
