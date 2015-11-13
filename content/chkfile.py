#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import exists
from datetime import datetime
import time
from traceback import print_exc
import re
from pdb import set_trace


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pbold(s):
    return bcolors.OKBLUE + s + bcolors.ENDC


def pwarn(s):
    return bcolors.WARNING + s + bcolors.ENDC


begint = datetime.fromordinal(datetime.now().toordinal() - 1)
srcpath = '/home/gilbert/repos/rating/result/'


def gett(fi):
    try:
        return time.ctime(os.path.getmtime(fi))
    except:
        return 0


def watch(fis, dstpaths):
    def chk(mainfi, srcpath, dstpath, fidic):
        print bcolors.HEADER, mainfi, bcolors.ENDC
        [chkfi(srcpath, dstpath, fi, fidic) for fi in reads(mainfi)]

    t0 = {fi: gett(fi) for fi in fis}
    fidics = {}
    for fi, dstpath in zip(fis, dstpaths):
        fidics[fi] = {}
        chk(fi, srcpath, dstpath, fidics[fi])

    def chking(fi, dstpath):
        t1 = gett(fi)
        if t1 != t0[fi]:
            print datetime.now().strftime('%H:%M:%S')
            try:
                chk(fi, srcpath, dstpath, fidics[fi])
                os.chdir('..')
                os.system('make html')
                os.chdir('content')
                t0[fi] = t1
            except:
                print_exc()

    while 1:
        map(chking, fis, dstpaths)
        time.sleep(1)


def reads(fi):
    keys = [
        re.compile('\{filename\}/?([\/\w\.]+)'),
        ]

    while 1:
        try:
            f = open(fi)
            break
        except:
            print_exc()
            time.sleep(1)

    for li in f:
        for key in keys:
            x = key.search(li)
            if x:
                yield x.groups()[0]
    f.close()


def chkfi(srcpath, dstpath, fi, fidic):
    fi1 = fi.replace(dstpath, '')
    src = srcpath + fi1

    if not os.path.exists(src):
        print pwarn('WARNING: {0} not exists!'.format(src))
        return

    t0 = fidic.get(src)
    t1 = gett(src)
    if t0 != t1:
        cp(src, dstpath, t1)
        fidic[src] = t1


def cp(src, dstpath, t1):
    try:
        t1 = datetime.strptime(t1, '%a %b %d %H:%M:%S %Y')
        os.system('cp %s %s' % (src, dstpath))
        src1 = src.replace(srcpath, '')
        if t1 >= begint:
            print pbold('COPY: {0:40} {1}'.format(src1, t1))
        else:
            print ('COPY: {0:40} {1}'.format(src1, t1))
    except:
        print 'ERROR COPY:', src1
        print_exc()
        set_trace()


if __name__ == '__main__':
    mainfis = [
        '2015-10-ivstSNA.md',
        # '2015-09-kmt_history.md',
        '2015-10-twcom_tej.md',
        '2015-10-ivstSNA_stat.md',
        ]
    paths = ['ivstSNA', 'twcom_tej', 'ivstSNA_stat']
    dstpaths = [('images/%s_files/' % fi) for fi in paths]
    watch(mainfis, dstpaths)

