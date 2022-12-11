import pandas as pd
import numpy as np
import gensim
from gsdmm import MovieGroupProcess
from ques_paper_to_dic import qp_pre_list

docs = qp_pre_list("./DWM/T1.docx")

# create dictionary of all words in all documents
dictionary = gensim.corpora.Dictionary(docs)

# create variable containing length of dictionary/vocab
vocab_length = len(dictionary)

# create BOW dictionary
bow_corpus = [dictionary.doc2bow(doc) for doc in docs]

# initialize GSDMM
gsdmm = MovieGroupProcess(K=8, alpha=0.1, beta=0.3, n_iters=8)

# fit GSDMM model
y = gsdmm.fit(docs, vocab_length)

# print number of documents per topic
doc_count = np.array(gsdmm.cluster_doc_count)
print('Number of documents per topic :', doc_count)

# Topics sorted by the number of document they are allocated to
top_index = doc_count.argsort()[-15:][::-1]
print('Most important clusters (by number of docs inside):', top_index)

for_wcloud = []
topics = []
def top_words(cluster_word_distribution, top_cluster, values):
    for cluster in top_cluster:
        sort_dicts = sorted(cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:values]
        sort_dicts = dict(sort_dicts)
        sum = 0
        topic = []
        for ky in sort_dicts:
            sum += sort_dicts[ky]
            topic.append(ky)
        for ky in sort_dicts:
            sort_dicts[ky] /= sum
            sort_dicts[ky] = round(sort_dicts[ky], 2)

        if len(sort_dicts) == 0:
            continue
        for_wcloud.append(sort_dicts)
        print("\nCluster %s : %s"%(cluster, sort_dicts))

        # append topics to topics list
        topics.append(topic)
    return topics

# get top words in topics
topics = top_words(gsdmm.cluster_word_distribution, top_index, 8)
# print(gsdmm.cluster_word_distribution)