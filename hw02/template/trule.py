#-------------------------------------------------------------------------
#
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

import parser
import tfact
import truleitem

class TRule:   
	def __init__(self, rule):

		self._ruleItems = []
		self._ruleFact = None
		self._listOfArguments = []

		ident = ""
		p = parser.TParserData
		rule = list( rule)

		while True:
			p = parser.parse( rule)
			parser.check( parser.TParserProductType.P_IDENT, p, rule)
			ident = p.value
			
			if ident == "not":
				self._ruleItems.append( truleitem.TRuleItem( truleitem.TRuleItemType.R_NOT));
			else:
				p = parser.parse( rule)
				if p.productType == parser.TParserProductType.P_NOTEQUAL:
					self._ruleItems.append( truleitem.TRuleItem( truleitem.TRuleItemType.R_NOT))
					p.productType = parser.TParserProductType.P_EQUAL
					
				if p.productType == parser.TParserProductType.P_EQUAL:
					leftAtom = ident;
					p = parser.parse( rule)
					parser.check( parser.TParserProductType.P_IDENT, p, rule)
					ident = p.value
					self._ruleItems.append( truleitem.TRuleItem([ leftAtom, ident ]))
				else:
					parser.check( parser.TParserProductType.P_LEFT, p, rule)
					f = tfact.TFact(None);
					f.load( ident, rule);
					self._ruleItems.append( truleitem.TRuleItem(f))

				p = parser.parse( rule)
				parser.check( parser.TParserProductType.P_IDENT, p, rule)
				ident = p.value

				if ident == "then":
					break
				if ident == "and":
					self._ruleItems.append( truleitem.TRuleItem( truleitem.TRuleItemType.R_AND))
				elif ident == "or":
					self._ruleItems.append( truleitem.TRuleItem( truleitem.TRuleItemType.R_OR))
				else:
					raise NameError('Missing then/and/or');
			
		# then
		self._ruleFact = tfact.TFact( None)
		self._ruleFact.loadAll( rule)

		p = parser.parse( rule)
		parser.check( parser.TParserProductType.P_NULL, p, rule)

		for r in self._ruleItems:
			r.updateListOfArguments( self._listOfArguments)

		# check for unknown arguments in the fact
		args = self._ruleFact.getArguments()
		for r in args:
			if not( r in self._listOfArguments):
				raise NameError('Unknown atom "' + r + '" in the argument of the fact.')
	
	def print( self):
		prvni = True
		for i in self._ruleItems:
			if not prvni:
				print(' ', end='')
			else:
				prvni = False
			i.print()
		print(' => ', end='')
		self._ruleFact.print()
		
	def argNum( self):
		return len( self._listOfArguments)
	
	def evaluate( self, args, facts):
		if len( args) != len( self._listOfArguments):
			raise NameError("Internal error: Size of the vector passed as parameter to TRule::evaluate() and size of listOfArguments must be same.")

		dictionary = dict()
		i = 0
		for k in self._listOfArguments:
			dictionary[k] = args[i]
			i = i + 1

		negation = False
		result = True

		for r in self._ruleItems:
			if r.itemType == truleitem.TRuleItemType.R_FACT:
				tf = r.translateFact( dictionary)

				result = False
				for f in facts:
					if f.compare(tf):
						result = True
						break;					
				
				if negation:
					negation = False
					result = not result

			elif r.getType == truleitem.TRuleItemType.R_NOT:
				negation = not negation
				
			elif r.getType == truleitem.TRuleItemType.R_AND:
				if not result:
					return None

			elif r.getType == truleitem.TRuleItemType.R_OR:
				if not result:
					return None
					
			elif r.getType == truleitem.TRuleItemType.R_EQUAL:
				result = r.compareAtoms( dictionary)
				if negation:
					negation = False
					result = not result

		if not result:
			return None

		return self._ruleFact.translate( dictionary)
		

#-------------------------------------------------------------------
def createListOfAtoms( facts):
	atoms = []
	atomsInFact = []

	for f in facts:
		atomsInFact = f.getArguments()
		for a in atomsInFact:
			if not( a in atoms):
				atoms.append(a)
	return atoms

