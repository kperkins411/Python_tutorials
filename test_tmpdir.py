# content of test_tmpdir.py
import shutil, tempfile
from os import path
from unittest import TestCase, main


class TestExample(TestCase):
    numb_dirs = 4
    numb_files = [5,4,3,2]

    def setUp(self):
        self.dir_list = []
        self.file_list = []

        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        #create subdirs
        for _ in range(TestExample.numb_dirs):
            self.dir_list.append(tempfile.mkdtemp(dir=self.test_dir))

        for numb,dir in enumerate(self.dir_list):
            for val in range(TestExample.numb_files[numb]):
                self.file_list.append(tempfile.mkstemp(suffix=".png",dir=dir))

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_something(self):
        # Create a file in the temporary directory
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        # Write something to it
        f.write('The owls are not what they seem')
        # Reopen the file and check if what we read back is the same
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(f.read(), 'The owls are not what they seem')

if __name__ == '__main__':
    main()