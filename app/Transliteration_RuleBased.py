from itertools import count
import sys
import argparse
'''
A python library to transliterate the date. The library is dependent on the generic rule file and punctuation file.
'''


class GenericTransliteration(object):
	def __init__(self):
		self.dicGroupMapping = {}
		self.dicRuleMapping = {}
		self.dicStandAloneRules = []
		self.dicInitialRules = []
		self.dicMiddleRules = []
		self.dicFinalRules = []
		self.Groups=[]
		self.punctList = []
		self.lenMaxGroupCharacters =1
		# self.debugProg = True
		self.logFile = None
	
	def count(self, s, c) :
     
		# Count variable
		res = 0
		
		for i in range(len(s)) :
			
			# Checking character in string
			if (s[i] == c):
				res = res + 1
		return res

	def read_text_file(file):
		encodings_available = ["utf8", "utf16", "utf-16-be", "utf-16-le"]
		with open(file, "rb") as f:
			contents = f.read()
		for encoding in encodings_available:
			try:
				contents = contents.decode(encoding)
				return contents
			except:
				pass
		return None, "Failed decoding"

	def loadDictionaries(self, dicRule, dicPunct, bDebug=False):
		Rules = []
		self.logFile = open('log.txt','w',encoding='utf-8')
		
		with open(dicRule,'r',encoding='utf-8') as fRul:
			Rules = fRul.read().replace('\r\n','\n').split('\n')
			# print(Rules[:2])


		with open(dicPunct,'r',encoding='utf-8') as fPunct:
			self.punctList = fPunct.read().replace('\r\n','\n').split('\n')
			self.punctList.append(' ')

		if ' ' not in self.punctList:
			self.punctList.append(' ')
		cGroup = ''
		firstline=True
		for rule in Rules:
			if firstline:
				# print(len(rule))
				rule = rule[1:]
				# print(rule)
				firstline = False
			if not (rule.startswith('Group') or rule.startswith('#')):
				if not (rule=='' or rule.startswith(';')):
					# ACTUAL GROUP READING CODE HERE - Fill the mapping from the rule file
					if '>' in rule:
						strSplittedGroups = rule.split('>')
						if len(strSplittedGroups[0]) > self.lenMaxGroupCharacters:
							self.lenMaxGroupCharacters = len(strSplittedGroups[0])
						self.dicGroupMapping[strSplittedGroups[0]]=cGroup
						if len(strSplittedGroups) == 1:
							self.dicRuleMapping[strSplittedGroups[0]]=''
						elif len(strSplittedGroups) == 2:
							self.dicRuleMapping[strSplittedGroups[0]]=strSplittedGroups[1]
					elif '(' in rule:
						# print(rule)
						if bDebug:
							if ';' not in rule:
								self.logFile.write('Missing ; in Rule \t '+rule+'\n')
								continue
							elif ')' not in rule:
								self.logFile.write('Missing ) in Rule \t '+rule+'\n')
								print(rule)
								print('here')
								continue
							elif  self.count(rule,';') > 1:
								self.logFile.write('More than ; in Rule \t '+rule+'\n')
								continue
						ruleMapping = rule.split(';')
						startindex = ruleMapping[0].index('(')
						endindex = ruleMapping[0].index(')')
						strLeft = ruleMapping[0][:startindex].strip()
						strRight = ruleMapping[0][endindex+1:].strip()


						if (strLeft == "" and strRight == ""):
							self.dicStandAloneRules.append([ruleMapping[0][startindex+1:endindex],ruleMapping[1]])
						elif strLeft == "":
							# print(rule)
							self.dicInitialRules.append([ruleMapping[0][startindex+1:endindex],strRight,ruleMapping[1]])
						elif strRight == "":
							self.dicFinalRules.append([ruleMapping[0][startindex+1:endindex],strLeft,ruleMapping[1]])
							# f.write(str(self.dicFinalRules)+'\n')	
						else:
							self.dicMiddleRules.append([ruleMapping[0][startindex+1:endindex],strLeft,strRight,ruleMapping[1]])
				

				# print(self.dicInitialRules)
					# print(rule)
			else:
				# print(rule)
				if rule.startswith('Group'):
					cGroup = rule[5]
					self.Groups.append(cGroup)
					# print(cGroup)
				elif rule.startswith('#'):
					cGroup=""
		temp = sorted(self.dicStandAloneRules, key=lambda x: len(x[0]),reverse=True)
		self.dicStandAloneRules = []
		self.dicStandAloneRules = temp
		temp = []

		temp = sorted(self.dicInitialRules, key=lambda x: len(x[0]),reverse=True)
		self.dicInitialRules = []
		self.dicInitialRules = temp
		temp = []

		temp = sorted(self.dicMiddleRules, key=lambda x: len(x[0]),reverse=True)
		self.dicMiddleRules = []
		self.dicMiddleRules = temp
		temp = []

		temp = sorted(self.dicFinalRules, key=lambda x: len(x[0]),reverse=True)
		self.dicFinalRules = []
		self.dicFinalRules = temp
		print('parsed all the rules')

	def returnConsMapping(self,strInput):
		i=0
		dicConstMapping = []
		while(i<len(strInput)):
			if len(strInput)-i < self.lenMaxGroupCharacters:
				lenofChar = len(strInput)-i
			else:
				lenofChar = self.lenMaxGroupCharacters
			bMappingFound = False
			while lenofChar >= 1:
				# print(self.lenMaxGroupCharacters)
				# f.write(strInput[i:i+lenofChar]+'\n')
				# if strInput[i:i+j] in dicRuleMapping.keys():
				if strInput[i:i+lenofChar] in self.dicGroupMapping.keys():
					
					# dicConstMapping.append([dicRuleMapping[strInput[i:i+j]],strInput[i:i+j]])
					dicConstMapping.append([self.dicGroupMapping[strInput[i:i+lenofChar]],strInput[i:i+lenofChar]])
					i = i+lenofChar
					# print('m here'+str(lenofChar)+str(i))
					bMappingFound = True
					break
				else:
					# dicConstMapping.append(['?',strInput[i:i+lenofChar]])
					# i = i+lenofChar
					# bMappingFound = True
					# break
					# print(strInput[i:i+lenofChar])
					# if j==1: 
					lenofChar=lenofChar-1
			if not bMappingFound:
				dicConstMapping.append(['?',strInput[i]])
				i = i+1
		# print(dicConstMapping)
		return dicConstMapping


	def returnTransliterationLine(self,strInput,suggestions=False):
		print('inside returnTransliterationLine')
		wordForTransliteration=""
		strOutputTransliteration=""
		for cTransliteration in strInput:
			if cTransliteration in self.punctList:
				if wordForTransliteration!="":
					strOutputTransliteration=strOutputTransliteration+self.returnTransliteration(wordForTransliteration,suggestions)
					wordForTransliteration = ""
				strOutputTransliteration = strOutputTransliteration+cTransliteration
			else:
				wordForTransliteration = wordForTransliteration+cTransliteration
		if wordForTransliteration!="":
			strOutputTransliteration=strOutputTransliteration+self.returnTransliteration(wordForTransliteration,suggestions)
		return strOutputTransliteration
					

	def returnTransliteration(self,strInput,suggestions=False):
		outString= ""
		arrConsts = self.returnConsMapping(strInput)
		outString = self.checkForStandaloneRules(strInput,arrConsts)
		if outString=="":
			outInitial,nStartIndex,suggestionInitial = self.checkForInitialRules(strInput,arrConsts)
			# print(outInitial,nStartIndex)
			outFinal,nStartIndex,nEndIndex,suggestionFinal = self.checkForFinalRules(strInput,arrConsts,nStartIndex)
			# print(outFinal,nStartIndex,nEndIndex)
			outMiddle,suggestionMiddle = self.checkForMiddleRules(strInput,arrConsts,nStartIndex,nEndIndex)
			# print(outMiddle)
			
			if suggestions:
				suggestionOut = []
				suggestionOutFinal = []
				suggestionOut = suggestionInitial
				if len(suggestionMiddle)!=0:
					suggestionOut=[]
					for strMiddle in suggestionMiddle:
						if len(suggestionInitial)==0:
							suggestionOut = suggestionMiddle
							break
						else:
							temp = suggestionInitial
							temp = [s+strMiddle for s in temp]
							suggestionOut.extend(temp)
				if len(suggestionFinal)==0:
					suggestionOutFinal=suggestionOut
				else:
					for strFinal in suggestionFinal:
						if len(suggestionOut)==0:
							suggestionOutFinal = suggestionOut
							break
						else:
							temp = suggestionOut
							temp = [s+strFinal for s in temp]
							suggestionOutFinal.extend(temp)
				outString = ('/').join(suggestionOutFinal)
			else:
				outString = outInitial +outMiddle+outFinal
			# print(outString)
			return outString
		else:
			if not suggestions:
				outString = outString.split('/')[0]
			return outString


	def checkForStandaloneRules(self,strInput,arrConsts):
		bExactStringFound = False
		strOut = ""
		for rule in self.dicStandAloneRules:
			if rule[0] == strInput:
				bExactStringFound = True
				strOut = rule[1]
				break

		if bExactStringFound:
			return strOut
		else:
			# print('else')
			bRuleFound = False
			strRuleValue = ""
			
			for rule in self.dicStandAloneRules:
				# print(key,value)
				key = rule[0]
				value = rule[1]
				if len(key) == len(strInput):
					i = 0
					# print(len(arrConsts))
					# print(key)
					while i < len(arrConsts):
						if (key[i] == arrConsts[i][0] or key[i] == arrConsts[i][1]):
							i=i+1
							bRuleFound = True
						else:
							bRuleFound = False
						if not bRuleFound:
							break
				if bRuleFound:
					strRuleValue = rule[1]
					break
				
			strOut = ""
			SuggestionList =[]
			if bRuleFound:
				i=0
				j=0
				strRule = strRuleValue
				# print(strRule,i)
				while i < len(strRule):
					if j<len(arrConsts):
						if strRule[i] == arrConsts[j][0]:					
							strOut = strOut + (self.dicRuleMapping[arrConsts[j][1]].split(','))[0]
							for sugg in self.dicRuleMapping[arrConsts[j][1]].split(','):
								SuggestionList= [s + sugg for s in SuggestionList]
							i=i+2
							j=j+1
							# continue
						else:
							strOut = strOut + strRule[i]
							i = i+1
							# continue
					else:
						strOut = strOut + strRule[i]
						i = i+1
						# continue
			return strOut


	def checkForInitialRules(self,strInput,arrConsts):
		bRuleFound = False
		strRuleValue = ""
		iStartIndex = 0
		
		key = ""
		value = ""
		strRight = ""
		for rule in self.dicInitialRules:
			# print(key,value)
			i = 0
			key = rule[0]
			strRight = rule[1]
			value = rule[2]
			# if strInput.startswith(key):
			# 	bRuleFound = True
			# 	i = i + len(key)
			# else:
			# 	# print(len(arrConsts))
			# 	# print(key)
			if len(arrConsts) > len(key):

				while i < len(key):
					if (key[i] == arrConsts[i][0] or key[i] == arrConsts[i][1]):
						# print(key)

						i=i+1

						bRuleFound = True
					else:
						bRuleFound = False
					if not bRuleFound:
						break
			if bRuleFound:
				# print(key)
				
				# f.write(key+str(strRuleValue))
				if strInput[i] ==  strRight or strRight == arrConsts[i][1] or strRight == arrConsts[i][0]:
					# print(strRuleValue[0])
					iStartIndex = i
					break
				elif strRight == '?':
					# print(strRuleValue[0])
					iStartIndex = i
					break
				else:
					bRuleFound= False
					continue
		# print(bRuleFound)
		# print(bRuleFound,key,strRuleValue)		
		strOut = ""
		SuggestionList = []
		if bRuleFound:
			i=0
			j=0
			strRule = value
			# print(key,value,strRight)
			while i < len(strRule):
				if j<len(arrConsts):
					# print(i,j,strRule[i],arrConsts)
					# f.write(strRule[i])
					if strRule[i] == arrConsts[j][0]:					
						# print('1'+dicRuleMapping[arrConsts[j][1]].split(',')[0])
						strOut = strOut + (self.dicRuleMapping[arrConsts[j][1]].split(',')[0])
						temp=[]
						for sugg in self.dicRuleMapping[arrConsts[j][1]].split(','):
							if len(SuggestionList) == 0:
								SuggestionList.append(sugg)
							else:
								temp.extend([s + sugg for s in SuggestionList])
						if len(temp)!=0:
							SuggestionList=temp 
						i=i+2
						j=j+1
						# continue
					elif strRule[i] == arrConsts[j][1]:					
						# print('2'+dicRuleMapping[arrConsts[j][1]].split(',')[0])
						strOut = strOut + (self.dicRuleMapping[arrConsts[j][1]].split(',')[0])
						temp=[]
						for sugg in self.dicRuleMapping[arrConsts[j][1]].split(','):
							if len(SuggestionList) == 0:
								SuggestionList.append(sugg)
							else:
								temp.extend([s + sugg for s in SuggestionList])
						if len(temp)!=0:
							SuggestionList=temp 
						
						i=i+2
						j=j+1
					else:
						if strRule[i] in self.Groups:
							j=j+1
						else:
							strOut = strOut + strRule[i]
							
							if len(SuggestionList) == 0:
								SuggestionList.append(strRule[i])
							else:
								SuggestionList= [s + strRule[i] for s in SuggestionList]
							i = i+1
						# continue
				else:
					strOut = strOut + strRule[i]
					if len(SuggestionList) == 0:
						SuggestionList.append(strRule[i])
					else:
						SuggestionList= [s + strRule[i] for s in SuggestionList]
					i = i+1
					# continue
		# f.write(strOut)
		else:
			iStartIndex  = 0

		return strOut,iStartIndex,SuggestionList


	def checkForFinalRules(self,strInput,arrConsts,nStartIndex):
		# print(strInput,nIndexStart)
		bRuleFound = False
		strRuleValue = ""
		nEndIndex = len(strInput)
		strtoMatch =  strInput[nStartIndex+1:]
		# f.write(strtoMatch+'\n')
		key = ""
		value = ""
		strLeft = ""		
		for rule in self.dicFinalRules:
			key = rule[0]
			strLeft = rule[1]
			value = rule[2]
			# print(key,value)
			i = len(key)-1
			# j= len(strInput)-1
			j= len(arrConsts)-1

			if len(key) <= len(strtoMatch):

				while i >= 0:
					# print(key,i,j,arrConsts)
					if (key[i] == arrConsts[j][0]):
						i=i-1
						j=j-1
						bRuleFound = True
						# print(key,i,j,strtoMatch)
					elif key[i] == arrConsts[j][1]: 
						i=i-1
						j=j-1
						bRuleFound = True
						# print(key,i,j,strtoMatch)
					else:
						bRuleFound = False
					if not bRuleFound:
						break
			
			if bRuleFound:
				# f.write(strInput[j-1]+'\n')
				if strInput[j] ==  strLeft:
					# print(strRuleValue[0])
					nEndIndex = j+1
					# print('1')
					break
				elif strLeft == arrConsts[j][1]:
					# print(strRuleValue[0])
					# print('2')
					nEndIndex = j+1
					break
				elif strLeft == arrConsts[j][0]:
					# print(strRuleValue[0])
					# print(strRuleValue[0],arrConsts[j][0])
					nEndIndex = j+1
					# print('3')
					break
				elif strLeft == '?':
					# print(strRuleValue[0])
					nEndIndex = j+1
					# print('4')
					break
				else:
					bRuleFound= False
					continue
		# print(bRuleFound,key,strRuleValue)
		# f.write(str(arrConsts))		
		strOut = ""
		SuggestionList = []
		if bRuleFound:
			# print(key,value,strLeft)
				
			i=0
			j=nEndIndex
			strRule = value

			while i < len(strRule):
				if j<len(arrConsts):
					# print(i,j,strRule[i],arrConsts[j][0])
					if strRule[i] == arrConsts[j][0]:					
						# print('here')
						strOut = strOut + (self.dicRuleMapping[arrConsts[j][1]].split(',')[0])
						temp=[]
						for sugg in self.dicRuleMapping[arrConsts[j][1]].split(','):
							if len(SuggestionList) == 0:
								SuggestionList.append(sugg)
							else:
								temp.extend([s + sugg for s in SuggestionList])
						if len(temp)!=0:
							SuggestionList=temp 
						i=i+2
						j=j+1
						# continue
					else:
						strOut = strOut + strRule[i]
						if len(SuggestionList) == 0:
							SuggestionList.append(strRule[i])
						else:
							SuggestionList= [s + strRule[i] for s in SuggestionList]
						i = i+1
						# continue
				else:
					strOut = strOut + strRule[i]
					if len(SuggestionList) == 0:
						SuggestionList.append(strRule[i])
					else:
						SuggestionList= [s + strRule[i] for s in SuggestionList]
					i = i+1
					# continue
		# print('----------'+strOut+str(nEndIndex)+str(nStartIndex))
		return strOut,nStartIndex,nEndIndex,SuggestionList


	def checkForMiddleRules(self,strInput,arrConsts,nStartIndex,nEndIndex):
		# print(strInput,nIndexStart)
		strOutput = ""
		SuggestionList = []
		while (nStartIndex <nEndIndex):
			# print(strOutput,nStartIndex,nEndIndex)
			bRuleFound = False
			strRuleValue = ""
			strtoMatch =  strInput[nStartIndex:nEndIndex]
			# print('string '+strtoMatch)
			key = ""
			strLeft = ""
			strRight = ""
			value = ""
			# f.write(strtoMatch+'\n')
					
			for rule in self.dicMiddleRules:
				# print(key,value)
				i = 0
				j=nStartIndex
				# j= len(strInput)-1
				# print(arrConsts)
				key = rule[0]
				strLeft = rule[1]
				strRight = rule[2]
				value = rule[3]

				if len(key) <= len(strtoMatch):
					# print(arrConsts)
					while i < len(key):
						if j < len(arrConsts):
							if (key[i] == arrConsts[j][0] or key[i] == arrConsts[j][1]):
								i=i+1
								j=j+1
								# j=j-1
								bRuleFound = True
							else:
								bRuleFound = False
						else:
							bRuleFound = False
						if not bRuleFound:
							break
				
				# print(bRuleFound)
				if bRuleFound:
					if nStartIndex-1 >=0:
						if (strInput[nStartIndex-1] ==  strLeft or strLeft == arrConsts[nStartIndex-1][1] or strLeft == arrConsts[nStartIndex-1][0] or strLeft == '?'):
						# print(strRuleValue[0])
							if nEndIndex < len(arrConsts): 
								if (strInput[nEndIndex-1] ==  strRight or strRight == arrConsts[nEndIndex-1][1] or strRight == arrConsts[nEndIndex-1][0] or strRight == '?'):
									nEndIndex = j+1
									break
					else:
						bRuleFound= False
						continue
			# print(bRuleFound,key,strRuleValue)
					
			strOut = ""
			SuggestionList = []
			if bRuleFound:
				i=0
				j=nStartIndex
				strRule = value

				while i < len(strRule):
					if j<len(arrConsts):
						# print(i,j,strRule[i],arrConsts[j][0])
						if strRule[i] == arrConsts[j][0]:					
							# print('here')
							strOut = strOut + (self.dicRuleMapping[arrConsts[j][1]].split(',')[0])
							temp=[]
							for sugg in self.dicRuleMapping[arrConsts[j][1]].split(','):
								if len(SuggestionList) == 0:
									SuggestionList.append(sugg)
								else:
									temp.extend([s + sugg for s in SuggestionList])
							if len(temp)!=0:
								SuggestionList=temp 
							i=i+2
							j=j+1
							# continue
						else:
							strOut = strOut + strRule[i]
							if len(SuggestionList) == 0:
								SuggestionList.append(strRule[i])
							else:
								SuggestionList= [s + strRule[i] for s in SuggestionList]
							i = i+1
							# continue
					else:
						strOut = strOut + strRule[i]
						if len(SuggestionList) == 0:
							SuggestionList.append(strRule[i])
						else:
							SuggestionList= [s + strRule[i] for s in SuggestionList]
						i = i+1
						# continue
				strOutput = strOutput + strOut
				nStartIndex = j
			else:
				i = nStartIndex
				end = 0
				if nEndIndex > len(arrConsts):
					end = len(arrConsts)
				else:
					end = nEndIndex
				# while i<len(arrConsts):
				# print('here',i,end)
				if i == end:
					i = i+1
				else:
					while i<end:
						if arrConsts[i][0] == '?':
							strOut = strOut + (arrConsts[i][1].split(',')[0])
							temp=[]
							for sugg in arrConsts[i][1].split(','):
								if len(SuggestionList) == 0:
									SuggestionList.append(sugg)
								else:
									temp.extend([s + sugg for s in SuggestionList])
							if len(temp)!=0:
								SuggestionList=temp 
						else:
							strOut = strOut + (self.dicRuleMapping[arrConsts[i][1]].split(',')[0])
							temp=[]
							for sugg in self.dicRuleMapping[arrConsts[i][1]].split(','):
								if len(SuggestionList) == 0:
									SuggestionList.append(sugg)
								else:
									temp.extend([s + sugg for s in SuggestionList])
							if len(temp)!=0:
								SuggestionList=temp
							# print(strOut)
						i = i+1
					strOutput = strOutput + strOut
				# if i == end:
				# 	nStartIndex = nStartIndex+1
				# else:
				if i < len(arrConsts):
					nStartIndex = i
				else:
					nStartIndex = nEndIndex

				# print('>>>>>>>>',strOutput,nStartIndex,nEndIndex,len(arrConsts),strOut)
				
			# print('----------'+strOut+str(nEndIndex)+str(nStartIndex))
			
		return strOutput,SuggestionList

# with open('test.txt','w',encoding='utf-8') as f:
	# f.write(str(returnConsMapping('યુસુફ')))

# f.write(str(self.dicFinalRules))
# f.write((returnTransliteration('Cંપ')))
  # યુસુફ')))
'''
def main():
	print("command to run the file python Transliteration.py --rule_file <RuleFile> --punct_file <PunctuationFile> --source_file <InputFile> --target_file <OutputFile> --suggestions <OPTIONAL-default False> --debug <OPTIONAL-default False>")
	
	parserConfig = argparse.ArgumentParser()
	parserConfig.add_argument("--rule_file", type=str, default="")
	parserConfig.add_argument("--punct_file", type=str, default="")
	parserConfig.add_argument("--source_file", type=str, default="")
	parserConfig.add_argument("--target_file", type=str, default="")
	parserConfig.add_argument("--suggestions", default=False, action='store_true')
	parserConfig.add_argument("--debug", default=False, action='store_true')


	args = parserConfig.parse_args()
	# print("rulefile {}".format(sys.argv[1]))
	# print("punctuation file {}".format(sys.argv[2]))
	# print("input file {}".format(sys.argv[3]))
	# print("output file {}".format(sys.argv[4]))
	
	print("rulefile {}".format(args.rule_file))
	print("punctuation file {}".format(args.punct_file))
	print("input file {}".format(args.source_file))
	print("output file {}".format(args.target_file))
	print("input file {}".format(args.suggestions))
	print("output file {}".format(args.debug))
	
	
	# bMultipleSuggestions = False

	# if len(sys.argv)>=6:
	# 	print("Suggestions {}".format(sys.argv[5]))
	# 	if sys.argv[5] == 'True':
	# 		bMultipleSuggestions = True
	# 	# bMultipleSuggestions = bool(str(sys.argv[5]))
	
	f = open(args.target_file,'w',encoding='utf-8')
	objGeneticTransliteration = GenericTransliteration()
	objGeneticTransliteration.loadDictionaries(args.rule_file,args.punct_file,bDebug=args.debug)
	with open(args.source_file,'r',encoding ='utf-8') as fw:
		lines = fw.read().replace('\ufeff','').split('\n')
		i=0
		for line in lines:
			if i%1000 == 0:
				print('parsed {}'.format(i))
			line = line.strip()
			# print(line)
			if line!="":
				f.write(objGeneticTransliteration.returnTransliterationLine(line,suggestions=args.suggestions)+'\n')
			i=i+1


if __name__ == "__main__":
	main()

# f.write(returnTransliteration('પ્રવિણ'))
# print(returnTransliteration('વિટ્ટઃલ'))

'''