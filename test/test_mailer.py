#-*- encoding: utf8 -*-
import unittest

from roundup import mailer

class EncodingTestCase(unittest.TestCase):
    def test(self):
        a = lambda n, a, c, o: self.assertEquals(mailer.nice_sender_header(n,
            a, c), o)
        a('ascii', 'ascii@test.com', 'latin1', 'ascii <ascii@test.com>')
        a(u'café', 'ascii@test.com', 'latin1',
            '=?latin1?q?caf=E9?= <ascii@test.com>')
        a('as"ii', 'ascii@test.com', 'latin1', '"as\\"ii" <ascii@test.com>')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(EncodingTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)

# vim: set et sts=4 sw=4 :
