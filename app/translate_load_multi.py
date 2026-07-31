# from translate import initModel as model_bi_directional_translate   
from .translate_multi import get_translate as bi_directional_translate
from .translate_multi import expand_abbreviations
import os
import json
import re
import logging
from pathlib import Path
import ctranslate2
from .subWordNMT import initSubWordModel
from .Transliteration_RuleBased import GenericTransliteration
from .transliteration_load_ct_multi import returnTransliterationLine

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

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Translation_Models"
BPE_DIR = BASE_DIR / "BPE_Models"



# fengmultilog = None


# ip_client = None


def initModeltranslation():

        global objEngmulti_translation
        global objmultiEng_translation
        global objEng_hintourism_translation
        global objEngBodo_translation
        global objEngManipuri_translation
        global objEng_hinLegal_translation
        global objhin_EngLegal_translation
        global objEng_IL_domain_translation
        global objIL_Eng_domain_translation

        global objEng_IL_high_resource_translation
        global objEng_IL_mid_resource_translation
        global objEng_IL_dravidian_translation
        global objIL_Eng_high_resource_translation
        global objIL_Eng_mid_resource_translation
        global objIL_Eng_darvidian_translation
        global objEng_IL_low_resource_translation
        global objIL_Eng_low_resource_translation


        # objEngmulti_translation = ctranslate2.Translator("./Translation_Models/en_il_ct2_model_400000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objmultiEng_translation = ctranslate2.Translator("./Translation_Models/il_en_ct2_model_220000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objEng_hintourism_translation = ctranslate2.Translator("./Translation_Models/ct2_model_tourism_404000", device="cpu")#,intra_threads=32)  # or "cuda" for GPU
        # objEngBodo_translation = ctranslate2.Translator("./Translation_Models/en_brx_372000_ctranslate2", device="cpu")
        # objEngManipuri_translation = ctranslate2.Translator("./Translation_Models/en_mni_194000_ctranslate2", device="cpu")
        # # objEng_hinLegal_translation = ctranslate2.Translator("./Translation_Models/en_hi_legal", device="cpu")
        # # objhin_EngLegal_translation = ctranslate2.Translator("./Translation_Models/hi_en_legal", device="cpu")
        # objEng_IL_domain_translation = ctranslate2.Translator("./Translation_Models/en_il_gov_domain", device="cpu")
        # objIL_Eng_domain_translation = ctranslate2.Translator("./Translation_Models/il_en_gov_domain", device="cpu")

        objEng_IL_high_resource_translation = ctranslate2.Translator(str(MODEL_DIR / "en-il-high-resource"), device="cpu")
        # objEng_IL_mid_resource_translation = ctranslate2.Translator("./Translation_Models/en-il-mid-resource", device="cpu")
        # objEng_IL_dravidian_translation = ctranslate2.Translator("./Translation_Models/en-il-dravidian", device="cpu")
        # objEng_IL_low_resource_translation = ctranslate2.Translator("./Translation_Models/en-il-low-resource", device="cpu")
        objIL_Eng_high_resource_translation = ctranslate2.Translator(str(MODEL_DIR / "il-en-high-resource"), device="cpu")
        # objIL_Eng_mid_resource_translation = ctranslate2.Translator("./Translation_Models/il-en-mid-resource", device="cpu")
        # objIL_Eng_darvidian_translation = ctranslate2.Translator("./Translation_Models/il-en-dravidian", device="cpu")
        # objIL_Eng_low_resource_translation = ctranslate2.Translator("./Translation_Models/il-en-low-resource", device="cpu")
        # print('objhin_EngLegal_translation:',objhin_EngLegal_translation)
        # global fenghinlog
        # global logger_enghin
        # global fhandler_enghin
        

        # logger_enghin = logging.getLogger('enghin')
       
        # fhandler_enghin = logging.FileHandler('./Transliteration_logs_ct/eng_hin.log',mode ='a+',encoding ='UTF-8')
       
        
        global objSubwordEngmulti_translation
        global objSubwordmultiEng_translation
        global objSubwordEngHintourism_translation
        global objSubwordEngBodo_translation
        global objSubwordEngManipuri_translation

        global objSubwordEngmulti_high_resource_translation
        global objSubwordEngmulti_mid_resource_translation
        global objSubwordEngmulti_dravidian_translation
        global objSubwordmultiEng_high_resource_translation
        global objSubwordmultiEng_mid_resource_translation
        global objSubwordmultiEng_dravidian_translation
        global objSubwordEngmulti_low_resource_translation
        global objSubwordmultiEng_low_resource_translation

        #codes files  Bengali, Tamil, Malayalam, Kannada, Gujaratti, Punjabi, Telugu
        # objSubwordEngmulti_translation = initSubWordModel('./BPE_Models/codes_file_en_il')
        # objSubwordmultiEng_translation = initSubWordModel('./BPE_Models/codes_file_il_en')        
        # objSubwordEngHintourism_translation = initSubWordModel('./BPE_Models/codes_file_en_tourism')
        # objSubwordEngBodo_translation = initSubWordModel('./BPE_Models/codes_file_br')
        # objSubwordEngManipuri_translation = initSubWordModel('./BPE_Models/codes_file_mn')

        objSubwordEngmulti_high_resource_translation = initSubWordModel(str(BPE_DIR / "codes_file_en_il_high_resource"))
        # objSubwordEngmulti_mid_resource_translation = initSubWordModel('./BPE_Models/codes_file_en_il_mid_resource')
        # objSubwordEngmulti_dravidian_translation = initSubWordModel('./BPE_Models/codes_file_en_il_Dravidian')
        # objSubwordEngmulti_low_resource_translation = initSubWordModel('./BPE_Models/codes_file_en_il_low_resource')
        objSubwordmultiEng_high_resource_translation = initSubWordModel(str(BPE_DIR / "codes_file_il_en_high_resource"))
        # objSubwordmultiEng_mid_resource_translation = initSubWordModel('./BPE_Models/codes_file_il_en_mid_resource')
        # objSubwordmultiEng_dravidian_translation = initSubWordModel('./BPE_Models/dravidian_reverse_bpe')
        # objSubwordmultiEng_low_resource_translation = initSubWordModel('./BPE_Models/codes_file_il_en_low_resource')


        # for marthi modi transliteration when you do english to modi translation
        # global punctList
        # with open("punct.txt",'r',encoding='utf-8') as fPunct:
        #         punctList = fPunct.read().replace('\r\n','\n').split('\n')
        #         punctList.append(' ')
        #         # print(punctList) 

        # global objMarModiRuleTrans
        # objMarModiRuleTrans = GenericTransliteration()
        # objMarModiRuleTrans.loadDictionaries("./genericTrans/marathi2modi.rul","punct.txt") 


        global GLOSSARY_LOOKUP
        global ABBREVIATIONS
        global GLOSSARY

        GLOSSARY_FILE = "./app/glossary.json"
        ABBREVIATION_FILE = "./app/abbrevations.txt"

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


            elif tgtLang == 'mar-deva' or tgtLang == 'mar-modi':
                # logger_level = logger_engmar.level
                # print('logger_level:',logger_level)
                # print('objSubwordEngmulti_translation:',objSubwordEngmulti_translation)
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                # print('op of eng_mar translation:',op)
                # if tgtLang == 'mar-modi':
                #     # print('inside eng-modi translation')
                #     # op =  bi_directional_translate(ip_text.strip(),srcLang,'mar-deva',objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                #     op =  bi_directional_translate(ip_text.strip(),srcLang,'mar-deva',objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)
                #     # print('op of eng_mar translation:',op)
                #     if op!='':
                #         # print('op of eng_mar translation:',op)
                #         op = objMarModiRuleTrans.returnTransliterationLine(op.strip())
                       
                # else:

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)
            


            elif tgtLang=='ben-beng':
                # ip_text= ip_text.lower()
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEngmulti_translation,objSubwordEngmulti_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objEng_IL_high_resource_translation,objSubwordEngmulti_high_resource_translation,delimiter,nOptions)





        elif tgtLang == 'eng-latn':

            if srcLang == 'hin-deva':
                # op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objmultiEng_translation,objSubwordmultiEng_translation,delimiter,nOptions)
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)
               
            elif srcLang == 'mar-deva':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)


            elif srcLang == 'ben-beng':
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_high_resource_translation,objSubwordmultiEng_high_resource_translation,delimiter,nOptions)

            elif srcLang == 'guj-gujr':

                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objIL_Eng_mid_resource_translation,objSubwordmultiEng_mid_resource_translation,delimiter,nOptions)
                

         

        else:
            op = "Currently this web service is not supporting"


        # print('op1:',op)
        return(op)
