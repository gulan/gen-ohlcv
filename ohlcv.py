#! /usr/bin/env python3

import argparse
import calendar
import datetime
import random
import sys
import time

# TBD: Replace hard-coded parameters with program arguments.
# TBD: Decouple data generation from output file formatting.
# TBD: Use a model to generate more realistic data.
# TBD: Make app-specific date/time interface.

random.seed(1701)
R = (9*100, 999*100)  # dollar range

def gentimes(year=2014):
    '''yield unix time for every hour in 2014'''
    for m in range(1,13):
        (_,numdays) = calendar.monthrange(year,m)
        for d in range(1,numdays+1):
            for h in range(0,24):
                dt = datetime.datetime(year,m,d,hour=h)
                ts = calendar.timegm(dt.timetuple())
                dt_ = time.gmtime(ts)
                yield (dt,ts)

def genrec(openp):
    '''make-up currency values for one record'''
    highp = random.randint(*R)
    lowp = random.randint(9*100, highp)
    closep = random.randint(lowp, highp)
    volumep = random.randint(10000,100000)
    return (highp, lowp, closep, volumep)

def mkrecs():
    # The opening time is the previous closing time.
    openp = random.randint(*R)
    for (_,ts) in gentimes():
        (hi,lo,cl,vo) = genrec(openp)
        yield (ts, openp, hi, lo, cl, vo)
        openp = cl

def mksql():
    # Despite appearances, there is no opportunity for SQL injection here.
    for i in mkrecs():
        template = 'insert into ohlcv values (%s,%s,%s,%s,%s,%s);'
        print (template % i)

def mkhaskell():
    # The output also happens to be valid python.
    # TBD: be more clever with indenting the generated code.
    a = [','.join(str(t) for t in s) for s in mkrecs()]
    m = ['[%s]' % u for u in a]
    s = 'ohlcv = [' + m[0] + ','
    print (s)
    for i in range(1,len(m)-1):
        print ('         %s,' % m[i])
    print ('         %s]' % m[-1])


if __name__ == '__main__':
    # TBD: many other data formats are simple to add.
    p = argparse.ArgumentParser(description='Generate OHLCV test data.')
    p.add_argument(
        'language',
        help="write data in 'sql' or 'haskell' format")
    p.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0')
    args = p.parse_args()
    if args.language == 'sql':
        mksql()
    elif args.language == 'haskell':
        mkhaskell()
    else:
        fmt = '%s: error: unrecognised language: %s'
        print (fmt % (p.prog, args.language), file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
