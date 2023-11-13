#-------------------------------------------------------------------------
#
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

import parser

class TFact:
	def __init__(self,args):
		self._arguments = []
		self._id = ''

		if args is None:
			return
			
		if isinstance( args, str):
			factOrig = args
			flist = list( args)
			p = parser.parse( flist)

			parser.check( parser.TParserProductType.P_IDENT, p, factOrig)
			self._id = p.value

			p = parser.parse( flist)
			parser.check( parser.TParserProductType.P_LEFT, p, factOrig);
			while True:
				p = parser.parse( flist)
				parser.check( parser.TParserProductType.P_IDENT, p, factOrig)
				self._arguments.append( p.value)

				p = parser.parse( flist)
				if p.productType == parser.TParserProductType.P_RIGHT:
					break
					
				parser.check( parser.TParserProductType.P_COMMA, p, factOrig)

			p = parser.parse( flist)
			parser.check( parser.TParserProductType.P_NULL, p, factOrig)
			
		else:
			if isinstance( args, list):
				self._id = args[0];
				if isinstance( args[1], list):
					self._arguments = args[1]
				else:
					self._arguments = []
					flist = list( args[1])
					while True:
						p = parser.parse( flist)
						parser.check( parser.TParserProductType.P_IDENT, p, args[1])
						self._arguments.append( p.value)

						p = parser.parse( flist)
						if (p.productType == parser.TParserProductType.P_RIGHT):
							break
						parser.check( parser.TParserProductType.P_COMMA, p, args[1])

	def getName( self):
		return self._id

	def getNumberOfArguments( self):
		return len( self._arguments)
		
	def getArguments( self):
		return self._arguments
		
	def translate( self, dictionary):
		args = []
		for a in self._arguments:
			args.append( dictionary[a])
		return TFact([self._id, args])

	def compare( self, fact):
		if self._id != fact.getName():
			return False
		args = fact.getArguments()
		if len( args) != len( self._arguments):
			return False;
		j = 0
		for i in self._arguments:
			if i != args[j]:
				return False;
			j = j + 1;
		return True;

	def print( self):
		print( self._id + '(', end='')
		prvni = True
		for i in self._arguments:
			if prvni:
				prvni = False
				print( i, end='')
			else:
				print(',' + i, end='')
		print(')', end='');

	def load( self, newId, src):
		self._arguments = []
		self._id = newId
		srcTxt = ""
		srcTxt = srcTxt.join(src)
		while True:
			p = parser.parse( src)
			parser.check( parser.TParserProductType.P_IDENT, p, srcTxt)
			self._arguments.append( p.value)

			p = parser.parse( src)
			if (p.productType == parser.TParserProductType.P_RIGHT):
				break
			parser.check( parser.TParserProductType.P_COMMA, p, srcTxt)
		
	def loadAll( self, src):
		self._arguments = []
		factOrig = ""
		factOrig = factOrig.join( src)

		p = parser.parse( src)

		parser.check( parser.TParserProductType.P_IDENT, p, factOrig)
		self._id = p.value

		p = parser.parse( src)
		parser.check( parser.TParserProductType.P_LEFT, p, factOrig);
		while True:
			p = parser.parse( src)
			parser.check( parser.TParserProductType.P_IDENT, p, factOrig)
			self._arguments.append( p.value)

			p = parser.parse( src)
			if p.productType == parser.TParserProductType.P_RIGHT:
				break
				
			parser.check( parser.TParserProductType.P_COMMA, p, factOrig)

		p = parser.parse( src)
		parser.check( parser.TParserProductType.P_NULL, p, factOrig)
