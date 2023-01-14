# Google Map Address Lookup Tool
# mapIt.py displays in map, an address either in the command prompt or the clipboard

import webbrowser, pyperclip, sys

def map(address):
    print(address)
    webbrowser.open_new("https://www.google.com/maps/place/"+address)

if len(sys.argv)>1:
    address = "".join(sys.argv[1:]) # -> extracts the address from command prompt
else:
    address = pyperclip.paste()

map(address.replace(" ","+").replace(",",""))
