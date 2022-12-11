import pandas as pd
from course_des_to_dic import ext_cod
from ques_paper_to_dic import get_dict, qp_pre
from n_gram_generate import n_grams

import math
import re
from collections import Counter

import pandas as pd

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_topics_and_cosine_similarity(ques_paper, cd, exam):
    topic_arr = []
    cosine_arr = []
    bigrams_ques = n_grams(exam, 2)
    trigrams_ques = n_grams(exam, 3)
    index = 0
    for key, ele in ques_paper.items():
        max_cosine_bigram = 0
        most_rel_topic_bigram = ""
        for word in bigrams_ques[index]:
            for module, topics in cd.items():
                for topic in topics : 
                    vector1 = text_to_vector(word)
                    vector2 = text_to_vector(topic)
                    cosine_sim_bigram = get_cosine(vector1, vector2)
                    if(cosine_sim_bigram > max_cosine_bigram):
                        max_cosine_bigram = cosine_sim_bigram
                        most_rel_topic_bigram = topic

        max_cosine_trigram = 0
        most_rel_topic_trigram = ""
        for word in trigrams_ques[index]:
            for module, topics in cd.items():
                for topic in topics: 
                    vector1 = text_to_vector(word)
                    vector2 = text_to_vector(topic)
                    cosine_sim_trigram = get_cosine(vector1, vector2)
                    if(cosine_sim_trigram > max_cosine_trigram):
                        max_cosine_trigram = cosine_sim_trigram
                        most_rel_topic_trigram = topic
        
        if(max_cosine_bigram >= max_cosine_trigram):
            topic_arr.append(most_rel_topic_bigram)
            cosine_arr.append(max_cosine_bigram)
        else:
            topic_arr.append(most_rel_topic_trigram)
            cosine_arr.append(max_cosine_trigram)
        
        index+=1
    
    return topic_arr, cosine_arr

def save_csv(topics, cosine, ques_paper):
    ques = get_dict(ques_paper)
    ques_num = list(ques.keys())
    df = pd.DataFrame(list(zip(ques_num, topics, cosine)), 
        columns =['Question Number', 'Topic', 'Cosine Similarity'])
    df.to_csv('ques_topics.csv', index=False)

if __name__ == "__main__":
    exam = "./DWM/T3.docx"
    ques_paper = qp_pre(exam)
    cd = ext_cod("./DWM/course_des.docx")
    topics, cosine = get_topics_and_cosine_similarity(ques_paper, cd, exam)
    save_csv(topics, cosine, exam)