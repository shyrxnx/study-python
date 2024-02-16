import webbrowser
import pyperclip

place = input("Enter place you want to search in Google Maps: ").split()

if len(place) > 1:
    address = '+'.join(place)
elif len(place) == 1:
    address = place[0]
else:
    address = pyperclip.paste()

webbrowser.open(r'https://www.google.com/maps/place/' + address)