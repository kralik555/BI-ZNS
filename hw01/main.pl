% (c) FIT CVUT 
% BI-ZNS ZS2023
% Jakub Král
% Řešení 1. domácí úlohy

% hlavni telo programu, tento kod je zodpovedny za vypsani textu uvadejiciho uzivatele do problematiky, volani dotazu a vypis reseni

main :- identifikace.

identifikace:-
  retractall(known(_,_,_,_)),       
  writeln('Vítá vás jednoduchý expertní systém na kontrolu účtenek.'),
    writeln('Prosím odpovídejte na dotazy ano nebo ne. Každou odpověď je třeba zakončit tečkou.'), nl,
  chyba(X), nl,
  write('V účtence se vyskytuje chyba: '), write(X),  write('.'), nl.
identifikace:-
  write('Účtenka je v pořádku.').

% ----------------------
% Báze znalostí
% ----------------------

chyba("Neplatné IČO odběratele"):-
	je_na_dokladu("IČO odběratele"),
	algo_chyba("IČO odběratele").

chyba("Chybná celková částka"):-
	je_na_dokladu("celková částka jiná než celkový součet všech položek").

chyba("Chybí rekapitulace DPH"):-
	typ("Daňový dkolad")->
	chybi_na_dokladu("rekapitulace DPH");
	chybi_na_dokladu("sazba DPH pro celkovou částku").

chyba("Chyba v datu"):-
	datum("2021").

chyba("Chybí údaje o dodavateli"):-
	chybi_na_dokladu("IČO dodavatele");
	\+typ("Zjednodušený doklad")->
	chybi_na_dokladu("DIČ dodavatele").

chyba("Chybné sazby DPH"):-
	jsou_uctovany("potraviny")->
	\+sazba_dph("10 %");
	sazba_dph("10 %")->
	konzumovany("v prostorách dodavatele").

chyba("Chybí údaje o zápisu do živnostenského nebo obchodního rejstříku"):-
	chybi_na_dokladu("údaje o zápiso dodavatele do obchodního nebo živnostenského rejstříku").

chyba("Chybí číslo dokladu"):-
	chybi_na_dokladu("číslo dokladu").

chyba("Chybné IČO odběratele"):-
	algo_chyba("IČO odběratele").

chyba("Chybné DIČ odběratele"):-
	algo_chyba("DIČ odběratele").

chyba("Chybné DIČ odběratele"):-
	typ("Daňový doklad"),
	typ("Zjednodušený doklad"),
	algo_chyba("DIČ odběratele").

chyba("Chybí datum uskutečnění zdanitelného plnění"):-
	chybi_na_dokladu("datum vystavení dokladu").

chyba("Zjednodušený daňový doklad s částkou přesahující 10 000 Kč"):-
	typ("Zjednodušený doklad"),
	castka("10 000 Kč").


typ("Daňový doklad"):-
	je_na_dokladu("IČO dodavatele").

typ("Zjednodušený doklad"):-
	je_na_dokladu("DIČ odběratele").
% ----------------------
% Uživatelské rozhraní
% ----------------------

% ziskani hodnoty atributu od uzivatele

je_na_dokladu(X):- dotaz("Je na účtence ", ico_odb, X).
algo_chyba(X):- dotaz("Je na účtence podle algoritmu špatně ", alog_chyba, X).
chybi_na_dokladu(X):- dotaz("Chybí na dokladu ", chybi_na_dokladu, X).
datum(X):- dotaz("Je rok v datu na účtence jiný než ", datum, X).
jsou_uctovany(X):- dotaz("Jsou účtovány ", jsou_uctovay, X).
sazba_dph(X):- dotaz("Je sazba DPH na účtence ", sazba_dph, X).
konzumovany(X):- dotaz("Jsou položky v sazbě DPH 10 % konzumovány ", konzumovany, X).
castka(X):- dotaz("Je částka na dokladu vyšší než ", castka, X).

% uzivatelske rozhrani, implementace klauzule dotaz
             
% otestuje, zda je zaznam odpovedi ano pro danou kombinaci atributu a hodnoty jiz v bazi faktu
dotaz(O,X,Y):-
  known(ano,O,X,Y),  !.       
                           
% otestuje, zda je zaznam odpovedi ne pro danou kombinac atribut a hodnoty jiz v bazi faktu
dotaz(O,X,Y):-
  known(ne,O, X,Y),     
  !, fail.
   
     
% otestuje, zda je v bazi faktu zaznam odpovedi ano pro dany atribut bez ohledu na jeho hodnotu

dotaz(O,X,_):-
  known(ano,O,X,_),  !, fail.


% dotaz, zobrazi otazku a nacte hodnotu ze vstupu
dotaz(O,X,Y):-
write(O), write(Y),
write('? (ano nebo ne): '),
read(A),                          
asserta(known(A,O,X,Y)),            
A = ano. 
