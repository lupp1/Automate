#! python3
# adds wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip
TEXT = pyperclip.paste()
#separate lines add stars
lines = TEXT.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
TEXT = '\n'.join(lines)
pyperclip.copy(TEXT)
print(TEXT)