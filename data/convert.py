#!/usr/bin/python

from pcaxis import parsePX
import csv

def get_dataset(fn):
    fd = open('stat/' + fn)
    data = fd.read()
    fd.close()
    d = parsePX(data, encoding='cp1250')
    return d

if __name__ == "__main__":
    imena_fd = open('csv/imena.csv', 'wb')
    imena_csv = csv.writer(imena_fd)

    for fn in ['05X1005S.px', '05X1010S.px']:
        d = get_dataset(fn)
        imena = d['VALUES']['IME']
        #print len(imena)
        for i in imena:
            imena_csv.writerow([i.encode('utf-8')])

    imena_fd.close()

    priimki_fd = open('csv/priimki.csv', 'wb')
    priimki_csv = csv.writer(priimki_fd)

    for fn in ['05X1015S.px', '05X1016S.px', '05X1017S.px', '05X1018S.px']:
        d = get_dataset(fn)
        priimki = d['VALUES']['PRIIMEK']
        #print len(priimki)
        for i in priimki:
            priimki_csv.writerow([i.encode('utf-8')])

    priimki_fd.close()

