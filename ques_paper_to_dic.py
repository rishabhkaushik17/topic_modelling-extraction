import docx
import gensim
from nltk.stem import WordNetLemmatizer

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

def lem(text):
    return WordNetLemmatizer().lemmatize(text, pos='v')

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lem(token))

    return result

def get_dict(filename):
    dlist = getText(filename)
    dict = {}
    flag = 0  
    ques = ''
    for eachl in dlist:
        if len(eachl) == 0:
            continue
        if eachl[0] == 'Q':
            ques = eachl[0:2]
            dict[ques] = eachl.split(']')[2]
            flag = 1
        elif flag == 1:
            prevstr = dict[ques]
            curstr = eachl
            joinstr = prevstr + ' ' + curstr
            dict[ques] = joinstr
    return dict

def qp_pre(filename):
    prepro_data = {}
    dict = get_dict(filename)
    for key,ele in dict.items():
        prepro_data[key] = preprocess(ele)

    pre_without_dup = {}

    for key,ele in prepro_data:
        res = []
        [res.append(x) for x in ele if x not in res]
        pre_without_dup[key] = res

    return prepro_data

def qp_pre_list(filename):
    prepro_data = []
    dict = get_dict(filename)
    for key,ele in dict.items():
        prepro_data.append(preprocess(ele))

    pre_with_no_dup = []

    for pre in prepro_data:
        res = []
        [res.append(x) for x in pre if x not in res]
        pre_with_no_dup.append(res)

    return pre_with_no_dup

def get_ques_marks(filename):
    marks = []
    dlist = getText(filename)
    for eachl in dlist:
        if len(eachl) == 0:
            continue
        if eachl[0] == 'Q':
            b_count = 0
            str = ""
            for i in range(0, len(eachl)):
                if(eachl[i] == '['):
                    b_count+=1
                    if(b_count == 2):
                        for j in range(i, len(eachl)):
                            if(eachl[j] == ']'):
                                break
                            if(eachl[j].isdigit() or eachl[j] == '+'):
                                str += eachl[j]
            marks.append(eval(str))
    return marks

if __name__ == "__main__":
    pre_data = qp_pre("./DWM/T2.docx")
    print(pre_data)