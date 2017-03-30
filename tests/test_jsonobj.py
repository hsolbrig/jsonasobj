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
import json
from dict_compare import compare_dicts

import jsonasobj

test_json = """{
  "@context": {
    "name": "http://xmlns.com/foaf/0.1/name",
    "knows": "http://xmlns.com/foaf/0.1/knows",
    "menu": {
      "@id": "name:foo",
      "@type": "@id"
    }
  },
  "@id": "http://me.markus-lanthaler.com/",
  "name": "Markus Lanthaler",
  "knows": [
    {
      "name": "Dave Longley",
      "menu": "something",
      "modelDate" : "01/01/2015"
    }
  ]
}"""


class BasicFunctionsTestCase(unittest.TestCase):
    """ Test the basic JSON access for the JSON-LD source
    """
    def test_basic_json_read(self) -> None:
        """ Test the basic JSON level read
        """
        py_obj = jsonasobj.loads(test_json)
        self.assertEqual("Markus Lanthaler", py_obj.name)
        self.assertEqual("Dave Longley", py_obj.knows[0].name)
        self.assertEqual("http://xmlns.com/foaf/0.1/name", py_obj["@context"].name)
        self.assertEqual("http://me.markus-lanthaler.com/", py_obj["@id"])

    def test_as_json(self):
        """ Test the JSON serialization
        """
        py_obj = jsonasobj.loads(test_json)
        self.assertEqual(json.loads(test_json), json.loads(py_obj._as_json))

    def test_setdefault(self):
        py_obj = jsonasobj.JsonObj()
        py_obj._setdefault('test', dict(foo=17))
        py_obj._setdefault('test', 'nada')
        py_obj._setdefault('test2', 'sama')
        self.assertTrue(compare_dicts(dict(test=dict(foo=17), test2="sama"), py_obj._as_dict))
