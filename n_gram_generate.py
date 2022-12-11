from nltk.util import ngrams
from ques_paper_to_dic import qp_pre_list

def n_grams(filename, n):
    ques = qp_pre_list(filename)
    out = []
    for tokens in ques:
        output = list(ngrams(tokens, n))
        for i in range(len(output)):
            output[i] = list(output[i])
            output[i] = ' '.join(output[i])
        out.append(output)
    return out

if __name__ == "__main__":
    output = n_grams("./DWM/T1.docx", 3)
    for i in output:
        print(i)