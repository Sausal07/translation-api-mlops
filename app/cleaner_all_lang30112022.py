#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Yogesh Shishodia
"""

import sys
import re


shortest = 1 # used to compare line length
lineToDelete = "" # the line we want to remove

# file = open(sys.argv[2], 'w',encoding='utf-8')
# with open(sys.argv[1], 'r', encoding='UTF-8') as f:
#     lines = f.read().split('\n')

#     for line in lines:
        #line = line.lower()
def returnCleanDataILIL(line):
        
        # print('line:',line)
        # print(type(line))
        # line = ' '.join(line)
        # print('line:',line)
        # print(type(line))


        line = re.sub('i\'m','i am ',line)
        line = re.sub('isn\'t','is not',line)
        line = re.sub('aren\'t','are not',line)
        line = re.sub('he\'s','he is',line)
        line = re.sub('she\'s','she is',line)
        line = re.sub('it\'s','it is',line)
        line = re.sub('you\'re','you are',line)
        line = re.sub('we\'re','we are',line)
        line = re.sub('they\'re','they are',line)
        line = re.sub('wasn\'t','was not',line)
        line = re.sub('weren\'t','were not',line)
        line = re.sub('don\'t','do not',line)
        line = re.sub('doesn\'t','does not',line)
        line = re.sub('i\'ve','i have',line)
        
        line = re.sub('you\'ve not','you have not',line)
        line = re.sub('we\'ve not','we have not',line)
        line = re.sub('they\'ve not','they have not',line)
        line = re.sub('hasn\'t','has not',line)
        line = re.sub('haven\'t','have not',line)
        
        line = re.sub('i\'d not','i had not',line)
        line = re.sub('he\'d not','he had not',line)
        line = re.sub('she\'d not','she had not',line)
        line = re.sub('it\'d not','it had not',line)
        line = re.sub('you\'d not','i had not',line)
        line = re.sub('we\'d not','we had not',line)
        line = re.sub('they\'d not','they had not',line)
        line = re.sub('i\'d','i had',line)
        line = re.sub('he\'d','he had',line)
        line = re.sub('she\'d','she had',line)
        line = re.sub('it\'d','it had',line)
        line = re.sub('you\'d','i had',line)
        line = re.sub('we\'d','we had',line)
        line = re.sub('they\'d','they had',line)

        line = re.sub('can\'t','can not',line)
        line = re.sub('couldn\'t','could not',line)
        line = re.sub('mustn\'t','must not',line)
        line = re.sub('shan\'t','shall not',line)
        line = re.sub('shouldn\'t','should not',line)
        line = re.sub('wouldn\'t','would not',line)
        line = re.sub('they\'d not','they had not',line)

        line = re.sub('i\'ll not','i will not',line)
        line = re.sub('we\'ll not','we will not',line)
        line = re.sub('he\'ll not','he will not',line)
        line = re.sub('she\'ll not','she will not',line)
        line = re.sub('it\'ll not','it will not',line)
        line = re.sub('you\'ll not','you will not',line)
        line = re.sub('we\'ll not','we will not',line)
        line = re.sub('they\'ll not','they will not',line)
        line = re.sub('i\'ll','i will',line)
        line = re.sub('we\'ll','we will',line)
        line = re.sub('he\'ll','he will',line)
        line = re.sub('she\'ll','she will',line)
        line = re.sub('it\'ll','it will',line)
        line = re.sub('you\'ll','you will',line)
        line = re.sub('we\'ll','we will',line)
        line = re.sub('they\'ll','they will',line) 

        line = re.sub('could\'ve','could have',line)
        line = re.sub('should\'ve','should have',line)
        line = re.sub('must\'ve','must have',line)
        line = re.sub('couldve','could have',line)
        line = re.sub('shouldve','should have',line) 
        line = re.sub('mustve','must have',line)  

        line = re.sub('couldnt','could not',line)
        line = re.sub('mustnt','must not',line)
        line = re.sub('shouldnt','should not',line)
        line = re.sub('wouldnt','would not',line)

        line = re.sub('I\'m','I am ',line)
        line = re.sub('Isn\'t','Is not',line)
        line = re.sub('Aren\'t','Are not',line)
        line = re.sub('He\'s','He is',line)
        line = re.sub('She\'s','She is',line)
        line = re.sub('It\'s','It is',line)
        line = re.sub('You\'re','You are',line)
        line = re.sub('We\'re','We are',line)
        line = re.sub('They\'re','They are',line)
        line = re.sub('Wasn\'t','Was not',line)
        line = re.sub('Weren\'t','Were not',line)
        line = re.sub('Don\'t','Do not',line)
        line = re.sub('Doesn\'t','Does not',line)
        line = re.sub('I\'ve','I have',line)    
        line = re.sub('You\'ve not','You have not',line)
        line = re.sub('We\'ve not','We have not',line)
        line = re.sub('They\'ve not','They have not',line)
        line = re.sub('Hasn\'t','Has not',line)
        line = re.sub('Haven\'t','Have not',line)        
        line = re.sub('I\'d not','I had not',line)
        line = re.sub('He\'d not','He had not',line)
        line = re.sub('She\'d not','She had not',line)
        line = re.sub('It\'d not','It had not',line)
        line = re.sub('You\'d not','I had not',line)
        line = re.sub('We\'d not','We had not',line)
        line = re.sub('They\'d not','They had not',line)
        line = re.sub('I\'d','I had',line)
        line = re.sub('He\'d','He had',line)
        line = re.sub('She\'d','She had',line)
        line = re.sub('It\'d','It had',line)
        line = re.sub('Tou\'d','I had',line)
        line = re.sub('We\'d','We had',line)
        line = re.sub('They\'d','They had',line)
        line = re.sub('Can\'t','Can not',line)
        line = re.sub('Couldn\'t','Could not',line)
        line = re.sub('Mustn\'t','Must not',line)
        line = re.sub('Shan\'t','Shall not',line)
        line = re.sub('Shouldn\'t','Should not',line)
        line = re.sub('Wouldn\'t','Would not',line)
        line = re.sub('They\'d not','They had not',line)
        line = re.sub('I\'ll not','I will not',line)
        line = re.sub('We\'ll not','We will not',line)
        line = re.sub('He\'ll not','He will not',line)
        line = re.sub('She\'ll not','She will not',line)
        line = re.sub('It\'ll not','It will not',line)
        line = re.sub('You\'ll not','You will not',line)
        line = re.sub('We\'ll not','We will not',line)
        line = re.sub('They\'ll not','They will not',line)
        line = re.sub('I\'ll','I will',line)
        line = re.sub('We\'ll','We will',line)
        line = re.sub('He\'ll','He will',line)
        line = re.sub('She\'ll','She will',line)
        line = re.sub('It\'ll','It will',line)
        line = re.sub('You\'ll','You will',line)
        line = re.sub('We\'ll','We will',line)
        line = re.sub('They\'ll','They will',line) 
        line = re.sub('Could\'ve','Could have',line)
        line = re.sub('Should\'ve','Should have',line)
        line = re.sub('Must\'ve','Must have',line)
        line = re.sub('Couldve','Could have',line)
        line = re.sub('Shouldve','Should have',line) 
        line = re.sub('Mustve','Must have',line)  


        line = re.sub(r'!+',' ! ',line)
        line = re.sub(r'\?+',r' ? ',line)
        line = re.sub(r'\.+',r' . ',line)
        line = re.sub(',+',' , ',line)
        line = re.sub('-+',' - ',line)
        line = re.sub(r'\\',r' \\ ',line)
        line = re.sub('\\s+',' ',line)
        line = re.sub(r'\/+',r' / ',line)

        line = re.sub(r'\@+',r' @ ',line)
        line = re.sub(r'\#+',r' # ',line)
        line = re.sub(r'\$+',r' $ ',line)
        line = re.sub(r'\€+',r' € ',line)
        line = re.sub(r'\£+',r' £ ',line)
        line = re.sub(r'\¥+',r' ¥ ',line)
        line = re.sub(r'\₹+',r' ₹ ',line)

        line = re.sub(r'\^+',r' ^ ',line)
        line = re.sub(r'\`+',r' ` ',line)
        line = re.sub(r'\~+',r' ~ ',line)
        line = re.sub(r'\*+',r' * ',line)
        line = re.sub(r'\<+',r' < ',line)
        line = re.sub(r'\>+',r' > ',line)
        line = re.sub(r'\%+',r' % ',line)
        line = re.sub(r'\+',r' + ',line)
        line = re.sub(r'\=+',r' = ',line)
        line = re.sub(r'\_+',r' _ ',line)


        line = re.sub(r"\(+"," ( ",line)
        line = re.sub(r"\)+"," ) ",line)
        line = re.sub(r"\}+"," } ",line)   
        line = re.sub(r"\{+"," { ",line)
        line = re.sub(r"\[+"," [ ",line)
        line = re.sub(r"\]+"," ] ",line)
        line = re.sub(r"\;+"," ; ",line)
        line = re.sub(r"\&+"," & ",line)
        line = re.sub(r"\:+"," : ",line)
        line = re.sub(r"\|+"," | ",line)
        line = re.sub(r"\|$"," .",line)

        line = re.sub(r"\।$"," .",line)
        line = re.sub(r"\।+"," । ",line)

        line = re.sub(r"\'+"," ' ",line)

        line = re.sub(r"\‘+"," ' ",line)

        line = re.sub(r"\’+"," ' ",line)

        line = re.sub(r'\"+',' " ',line)        

        line = re.sub(r'\“+',' " ',line)       

        line = re.sub(r'\”+',' " ',line)

        line = re.sub('\\s+',' ',line)



        # For Devanagari Numbers 
        line = re.sub(r'([\u0966-\u096F]+) (\.) ([\u0966-\u096F]+) (\.) ([\u0966-\u096F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0966-\u096F]+) (\.) ([\u0966-\u096F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0966-\u096F]+) (-) ([\u0966-\u096F]+) (-) ([\u0966-\u096F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0966-\u096F]+) (-) ([\u0966-\u096F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0966-\u096F]+) (/) ([\u0966-\u096F]+) (/) ([\u0966-\u096F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0966-\u096F]+) (/) ([\u0966-\u096F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0966-\u096F]+) (,) ([\u0966-\u096F]+) (,) ([\u0966-\u096F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0966-\u096F]+) (,) ([\u0966-\u096F]+)',r'\1\2\3',line)

        # For Devanagari letters and english digits
        line = re.sub(r'([\u0900-\u097F]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0900-\u097F]+)',r'\1 \2',line)

        # For Devanagari letters and english letters
        line = re.sub(r'([\u0900-\u097F]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0900-\u097F]+)',r'\1 \2',line)

        # separate devanagari numbers and letters
        line = re.sub(r'([\u0966-\u096F])([\u0900-\u0963])',r'\1 \2',line)
        line = re.sub(r'([\u0900-\u0963])([\u0966-\u096F])',r'\1 \2',line)




        # for english langauge:
        line = re.sub(r'([0-9]+) (\.) ([0-9]+) (\.) ([0-9]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([0-9]+) (\.) ([0-9]+)',r'\1\2\3',line)

        line = re.sub(r'([0-9]+) (-) ([0-9]+) (-) ([0-9]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([0-9]+) (-) ([0-9]+)',r'\1\2\3',line)

        line = re.sub(r'([0-9]+) (/) ([0-9]+) (/) ([0-9]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([0-9]+) (/) ([0-9]+)',r'\1\2\3',line)

        line = re.sub(r'([0-9]+) (,) ([0-9]+) (,) ([0-9]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([0-9]+) (,) ([0-9]+)',r'\1\2\3',line)

        line = re.sub(r'([0-9]+) (:) ([0-9]+) (:) ([0-9]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([0-9]+) (:) ([0-9]+)',r'\1\2\3',line)

        line = re.sub(r'([0-9]+)([a-zA-Z]+)',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z]+)([0-9]+)',r'\1 \2',line)

        line = re.sub(r'([A-Z]) (\.) ([A-Z]) (\.) ([A-Z])',r'\1\2\3\4\5',line)
        line = re.sub(r'([A-Z]) (\.) ([A-Z])',r'\1\2\3',line)



        # For Bengali Numbers 
        line = re.sub(r'([\u09E6-\u09EF]+) (\.) ([\u09E6-\u09EF]+) (\.) ([\u09E6-\u09EF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u09E6-\u09EF]+) (\.) ([\u09E6-\u09EF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u09E6-\u09EF]+) (-) ([\u09E6-\u09EF]+) (-) ([\u09E6-\u09EF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u09E6-\u09EF]+) (-) ([\u09E6-\u09EF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u09E6-\u09EF]+) (/) ([\u09E6-\u09EF]+) (/) ([\u09E6-\u09EF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u09E6-\u09EF]+) (/) ([\u09E6-\u09EF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u09E6-\u09EF]+) (,) ([\u09E6-\u09EF]+) (,) ([\u09E6-\u09EF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u09E6-\u09EF]+) (,) ([\u09E6-\u09EF]+)',r'\1\2\3',line)

        # For Bengali letters and english digits
        line = re.sub(r'([\u0980-\u09FF]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0980-\u09FF]+)',r'\1 \2',line)

        # For Bengali letters and english letters
        line = re.sub(r'([\u0980-\u09FF]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0980-\u09FF]+)',r'\1 \2',line)

        # separate Bengali numbers and letters
        line = re.sub(r'([\u09E6-\u09EF])([\u0980-\u09E3])',r'\1 \2',line)
        line = re.sub(r'([\u0980-\u09E3])([\u09E6-\u09EF])',r'\1 \2',line)




        # For Malayalam Numbers
        line = re.sub(r'([\u0D66-\u0D72]+) (\.) ([\u0D66-\u0D72]+) (\.) ([\u0D66-\u0D72]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0D66-\u0D72]+) (\.) ([\u0D66-\u0D72]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0D66-\u0D72]+) (-) ([\u0D66-\u0D72]+) (-) ([\u0D66-\u0D72]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0D66-\u0D72]+) (-) ([\u0D66-\u0D72]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0D66-\u0D72]+) (/) ([\u0D66-\u0D72]+) (/) ([\u0D66-\u0D72]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0D66-\u0D72]+) (/) ([\u0D66-\u0D72]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0D66-\u0D72]+) (,) ([\u0D66-\u0D72]+) (,) ([\u0D66-\u0D72]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0D66-\u0D72]+) (,) ([\u0D66-\u0D72]+)',r'\1\2\3',line)

        # For Malayalam letters and english digits
        line = re.sub(r'([\u0D00-\u0D7F]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0D00-\u0D7F]+)',r'\1 \2',line)

        # For Malayalam letters and english letters
        line = re.sub(r'([\u0D00-\u0D7F]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0D00-\u0D7F]+)',r'\1 \2',line)

        # separate Malayalam numbers and letters
        line = re.sub(r'([\u0D66-\u0D72])([\u0D00-\u0D63])',r'\1 \2',line)
        line = re.sub(r'([\u0D00-\u0D63])([\u0D66-\u0D72])',r'\1 \2',line)




        # For Tamil Numbers
        line = re.sub(r'([\u0BE6-\u0BF2]+) (\.) ([\u0BE6-\u0BF2]+) (\.) ([\u0BE6-\u0BF2]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0BE6-\u0BF2]+) (\.) ([\u0BE6-\u0BF2]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0BE6-\u0BF2]+) (-) ([\u0BE6-\u0BF2]+) (-) ([\u0BE6-\u0BF2]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0BE6-\u0BF2]+) (-) ([\u0BE6-\u0BF2]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0BE6-\u0BF2]+) (/) ([\u0BE6-\u0BF2]+) (/) ([\u0BE6-\u0BF2]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0BE6-\u0BF2]+) (/) ([\u0BE6-\u0BF2]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0BE6-\u0BF2]+) (,) ([\u0BE6-\u0BF2]+) (,) ([\u0BE6-\u0BF2]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0BE6-\u0BF2]+) (,) ([\u0BE6-\u0BF2]+)',r'\1\2\3',line)

        # For Tamil letters and english digits
        line = re.sub(r'([\u0B80-\u0BFF]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0B80-\u0BFF]+)',r'\1 \2',line)

        # For Tamil letters and english letters
        line = re.sub(r'([\u0B80-\u0BFF]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0B80-\u0BFF]+)',r'\1 \2',line)

        # separate Tamil numbers and letters
        line = re.sub(r'([\u0BE6-\u0BF2])([\u0B80-\u0BE5])',r'\1 \2',line)
        line = re.sub(r'([\u0B80-\u0BE5])([\u0BE6-\u0BF2])',r'\1 \2',line)




        # For Telugu Numbers
        line = re.sub(r'([\u0C66-\u0C6F]+) (\.) ([\u0C66-\u0C6F]+) (\.) ([\u0C66-\u0C6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0C66-\u0C6F]+) (\.) ([\u0C66-\u0C6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0C66-\u0C6F]+) (-) ([\u0C66-\u0C6F]+) (-) ([\u0C66-\u0C6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0C66-\u0C6F]+) (-) ([\u0C66-\u0C6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0C66-\u0C6F]+) (/) ([\u0C66-\u0C6F]+) (/) ([\u0C66-\u0C6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0C66-\u0C6F]+) (/) ([\u0C66-\u0C6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0C66-\u0C6F]+) (,) ([\u0C66-\u0C6F]+) (,) ([\u0C66-\u0C6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0C66-\u0C6F]+) (,) ([\u0C66-\u0C6F]+)',r'\1\2\3',line)

        # For Telugu letters and english digits
        line = re.sub(r'([\u0C00-\u0C7F]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0C00-\u0C7F]+)',r'\1 \2',line)

        # For Telugu letters and english letters
        line = re.sub(r'([\u0C00-\u0C7F]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0C00-\u0C7F]+)',r'\1 \2',line)

        # separate Telugu numbers and letters
        line = re.sub(r'([\u0C66-\u0C6F])([\u0C00-\u0C63])',r'\1 \2',line)
        line = re.sub(r'([\u0C00-\u0C63])([\u0C66-\u0C6F])',r'\1 \2',line)




        # For Gujarati Numbers
        line = re.sub(r'([\u0AE6-\u0AEF]+) (\.) ([\u0AE6-\u0AEF]+) (\.) ([\u0AE6-\u0AEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0AE6-\u0AEF]+) (\.) ([\u0AE6-\u0AEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0AE6-\u0AEF]+) (-) ([\u0AE6-\u0AEF]+) (-) ([\u0AE6-\u0AEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0AE6-\u0AEF]+) (-) ([\u0AE6-\u0AEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0AE6-\u0AEF]+) (/) ([\u0AE6-\u0AEF]+) (/) ([\u0AE6-\u0AEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0AE6-\u0AEF]+) (/) ([\u0AE6-\u0AEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0AE6-\u0AEF]+) (,) ([\u0AE6-\u0AEF]+) (,) ([\u0AE6-\u0AEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0AE6-\u0AEF]+) (,) ([\u0AE6-\u0AEF]+)',r'\1\2\3',line)

        # For Gujarati letters and english digits
        line = re.sub(r'([\u0A80-\u0AFF]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0A80-\u0AFF]+)',r'\1 \2',line)

        # For Gujarati letters and english letters
        line = re.sub(r'([\u0A80-\u0AFF]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0A80-\u0AFF]+)',r'\1 \2',line)

        # separate Gujarati numbers and letters
        line = re.sub(r'([\u0AE6-\u0AEF])([\u0A80-\u0AE3])',r'\1 \2',line)
        line = re.sub(r'([\u0A80-\u0AE3])([\u0AE6-\u0AEF])',r'\1 \2',line)




        # For Kannada Numbers
        line = re.sub(r'([\u0CE6-\u0CEF]+) (\.) ([\u0CE6-\u0CEF]+) (\.) ([\u0CE6-\u0CEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0CE6-\u0CEF]+) (\.) ([\u0CE6-\u0CEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0CE6-\u0CEF]+) (-) ([\u0CE6-\u0CEF]+) (-) ([\u0CE6-\u0CEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0CE6-\u0CEF]+) (-) ([\u0CE6-\u0CEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0CE6-\u0CEF]+) (/) ([\u0CE6-\u0CEF]+) (/) ([\u0CE6-\u0CEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0CE6-\u0CEF]+) (/) ([\u0CE6-\u0CEF]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0CE6-\u0CEF]+) (,) ([\u0CE6-\u0CEF]+) (,) ([\u0CE6-\u0CEF]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0CE6-\u0CEF]+) (,) ([\u0CE6-\u0CEF]+)',r'\1\2\3',line)

        # For Kannada letters and english digits
        line = re.sub(r'([\u0C80-\u0CFF]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0C80-\u0CFF]+)',r'\1 \2',line)

        # For Kannada letters and english letters
        line = re.sub(r'([\u0C80-\u0CFF]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0C80-\u0CFF]+)',r'\1 \2',line)

        # separate Kannada numbers and letters
        line = re.sub(r'([\u0CE6-\u0CEF])([\u0C80-\u0CE3])',r'\1 \2',line)
        line = re.sub(r'([\u0C80-\u0CE3])([\u0CE6-\u0CEF])',r'\1 \2',line)




        # For Oriya Numbers
        line = re.sub(r'([\u0B66-\u0B6F]+) (\.) ([\u0B66-\u0B6F]+) (\.) ([\u0B66-\u0B6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0B66-\u0B6F]+) (\.) ([\u0B66-\u0B6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0B66-\u0B6F]+) (-) ([\u0B66-\u0B6F]+) (-) ([\u0B66-\u0B6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0B66-\u0B6F]+) (-) ([\u0B66-\u0B6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0B66-\u0B6F]+) (/) ([\u0B66-\u0B6F]+) (/) ([\u0B66-\u0B6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0B66-\u0B6F]+) (/) ([\u0B66-\u0B6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0B66-\u0B6F]+) (,) ([\u0B66-\u0B6F]+) (,) ([\u0B66-\u0B6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0B66-\u0B6F]+) (,) ([\u0B66-\u0B6F]+)',r'\1\2\3',line)

        # For Oriya letters and english digits
        line = re.sub(r'([\u0B00-\u0B7F]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0B00-\u0B7F]+)',r'\1 \2',line)

        # For Oriya letters and english letters
        line = re.sub(r'([\u0B00-\u0B7F]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0B00-\u0B7F]+)',r'\1 \2',line)

        # separate Oriya numbers and letters
        line = re.sub(r'([\u0B66-\u0B6F])([\u0B00-\u0B63])',r'\1 \2',line)
        line = re.sub(r'([\u0B00-\u0B63])([\u0B66-\u0B6F])',r'\1 \2',line)




        # For Punjabi Numbers
        line = re.sub(r'([\u0A66-\u0A6F]+) (\.) ([\u0A66-\u0A6F]+) (\.) ([\u0A66-\u0A6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0A66-\u0A6F]+) (\.) ([\u0A66-\u0A6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0A66-\u0A6F]+) (-) ([\u0A66-\u0A6F]+) (-) ([\u0A66-\u0A6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0A66-\u0A6F]+) (-) ([\u0A66-\u0A6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0A66-\u0A6F]+) (/) ([\u0A66-\u0A6F]+) (/) ([\u0A66-\u0A6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0A66-\u0A6F]+) (/) ([\u0A66-\u0A6F]+)',r'\1\2\3',line)

        line = re.sub(r'([\u0A66-\u0A6F]+) (,) ([\u0A66-\u0A6F]+) (,) ([\u0A66-\u0A6F]+)',r'\1\2\3\4\5',line)
        line = re.sub(r'([\u0A66-\u0A6F]+) (,) ([\u0A66-\u0A6F]+)',r'\1\2\3',line)

        # For Punjabi letters and english digits
        line = re.sub(r'([\u0A00-\u0A7F]+)([0-9]+)',r'\1 \2',line)
        line = re.sub(r'([0-9]+)([\u0A00-\u0A7F]+)',r'\1 \2',line)

        # For Punjabi letters and english letters
        line = re.sub(r'([\u0A00-\u0A7F]+)([a-zA-Z])',r'\1 \2',line)
        line = re.sub(r'([a-zA-Z])([\u0A00-\u0A7F]+)',r'\1 \2',line)

        # separate Punjabi numbers and letters
        line = re.sub(r'([\u0A66-\u0A6F])([\u0A00-\u0A5E])',r'\1 \2',line)
        line = re.sub(r'([\u0A00-\u0A5E])([\u0A66-\u0A6F])',r'\1 \2',line)




        line = re.sub('\\s+',' ',line)
        line = line.strip()
        
        # print('cleaned_line:'.line)
        # file.write(line+'\n')
        return line







