# -*- coding: utf-8 -*-
# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import jsonasobj


class ExtendedNamespaceTestCase(unittest.TestCase):
    """ ExtendedNamespace is a dictionary / namespace combination.  Any valid python identifiers are also available
    as first class members.
    """
    def test_extendednamespace(self) -> None:
        # Direct constructor
        ens = jsonasobj.ExtendedNamespace(i1=1, i2='a', i3='17')
        # Test dictionary and namespace behavior
        self.assertEqual(1, ens.i1)
        self.assertEqual('a', ens.i2)
        self.assertEqual('17', ens.i3)
        self.assertEqual(3, len(ens))
        self.assertTrue('i1' in ens)
        self.assertFalse('i4' in ens)
        del ens['i1']
        self.assertEqual(2, len(ens))
        self.assertFalse('i1' in ens)
        ens.i4 = 243
        self.assertEqual(243, ens.i4)
        self.assertEqual(243, ens['i4'])

        # Construct from a dictionary, using common json-ld idioms
        ens1 = jsonasobj.ExtendedNamespace(**{'i1': 1, '@foo': "bar", 'x:y': ens})
        self.assertEqual(1, ens1.i1)
        self.assertEqual('bar', ens1['@foo'])
        self.assertEqual(ens, ens1['x:y'])
        self.assertEqual(3, len(ens1))

    def test_extended_access(self) -> None:
        ens = jsonasobj.ExtendedNamespace(i1=1, i2='a', i3='17')
        self.assertEqual("no", ens._get('i4', 'no'))


if __name__ == '__main__':
    unittest.main()
