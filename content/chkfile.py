#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import exists
from datetime import datetime
import time
from traceback import print_exc
import re
from pdb import set_trace


def gett(fi):
    try:
        return time.ctime(os.path.getmtime(fi))
    except:
        return 0


srcpath = '/home/gilbert/repos/rating/result/'


def watch(fis, dstpaths):
    chk = lambda mainfi, srcpath, dstpath, fidic: [
        chkfi(srcpath, dstpath, fi, fidic) for fi in reads(mainfi)]

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
    t1 = gett(src)

    if not exists(fi):
        cp(src, dstpath)
        fidic[src] = t1

    if src not in fidic:
        fidic[src] = gett(fi)
        # fidic[src] = t1
    if fidic[src] != t1:
        cp(src, dstpath)
        fidic[src] = t1


def cp(src, dstpath):
    try:
        os.system('cp %s %s' % (src, dstpath))
        print src, 'copied'
    except:
        print 'ERROR COPY:', src
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

