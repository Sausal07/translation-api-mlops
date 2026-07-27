# 
#  Copyright (c) Neha Gupta, C-DAC
#  All rights reserved.
# Last updated on 6th December 2021

## language codes 
# LC_TA='ta'

SCRIPT_RANGES={
                 'en-latn':[0x0021,0x007f] ,
                 'pan-guru':[0x0a00,0x0a7f] ,  
                 'guj-gujr':[0x0a80,0x0aff] ,  
                 'ory-orya':[0x0b00,0x0b7f] ,  
                 'tam-taml':[0x0b80,0x0bff] ,  
                 'tel-telu':[0x0c00,0x0c7f] ,  
                 'kan-knda':[0x0c80,0x0cff] ,  
                 'mal-mlym':[0x0d00,0x0d7f] ,  
                 'si':[0x0d80,0x0dff] ,  
                 'hin-deva':[0x0900,0x097f] ,  
                 'mar-deva':[0x0900,0x097f] ,   
                 'kK':[0x0900,0x097f] ,   
                 'sa':[0x0900,0x097f] ,   
                 'ne':[0x0900,0x097f] ,   
                 'sd':[0x0900,0x097f] ,  
                 'ben-beng':[0x0980,0x09ff] ,  
                 'as':[0x0980,0x09ff] ,  
              }

'''
english - ha added for hectare
'''
# here
ACRO_ABBR_RANGES={
                 'eng-latn':['Adj','Adm','Adv','Asst','Bart','Bldg','Brig','Bros','Capt','Cmdr','Col','Comdr','Con','Corp','Cpl','DR','Dr','Drs','Ens','Gen','Gov','Hon','Hr','Hosp','Insp','Lt','MM','MR','MRS','MS','Maj','Messrs','Mlle','Mme','Mr','Mrs','Ms','Msgr','Op','Ord','Pfc','Ph','Prof','Pvt','Rep','Reps','Res','Rev','Rt','Sen','Sens','Sfc','Sgt','Sr','St','Supt','Surg','Smt','Shri','Rs','Mon','Tues','Tue','Wed','Thu','Thurs','Fri','Sat','Sun','Jan','Feb','mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec','ff','Std','evtl','Ltd','spp','Co','Corp','etc','Rs','Miss','Ms','Govt','Vs','Dr','Prof','Smt','Sri','Mr','Dt','Lt','ml','KM','Km','ie','mg','KG','Kg','OK','Ok','Jr','Sr','No',"ha", "sq","approx","no","viz","e.g","w.e.f","m.v"], 
                 'pan-guru':[] ,
                 'guj-gujr':[] ,  
                 'ory-orya':[] ,  
                 'tam-taml':[] ,  
                 'tel-telu':[] ,  
                 'kan-knda':[] ,  
                 'mal-mlym':[] ,  
                 'si':[] ,  
                 'hin-deva':['श्री','डॉ','कु','चि','सौ','डॉ'] ,  
                 'mar-deva':[] ,   
                 'kK':[] ,   
                 'sa':[] ,   
                 'ne':[] ,   
                 'sd':[] ,  
                 'ben-beng':[] ,  
                 'as':[] ,  
              }
DRAVIDIAN_LANGUAGES=['tam-taml', 'tel-telu', 'kan-knda', 'mal-mlym',]
BRAHMI_LANGUAGES=['hin-deva', 'mar-deva', 'kK', 'sa', 'ne', 'sd', 'ben-beng', 'as', 'pan-guru', 'guj-gujr', 'ory-orya', 'si', ]
ARABIC_LANGUAGES=['ur', 'sn', 'ka' ]
#here
DANDA_DELIM_LANGUAGES=['as','ben-beng','hin-deva','ne','ory-orya','pan-guru','sa','sd']

URDU_RANGES=[
                [0x0600,0x06ff], 
                [0x0750,0x077f], 
                [0xfb50,0xfdff], 
                [0xfe70,0xfeff], 
            ]

COORDINATED_RANGE_START_INCLUSIVE=0
COORDINATED_RANGE_END_INCLUSIVE=0x6f

NUMERIC_OFFSET_START=0x66
NUMERIC_OFFSET_END=0x6f

HALANTA_OFFSET=0x4d
AUM_OFFSET=0x50
NUKTA_OFFSET=0x3c

RUPEE_SIGN=0x20b9

DANDA=0x0964
DOUBLE_DANDA=0x0965

#TODO: add missing fricatives and approximants
VELAR_RANGE=[0x15,0x19]
PALATAL_RANGE=[0x1a,0x1e]
RETROFLEX_RANGE=[0x1f,0x23]
DENTAL_RANGE=[0x24,0x29]
LABIAL_RANGE=[0x2a,0x2e]

# verify
VOICED_LIST=[0x17,0x18,0x1c,0x1d,0x21,0x22,0x26,0x27,0x2c,0x2d]
UNVOICED_LIST=[0x15,0x16,0x1a,0x1b,0x1f,0x20,0x24,0x25,0x2a,0x2b] #TODO: add sibilants/sonorants
ASPIRATED_LIST=[0x16,0x18,0x1b,0x1d,0x20,0x22,0x25,0x27,0x2b,0x2d]
UNASPIRATED_LIST=[0x15,0x17,0x1a,0x1c,0x1f,0x21,0x24,0x26,0x2a,0x2c]
NASAL_LIST=[0x19,0x1e,0x23,0x28,0x29,0x2d]
FRICATIVE_LIST=[0x36,0x37,0x38]
APPROXIMANT_LIST=[0x2f,0x30,0x31,0x32,0x33,0x34,0x35]

#TODO: ha has to be properly categorized 
def isAcroAbbr(lang):
    """
    Returns True if danda/double danda is a possible delimiter for the language
    """
    # print(ACRO_ABBR_RANGES[lang])
    return ACRO_ABBR_RANGES[lang]

def is_danda_delim(lang):
    """
    Returns True if danda/double danda is a possible delimiter for the language
    """
    return lang in DANDA_DELIM_LANGUAGES

def get_offset(c,lang): 
    """
    Applicable to Brahmi derived Indian scripts 
    """
    return ord(c)-SCRIPT_RANGES[lang][0]

def offset_to_char(c,lang): 
    """
    Applicable to Brahmi derived Indian scripts 
    """
    return chr(c+SCRIPT_RANGES[lang][0])

def in_coordinated_range(c_offset): 
    """
    Applicable to Brahmi derived Indian scripts 
    """
    return  (c_offset>=COORDINATED_RANGE_START_INCLUSIVE and c_offset<=COORDINATED_RANGE_END_INCLUSIVE) 
       
def is_Indianlang_char(c,lang): 
    """
    Applicable to Brahmi derived Indian scripts 
    """
    o=get_offset(c,lang)
    return (o>=0 and o<=0x7f) or ord(c)==DANDA or ord(c)==DOUBLE_DANDA

def is_vowel(c,lang): 
    """
    Is the character a vowel
    """
    o=get_offset(c,lang)
    return (o>=0x04 and o<=0x14) 

def is_vowel_sign(c,lang): 
    """
    Is the character a vowel sign (maatraa)
    """
    o=get_offset(c,lang)
    return (o>=0x3e and o<=0x4c) 

def is_halanta(c,lang): 
    """
    Is the character the halanta character
    """
    o=get_offset(c,lang)
    return (o==HALANTA_OFFSET) 

def is_nukta(c,lang): 
    """
    Is the character the halanta character
    """
    o=get_offset(c,lang)
    return (o==NUKTA_OFFSET) 

def is_aum(c,lang): 
    """
    Is the character a vowel sign (maatraa)
    """
    o=get_offset(c,lang)
    return (o==AUM_OFFSET)

def is_consonant(c,lang): 
    """
    Is the character a consonant
    """
    o=get_offset(c,lang)
    return (o>=0x15 and o<=0x39) 

def is_velar(c,lang): 
    """
    Is the character a velar
    """
    o=get_offset(c,lang)
    return (o>=VELAR_RANGE[0] and o<=VELAR_RANGE[1]) 

def is_palatal(c,lang): 
    """
    Is the character a palatal
    """
    o=get_offset(c,lang)
    return (o>=PALATAL_RANGE[0] and o<=PALATAL_RANGE[1]) 

def is_retroflex(c,lang): 
    """
    Is the character a retroflex
    """
    o=get_offset(c,lang)
    return (o>=RETROFLEX_RANGE[0] and o<=RETROFLEX_RANGE[1]) 

def is_dental(c,lang): 
    """
    Is the character a dental
    """
    o=get_offset(c,lang)
    return (o>=DENTAL_RANGE[0] and o<=DENTAL_RANGE[1]) 

def is_labial(c,lang): 
    """
    Is the character a labial
    """
    o=get_offset(c,lang)
    return (o>=LABIAL_RANGE[0] and o<=LABIAL_RANGE[1]) 

def is_voiced(c,lang): 
    """
    Is the character a voiced consonant
    """
    o=get_offset(c,lang)
    return o in VOICED_LIST

def is_unvoiced(c,lang): 
    """
    Is the character a unvoiced consonant
    """
    o=get_offset(c,lang)
    return o in UNVOICED_LIST

def is_aspirated(c,lang): 
    """
    Is the character a aspirated consonant
    """
    o=get_offset(c,lang)
    return o in ASPIRATED_LIST

def is_unaspirated(c,lang): 
    """
    Is the character a unaspirated consonant
    """
    o=get_offset(c,lang)
    return o in UNASPIRATED_LIST

def is_nasal(c,lang): 
    """
    Is the character a nasal consonant
    """
    o=get_offset(c,lang)
    return o in NASAL_LIST

def is_fricative(c,lang): 
    """
    Is the character a fricative consonant
    """
    o=get_offset(c,lang)
    return o in FRICATIVE_LIST

def is_approximant(c,lang): 
    """
    Is the character an approximant consonant
    """
    o=get_offset(c,lang)
    return o in APPROXIMANT_LIST

def is_number(c,lang): 
    """
    Is the character a number
    """
    o=get_offset(c,lang)
    return (o>=0x66 and o<=0x6f) 


##################################################

def is_vowel_offset(c_offset):
    """
    Is the offset a vowel
    """
    return (c_offset>=0x04 and c_offset<=0x14) 

def is_vowel_sign_offset(c_offset):
    """
    Is the offset a vowel sign (maatraa)
    """
    return (c_offset>=0x3e and c_offset<=0x4c) 

def is_halanta_offset(c_offset):
    """
    Is the offset the halanta offset
    """
    return (c_offset==HALANTA_OFFSET) 

def is_nukta_offset(c_offset):
    """
    Is the offset the halanta offset
    """
    return (c_offset==NUKTA_OFFSET) 

def is_aum_offset(c_offset):
    """
    Is the offset a vowel sign (maatraa)
    """
    return (c_offset==AUM_OFFSET)

def is_consonant_offset(c_offset):
    """
    Is the offset a consonant
    """
    return (c_offset>=0x15 and c_offset<=0x39) 

def is_velar_offset(c_offset):
    """
    Is the offset a velar
    """
    return (c_offset>=VELAR_RANGE[0] and c_offset<=VELAR_RANGE[1]) 

def is_palatal_offset(c_offset):
    """
    Is the offset a palatal
    """
    return (c_offset>=PALATAL_RANGE[0] and c_offset<=PALATAL_RANGE[1]) 

def is_retroflex_offset(c_offset):
    """
    Is the offset a retroflex
    """
    return (c_offset>=RETROFLEX_RANGE[0] and c_offset<=RETROFLEX_RANGE[1]) 

def is_dental_offset(c_offset):
    """
    Is the offset a dental
    """
    return (c_offset>=DENTAL_RANGE[0] and c_offset<=DENTAL_RANGE[1]) 

def is_labial_offset(c_offset):
    """
    Is the offset a labial
    """
    return (c_offset>=LABIAL_RANGE[0] and c_offset<=LABIAL_RANGE[1]) 

def is_voiced_offset(c_offset):
    """
    Is the offset a voiced consonant
    """
    return c_offset in VOICED_LIST

def is_unvoiced_offset(c_offset):
    """
    Is the offset a unvoiced consonant
    """
    return c_offset in UNVOICED_LIST

def is_aspirated_offset(c_offset):
    """
    Is the offset a aspirated consonant
    """
    return c_offset in ASPIRATED_LIST

def is_unaspirated_offset(c_offset):
    """
    Is the offset a unaspirated consonant
    """
    return c_offset in UNASPIRATED_LIST

def is_nasal_offset(c_offset):
    """
    Is the offset a nasal consonant
    """
    return c_offset in NASAL_LIST

def is_fricative_offset(c_offset):
    """
    Is the offset a fricative consonant
    """
    return c_offset in FRICATIVE_LIST

def is_approximant_offset(c_offset):
    """
    Is the offset an approximant consonant
    """
    return c_offset in APPROXIMANT_LIST

def is_number_offset(c_offset):
    """
    Is the offset a number
    """
    return (c_offset>=0x66 and c_offset<=0x6f) 
