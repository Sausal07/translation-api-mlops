#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import repeat

# from onmt.utils.logging import init_logger
# from onmt.utils.misc import split_corpus
# from onmt.translate.translator import build_translator

# import onmt.opts as opts
# from onmt.utils.parse import ArgumentParser
from nltk import sent_tokenize
from nmtCleanerNew_multi import returnCleanDataNew
from cleaner_all_lang30112022 import returnCleanDataILIL

from subWordNMT import initSubWordModel, convertSubWord, decodeSubword
from sentence_tokenize import sentence_split

from difflib import get_close_matches
import ctranslate2
import re

global supp_lang
supp_lang = ['eng-latn','asm-beng','ben-beng','guj-gujr','hin-deva','kan-knda','mal-mlym','mar-deva','ory-orya','pan-guru','tam-taml','tel-telu','hin-deva-legal']

def normalize_sentence(sentence):
    sentence = sentence.lower().strip()
    return re.sub(r"\s+", " ", sentence)

# ─────────────────────────────────────────────────────────
# EXPAND ABBREVIATIONS (Pipeline Entry Point)
# ─────────────────────────────────────────────────────────

def expand_abbreviations(text, target_tag,GLOSSARY,GLOSSARY_LOOKUP,ABBREVIATIONS):
    """
    Step 1: Expands shorthand text based on abbreviations.txt.
    Step 2: Feeds the expanded text into the fuzzy glossary matcher.
    """
    expanded_text = text

    # SORT LONGEST FIRST to prevent partial replacement conflicts
    sorted_abbreviations = sorted(
        ABBREVIATIONS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )

    for short_form, full_form in sorted_abbreviations:
        # WORD-BOUNDARY SAFE REPLACEMENT
        pattern = r'(?<!\w)' + re.escape(short_form) + r'(?!\w)'
        expanded_text = re.sub(
            pattern,
            full_form,
            expanded_text,
            flags=re.IGNORECASE
        )

    # Call the fuzzy match function automatically using the expanded text
    match_result = fuzzy_glossary_match(expanded_text, target_tag,GLOSSARY,GLOSSARY_LOOKUP)
    return match_result


# ─────────────────────────────────────────────────────────
# FUZZY GLOSSARY FUNCTIONS
# ─────────────────────────────────────────────────────────

def fuzzy_glossary_match(sentence, target_tag,GLOSSARY,GLOSSARY_LOOKUP):
    FUZZY_MATCH_THRESHOLD = 0.85
    if not target_tag or not target_tag.strip():
        return None

    normalized_input = normalize_sentence(sentence)

    # Locate the closest candidate instantly
    matches = get_close_matches(
        normalized_input, 
        GLOSSARY_LOOKUP.keys(), 
        n=1, 
        cutoff=FUZZY_MATCH_THRESHOLD
    )

    if matches:
        normalized_match = matches[0]
        original_glossary_key = GLOSSARY_LOOKUP[normalized_match]
        
        translation = GLOSSARY[original_glossary_key].get(target_tag, None)
        return translation

    return None


# def getTranslationBatch(sentences,objTranslator,srclanguage, tgtlanguage, delimiter):
def getTranslationBatch(sentence,srcLang,tgtLang,objTranslator, objSubword_translation,delimiter,nOptions):
    print('sentence at batch:',sentence)
    textToTranslate = []
    EOS_textToTranslate = []
    if int(nOptions)<1:
        nOptions=1
    elif int(nOptions)>5:
        nOptions=5

    for word in sentence:
        # print('word:',word)
        
        if word.endswith('.') or word.endswith('।'):
            EOS_textToTranslate.append(True)
        else:
            EOS_textToTranslate.append(False)
        
        if srcLang != 'eng-latn' and tgtLang != 'eng-latn':
            # print('IL-IL cleaner')  
            word = returnCleanDataILIL(word)

        if tgtLang == 'hin-deva' or srcLang == 'hin-deva':
                # print('inside hin-devaaa')
                # print('word:',word)
                word = '<2hi>'+' '+ word
                

        elif tgtLang == 'mar-deva' or tgtLang == 'mar-deva-gov' or srcLang == 'mar-deva':
                word = '<2mr>'+' '+ word

        elif tgtLang == 'ben-beng' or srcLang == 'ben-beng' :
                word = '<2bn>'+' '+ word

        elif tgtLang == 'asm-beng' or srcLang =='asm-beng':
                word = '<2as>'+' '+ word

        elif tgtLang == 'guj-gujr' or tgtLang == 'guj-gujr-gov' or srcLang == 'guj-gujr':
                word = '<2gu>'+' '+ word

        elif tgtLang == 'kan-knda' or tgtLang == 'kan-knda-gov' or srcLang == 'kan-knda':
                word = '<2kn>'+' '+ word


        elif tgtLang == 'mal-mlym' or srcLang == 'mal-mlym':
                word = '<2ml>'+' '+ word


        elif tgtLang == 'ory-orya' or srcLang == 'ory-orya':
                word = '<2or>'+' '+ word

        elif tgtLang == 'pan-guru' or srcLang =='pan-guru':
                word = '<2pa>'+' '+ word


        elif tgtLang == 'tam-taml' or srcLang == 'tam-taml':
                word = '<2ta>'+' '+ word
                # print('word after tag:',word)

        elif tgtLang == 'tel-telu' or srcLang == 'tel-telu':
                word = '<2te>'+' '+ word
                # print('word after tag:',word)

        elif tgtLang == 'urd-arab' or srcLang == 'urd-arab':
                word = '<2ur>'+' '+ word

        elif tgtLang == 'knn-deva' or srcLang == 'knn-deva':
                word = '<2kok>'+' '+ word

        elif tgtLang == 'brx-deva' or srcLang == 'brx-deva':
                word = '<2brx>'+' '+ word

        elif tgtLang == 'dgo-deva' or srcLang == 'dgo-deva':
                word = '<2doi>'+' '+ word

        elif tgtLang == 'mni-beng' or srcLang == 'mni-beng':
                word = '<2mni_Beng>'+' '+ word

        elif tgtLang == 'mni-mtei' or srcLang == 'mni-mtei':
                word = '<2mni_Mtei>'+' '+ word

        elif tgtLang == 'kas-arab' or srcLang == 'kas-arab':
                word = '<2ks_Arab>'+' '+ word

        elif tgtLang == 'mai-deva' or srcLang == 'mai-deva':
                word = '<2mai>'+' '+ word

        elif tgtLang == 'npi-deva' or srcLang == 'npi-deva':
                word = '<2ne>'+' '+ word

        elif tgtLang == 'san-deva' or srcLang == 'san-deva':
                word = '<2sa>'+' '+ word

        elif tgtLang == 'sat-olck' or srcLang == 'sat-olck':
                word = '<2sat>'+' '+ word

        elif tgtLang == 'snd-deva' or srcLang == 'snd-deva':
                word = '<2sd>'+' '+ word

        elif tgtLang == 'kas-deva' or srcLang == 'kas-deva':
                word = '<2ks_Deva>'+' '+ word

        # elif tgtLang == 'eng-latn':
        #         word = word

        elif tgtLang == 'hin-tourism' or tgtLang == 'hin-deva-legal' or tgtLang == 'hin-deva-gov':
                # print('inside hin-tourismmmm')
                # print('word:',word)
                word = '<2hi>'+ ' '+ word

        # else:
        #         print('this tgtlanguage is not supporting')



        # sentence = sentences.split(' ')
        # print('sentence:',sentence)
        # print('srclanguage:',srclanguage)
        # print('tgtlanguage:',tgtlanguage)
        # print('objSubword_transliteration:',objSubword_transliteration)
        # for word in sentence:
        # print('word:',word)
        if srcLang == 'eng-latn' or tgtLang == 'eng-latn':
            # print('eng-IL IL-eng cleaner')
            word = returnCleanDataNew(word)
            # print('after cleaning word:',word)
        # else:
        #     word = returnCleanDataILIL(word)

        text=convertSubWord(objSubword_translation,word)   
        # print('text after subword:',text)
        listText = text.split()
        textToTranslate.append(listText)

    

    # print('objTranslator:',objTranslator)
    # print('textToTranslate',textToTranslate)
    # print(type(nOptions))
    # objTranslator_1 = ctranslate2.Translator("./ctranslate2_transliteration/1.1eng_hin/en_hi_ct2_30000", device="cpu")
    translations = objTranslator.translate_batch(textToTranslate, batch_type="tokens",num_hypotheses=int(nOptions),beam_size=5, max_batch_size=4096)   #commentforreleasemodels
    # print('translations:',translations)
    # pred = [translation[0]['tokens'] for translation in translations] 
    pred = [translation.hypotheses for translation in translations]
    # print('outside subword')
    # print('pred:',pred)
    nSuggestionout= []
    temp_list = []
    bFirstEntry = True
    strOutput = ""
    lstParagraphSuggestion = []
    for EOS_InputSentence,sentpred in zip(EOS_textToTranslate,pred):
        lstSentenceSuggestion = []
        for sentPredSugg in sentpred:
            # print(">>>>>>>>>>>>>>>>>>>",sentPredSugg)
            res = ' '.join(sentPredSugg)
            temp = decodeSubword(res)
            if tgtLang == 'hin-deva':
                # print('before temp:',temp)
                if EOS_InputSentence:
                    temp = re.sub(r"\s\.$", "।", temp)
                else:
                    temp = re.sub(r"\s\.$", "", temp)
                # print('after temp:',temp)
            else:
                if EOS_InputSentence:
                    temp = re.sub(r"\s\.$", ".", temp)
                else:
                    temp = re.sub(r"\s\.$", "", temp)
            # print('temp_check:',temp)
            lstSentenceSuggestion.append(temp)
        lstParagraphSuggestion.append(("^").join(lstSentenceSuggestion))
    if nOptions>1:
        strOutput = (";=;".join(lstParagraphSuggestion))
    else:
        strOutput = (" ".join(lstParagraphSuggestion))
    # print("strOutSuggestion",strOutput)

    # for outPredictions in pred:
    #     i=0
    #     for predSubWord in outPredictions:
    #         # print(i)
    #         # print('predSubWord:',predSubWord)
    #         # print(pred[0])
    #         # temp = decodeSubword((" ").join(pred[0]))
    #         # res = (" ").join(i)

    #         # res = [''.join(x) for x in predSubWord]
    #         res = ' '.join(predSubWord)
    #         # print((res))
    #         temp = decodeSubword(res)
    #         # temp = re.sub(r"(@@ )|(@@ ?$)","",res[0])
    #         # print("temp:",temp)
    #         # print(temp)
    #         # print(temp_list)
    #         # temp_list.append(temp)
    #         # print(len(nSuggestionout[i]))
    #         # print('-------------', i)
    #         if bFirstEntry:
    #             nSuggestionout.append([temp])
    #         else:
    #             templst = nSuggestionout[i]
    #             templst.append(temp)
    #             nSuggestionout[i] = templst
    #         # if len(nSuggestionout[i])==0:
    #         #     nSuggestionout[i]=[temp]
    #         # else:
    #         #     nSuggestionout[i].extend([temp])
    #         i=i+1
    #     bFirstEntry = False
    # print('*************')
    # # print(nSuggestionout)
    # # print('tenp_list:',temp_list)
    # temp_str = []
    # for suggestionList in nSuggestionout:
    #     temp_str.append(" ".join(str(x) for x in suggestionList))
    # strOutput= "^".join(str(x) for x in temp_str)
    # # temp_str = " ".join(str(x) for x in temp_list)
    # # print('temp_list:',temp_list)
    # # print('temp_str:',temp_str)
    return strOutput


   
def get_translate(ip,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions):

    # print("inside get_translate")
    # print('objTranslator:',objTranslator)
    # print("delimiter : "+delimiter)
    # print('i am here')
    
    sentences = []
    bDelimiterFound = False
    bSentenceSplitting = True
    bSentenceSplittedbyNewLine = False
    # if delimiter.endswith(';ss'):
    #     bSentenceSplitting = True
    #     delimiter = delimiter[:-3]
    if '\n' in ip:
        bSentenceSplittedbyNewLine=True
    if delimiter != '':
        if delimiter in ip:
            # print('delimiter set to empty string')
            bDelimiterFound = True         
    resultTranslationBatchList = []
    # print('bDelimiterFound:',bDelimiterFound)
    if bDelimiterFound:
        # print('delimiter found')
        if bSentenceSplitting:
            if srclanguage in supp_lang:
                sentences_batches = ip.strip().split(delimiter)
                # print("first if",sentences_batches[:5])
                for sentences_batch in sentences_batches:
                    # print('sentences_batch:',sentences_batch)
                    if sentences_batch.strip()!="":
                        sentences = sentence_split(sentences_batch,srclanguage)
                        # print('sentences:',sentences)
                        resultTranslationBatchList.append(getTranslationBatch(sentences,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions))
                    else:
                        # print('none strng delimiter')
                        resultTranslationBatchList.append("")

            # elif srclanguage =='eng-latn':
            #     sentences_batches = ip.strip().split(delimiter)
            #     for sentences_batch in sentences_batches:
            #         if sentences_batch.strip()!="":
            #             sentences = sentence_split(sentences_batch,"en")
            #             resultTranslationBatchList.append(getTranslationBatch(sentences,objTranslator,srclanguage,tgtlanguage," "))
            else:
                sentences_batches = ip.strip().split(delimiter)
                print("else",sentences_batches[:5])
                for sentences_batch in sentences_batches:
                    if sentences_batch.strip()!="":
                        sentences = sent_tokenize(ip.strip())
                        resultTranslationBatchList.append(getTranslationBatch(sentences,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions))
                    else:
                        # print('none strng delimiter')
                        resultTranslationBatchList.append("")
            # print('resultTranslationBatchList:',resultTranslationBatchList)
            out = (delimiter).join([str(elem) for elem in resultTranslationBatchList])
            # print('out:',out)
        elif bSentenceSplittedbyNewLine:
            sentences_batches = ip.strip().split(delimiter)
            for sentences_batch in sentences_batches:
                if sentences_batch.strip()!="":
                    sentences = sentences_batch.split('\n')
                    resultTranslationBatchList.append(getTranslationBatch(sentences,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions))
            out = (delimiter).join([str(elem) for elem in resultTranslationBatchList])
        else:
            sentences = ip.strip().split(delimiter)
            # for sentences_batch in sentences_batches:
            #     if sentences_batch.strip()!="":
            #         resultTranslationBatchList.append(getTranslationBatch(sentences,objTranslator,srclanguage,tgtlanguage," "))
            out = getTranslationBatch(sentences,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions)
    else:
        # print('delimiter not found')
        if srclanguage in supp_lang:
            print("#####################  inside sentence_splitter #################")
            # print('ip:',ip)
            if srclanguage == 'hin-deva-legal':
                sentences = sentence_split(ip.strip(),"hin-deva")    
            else:
                sentences = sentence_split(ip.strip(),srclanguage)
            # print('sentence:',sentences)       
            # print("inside sentence split {}".format(sentences))
        # elif srclanguage =='eng-latn':
        #     sentences = sentence_split(ip.strip(),"en")
        else:
            print('nltk sent tokenizer')
            sentences = sent_tokenize(ip.strip())
            
        # out = getTranslationBatch(sentences,objTranslator,srclanguage,tgtlanguage," ")
        out = getTranslationBatch(sentences,srclanguage,tgtlanguage,objTranslator,objSubword_translation,delimiter,nOptions)

    return(out)

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



