#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join


def repurl(fi):
    lis = []
    with open(fi) as f:
        repfun = lambda li: li.replace(
            u'output/', u'http://weichengliou.github.io/blog/downloads/data/')
        for i, li in enumerate(f):
            if 'output/' in li:
                print i, repfun(li)
            lis.append(repfun(li))

    with open(fi, 'wb') as f:
        f.write(u''.join(lis))

if __name__ == '__main__':
    path = 'content/downloads/notebooks'
    fi = '2014-08-06-kmt.ipynb'
    fi1 = join(path, fi)
    repurl(fi1)

