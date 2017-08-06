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

import os


class LoadTestCase(unittest.TestCase):
    def test_load_file(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'file.json')
        json_obj = load(json_fname)
        self.assertEqual([1, False, -12.7, "qwert"], json_obj.a_dict.vals)

    def test_load_uri(self):
        from jsonasobj import load
        # A relatively stable JSON file
        json_obj = load("http://hl7.org/fhir/STU3/account-example.json")
        self.assertEqual('Coverage/7546D', json_obj.coverage[0].coverage.reference)

    def test_load_fp(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'file.json')
        with open(json_fname) as f:
            json_obj = load(f)
        self.assertEqual([1, False, -12.7, "qwert"], json_obj.a_dict.vals)

    def test_bad_load(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'filex.json')
        with self.assertRaises(FileNotFoundError):
            json_obj = load(json_fname)
        with self.assertRaises(TypeError):
            load(dict())

    def test_load_redirect(self):
        from jsonasobj import load
        json_obj = load("http://hl7.org/fhir/Patient/f001")
        self.assertEqual('male', json_obj.gender)

if __name__ == '__main__':
    unittest.main()
