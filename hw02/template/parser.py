#-------------------------------------------------------------------------
#
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

class TParserProductType:
	P_NULL = 0
	P_LEFT = 1
	P_RIGHT = 2
	P_COMMA = 3
	P_IDENT = 4
	P_EQUAL = 5
	P_NOTEQUAL = 6

class TParserData:
    productType: TParserProductType
    value: str


def parse( source):

	p = TParserData

	while (len( source) > 0) and (source[0] == ' '):
		del source[0]

	if (len( source) == 0):
		p.productType = TParserProductType.P_NULL
	else:
		if (source[0] == '('):
			p.productType = TParserProductType.P_LEFT
			del source[0]
		elif (source[0] == ')'):
			p.productType = TParserProductType.P_RIGHT
			del source[0]
		elif (source[0] == ','):
			p.productType = TParserProductType.P_COMMA
			del source[0]
		elif (source[0] == '='):
			p.productType = TParserProductType.P_EQUAL
			del source[0]
			if (len( source) == 0):
				raise NameError('Parser: argument is NULL')
			if (source[0] == '='):
				del source[0]
		elif (source[0] == '\\'):
			p.productType = TParserProductType.P_NOTEQUAL
			del source[0]
			if (len( source) == 0):
				raise NameError('Parser: argument is NULL')
			if (source[0] != '='):
				raise NameError('Parser: Probably you mean "\\=".')
			del source[0]
		else:
			if (((source[0] >= 'A') and (source[0] <= 'Z')) or ((source[0] >= 'a') and (source[0] <= 'z')) or ((source[0]) == '_')):
				num = 1;
				p.value = source[0];
				del source[0]

				while (len( source) > 0) and \
					   (((source[0] >= 'A') and (source[0] <= 'Z')) or \
					    ((source[0] >= 'a') and (source[0] <= 'z')) or \
					    ((source[0] >= '0') and (source[0] <= '9')) or \
					    ((source[0]) == '_')):
					p.value = p.value + source[0];
					del source[0]
				
				p.productType = TParserProductType.P_IDENT
			
			else:
				raise NameError('Parser: syntax error\nhere --> ' + str( source));
	return p
	

def check( exceptedType, data, line):
	if (exceptedType != data.productType):
		
		if isinstance( line, str):
			tmp = line
		else:
			tmp = ""
			tmp = tmp.join(line)
			
		if (exceptedType == TParserProductType.P_LEFT):
			raise NameError('Syntax error: Left bracket is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_RIGHT):
			raise NameError('Syntax error: Right bracket is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_COMMA):
			raise NameError('Syntax error: Comma is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_IDENT):
			raise NameError('Syntax error: An identifier is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_NULL):
			raise NameError('Syntax error: End of line is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_EQUAL):
			raise NameError('Syntax error: "=" is excepted: ' + tmp)
		if (exceptedType == TParserProductType.P_NOTEQUAL):
			raise NameError('Syntax error: "\\=" is excepted: ' + tmp)
