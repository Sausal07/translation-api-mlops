# 
#  Copyright (c) 2013-present, Neha Gupta, C-DAC
#  All rights reserved.
# 

#Program for sentence splitting of Indian language input 
#
# @author Neha Gupta
#
"""
This code contains logic for Sentence splitting for Indian languages. It Contains a rule-based 
sentence splitter.
Last updated on 6th December 2021
"""

import re

import language_info


## for language which have danda as delimiter (Excluding Period)
DELIM_DANDA=re.compile(r'[\?!\u0964\u0965]')

## for languages which don't have danda as delimiter
DELIM_NO_DANDA=re.compile(r'[\.\?!\u0964\u0965]')

## pattern to check for presence of danda in text 
CONTAINS_DANDA=re.compile(r'[\u0964\u0965]')

fout= open('output.txt','w',encoding='utf-8')

def is_acronym_abbvr(text,lang):
	"""Is the text a non-breaking phrase

	Args:
		text (str): text to check for non-breaking phrase
		lang (str): ISO 639-2 language code

	Returns:
		boolean: true if `text` is a non-breaking phrase
	"""

	# print(text)
	# print(language_info.isAcroAbbr(lang))
	if text in language_info.isAcroAbbr(lang):
		# print('------------------------')
		return True
	else:
		return False


def sentence_split(text,lang,delim_info='auto'): ## New signature
	"""split the text into sentences

	A rule-based sentence splitter for Indian languages written in 
	Brahmi-derived scripts. The text is split at sentence delimiter 
	boundaries. The delimiters can be configured by passing appropriate
	parameters. 

	Args:
		text (str): text to split into sentence
		lang (str): ISO 639-2 language code
		delim_info (str): regular expression to identify sentence delimiter characters. If set to 'auto', the delimiter pattern is chosen automatically based on the language and text. 

	Returns:
		list: list of sentences identified from the input text 
	"""
	
	#print('Input: {}'.format(delim_info))
	if delim_info=='auto':
		if language_info.is_danda_delim(lang):
			# in modern texts it is possible that period is used as delimeter
			# instead of DANDA. Hence, a check. Use danda delimiter pattern
			# only if text contains at least one danda
			if CONTAINS_DANDA.search(text) is None:
				delim_info=DELIM_NO_DANDA
				#print('LANG has danda delim. TEXT_CONTAINS_DANDA: FALSE --> DELIM_NO_DANDA')
			else:
				delim_info=DELIM_DANDA
				#print('LANG has danda delim. TEXT_CONTAINS_DANDA: TRUE --> DELIM_DANDA')
		else:
			delim_info=DELIM_NO_DANDA
			#print('LANG has no danda delim --> DELIM_NO_DANDA')

	## otherwise, assume the caller set the delimiter pattern
	
	### Phase 1: break on sentence delimiters.
	cand_sentences=[]
	begin=0
	text = text.strip()
	text = text.replace("।.","।")
	if delim_info == DELIM_DANDA:
		for mo in delim_info.finditer(text):
			p1=mo.start()
			p2=mo.end()
			
			## NEW
			if p1>0 and text[p1-1].isnumeric() :
				continue

			end=p1+1
			s= text[begin:end].strip()
			if len(s)>0:
				cand_sentences.append(s)
			begin=p1+1

		s= text[begin:].strip()
		if len(s)>0:
			cand_sentences.append(s)
	else:
		s = ""
		bDelimFoundinEnd = False
		for word in text.split(' '):
			# print(word)
			if word!="":
				if bDelimFoundinEnd:
					bDelimFoundinEnd = False
				if delim_info.match(word[-1]):
					# print(len(word[:-1]))
					if is_acronym_abbvr(word[:-1],lang) or (word[:-1].isnumeric() and len(word[:-1])<3):
						s+=word+" "
					# elif is_acronym_abbvr(word[:-1],"hi") or (word[:-1].isnumeric() and len(word[:-1])<3):
					# 	s+=word+" "
						# print('else')
					else:
						s+=word+" "
						cand_sentences.append(s.strip())
						s=""
						bDelimFoundinEnd = True
				else:
					s+=word+" "
		if not bDelimFoundinEnd:
			cand_sentences.append(s.strip())

	if not delim_info.search('.'):
		## run phase 2 only if delimiter pattern contains period
		#print('No need to run phase2')
		return cand_sentences
#     print(cand_sentences)
#     print('====')

	### Phase 2: Address the fact that '.' may not always be a sentence delimiter
	### Method: If there is a run of lines containing only a word (optionally) and '.',
	### merge these lines as well one sentence preceding and succeeding this run of lines.
	final_sentences=[]
	sen_buffer=''        
	bad_state=False
	# print(cand_sentences)
	for i, sentence in enumerate(cand_sentences): 
		words=sentence.split(' ')
		#if len(words)<=2 and words[-1]=='.':
		if len(words)==1 and sentence[-1]=='.':
			bad_state=True
			sen_buffer = sen_buffer + ' ' + sentence
		## NEW condition    
		elif sentence[-1]=='.' and is_acronym_abbvr(words[-1][:-1],lang):
			# print('>>>>>>>>>>>>>>>>>>>>>>>>')
			# print(final_sentences,sentence)
			if len(sen_buffer)>0 and not bad_statse:
				final_sentences.append(sen_buffer)
			bad_state=True
			sen_buffer = sentence
		elif bad_state:
			sen_buffer = sen_buffer + ' ' + sentence
			if len(sen_buffer)>0:
				final_sentences.append(sen_buffer)
			sen_buffer=''
			bad_state=False
		else: ## good state                    
			if len(sen_buffer)>0:
				final_sentences.append(sen_buffer)
			sen_buffer=sentence
			bad_state=False

	if len(sen_buffer)>0:
		final_sentences.append(sen_buffer)
	
	return final_sentences

if __name__=='__main__':
	fout = open("log_ss.txt","w",encoding='utf-8')
	fout.write(('\n').join(sentence_split("पेड़ सूखा तो परिंदों ने ठिकाना बदला।","hi")))