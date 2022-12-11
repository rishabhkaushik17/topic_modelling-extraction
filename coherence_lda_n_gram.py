from lda_n_grams import *
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt

coherence_model_lda = CoherenceModel(model=ldamodel, texts=topicwise_words, dictionary=dict_, coherence='u_mass')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)

# coherence_values = []

# for num_topic in range(5, 50):
#     lda_model = Lda(doc_term_matrix, num_topics=num_topic, id2word = dict_, passes=1, random_state=0, eval_every=None)
#     coherencemodel = CoherenceModel(model=lda_model, texts=topicwise_words, dictionary=dict_, coherence='u_mass')
#     coherence_values.append(coherencemodel.get_coherence())

# x = range(5, 50)
# plt.plot(x, coherence_values)
# print(coherence_values)
# plt.xlabel("Num Topics")
# plt.ylabel("Coherence score")
# plt.legend(("coherence_values"), loc='best')
# plt.show()