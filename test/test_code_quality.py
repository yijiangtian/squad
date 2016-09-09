import subprocess
import shutil


from django.test import TestCase

if shutil.which('flake8'):
    class TestCodeQuality(TestCase):
        def test_flake8(self):
            self.assertEqual('', subprocess.getoutput('flake8'))
else:
    print("I: skipping flake8 test (flake8 not available)")
