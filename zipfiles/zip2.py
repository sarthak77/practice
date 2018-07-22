import zipfile
"""
zipfile.ZIP_DEFLATED. (This specifies the deflate compression
algorithm, which works well on all types of data.)
"""
a=zipfile.ZipFile('jj.zip','w')#'a' to append
a.write('createg1',compress_type=zipfile.ZIP_DEFLATED)
a.close()
"""
this will create jj.zip folder and it will contain createg1 compressed
"""