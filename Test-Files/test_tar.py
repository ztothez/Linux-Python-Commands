import tarfile,os
import sys
os.chdir("/tmp/foo")
tar = tarfile.open("test.tar")
for member in tar.getmembers():
    f=tar.extractfile(member)
    content=f.read()
    print("%s has %d newlines" %(member, content.count("\n")))
    print("%s has %d spaces" % (member,content.count(" ")))
    print("%s has %d characters" % (member, len(content)))
    sys.exit()
tar.close()
