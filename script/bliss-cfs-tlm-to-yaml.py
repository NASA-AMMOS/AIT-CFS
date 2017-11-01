#!/usr/bin/env python

import sys


types = { 'B': 'U8', 'H': 'MSB_U16', 'I': 'MSB_U32' }


if len(sys.argv) != 2:
    print 'usage: bliss-cfs-tlm-to-yaml.py tlm.txt'
    print
    print 'Where tlm.txt is a telemetry text file from'
    print 'cFE/tools/cFS-GroundSystem/Subsystems/tlmGUI'
    print
    sys.exit(2)

filename = sys.argv[1]

with open(filename, 'rt') as stream:
    for line in stream.readlines():
        line = line.strip()

        if line.startswith('#') or len(line) == 0:
            continue

        cols  = [ c.strip() for c in line.split(',') ]
        bytes = int(cols[1])
        size  = int(cols[2])

        print '    - !Field'
        print '      name:  %s' % cols[0].replace(' ', '')
        print '      desc:  '

        if size == 1:
            print '      bytes: %d' % bytes
        else:
            print '      bytes: [%d, %d]' % (bytes, bytes + size - 1)

        print '      type:  %s' % types[ cols[3] ]

        if cols[4] == 'Enm':
            print '      enum:'
            for n in range(4):
                if cols[5 + n] != 'NULL':
                    print '        %d: %s' % (n, cols[5 + n])

        print
