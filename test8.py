
import os 
import shutil
import zipfile

class ZipProcessor:

    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = "unizpped-{}".format(
                              zipname[:-4])

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        self.unzip_files()
        self.process_files() # This method is in ZipReplace class
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)

import sys

    class ZipReplace(ZipProcessor):
        def __init__(self, filename, search_string, replace_string):
            super().__init__(filename)
            self.search_sting = search_string
            self.replace_string = replace_string

        def process_files(self):
            for filename in os.listdir(self.temp_directory):
                with open(self._full_filename(filename)) as file:
                    contents = file.read()
                contents = contents.replace(
                           self.search_string, self.replace_string)
                with open(
                          self._full_filename(filename), 'w') as file:
                    file.write(contents)

if __name__ == '__main__':
    ZipReplace(*sys.argv[1:4]).process_zip()


class ScaleZip(ZipProcessor):
    def process_files(self):
        pass

if __name__ == '__main__':
    ScaleZip(*sys.argv[1:4]).process_zip()


