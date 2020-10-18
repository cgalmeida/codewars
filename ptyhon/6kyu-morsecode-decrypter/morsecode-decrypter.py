 #morsecode-decrypter.py
class Tree:

	def __init__(self, data, left=None, right=None):

		self.data = data
		self.left = left
		self.right = right

	# print object
	def __str__(self):
		return str(self.data)


def decodeMorse(morse_code):

	#initializes binary tree with morse code
	morseTree = Tree('',
		Tree('E',
			Tree('I',
				Tree('S',Tree('H','5','4'),Tree('V', Tree('SN',None,'SK'),Tree('3',None,Tree('',Tree('',Tree('',Tree('SOS')),None),None)))),
				Tree('U','F',Tree('',Tree('','?','_'),Tree('2')))),
			Tree('A', Tree('R', Tree('L','AS',Tree('','"',None)), Tree('AA', Tree('+',None,'.'), None)), Tree('W', Tree('P',None,Tree('','@',None)), Tree('J', None, '1')))),
		Tree('T',
			Tree('N',
				Tree('D', Tree('B', Tree('6',None,'-'), Tree('=',Tree('',None,'BK'),None)), Tree('X', Tree('/'), Tree('',None,'DO'))),
				Tree('K',
					Tree('C',Tree('CT',None,Tree('',Tree('','CL',None),None)),Tree('',';','!')),
					Tree('Y',Tree('KN',None,')'),None))),
			Tree('M',
				Tree('G', Tree('Z', Tree('7'), Tree('',None,',')), Tree('Q')), Tree('O', Tree('', Tree('8',None,Tree(':')), None), Tree('', Tree('9'), Tree('0'))))))


	actual = morseTree

	decCodeLst = " "
	morse_code = morse_code.lstrip().replace('   '," *** ").strip()
	for wrd in morse_code.split():
	    if wrd == '***':
	        decCodeLst += str(" ")
	        
	    else:
	        for c in wrd:
	            if actual:
	                if c is '.':
	                    if actual.left:
	                        actual = actual.left
	                elif c is '':
	                    actual = actual
	                elif actual.right:
	                    actual = actual.right
	        if actual:
	        	decCodeLst += str(actual)
	        actual = morseTree
	        

	# ToDo: Accept dots, dashes and spaces, return human-readable message
	#return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
	
	#format and return
	return decCodeLst.lstrip()
