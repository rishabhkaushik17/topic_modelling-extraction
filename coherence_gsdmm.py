from gensim.models import CoherenceModel
from GSDMM import *
import matplotlib.pyplot as plt

cm_gsdmm = CoherenceModel(topics=topics,
                          dictionary=dictionary,
                          corpus=bow_corpus,
                          texts=docs,
                          coherence='u_mass')

# get coherence value
coherence_gsdmm = cm_gsdmm.get_coherence()
print()
print("Coherence : ",coherence_gsdmm)

# coherence_values = []
# for num_topic in range(5, 50):
#     cm_gsdmm = CoherenceModel(topics=num_topic,
#                           dictionary=dictionary,
#                           corpus=bow_corpus,
#                           texts=docs,
#                           coherence='u_mass')
#     coherence_values.append(cm_gsdmm.get_coherence())

# x = range(5, 50)
# plt.plot(x, coherence_values)
# print(coherence_values)
# plt.xlabel("Num Topics")
# plt.ylabel("Coherence score")
# plt.legend(("coherence_values"), loc='best')
# plt.show()