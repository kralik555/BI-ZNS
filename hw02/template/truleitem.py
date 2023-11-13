#-------------------------------------------------------------------------
#
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

import tfact

class TRuleItemType:
	R_FACT = 0
	R_NOT = 1
	R_AND = 2
	R_OR = 3
	R_EQUAL = 4

#-------------------------------------------------------------------
class TRuleItem:
	def __init__(self, args):
		self._itemType = TRuleItemType
		self._fact = None
		self._leftAtom = ''
		self._rightAtom = ''

		if isinstance( args, list):
			self._itemType = TRuleItemType.R_EQUAL
			self._leftAtom = args[0]
			self._rightAtom = args[1]
		else:
			if isinstance( args, int):
				self._itemType = args
			elif isinstance( args, tfact.TFact):
				self._itemType = TRuleItemType.R_FACT
				self._fact = args
			else:
				raise NameError('Chybne zadane argumenty kontruktoru TRuleItem.')
	
	def print( self):
		if self._itemType == TRuleItemType.R_FACT:
			self._fact.print()
		elif self._itemType == TRuleItemType.R_NOT:
			print('not', end='')
		elif self._itemType == TRuleItemType.R_AND:
			print('and', end='')
		elif self._itemType == TRuleItemType.R_OR:
			print('or', end='')
		elif self._itemType == TRuleItemType.R_EQUAL:
			print('(' + self._leftAtom + '=' + self._rightAtom + ')', end='')
		
	def updateListOfArguments( self, aList):
		if self._itemType == TRuleItemType.R_FACT:
			a = self._fact.getArguments()
			for i in a:
				if not(i in aList):
					aList.append(i)
		elif self._itemType == TRuleItemType.R_EQUAL:
			if not(self._leftAtom in aList):
				aList.append( self._leftAtom)
			if not(self._rightAtom in aList):
				aList.append( self._rightAtom)
	
	@property
	def itemType( self):
		return self._itemType

	def translateFact( self, dictionary):
		if self._itemType != TRuleItemType.R_FACT:
			return None;
		return self._fact.translate( dictionary)

	def compareAtoms( self, dictionary):
		return dictionary[ self._leftAtom] == dictionary[ self._rightAtom]
