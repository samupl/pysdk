#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Jakub 'samu' Szafrański <kontakt@samu.pl>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.


import sys
import os
import urllib2
import BeautifulSoup

if len(sys.argv) != 2:
    print("Invalid syntax!\nsyntax: %s <sdx file>" % (sys.argv[0]))
    sys.exit(1)

fpath = sys.argv[1]

if not os.path.exists(fpath):
    print("%s: %s: No such file or directory" % (sys.argv[0], fpath))

print("Opening %s..." % (fpath,))
fp = open(fpath, 'r')
link = fp.readline()
fp.close()

#print("Found URL: %s" % (link,))
url = urllib2.urlopen(link).read()
#url = open('url', 'r').read()
#print url

# <input type='hidden' id='fileID2' value='41065c00-4bf1-e111-a77d-f04da23e67f6' />
soup = BeautifulSoup.BeautifulSoup(url)
xml = BeautifulSoup.BeautifulSoup(soup.find("input", {"id": "hfFileInfo"})['value'])
files = xml.findAll('file')
for f in files:
    fname = f['filename']
    fps = f.findAll('filepart')
    rfps = {}
    for fp in fps:
        rfps[fp['filepartkey']] = fp['fileurl']

    print("FILENAME:\t %s" % (fname,))
    print("PARTS:")
    for fp in rfps:
        print("%s -> %s" % (fp, rfps[fp]))
    print ''
    
