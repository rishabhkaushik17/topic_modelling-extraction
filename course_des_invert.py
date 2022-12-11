from course_des_to_dic import ext_cod

def get_inverted():
    cd = ext_cod('./DWM/course_des.docx')
    inverted_cd = {}
    for key,val in cd.items():
        for i in val:
            inverted_cd[i] = key
    
    return inverted_cd

if __name__ == "__main__":
    print(get_inverted())