Imenar
======

Funkcije, ki razdelijo skupno polje `ime_priimek` na ločeni `ime, priimek`. Funkcije vzamejo po dva parametra, string in hint. String je vrednost polja `ime_priimek`. Neobvezni parameter `hint` je `imenar.PRVA_IME` ali `imenar.PRVA_PRIIMEK`, ki algoritmu poda namig kaj je prvo v polju.

Priporoča se raba funkcije `lookup_stat_adv`.

Primer rabe::

	>>> import imenar
	>>> imenar.lookup_stat_adv(u'Gazvoda Nejc')
	[u'Nejc', u'Gazvoda']
	>>> imenar.lookup_stat_adv(u'Nejc Gazvoda')
	[u'Nejc', u'Gazvoda']
	>>> imenar.lookup_stat_adv(u'Marica Gregorič-Stepančič')
	[u'Marica', u'Gregori\u010d Stepan\u010di\u010d']
	>>> imenar.lookup_stat_adv(u'Goljevšček Kermauner Alenka')
	[u'Alenka', u'Goljev\u0161\u010dek Kermauner']


Funkcije in uspešnost::

	score           hint    func
	----------------------------------------
	0.9923077       False   lookup
	0.9567308       False   lookup_stat_adv
	0.9096154       False   lookup_stat
	0.4903846       False   split_left
	0.4692308       False   split_right
	----------------------------------------
	0.9923077       True    lookup
	0.9740385       True    lookup_stat_adv
	0.9096154       True    lookup_stat
	0.4903846       True    split_left
	0.4692308       True    split_right

