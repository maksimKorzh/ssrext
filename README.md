# Simple Screen Recorder
Extension for Tiny Core Linux x86_64

# What is in there
/ext/deps.txt - is the output of "ldd /bin/simplescreenrecorder" command<br>
/ext/out.txt - is the output of "submitqc" script to verify the extension<br>
/ext/simplescreenrecorder.tcz - is the extension in squashfs format<br>
/ext/simplescreenrecorder.tcz.md5 - is the md5 checksum<br>
/ext/simplescreenrecorder.tcz.dep - is tcz dependenies file (most likely incomplete!!!)<br>
/ext/*.list and /ext/*.zsync - has been generated by "submitqc"<br>
/candidates.tcz.dep - is an attempt (not very successful) to get tcz packages list that corresponds to involved .so files<br>
/getdeps.py - is a python script to generate "candidates.tcz.dep" (pretty useless because it skips a lot)

# How to use it
Let's hope it would be include into TinyCoreLinux repo, so that we can simply do:<br>
tce-load -wi simplescreenrecorder<br>
But for now I just manually include ".tcz" file into /tce/optional and add simplescreenrecorder.tcz to onboot.lst<br>
Since I compiled it under CorePure64 all the dependencies are already included.
