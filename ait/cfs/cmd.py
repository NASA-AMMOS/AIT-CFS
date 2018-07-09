# Advanced Multi-Mission Operations System (AMMOS) Instrument Toolkit (AIT)
# Bespoke Link to Instruments and Small Satellites (BLISS)
#
# Copyright 2017, by the California Institute of Technology.  ALL
# RIGHTS RESERVED. United States Government Sponsorship
# acknowledged. Any commercial use must be negotiated with the Office
# of Technology Transfer at the California Institute of Technology.
#
# This software may be subject to U.S. export control laws. By
# accepting this software, the user agrees to comply with all
# applicable U.S. export laws and regulations. User has the
# responsibility to obtain export licenses, or other export authority
# as may be required before exporting such information to foreign
# countries or providing access to foreign persons.

"""
Core Flight Software (cFS) Commands

The ait.cfs.cmd module specializes ait.core.cmd for
NASA's Core Flight Software (cFS;  http://cfs.gsfc.nasa.gov).
"""


import struct
from ait.core import ccsds, cmd


class cFSCmd(cmd.Cmd):
    def __init__(self, defn, *args):
        super(cFSCmd, self).__init__(defn, *args)

    def encode(self, pad=0, header=True):
        """Encodes this cFS command to binary.

        If pad is specified, it indicates the maximum size of the
        encoded command in bytes.  If the encoded command is less than
        pad, the remaining bytes are set to zero.

        The optional header argument controls whether or not a header
        is prepended to the encoded command and offers several levels
        of granularity.  If False or None, no header is prepended.  If
        True, a CCSDS header is computed based on the `APID` found in
        the command's corresponding :class:`CmdDefn`.  To control the
        CCSDS sequence count (`seqcount`) only set header to an
        instance of :class:`CcsdsHeader` with the desired `seqcount`.
        For complete control over the header contents, set header to a
        bytearray.

        NOTE: This method sets the cFS command checksum byte to zero
        in accordance with the current cFS ground system tools and cFE
        source code.  That is, as far as we can tell, the checksum is
        not used.

        """
        checksum  = 0
        secondary = struct.pack('BB', checksum, self.defn.opcode)
        offset    = len(secondary)
        size      = max(offset + self.defn.argsize, pad)
        encoded   = bytearray(size)

        encoded[0:offset] = secondary
        index             = 0

        for defn in self.defn.argdefns:
            if defn.fixed:
                value = defn.value
            else:
                value  = self.args[index]
                index += 1
            encoded[ defn.slice(offset) ] = defn.encode(value)

        if header is True:
            header = ccsds.CcsdsHeader()

        if isinstance(header, ccsds.CcsdsHeader):
            header.type     = 1
            header.apid     = self.defn.ccsds.apid if self.defn.ccsds else 0
            header.shflag   = 1
            header.seqflags = 0b11
            print 'len(encoded) =', len(encoded)
            header.length   = len(encoded) - 1
            header          = header._data

        if isinstance(header, bytearray):
            encoded = header + encoded

        return encoded
