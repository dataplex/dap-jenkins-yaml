import unittest


from onboarding import ConjurPolicyOutputParser

class TestConjurPolicyOutputParser(unittest.TestCase):
    def test_no_hosts_in_output(self):
        parser = ConjurPolicyOutputParser()
        hosts = parser.hosts('')
        self.assertCountEqual(hosts, [])

if __name__ == '__main__':
    unittest.main()
