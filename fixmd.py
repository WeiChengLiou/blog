#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join, exists
from os import remove
from datetime import datetime
from pdb import set_trace


def gettags():
    tags = {'comments': 'true'}

    print 'Please input title:'
    tags['title'] = raw_input().decode('utf8')
    d = datetime.now()
    print 'Please input date(yyyy-mm-dd): [{0:%Y-%m-%d}]'.format(d)
    ret = raw_input()
    try:
        tags['date'] = datetime.strptime(ret, '%Y-%m-%d')
    except:
        tags['date'] = d
    print 'Please input slug:'
    tags['slug'] = raw_input()
    print 'Please input tags:'
    tags['tags'] = raw_input().decode('utf8')

    for k, v in tags.iteritems():
        print k, v

    print 'Is that ok? Press n to repeat:'
    if raw_input() == 'n':
        return gettags()
    else:
        return tags


def repfun(li):
    return li.replace(
        u'output/',
        u'http://weichengliou.github.io/blog/downloads/data/'
        ).replace('<p>', '').replace('</p>', '')


def process(li):
    # delete code section
    # png url
    # output url
    # <p>

    if len(li) > 4 and li[:4] == '    ':
        # remove code section
        return u''
    elif '![png]' in li:
        # since png files move into [image], change png url
        return li.replace('[png](', '[png]({filename}/images/')
    else:
        # replace <p> tag, change 'output/' into github real path
        return repfun(li)


def modifymd(path, fi, tags):
    tagstr = [u'title: {0}'.format(tags['title']),
              u'date: {0:%Y-%m-%d %H:%M}'.format(tags['date']),
              u'comments: {0}'.format(tags['comments']),
              u'slug: {0}'.format(tags['slug']),
              u'tags: {0}'.format(tags['tags'])]
    lis = []
    lis.append(u'\n'.join(tagstr))
    lis.append(u'\n')
    cnt = 0

    fi0 = join(path, fi)
    with open(fi0) as f:
        for i, li in enumerate(f):
            ret = process(li.decode('utf8'))
            if ret == '\n' or ret == '':
                cnt += 1
                if cnt > 2:
                    continue
            else:
                cnt = 0
            lis.append(ret)

    lis.append(u'\n\n' + getCC())
    fi1 = join(path, '{0:%Y-%m-%d}-{1}'.format(tags['date'], fi))
    with open(fi1, 'wb') as f:
        f.write(u''.join(lis).encode('utf8'))
    print 'Export to %s' % fi1


def getCC():
    with open('content/downloads/notebooks/creative_commons.txt') as f:
        return u''.join(f.readlines())


def writemd(path, fi):
    if exists(join(path, fi)):
        tags = gettags()
        modifymd(path, fi, tags)
        remove(join(path, fi))
    else:
        print 'file not found'


if __name__ == '__main__':
    path = 'content'
    fi = 'kmt.md'
    writemd(path, fi)

