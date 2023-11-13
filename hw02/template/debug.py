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

def forTestPurposesOnly():
	print('------------------')
	f = tfact.TFact('father(tony,abe)')
	f2 = tfact.TFact(['f2',f.getArguments()])
	f3 = tfact.TFact(['f3','x,y,z)'])
	d = dict()
	d['x'] = 'a'
	d['y'] = 'b'
	d['z'] = 'c'
	f4 = f3.translate(d)
	f.print()
	print()
	f2.print()
	print()
	f3.print()
	print()
	f4.print()
	print()
	print( f4.compare(f4))

	f5 = tfact.TFact(None)
	f5.load('hastrman',['x',',','y',')'])
	f5.print()
	print()

	f6 = tfact.TFact(None)
	f6.loadAll([' ','h','a','s','t','r','m','a','n','(','x',',','y',')'])
	f6.print()
	print()
	
	r = truleitem.TRuleItem(['x','y'])
	r.print()
	print()
	r = truleitem.TRuleItem( truleitem.TRuleItemType.R_AND)
	r.print()
	print()
	r3 = truleitem.TRuleItem( f3)
	r3.print()
	print()
	r4 = truleitem.TRuleItem( f4)
	r4.print()
	print()
	
	a = [];
	r3.updateListOfArguments(a)
	r4.updateListOfArguments(a)
	print(a)
	
	r = trule.TRule(' f1(x,y) then f2(x,y)')
	r.print()
	print()
	
	r = trule.TRule(' f1(x) or f2(y) and x\=y then f3(x,y)')
	r.print()
	print()
	print('------------------')
