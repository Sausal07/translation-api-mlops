# from translate import initModel as model_bi_directional_translate   
from .translate_multi import get_translate as bi_directional_translate
import os
import logging
import ctranslate2
from .subWordNMT import initSubWordModel
from pathlib import Path


objILIL_translation = None
objSubwordILIL_translation =None

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Translation_Models"
BPE_DIR = BASE_DIR / "BPE_Models"
# fengmultilog = None


# ip_client = None


def initModeltranslation():

        global objILIL_translation

        objILIL_translation = ctranslate2.Translator(str(MODEL_DIR / "il_2_il_model"), device="cpu")#,intra_threads=32)  # or "cuda" for GPU
       
        
        global objSubwordILIL_translation

        #codes files  Bengali, Tamil, Malayalam, Kannada, Gujaratti, Punjabi, Telugu
        objSubwordILIL_translation = initSubWordModel(str(BPE_DIR / "codes_file_il_2_il"))      
                


# def pass_variable(ip):
#         global ip_client
#         ip_client = ip  
#         print(ip_client)  
#         print('==================================')  



def translation_model_ILIL(ip_text,srcLang,tgtLang,delimiter,nOptions):
        # print("inside translation_model_multi")
        # print("==========================================================")
        # print(lang_id)
        # print(ip_text)
        if srcLang == 'asm-beng':

            if tgtLang == 'ben-beng':
                
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang == 'guj-gujr':
                
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang=='hin-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang=='kan-knda':
                # print("inside tamil: input {}".format(ip_text))
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
            
            elif tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"
          

        elif srcLang == 'ben-beng':

            if tgtLang == 'guj-gujr':
                
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang=='hin-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang=='kan-knda':
                # print("inside tamil: input {}".format(ip_text))
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
            
            elif tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'guj-gujr':

            if tgtLang=='hin-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)

            elif tgtLang=='kan-knda':
                # print("inside tamil: input {}".format(ip_text))
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
            
            elif tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'hin-deva':

            if tgtLang=='kan-knda':
                # print("inside tamil: input {}".format(ip_text))
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
            
            elif tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'kan-knda':

            if tgtLang=='mal-mlym':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"



        elif srcLang == 'mal-mlym':

            if tgtLang=='mar-deva':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'mar-deva':

            if tgtLang=='ory-orya':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'ory-orya':

            if tgtLang=='pan-guru':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"


        elif srcLang == 'pan-guru':

            if tgtLang=='tam-taml':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)

            elif tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"

        elif srcLang == 'tam-taml':

            if tgtLang=='tel-telu':
                # ip_text= ip_text.lower()
                op =  bi_directional_translate(ip_text.strip(),srcLang,tgtLang,objILIL_translation,objSubwordILIL_translation,delimiter,nOptions)
                # print(op)
            else:
                op = "Currently this web service is not supporting"

        else:
            op = "Currently this web service is not supporting"


        # print('op1:',op)
        return(op)
