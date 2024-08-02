from __future__ import division

import unittest
import hashlib

from p2pool.bitcoin import sha256
import secrets

class Test(unittest.TestCase):
    def test_all(self):
        for test in ['', 'a', 'b', 'abc', 'abc'*50, 'hello world']:
            #print test
            #print sha256.sha256(test).hexdigest()
            #print hashlib.sha256(test).hexdigest()
            #print
            assert sha256.sha256(test).hexdigest() == hashlib.sha256(test).hexdigest()
        def random_str(l):
            return ''.join(chr(secrets.SystemRandom().randrange(256)) for i in xrange(l))
        for length in xrange(150):
            test = random_str(length)
            a = sha256.sha256(test).hexdigest()
            b = hashlib.sha256(test).hexdigest()
            assert a == b
        for i in xrange(100):
            test = random_str(int(secrets.SystemRandom().expovariate(1/100)))
            test2 = random_str(int(secrets.SystemRandom().expovariate(1/100)))
            
            a = sha256.sha256(test)
            a = a.copy()
            a.update(test2)
            a = a.hexdigest()
            
            b = hashlib.sha256(test)
            b = b.copy()
            b.update(test2)
            b = b.hexdigest()
            assert a == b
