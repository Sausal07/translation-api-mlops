#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import repeat

# from onmt.utils.logging import init_logger
# from onmt.utils.misc import split_corpus
# from onmt.translate.translator import build_translator

# import onmt.opts as opts
# from onmt.utils.parse import ArgumentParser
# from nltk import sent_tokenize
# from nmtCleanerNew import returnCleanDataNew

from .subWordNMT import initSubWordModel, convertSubWord, decodeSubword
# from sentence_tokenize import sentence_split

import ctranslate2
import re




def getTranslationBatch(word,srcLang,tgtLang,objTranslator, objSubword_transliteration,nOptions,objTransliterationDic):
    print('word:',word)
    textToTranslate = []
    temp_list = []
    print(objTransliterationDic)
    if objTransliterationDic!=None:
        print(objTransliterationDic.getSuggestion(word))
        temp_list.extend(objTransliterationDic.getSuggestion(word))
    if tgtLang == 'hin-deva':
            word = '<2hi>'+' '+ word

    elif tgtLang == 'mar-deva':
            word = '<2mr>'+' '+ word

    elif tgtLang == 'ben-beng':
            word = '<2bn>'+' '+ word

    elif tgtLang == 'asm-beng':
            word = '<2as>'+' '+ word

    elif tgtLang == 'brx-deva':
            word = '<2br>'+' '+ word

    elif tgtLang == 'guj-gujr':
            word = '<2gu>'+' '+ word

    elif tgtLang == 'kan-knda':
            word = '<2kn>'+' '+ word

    elif tgtLang == 'kas-arab':
            word = '<2ks>'+' '+ word

    elif tgtLang == 'knn-deva':
            word = '<2kk>'+' '+ word

    elif tgtLang == 'mai-deva':
            word = '<2ma>'+' '+ word

    elif tgtLang == 'mal-mlym':
            word = '<2ml>'+' '+ word

    elif tgtLang == 'npi-deva':
            word = '<2np>'+' '+ word

    elif tgtLang == 'ory-orya':
            word = '<2or>'+' '+ word

    elif tgtLang == 'pan-guru':
            word = '<2pa>'+' '+ word

    elif tgtLang == 'san-deva':
            word = '<2sn>'+' '+ word

    elif tgtLang == 'snd-arab':
            word = '<2sd>'+' '+ word

    elif tgtLang == 'tam-taml':
            word = '<2ta>'+' '+ word

    elif tgtLang == 'tel-telu':
            word = '<2te>'+' '+ word

    elif tgtLang == 'eng-latn':
            word = word

    else:
            print('this tgtlanguage is not supporting')



    # sentence = sentences.split(' ')
    # print('sentence:',sentence)
    # print('srclanguage:',srclanguage)
    # print('tgtlanguage:',tgtlanguage)
    # print('objSubword_transliteration:',objSubword_transliteration)
    # for word in sentence:
        # print('word:',word)

    text=convertSubWord(objSubword_transliteration,word)   
    print('text'+text)
    listText = text.split()
    textToTranslate.append(listText)
    nOptions = int(nOptions)
    if nOptions <1:
        nOptions = 1
    elif nOptions>5:
        nOptions = 5
    

    print('objTranslator:',objTranslator)
    print('textToTranslate',textToTranslate)
    # print(type(nOptions))
    # objTranslator_1 = ctranslate2.Translator("./ctranslate2_transliteration/1.1eng_hin/en_hi_ct2_30000", device="cpu")
    translations = objTranslator.translate_batch(textToTranslate, batch_type="tokens",num_hypotheses=10,beam_size=10, max_batch_size=4096)   #commentforreleasemodels
    # print('translations:',translations)
    # pred = [translation[0]['tokens'] for translation in translations] 
    pred = [translation.hypotheses for translation in translations]
    # print('outside subword')
    print('pred:',pred)
    
    for outPredictions in pred:
        for predSubWord in outPredictions:
            # print('predSubWord:',predSubWord)
            # print(pred[0])
            # temp = decodeSubword((" ").join(pred[0]))
            # res = (" ").join(i)

            # res = [''.join(x) for x in predSubWord]
            res = ' '.join(predSubWord)
            # print((res))
            temp = decodeSubword(res)
            # temp = re.sub(r"(@@ )|(@@ ?$)","",res[0])
            # print("temp")
            # print(temp)
            # print(temp_list)
            temp_list.append(temp)

    temp_list = list(dict.fromkeys(temp_list))
    temp_str = "^".join(str(x) for x in temp_list[:int(nOptions)])
    # temp_str = temp_str+"^"
    # print('temp_list:',temp_list)
    print('temp_str:',temp_str)
    return temp_str


   
def get_translate(ip,srcLang,tgtLang,objTranslator,objSubword_transliteration, nOptions,objTransliterationDic):

    
    # print("delimiter : "+delimiter)

    print("inside get_translate")
    # print("sentences:",ip)
    out = getTranslationBatch(ip,srcLang,tgtLang,objTranslator,objSubword_transliteration,nOptions,objTransliterationDic)
    print('out:',out)
    return out

def main(opt):
    initModel()
    ArgumentParser.validate_translate_opts(opt)
    logger = init_logger(opt.log_file)

   
    # print(get_translate("hello my name is varun. i go to school"))


def _get_parser():
    parser = ArgumentParser(description='translate.py')

    opts.config_opts(parser)
    opts.translate_opts(parser)
    return parser



