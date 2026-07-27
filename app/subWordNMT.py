from apply_bpe import BPE 
import codecs
import re
obj_bpe=None

def initSubWordModel(codefile):
    codes = codecs.open(codefile, encoding='utf-8')
    obj_bpe = BPE(codes, -1, '@@', None, None)
    return obj_bpe


def convertSubWord(obj_bpe,text):
    return obj_bpe.process_line(text,0)


def decodeSubword(text):
    #file = open("detok.txt", 'w',encoding='utf-8')
    text = re.sub(r"(@@ )|(@@ ?$)","",text)
    return text
    #file.write(text+'\n')



# if obj_bpe != None:
#     print('Success')
#     print(obj_bpe.process_line("i am neha",0))
# else:
#     print('fail')
