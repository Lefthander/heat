#!/usr/bin/python

import sys
import os.path
import json

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'heat', '__init__.py')):
    sys.path.insert(0, possible_topdir)

from heat.engine import parser


def setparam(t, key, value):
    if not t.has_key('Parameters'):
        t['Parameters'] = {}

    if not t['Parameters'].has_key(key):
        t['Parameters'][key] = {}

    t['Parameters'][key]['Value'] = value


filename = sys.argv[1]
with open(filename) as f:
    blob = json.load(f)

    (stack_name, tmp) = os.path.splitext(os.path.basename(filename))
    setparam(blob, 'AWS::StackName', stack_name)

    setparam(blob, 'KeyName', '309842309484') # <- that gets inserted into image

    setparam(blob, 'InstanceType', 'm1.large')
    setparam(blob, 'DBUsername', 'eddie.jones')
    setparam(blob, 'DBPassword', 'adm1n')
    setparam(blob, 'DBRootPassword', 'admone')
    setparam(blob, 'LinuxDistribution', 'F16')

    stack = parser.Stack(blob, stack_name)
    stack.start()
