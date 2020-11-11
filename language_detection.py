#MULTIPLE LANGUAGE DETECTION 

from googletrans import Translator, LANGUAGES
#LANGUGAES is an in-built dictionary in googletrans with keys as codes and values as language names.

translator= Translator()

#Creating an empty list to store input sentences
input_sentences = [] 

print("ENTER TEXT:")

#Take multiline or single line input from user
while True:
    line = input()
    if(line):
        input_sentences.append(line)
    else:   #If line is empty, break loop
        break

heading= ['Language Code', 'Input Sentence']
format_text= '{:25}' *(len(heading)+1)

print('\n',format_text.format('Language Name', *heading), '\n', '='*120)

for data in input_sentences:
    try:
        detection= translator.detect(data)
        sentence= [LANGUAGES.get(detection.lang).title(), detection.lang, data]
		#detection consists of language code and confidence.
		#detection.lang gives language code.
		#LANGUAGE.get(detection.lang) gives the language name corresponding to the code from dict.
		#language name in dict is in lowercase, therefore printing in title format using title method.
        print(format_text.format(*sentence))
    except:
        detection= 'error'
        print(format_text.format('Not Detected', 'Not Detected', data))