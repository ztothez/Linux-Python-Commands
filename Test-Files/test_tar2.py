import tarfile,os,zipfile
import sys

archive = zipfile.ZipFile('test.tar.gz.zip', 'r')

tar = archive.open("test.tar.gz")
os.chdir("/root/Desktop")
tar = tarfile.open("asd.tar.gz")
for member in tar.getmembers():
    f=tar.extractfile(member)
    content=f.read()
    print(member, content.count)
    print(member,content.count)
    print(member, len(content))
    print(content)
    sys.exit()
tar.close()
