#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: gen_emoji_css.py
# Date: Sat Dec 20 17:50:57 2014 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

import os
import glob
import base64

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(DIR_PATH, 'smiley.css')

HEAD = """.smiley {
    background-position: -2px -2px;
    background-repeat: norepeat;
    width: 20px;
    height: 20px;
    display: inline-block;
    vertical-align: top;
    zoom: 1;
}
"""

TEMPLATE = """.smiley{name} {{
    background-image: url("data:image/png;base64,{b64}");
}}"""

def get_file_b64(fname):
    data = open(fname, 'rb').read()
    return base64.b64encode(data)

with open(OUTPUT_FILE, 'w') as f:
    print >> f, HEAD
    for fname in glob.glob(os.path.join(DIR_PATH, 'smileys', '*.png')):
        b64 = get_file_b64(fname)
        basename = os.path.basename(fname)
        smileyname = basename[:-4]
        print >> f, TEMPLATE.format(name=smileyname, b64=b64);