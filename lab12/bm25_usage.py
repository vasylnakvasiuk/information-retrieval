from rank_bm25 import BM25Okapi

corpus = [
    "The official home of the Python Programming Language.",
    "Syntax compared to other programming languages.",
    "It took the best programming community a couple of decades to appreciate Python.",
    "Graphical block-based programming language Scratch has entered the TIOBE.",
    "What tools and techniques does the Python programming language provide for such work?"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)

query = "best programming language"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
best_doc = bm25.get_top_n(tokenized_query, corpus, n=1)[0]

print('Doc scores:\n{}\n'.format(doc_scores))
print('Best doc:\n{}'.format(best_doc))
