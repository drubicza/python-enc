import os
import sys
import time
import random
import marshal

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

os.system('clear')
mengetik('#####################################')
mengetik('#### <\\> \x1b[31;1mProgram Information \x1b[37;1m</> ####')
mengetik('#####################################')
mengetik('- Author       : ./ExGeneralTz')
mengetik('- Name Program : Python Code Encrypt')
mengetik('- Created Date : 26-07-2019')
print('\ncontoh : /sdcard/namafile.py')
inp  = input('Nama File Anda : ')
file = open(inp).read()
com  = compile(file, '', 'exec')
with open(inp + '.enc', 'w') as file_out:
    file_out.write('#Encrypt By ./ExGeneralTz\n#Github : https://github.com/ExGeneralTz\nimport marshal\nexec(marshal.loads(' + repr(marshal.dumps(com)) + '))')
print('Berhasil Menyimpan File Dengan Nama', inp + '.enc')
