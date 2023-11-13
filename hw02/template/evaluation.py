#-------------------------------------------------------------------------
#  BI-ZNS: Šablona pro úlohu Inferenční systém s dopředným řetězením
#  (c) 2022 Ladislava Smítková Janků <ladislava.smitkova@fit.cvut.cz>
#
#-------------------------------------------------------------------------

import parser
import tfact
import truleitem
import trule

def solve( facts, rules, atoms):
	# ======================================================================
	# Zde doplňte vhodný kód, který provede doplnění faktů v seznamu facts.
	# Seznam rules obsahuje pravidla a vektor atoms seznam všech atomů.
	# Po dokončení této procedury musí být v seznamu facts všechny fakty,
	# které lze podle daných pravidel odvodit.
	# Při implementaci se nemusíte omezovat pouze na tuto funkci. Pokud se
	# vám to hodí, upravte si (třeba v zájmu unifikace) i třídu TRule.
	# ======================================================================
   
    new_facts = facts.copy()   
    for rule in rules:
        rule.print()
        print()

"""
    Často kladené otázky
     --------------------

Jak přidám fakt?

	facts.append( tfact.TFact('zvire(slon)'))

Jak projdu (a vypíšu) všecha pravidla uložená ve vektoru rules?

	for rule in rules:
		rule.print()
		print()


Jak zjistím počet argumentů pravidla?

	numOfRuleArgs = rules[0].argNum()
	print( numOfRuleArgs)

Jak vyhodnotím pravidlo ?

	rule = rules[0]
	argNames = ['tony','abe']
	newFact = rule.evaluate( argNames, facts)
	if newFact is None:
		print("None.")
	else:
		newFact.print()
		print()

    Pokud je newFact None, potom nelze pravidlo vyhodnotit.
    V opačném případě je vrácen důsledek pravidla.
    Parametr argNames obsahuje vektor s dosazovanými atomy.
    Parametr facts obsahuje všechny doposud známé fakty.

Jak porovnám dva fakty?

	print( f.compare(f))	# napíše True

    Porovnává se název faktů i názvy jejich parametrů.

Jak jsou pravidla v paměti organizovaná?

    Všechna pravidla jsou uložena v seznamu instancí třídy TRule.
    Každé pravidlo (třída TRule) obsahuje seznam instancí třídy TRuleItem.
    Tento seznam vytvořil parser tak, aby namodeloval chování pravidla.
    Zjednodušeně řečeno se jedná o sekvenci faktů a operací. Tato sekvence
    se prochází při každém vyhodnocování pravidla.

Jak zjistím seznam predikátů použitých v pravidle?

    Upravte si třídu TRule podle svých záměrů.
    Pro predikáty se používá třída TFact, stejně jako pro fakty.
    Jsou schované ve třídě TRuleItem v instancích, které mají nastavený
    typ na R_FACT. Typ zjistíte voláním TRuleItem.getType().
    
"""
