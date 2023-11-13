#-------------------------------------------------------------------------
#
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

import parser
import tfact
import truleitem
import trule
import evaluation
import debug
import sys

def printFacts():
    print("[facts]");
    for f in facts:
        f.print()
        print('')
    print('')

def printRules():
    print("[rules]");
    for r in rules:
        r.print()
        print('')
    print('')

def printAtoms():
	print("[atoms]");
	for a in atoms:
		print(a)
	print('')

def loadRule( line):
	lineOrig = line
	line = list(line)
	p = parser.parse( line)
	parser.check( parser.TParserProductType.P_IDENT, p, lineOrig);
	if p.value != "if":
		# this is a fact
		facts.append( tfact.TFact( lineOrig))
		return
	# this is a rule
	try:
		rules.append( trule.TRule( line));
	except NameError as error:
		print("Parse error on this rule: " + lineOrig + ':')
		raise

def createListOfAtoms():
	for f in facts:
		atomsInFact = f.getArguments()
		for a in atomsInFact:
			if not( a in atoms):
				atoms.append(a)

#==========================================================================

facts = []
rules = []
atoms = []

if len( sys.argv) != 2:
	print("Usage: ./predikaty <rules.txt>")
	exit(1)

try:
	#debug.forTestPurposesOnly()
	
	with open( sys.argv[1]) as f:
		lines = f.readlines()

	for l in lines:
		l = l.strip()
		if l != '':
			loadRule( l.strip())

	createListOfAtoms()
	
	printAtoms()
	printFacts()
	printRules()

	print('---- solve ----')
	evaluation.solve( facts, rules, atoms);
	print('---- /solve ----')

	printFacts();
        
except NameError as error:
	print("Chyba: " + str( error))
