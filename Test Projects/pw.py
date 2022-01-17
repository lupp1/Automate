#!python3
#pw.py - Insecure password locker

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for {account} copied to clipboard.')
else:
    ('There is no account named {}'.format(account))
