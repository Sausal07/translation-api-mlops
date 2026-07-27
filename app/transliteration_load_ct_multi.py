# from translate import initModel as model_bi_directional_translate   
from transliteration_ct_multi import get_translate as bi_directional_translate
import os
import logging
import ctranslate2
from subWordNMT import initSubWordModel
from searchInTransliterationDic import Trie
import string


objEngmulti_transliteration = None
objmultiEng_transliteration = None
Eng_Hin_Trie = None
Hin_Eng_Trie = None

# fengmultilog = None


ip_client = None


def initModeltransliteration():

        global objEngmulti_transliteration
        global objmultiEng_transliteration
        global Eng_Hin_Trie
        global Hin_Eng_Trie
        global Mar_Eng_Trie

        objEngmulti_transliteration = ctranslate2.Translator("./ctranslate2_transliteration/Eng_Indic_Transliteration/eng_indic_ct2_150000", device="cuda")#,intra_threads=32)  # or "cuda" for GPU
        objmultiEng_transliteration = ctranslate2.Translator("./ctranslate2_transliteration/Indic_Eng_Transliteration/indic_eng_ct2_100000", device="cuda")#,intra_threads=32)  # or "cuda" for GPU

        # global fenghinlog
        # global logger_enghin
        # global fhandler_enghin
        

        # logger_enghin = logging.getLogger('enghin')
       
        # fhandler_enghin = logging.FileHandler('./Transliteration_logs_ct_multi/eng_hin.log',mode ='a+',encoding ='UTF-8')
        # code added by Neha Gupta on 12 Dec 2024
        Eng_Hin_Trie = Trie()
        Eng_Hin_Trie.Load_Trie("./TransliterationDictionaries/hn.txt")
        Hin_Eng_Trie = Trie()
        Hin_Eng_Trie.Load_Trie("./TransliterationDictionaries/hn.txt",True)
        Mar_Eng_Trie = Trie()
        Mar_Eng_Trie.Load_Trie("./TransliterationDictionaries/mr.txt")
               
        global objSubwordEngmulti_transliteration
        global objSubwordmultiEng_transliteration
       

        #codes files  Bengali, Tamil, Malayalam, Kannada, Gujaratti, Punjabi, Telugu
        objSubwordEngmulti_transliteration = initSubWordModel('./ctranslate2_transliteration/Eng_Indic_Transliteration/codes_file_eng_indic_ct2_150000_EN')
        objSubwordmultiEng_transliteration = initSubWordModel('./ctranslate2_transliteration/Indic_Eng_Transliteration/codes_file_indic_eng_ct2_100000_IL')        

        global punctList
        with open("punct.txt",'r',encoding='utf-8') as fPunct:
                punctList = fPunct.read().replace('\r\n','\n').split('\n')
                punctList.append(' ')
                # print(punctList)  



        #logs

        global fenghinlog
        global fhinenglog
        global fengmarlog
        global fmarenglog
        global fengbenlog
        global fbenenglog
        global fenggujlog
        global fgujenglog
        global fengtamlog
        global ftamenglog
        global fengmallog
        global fmalenglog
        global fengkanlog
        global fkanenglog
        global fengpunlog
        global fpunenglog
        global fengtellog
        global ftelenglog

        # global f_handler
     

        global logger_engmar
        global logger_enghin
        global logger_engben
        global logger_engguj
        global logger_engtam
        global logger_engmal
        global logger_hineng
        global logger_mareng
        global logger_beneng
        global logger_gujeng
        global logger_tameng
        global logger_maleng
        global logger_engkan
        global logger_kaneng
        global logger_engpun
        global logger_puneng
        global logger_engtel
        global logger_teleng

        
        global fhandler_engmar
        global fhandler_enghin
        global fhandler_engben
        global fhandler_engguj
        global fhandler_engtam
        global fhandler_engmal
        global fhandler_hineng
        global fhandler_mareng
        global fhandler_beneng
        global fhandler_gujeng
        global fhandler_tameng
        global fhandler_maleng
        global fhandler_engkan
        global fhandler_kaneng
        global fhandler_engpun
        global fhandler_puneng
        global fhandler_engtel
        global fhandler_teleng


        

        logger_enghin = logging.getLogger('enghin')
        logger_engmar = logging.getLogger('engmar')
        logger_engben = logging.getLogger('engben')
        logger_engguj = logging.getLogger('engguj')
        logger_engtam = logging.getLogger('engtam')
        logger_engmal = logging.getLogger('engmal')
        logger_hineng = logging.getLogger('hineng')
        logger_mareng = logging.getLogger('mareng')
        logger_beneng = logging.getLogger('beneng')
        logger_gujeng = logging.getLogger('gujeng')
        logger_tameng = logging.getLogger('tameng')
        logger_maleng = logging.getLogger('maleng')
        logger_engkan = logging.getLogger('engkan')
        logger_kaneng = logging.getLogger('kaneng')
        logger_engpun = logging.getLogger('engpun')
        logger_puneng = logging.getLogger('puneng')
        logger_engtel = logging.getLogger('engtel')
        logger_teleng = logging.getLogger('teleng')




        fhandler_engmar = logging.FileHandler('./Transliteration_logs_ct_multi/eng_mar.log',mode ='a+',encoding ='UTF-8')
        fhandler_enghin = logging.FileHandler('./Transliteration_logs_ct_multi/eng_hin.log',mode ='a+',encoding ='UTF-8')
        fhandler_engben = logging.FileHandler('./Transliteration_logs_ct_multi/eng_ben.log',mode ='a+',encoding ='UTF-8')
        fhandler_engguj = logging.FileHandler('./Transliteration_logs_ct_multi/eng_guj.log',mode ='a+',encoding ='UTF-8')
        fhandler_engtam = logging.FileHandler('./Transliteration_logs_ct_multi/eng_tam.log',mode ='a+',encoding ='UTF-8')
        fhandler_engmal = logging.FileHandler('./Transliteration_logs_ct_multi/eng_mal.log',mode ='a+',encoding ='UTF-8')
        fhandler_hineng = logging.FileHandler('./Transliteration_logs_ct_multi/hin_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_mareng = logging.FileHandler('./Transliteration_logs_ct_multi/mar_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_beneng = logging.FileHandler('./Transliteration_logs_ct_multi/ben_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_gujeng = logging.FileHandler('./Transliteration_logs_ct_multi/guj_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_tameng = logging.FileHandler('./Transliteration_logs_ct_multi/tam_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_maleng = logging.FileHandler('./Transliteration_logs_ct_multi/mal_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_engkan = logging.FileHandler('./Transliteration_logs_ct_multi/eng_kan.log',mode ='a+',encoding ='UTF-8')
        fhandler_kaneng = logging.FileHandler('./Transliteration_logs_ct_multi/kan_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_engpun = logging.FileHandler('./Transliteration_logs_ct_multi/eng_pun.log',mode ='a+',encoding ='UTF-8')
        fhandler_puneng = logging.FileHandler('./Transliteration_logs_ct_multi/pun_eng.log',mode ='a+',encoding ='UTF-8')
        fhandler_engtel = logging.FileHandler('./Transliteration_logs_ct_multi/eng_tel.log',mode ='a+',encoding ='UTF-8')
        fhandler_teleng = logging.FileHandler('./Transliteration_logs_ct_multi/tel_eng.log',mode ='a+',encoding ='UTF-8')

                
def pass_variable_ct(ip):
        global ip_client
        ip_client = ip  
        print(ip_client)  
        print('==================================')  



def returnTransliterationLine(input_text,srcLang,tgtLang,objTransliteration,objSubword_transliteration,nOptions,objTransliterationDic):
    print('inside returnTransliterationLine')
    print('input_text:',input_text)
    wordForTransliteration=""
    strOutputTransliteration=""
    delimiter=""
    input_text = input_text.replace('\'','')
    input_text = input_text.replace('’','')
    # print('transliteration input: {} , len of punctList {}'.format(input_text,len(punctList)))

    for cTransliteration in input_text:
        # print('cTransliteration:',cTransliteration)
        if cTransliteration in punctList or cTransliteration in string.punctuation:
            if wordForTransliteration!="":
                # print('wordForTransliteration' + wordForTransliteration)
                strOutputTransliteration=strOutputTransliteration+bi_directional_translate(wordForTransliteration,srcLang,tgtLang,objTransliteration,objSubword_transliteration,nOptions,objTransliterationDic)
                wordForTransliteration = ""
                # print('strOutputTransliteration:',strOutputTransliteration)
            strOutputTransliteration = strOutputTransliteration+cTransliteration
        else:
            wordForTransliteration = wordForTransliteration+cTransliteration

    # print('strOutputTransliteration:',strOutputTransliteration)
    if wordForTransliteration!="":
        # print('wordForTransliteration' + wordForTransliteration)
        strOutputTransliteration=strOutputTransliteration+bi_directional_translate(wordForTransliteration,srcLang,tgtLang,objTransliteration,objSubword_transliteration, nOptions,objTransliterationDic)
    
    print('strOutputTransliteration:',strOutputTransliteration)
    return strOutputTransliteration   


def transliteration_model_ct_multi(ip_text,srcLang,tgtLang,nOptions):
    print("==========================================================")
    # print(lang_id)
    # print(ip_text)
    lang_supp = ['asm-beng','ben-beng','brx-deva','guj-gujr','hin-deva','kan-knda','kas-arab','knn-deva','mai-deva','mal-mlym','mar-deva','npi-deva','ory-orya','pan-guru','san-deva','snd-arab','tam-taml','tel-telu']

    # print('ip_text:',ip_text)
    if tgtLang in lang_supp:
        if tgtLang == 'hin-deva':
            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,Eng_Hin_Trie)
            # print('inside eng-hin transliteration')
            # print('op:',op)
            fhandler_enghin.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_enghin = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_enghin.setFormatter(fformat_enghin)
            # Add handlers to the logger
            logger_enghin.addHandler(fhandler_enghin)
            logger_enghin.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_enghin.flush()
            # print('op_final:',op)

        elif tgtLang == 'mar-deva':
            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)

            fhandler_engmar.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engmar = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engmar.setFormatter(fformat_engmar)
            # Add handlers to the logger
            logger_engmar.addHandler(fhandler_engmar)
            logger_engmar.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engmar.flush()

        elif tgtLang == 'ben-beng':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)
                            # print('op:',op)
                            # print('after all operations')

            fhandler_engben.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engben = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engben.setFormatter(fformat_engben)
            # Add handlers to the logger
            logger_engben.addHandler(fhandler_engben)
            logger_engben.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engben.flush()


        elif tgtLang == 'guj-gujr':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)
            print('inside eng-guj')
            print('op:',op)
            fhandler_engguj.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engguj = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engguj.setFormatter(fformat_engguj)
            # Add handlers to the logger
            logger_engguj.addHandler(fhandler_engguj)
            logger_engguj.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engguj.flush()

        elif tgtLang == 'tam-taml':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)

            fhandler_engtam.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engtam = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engtam.setFormatter(fformat_engtam)
            # Add handlers to the logger
            logger_engtam.addHandler(fhandler_engtam)
            logger_engtam.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engtam.flush()

        elif tgtLang == 'mal-mlym':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)
                    #         print(op)
            fhandler_engmal.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engmal = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engmal.setFormatter(fformat_engmal)
            # Add handlers to the logger
            logger_engmal.addHandler(fhandler_engmal)
            logger_engmal.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engmal.flush()

        elif tgtLang == 'kan-knda':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)
                    #         # print(op)

            fhandler_engkan.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engkan = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engkan.setFormatter(fformat_engkan)
            # Add handlers to the logger
            logger_engkan.addHandler(fhandler_engkan)
            logger_engkan.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engkan.flush()


        elif tgtLang == 'pan-guru':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)
    #         # print(op)
            fhandler_engpun.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engpun = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engpun.setFormatter(fformat_engpun)
            # Add handlers to the logger
            logger_engpun.addHandler(fhandler_engpun)
            logger_engpun.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engpun.flush()


        elif tgtLang == 'tel-telu':

            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)

            fhandler_engtel.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_engtel = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_engtel.setFormatter(fformat_engtel)
            # Add handlers to the logger
            logger_engtel.addHandler(fhandler_engtel)
            logger_engtel.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_engtel.flush()

        else:
            # print('elseee')
            op =  returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objEngmulti_transliteration,objSubwordEngmulti_transliteration,nOptions,None)

    elif tgtLang == 'eng-latn' and srcLang in lang_supp:
        if srcLang == 'hin-deva':
            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,Hin_Eng_Trie)

            fhandler_hineng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_hineng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_hineng.setFormatter(fformat_hineng)
            # Add handlers to the logger
            logger_hineng.addHandler(fhandler_hineng)
            logger_hineng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_hineng.flush()

        elif srcLang == 'mar-deva':
            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,Mar_Eng_Trie)

            fhandler_mareng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_mareng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_mareng.setFormatter(fformat_mareng)
            # Add handlers to the logger
            logger_mareng.addHandler(fhandler_mareng)
            logger_mareng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_mareng.flush()

        elif srcLang == 'ben-beng':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)
            # print('after all processing')
            fhandler_beneng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_beneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_beneng.setFormatter(fformat_beneng)
            # Add handlers to the logger
            logger_beneng.addHandler(fhandler_beneng)
            logger_beneng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_beneng.flush()

        elif srcLang == 'guj-gujr':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)
            fhandler_gujeng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_gujeng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_gujeng.setFormatter(fformat_gujeng)
            # Add handlers to the logger
            logger_gujeng.addHandler(fhandler_gujeng)
            logger_gujeng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_gujeng.flush()

        elif srcLang == 'tam-taml':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)

            fhandler_tameng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_tameng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_tameng.setFormatter(fformat_tameng)
            # Add handlers to the logger
            logger_tameng.addHandler(fhandler_tameng)
            logger_tameng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_tameng.flush()

        elif srcLang == 'mal-mlym':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)

            fhandler_maleng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_maleng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_maleng.setFormatter(fformat_maleng)
            # Add handlers to the logger
            logger_maleng.addHandler(fhandler_maleng)
            logger_maleng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_maleng.flush()

        elif srcLang == 'kan-knda':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)

            fhandler_kaneng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_kaneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_kaneng.setFormatter(fformat_kaneng)
            # Add handlers to the logger
            logger_kaneng.addHandler(fhandler_kaneng)
            logger_kaneng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_kaneng.flush()

        elif srcLang == 'pan-guru':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)

            fhandler_puneng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_puneng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_puneng.setFormatter(fformat_puneng)
            # Add handlers to the logger
            logger_puneng.addHandler(fhandler_puneng)
            logger_puneng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_puneng.flush()

        elif srcLang =='tel-telu':

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)

            fhandler_teleng.setLevel(logging.ERROR)
            # Create formatters and add it to handlers
            fformat_teleng = logging.Formatter('INFO_Date = %(asctime)s \n%(message)s')
            fhandler_teleng.setFormatter(fformat_teleng)
            # Add handlers to the logger
            logger_teleng.addHandler(fhandler_teleng)
            logger_teleng.error(f'INFO_ip = {ip_client} \nINFO_Input = {ip_text} \nINFO_op = {op}')
            fhandler_teleng.flush()

        else:

            op = returnTransliterationLine(ip_text.strip(),srcLang,tgtLang,objmultiEng_transliteration,objSubwordmultiEng_transliteration,nOptions,None)
    else:
        op = "Currently this web service is not supporting"
    print('op1:',op)
    return(op)
