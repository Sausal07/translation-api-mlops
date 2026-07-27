# from translate import initModel as model_bi_directional_translate   
from translate_multi import get_translate as bi_directional_translate
from translate_multi import expand_abbreviations
import os
import json
import re
import logging
import ctranslate2
from subWordNMT import initSubWordModel
from Transliteration_RuleBased import GenericTransliteration
from transliteration_load_ct_multi import returnTransliterationLine

objEngmulti_translation = None
objSubwordEngmulti_translation =None

objmultiEng_translation = None
objSubwordmultiEng_translation = None

objEng_hintourism_translation = None
objSubwordEngHintourism_translation = None

objEngBodo_translation = None
objSubwordEngBodo_translation = None

objEngManipuri_translation = None
objSubwordEngManipuri_translation = None

objEng_hinLegal_translation = None
objhin_EngLegal_translation = None

objEng_IL_high_resource_translation = None
objSubwordEngmulti_high_resource_translation =None




# fengmultilog = None


# ip_client = None


def initModeltranslation():

        # global objEngmulti_translation
        # global objmultiEng_translation
        # global objEng_hintourism_translation
        # global objEngBodo_translation
        # global objEngManipuri_translation
        # global objEng_hinLegal_translation
        # global objhin_EngLegal_translation
        # global objEng_IL_domain_translation
        # global objIL_Eng_domain_translation

        global objEng_IL_high_resource_translation
        # global objEng_IL_mid_resource_translation
        # global objEng_IL_dravidian_translation
        global objIL_Eng_high_resource_translation
        # global objIL_Eng_mid_resource_translation
        # global objIL_Eng_darvidian_translation
        # global objEng_IL_low_resource_translation
        # global objIL_Eng_low_resource_translation


        # objEngmulti_translation = ctranslate2.Translator("./Translation_Models/en_il_ct2_model_400000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objmultiEng_translation = ctranslate2.Translator("./Translation_Models/il_en_ct2_model_220000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objEng_hintourism_translation = ctranslate2.Translator("./Translation_Models/ct2_model_tourism_404000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objEngBodo_translation = ctranslate2.Translator("./Translation_Models/en_brx_372000_ctranslate2", device="cpu")
        # objEngManipuri_translation = ctranslate2.Translator("./Translation_Models/en_mni_194000_ctranslate2", device="cpu")
        # objEng_hinLegal_translation = ctranslate2.Translator("./Translation_Models/en_hi_legal", device="cpu")
        # objhin_EngLegal_translation = ctranslate2.Translator("./Translation_Models/hi_en_legal", device="cpu")
        # objEng_IL_domain_translation = ctranslate2.Translator("./Translation_Models/en_il_gov_domain", device="cpu")
        # objIL_Eng_domain_translation = ctranslate2.Translator("./Translation_Models/il_en_gov_domain", device="cpu")

        objEng_IL_high_resource_translation = ctranslate2.Translator("./Translation_Models/en-il-high-resource", device="cpu")
        # objEng_IL_mid_resource_translation = ctranslate2.Translator("./Translation_Models/en-il-mid-resource", device="cpu")
        # objEng_IL_dravidian_translation = ctranslate2.Translator("./Translation_Models/en-il-dravidian", device="cpu")
        # objEng_IL_low_resource_translation = ctranslate2.Translator("./Translation_Models/en-il-low-resource", device="cpu")
        objIL_Eng_high_resource_translation = ctranslate2.Translator("./Translation_Models/il-en-high-resource", device="cpu")
        # objIL_Eng_mid_resource_translation = ctranslate2.Translator("./Translation_Models/il-en-mid-resource", device="cpu")
        # objIL_Eng_darvidian_translation = ctranslate2.Translator("./Translation_Models/il-en-dravidian", device="cpu")
        # objIL_Eng_low_resource_translation = ctranslate2.Translator("./Translation_Models/il-en-low-resource", device="cpu")
        # print('objhin_EngLegal_translation:',objhin_EngLegal_translation)
        # global fenghinlog
        # global logger_enghin
        # global fhandler_enghin
        

        # logger_enghin = logging.getLogger('enghin')
       
        # fhandler_enghin = logging.FileHandler('./Transliteration_logs_ct/eng_hin.log',mode ='a+',encoding ='UTF-8')
       
        
        # global objSubwordEngmulti_translation
        # global objSubwordmultiEng_translation
        # global objSubwordEngHintourism_translation
        # global objSubwordEngBodo_translation
        # global objSubwordEngManipuri_translation

        global objSubwordEngmulti_high_resource_translation
        # global objSubwordEngmulti_mid_resource_translation
        # global objSubwordEngmulti_dravidian_translation
        global objSubwordmultiEng_high_resource_translation
        # global objSubwordmultiEng_mid_resource_translation
        # global objSubwordmultiEng_dravidian_translation
        # global objSubwordEngmulti_low_resource_translation
        # global objSubwordmultiEng_low_resource_translation

        #codes files  Bengali, Tamil, Malayalam, Kannada, Gujaratti, Punjabi, Telugu
        # objSubwordEngmulti_translation = initSubWordModel('./BPE_Models/codes_file_en_il')
        # objSubwordmultiEng_translation = initSubWordModel('./BPE_Models/codes_file_il_en')        
        # objSubwordEngHintourism_translation = initSubWordModel('./BPE_Models/codes_file_en_tourism')
        # objSubwordEngBodo_translation = initSubWordModel('./BPE_Models/codes_file_br')
        # objSubwordEngManipuri_translation = initSubWordModel('./BPE_Models/codes_file_mn')

        objSubwordEngmulti_high_resource_translation = initSubWordModel('./BPE_Models/codes_file_en_il_high_resource')
        # objSubwordEngmulti_mid_resource_translation = initSubWordModel('./BPE_Models/codes_file_en_il_mid_resource')
        # objSubwordEngmulti_dravidian_translation = initSubWordModel('./BPE_Models/codes_file_en_il_Dravidian')
        # objSubwordEngmulti_low_resource_translation = initSubWordModel('./BPE_Models/codes_file_en_il_low_resource')
        objSubwordmultiEng_high_resource_translation = initSubWordModel('./BPE_Models/codes_file_il_en_high_resource')
        # objSubwordmultiEng_mid_resource_translation = initSubWordModel('./BPE_Models/codes_file_il_en_mid_resource')
        # objSubwordmultiEng_dravidian_translation = initSubWordModel('./BPE_Models/dravidian_reverse_bpe')
        # objSubwordmultiEng_low_resource_translation = initSubWordModel('./BPE_Models/codes_file_il_en_low_resource')


        # for marthi modi transliteration when you do english to modi translation
        global punctList
        with open("punct.txt",'r',encoding='utf-8') as fPunct:
                punctList = fPunct.read().replace('\r\n','\n').split('\n')
                punctList.append(' ')
                # print(punctList) 

        global objMarModiRuleTrans
        objMarModiRuleTrans = GenericTransliteration()
        objMarModiRuleTrans.loadDictionaries("./genericTrans/marathi2modi.rul","punct.txt") 


        global GLOSSARY_LOOKUP
        global ABBREVIATIONS
        global GLOSSARY

        GLOSSARY_FILE = "./glossary.json"
        ABBREVIATION_FILE = "./abbrevations.txt"

        def normalize_sentence(sentence):
            sentence = sentence.lower().strip()
            return re.sub(r"\s+", " ", sentence)


        # ─────────────────────────────────────────────────────────
        # LOAD GLOSSARY & PRECOMPUTE LOOKUP
        # ─────────────────────────────────────────────────────────

        with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
            GLOSSARY = json.load(f)

        # Precomputed lowercase map for O(1) matching speed instead of an explicit loop
        GLOSSARY_LOOKUP = {normalize_sentence(k): k for k in GLOSSARY.keys()}

        # ─────────────────────────────────────────────────────────
        # LOAD ABBREVIATIONS
        # ─────────────────────────────────────────────────────────

        ABBREVIATIONS = {}

        with open(ABBREVIATION_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(maxsplit=1)
                if len(parts) != 2:
                    continue

                short_form = parts[0].strip()
                full_form = parts[1].strip()    

                ABBREVIATIONS[short_form] = full_form
                

                


def pass_variable(ip):
        global ip_client
        ip_client = ip  
        # print(ip_client)  
        # print('==================================')  



# def returnTransliterationLine(input_text,tgtLang,objTransliteration,objSubword_transliteration,nOptions):
#     print('inside returnTransliterationLine')
#     print('input_text:',input_text)
#     wordForTransliteration=""
#     strOutputTransliteration=""
#     delimiter=""
#     input_text = input_text.replace('\'','')
#     input_text = input_text.replace('’','')
#     print('transliteration input: {} , len of punctList {}'.format(input_text,len(punctList)))

#     for cTransliteration in input_text:
#         print('cTransliteration:',cTransliteration)
#         if cTransliteration in punctList:
#             if wordForTransliteration!="":
#                 print('wordForTransliteration' + wordForTransliteration)
#                 strOutputTransliteration=strOutputTransliteration+bi_directional_translate(wordForTransliteration,tgtLang,objTransliteration,objSubword_transliteration,nOptions)
#                 wordForTransliteration = ""
#                 print('strOutputTransliteration:',strOutputTransliteration)
#             strOutputTransliteration = strOutputTransliteration+cTransliteration
#         else:
#             wordForTransliteration = wordForTransliteration+cTransliteration

#     if wordForTransliteration!="":
#         print('wordForTransliteration' + wordForTransliteration)
#         strOutputTransliteration=strOutputTransliteration+bi_directional_translate(wordForTransliteration,tgtLang,objTransliteration,objSubword_transliteration, nOptions)
#     return strOutputTransliteration   


def translation_model_multi(ip_text,srcLang,tgtLang,delimiter,nOptions):
        # print("inside translation_model_multi")
        # print("==========================================================")
        # print(lang_id)
        # print(ip_text)
        # lang_supp = ['asm-beng','ben-beng','guj-gujr','hin-deva','kan-knda','mal-mlym','mar-deva','ory-orya','pan-guru','tam-taml','tel-telu','hin-tourism']

        # print('ip_text:',ip_text)
        if srcLang == 'eng-latn':

            if tgtLang == 'hin-deva':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op = expand_abbreviations(ip_text,'<2hi>',GLOSSARY,GLOSSARY_LOOKUP,ABBREVIATIONS)
                # print('op after abbber:',op)
                if op != None:
                        # print('inside dict')
                        return op
                else:
                    # print('inside tranlsation model call')
                    op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)
                    # print('op load:',op)

            elif tgtLang == 'mar-deva' or tgtLang == 'mar-modi':
                if tgtLang == 'mar-modi':
                    # print('inside eng-modi translation')
                    # op =  bi_directional_translate(ip_text.strip(),srcLang,'mar-deva',objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                    op =  bi_directional_translate(ip_text.strip(),srcLang,'mar-deva',objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)
                    # print('op of eng_mar translation:',op)
                    if op!='':
                        # print('op of eng_mar translation:',op)
                        op = objMarModiRuleTrans.returnTransliterationLine(op.strip())
                      
                else:

                    op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)
            

            elif tgtLang=='ben-beng':
                # ip_text= ip_text.lower()
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)

                
            elif tgtLang=='tam-taml':
                # print("inside tamil: input {}".format(ip_text))
                # print('objEng_IL_dravidian_translation:',objEng_IL_dravidian_translation)
                # print('objSubwordEngmulti_dravidian_translation:',objSubwordEngmulti_dravidian_translation)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_dravidian_translation,objSubwordEngmulti_dravidian_translation,delimiter,nOptions)
               
            
            elif tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_dravidian_translation,objSubwordEngmulti_dravidian_translation,delimiter,nOptions)
                # print(op)



            elif tgtLang=='kan-knda':
                # ip_text= ip_text.lower()
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_dravidian_translation,objSubwordEngmulti_dravidian_translation,delimiter,nOptions)
                # print(op)

                # logger_engkan.setLevel(logging.INFO)
                # fhandler_engkan.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engkan = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engkan.setFormatter(fformat_engkan)
                # # Add handlers to the logger
                # logger_engkan.addHandler(fhandler_engkan)
                # logger_engkan.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engkan.flush()



            elif tgtLang=='asm-beng':
                # ip_text= ip_text.lower()
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engasm.setLevel(logging.INFO)
                # fhandler_engasm.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engasm = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engasm.setFormatter(fformat_engasm)
                # # Add handlers to the logger
                # logger_engasm.addHandler(fhandler_engasm)
                # logger_engasm.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engasm.flush()



            elif tgtLang=='guj-gujr':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_mid_resource_translation,objSubwordEngmulti_mid_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engguj.setLevel(logging.INFO)
                # fhandler_engguj.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engguj = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engguj.setFormatter(fformat_engguj)
                # # Add handlers to the logger
                # logger_engguj.addHandler(fhandler_engguj)
                # logger_engguj.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engguj.flush()


            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_mid_resource_translation,objSubwordEngmulti_mid_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engory.setLevel(logging.INFO)
                # fhandler_engory.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engory = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engory.setFormatter(fformat_engory)
                # # Add handlers to the logger
                # logger_engory.addHandler(fhandler_engory)
                # logger_engory.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engory.flush()


            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_mid_resource_translation,objSubwordEngmulti_mid_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engpan.setLevel(logging.INFO)
                # fhandler_engpan.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engpan = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engpan.setFormatter(fformat_engpan)
                # # Add handlers to the logger
                # logger_engpan.addHandler(fhandler_engpan)
                # logger_engpan.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engpan.flush()


            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_dravidian_translation,objSubwordEngmulti_dravidian_translation,delimiter,nOptions)
                # print(op)

                # logger_engtel.setLevel(logging.INFO)
                # fhandler_engtel.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engtel = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engtel.setFormatter(fformat_engtel)
                # # Add handlers to the logger
                # logger_engtel.addHandler(fhandler_engtel)
                # logger_engtel.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engtel.flush()


            elif tgtLang=='hin-tourism':
                # print('inside hin tourism')
                # print('ip_text at load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_hintourism_translation,objSubwordEngHintourism_translation,delimiter,nOptions)
                # print(op)

                # logger_enghintourism.setLevel(logging.INFO)
                # fhandler_enghintourism.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_enghintourism = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_enghintourism.setFormatter(fformat_enghintourism)
                # # Add handlers to the logger
                # logger_enghintourism.addHandler(fhandler_enghintourism)
                # logger_enghintourism.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_enghintourism.flush()

            elif tgtLang=='brx-deva':
                # print('inside eng-bodo translation')
                # print('ip_text at load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engbrx.setLevel(logging.INFO)
                # fhandler_engbrx.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engbrx = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engbrx.setFormatter(fformat_engbrx)
                # # Add handlers to the logger
                # logger_engbrx.addHandler(fhandler_engbrx)
                # logger_engbrx.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engbrx.flush()

            elif tgtLang=='mni-beng':
                # print('inside eng-manipuri translation')
                # print('ip_text at load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)
                # print(op)

                # logger_engmni.setLevel(logging.INFO)
                # fhandler_engmni.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_engmni = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_engmni.setFormatter(fformat_engmni)
                # # Add handlers to the logger
                # logger_engmni.addHandler(fhandler_engmni)
                # logger_engmni.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_engmni.flush()

            elif tgtLang == 'urd-arab':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_mid_resource_translation,objSubwordEngmulti_mid_resource_translation,delimiter,nOptions)

            elif tgtLang == 'knn-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'dgo-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'kas-arab':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'mai-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'npi-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'san-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'sat-olck':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'snd-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'kas-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)

            elif tgtLang == 'mni-mtei':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_low_resource_translation,objSubwordEngmulti_low_resource_translation,delimiter,nOptions)


            elif tgtLang == 'hin-deva-legal':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_hinLegal_translation,objSubwordEngmulti_translation,delimiter,nOptions)


            elif tgtLang == 'hin-deva-gov':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_domain_translation,objSubwordEngmulti_translation,delimiter,nOptions)


            elif tgtLang == 'mar-deva-gov':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_domain_translation,objSubwordEngmulti_translation,delimiter,nOptions)


            elif tgtLang == 'kan-knda-gov':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_domain_translation,objSubwordEngmulti_translation,delimiter,nOptions)

            elif tgtLang == 'guj-gujr-gov':
                # logger_enghin.setLevel(logging.INFO)
                # print('ip_text load:',ip_text)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_domain_translation,objSubwordEngmulti_translation,delimiter,nOptions)






        elif tgtLang == 'eng-latn':

            if srcLang == 'hin-deva':
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objmultiEng_translation,objSubwordmultiEng_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)
                # logger_hineng.setLevel(logging.INFO)
                # fhandler_hineng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_hineng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_hineng.setFormatter(fformat_hineng)
                # # Add handlers to the logger
                # logger_hineng.addHandler(fhandler_hineng)
                # logger_hineng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_hineng.flush()

            elif srcLang == 'mar-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)

                # logger_mareng.setLevel(logging.INFO)
                # fhandler_mareng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_mareng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_mareng.setFormatter(fformat_mareng)
                # # Add handlers to the logger
                # logger_mareng.addHandler(fhandler_mareng)
                # logger_mareng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_mareng.flush()

            elif srcLang == 'ben-beng':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)

                # logger_beneng.setLevel(logging.INFO)
                # fhandler_beneng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_beneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_beneng.setFormatter(fformat_beneng)
                # # Add handlers to the logger
                # logger_beneng.addHandler(fhandler_beneng)
                # logger_beneng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_beneng.flush()

            elif srcLang == 'guj-gujr':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_mid_resource_translation,objSubwordmultiEng_mid_resource_translation,delimiter,nOptions)
                # fhandler_gujeng.setLevel(logging.ERROR)
                # # Create formatters and add it to handlers
                # fformat_gujeng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_gujeng.setFormatter(fformat_gujeng)
                # # Add handlers to the logger
                # logger_gujeng.addHandler(fhandler_gujeng)
                # logger_gujeng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_gujeng.flush()

            elif srcLang == 'tam-taml':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_darvidian_translation,objSubwordmultiEng_dravidian_translation,delimiter,nOptions)

                # logger_tameng.setLevel(logging.INFO)
                # fhandler_tameng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_tameng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_tameng.setFormatter(fformat_tameng)
                # # Add handlers to the logger
                # logger_tameng.addHandler(fhandler_tameng)
                # logger_tameng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_tameng.flush()

            elif srcLang == 'mal-mlym':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_darvidian_translation,objSubwordmultiEng_dravidian_translation,delimiter,nOptions)

                # logger_maleng.setLevel(logging.INFO)
                # fhandler_maleng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_maleng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_maleng.setFormatter(fformat_maleng)
                # # Add handlers to the logger
                # logger_maleng.addHandler(fhandler_maleng)
                # logger_maleng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_maleng.flush()

            elif srcLang == 'kan-knda':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_darvidian_translation,objSubwordmultiEng_dravidian_translation,delimiter,nOptions)

                # logger_kaneng.setLevel(logging.INFO)
                # fhandler_kaneng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_kaneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_kaneng.setFormatter(fformat_kaneng)
                # # Add handlers to the logger
                # logger_kaneng.addHandler(fhandler_kaneng)
                # logger_kaneng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_kaneng.flush()

            elif srcLang == 'asm-beng':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

                # logger_asmeng.setLevel(logging.INFO)
                # fhandler_asmeng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_asmeng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_asmeng.setFormatter(fformat_asmeng)
                # # Add handlers to the logger
                # logger_asmeng.addHandler(fhandler_asmeng)
                # logger_asmeng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_asmeng.flush()

            elif srcLang == 'ory-orya':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_mid_resource_translation,objSubwordmultiEng_mid_resource_translation,delimiter,nOptions)

                # logger_oryeng.setLevel(logging.INFO)
                # fhandler_oryeng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_oryeng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_oryeng.setFormatter(fformat_oryeng)
                # # Add handlers to the logger
                # logger_oryeng.addHandler(fhandler_oryeng)
                # logger_oryeng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_oryeng.flush()

            elif srcLang == 'pan-guru':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_mid_resource_translation,objSubwordmultiEng_mid_resource_translation,delimiter,nOptions)

                # logger_paneng.setLevel(logging.INFO)
                # fhandler_paneng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_paneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_paneng.setFormatter(fformat_paneng)
                # # Add handlers to the logger
                # logger_paneng.addHandler(fhandler_paneng)
                # logger_paneng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_paneng.flush()

            elif srcLang == 'tel-telu':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_darvidian_translation,objSubwordmultiEng_dravidian_translation,delimiter,nOptions)

                # logger_teleng.setLevel(logging.INFO)
                # fhandler_teleng.setLevel(logging.INFO)
                # # Create formatters and add it to handlers
                # fformat_teleng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
                # fhandler_teleng.setFormatter(fformat_teleng)
                # # Add handlers to the logger
                # logger_teleng.addHandler(fhandler_teleng)
                # logger_teleng.info(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
                # fhandler_teleng.flush()
            elif srcLang == 'urd-arab':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_mid_resource_translation,objSubwordmultiEng_mid_resource_translation,delimiter,nOptions)

            elif srcLang == 'brx-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'mni-beng':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'knn-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'dgo-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'kas-arab':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'mai-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'npi-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'san-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'sat-olck':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            
            elif srcLang == 'kas-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'mni-mtei':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)

            elif srcLang == 'snd-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_low_resource_translation,objSubwordmultiEng_low_resource_translation,delimiter,nOptions)


            elif srcLang == 'hin-deva-legal':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objhin_EngLegal_translation,objSubwordmultiEng_translation,delimiter,nOptions)

            elif srcLang == 'hin-deva-gov':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_domain_translation,objSubwordmultiEng_translation,delimiter,nOptions)

            elif srcLang == 'mar-deva-gov':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_domain_translation,objSubwordmultiEng_translation,delimiter,nOptions)

            elif srcLang == 'kan-knda-gov':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_domain_translation,objSubwordmultiEng_translation,delimiter,nOptions)

            elif srcLang == 'guj-gujr-gov':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_domain_translation,objSubwordmultiEng_translation,delimiter,nOptions)



        else:
            op = "Currently this web service is not supporting"


        # print('op1:',op)
        return(op)
