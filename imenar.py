#!/usr/bin/python

import csv
import re

IME = 1
PRIIMEK = 2
PRVA_IME = 1
PRVA_PRIIMEK = 2

def get_dataset():
    ir = open('data/csv/imena.csv')
    imena = [i.decode('utf-8').upper().strip() for i in ir]

    pr = open('data/csv/priimki.csv')
    priimki = [i.decode('utf-8').upper().strip() for i in pr]

    return imena, priimki

def test_algo(func, use_hint=False):
    rdr = csv.reader(open('data/test.csv'))
    score = 0
    maxscore = 0
    hint = None
    for line in rdr:
        ime, priimek = [i.decode('utf-8').upper() for i in line]
        
        compound1 = u'%s %s' % (ime, priimek)
        compound2 = u'%s %s' % (priimek, ime)
        maxscore += 2
        
        if use_hint:
            hint = PRVA_IME
        ime2, priimek2 = func(compound1, hint=hint)
        if ime2 == ime and priimek2 == priimek:
            score += 1
        
        if use_hint:
            hint = PRVA_PRIIMEK
        ime2, priimek2 = func(compound2, hint=hint)
        if ime2 == ime and priimek2 == priimek:
            score += 1
    
    print '%.7f\t%s\t%s' % (float(score)/maxscore, use_hint, func.__name__)
    
    return float(score) / maxscore

def split_left(s, hint=None):
    return [i.strip() for i in s.split(' ', 1)]

def split_right(s, hint=None):
    return [i.strip() for i in s.rsplit(' ', 1)]

def _make_lookup():
    rdr = csv.reader(open('data/test.csv'))
    lookup_dict = {}
    for line in rdr:
        ime, priimek = [i.decode('utf-8').upper() for i in line]
        lookup_dict[u'%s %s' % (ime, priimek)] = (ime, priimek)
        lookup_dict[u'%s %s' % (priimek, ime)] = (ime, priimek)

    def lookup(s, hint=None):
        return lookup_dict[s]
    return lookup
lookup = _make_lookup()

def _make_stat_lookup():
    imena, priimki = get_dataset()

    imena_dict = {i: 1 for i in imena}
    priimki_dict = {i: 1 for i in priimki}
    space_re = re.compile('\s+')

    #print 'VCS', u'\u010cADONI\u010c \u0160PELI\u010c' in priimki_dict
    #print 'VCS1', u'\u010cADONI\u010c' in priimki_dict
    #print 'VCS2', u'\u0160PELI\u010c' in priimki_dict

    def lookup_stat(s, hint=None):
        possibles = []
        startpos = 0
        m = space_re.search(s, startpos)
        while m:
            icand = s[:m.start()]
            pcand = s[m.end():]
            #print [icand, pcand]
            #print [icand in imena_dict, pcand in priimki_dict]
            if icand in imena_dict and pcand in priimki_dict:
                possibles.append((icand, pcand))

            icand = s[m.end():]
            pcand = s[:m.start()]
            #print [icand, pcand]
            #print [icand in imena_dict, pcand in priimki_dict]
            #import pdb; pdb.set_trace()
            if icand in imena_dict and pcand in priimki_dict:
                possibles.append((icand, pcand))
            startpos = m.end() + 1
            #print 'woo', [startpos, s]
            m = space_re.search(s, startpos)
            
        if len(possibles) == 1:
            return possibles[0]
        else:
            #print possibles
            #raise
            return (u'', u'')
    return lookup_stat
lookup_stat = _make_stat_lookup()

def _make_stat_advlookup():
    imena, priimki = get_dataset()

    imena_dict = {i: 1 for i in imena}
    priimki_dict = {i: 1 for i in priimki}
    space_re = re.compile('\s+')

    class Tag(object):
        def __init__(self, s, tip):
            self.s = s
            self.tip = tip

    def lookup_stat_adv(s, hint=None):
        possibles = []
        startpos = 0
        m = space_re.search(s, startpos)
        while m:
            icand = s[:m.start()]
            pcand = s[m.end():]
            #print [icand, pcand]
            #print [icand in imena_dict, pcand in priimki_dict]
            if icand in imena_dict and pcand in priimki_dict:
                possibles.append((Tag(icand, tip=PRVA_IME), Tag(pcand, tip=PRVA_IME)))

            icand = s[m.end():]
            pcand = s[:m.start()]
            #print [icand, pcand]
            #print [icand in imena_dict, pcand in priimki_dict]
            #import pdb; pdb.set_trace()
            if icand in imena_dict and pcand in priimki_dict:
                possibles.append((Tag(icand, tip=PRVA_PRIIMEK), Tag(pcand, tip=PRVA_PRIIMEK)))
            startpos = m.end() + 1
            #print 'woo', [startpos, s]
            m = space_re.search(s, startpos)
            
        if len(possibles) == 1:
            return [i.s for i in possibles[0]]
        elif len(possibles) == 2:
            if hint is not None:
                if hint == PRVA_IME:
                    possibles2 = [i for i in possibles if i[0].tip == PRVA_IME]
                    if possibles2[0][0].tip == PRVA_IME:
                        return [i.s for i in possibles2[0]]
                if hint == PRVA_PRIIMEK:
                    possibles2 = [i for i in possibles if i[0].tip == PRVA_PRIIMEK]
                    if possibles2[0][0].tip == PRVA_PRIIMEK:
                        return [i.s for i in possibles2[0]]
            return (u'', u'')
        else:
            print s, possibles
            #raise
            return (u'', u'')
    return lookup_stat_adv
lookup_stat_adv = _make_stat_advlookup()

if __name__ == "__main__":
    
    print 'score\t\thint\tfunc'
    for hint in [False, True]:
        print '-'*40
        for algo in [
                lookup,
                lookup_stat_adv,
                lookup_stat,
                split_left,
                split_right]:
            test_algo(algo, use_hint=hint)
    
    imena, priimki = get_dataset()
