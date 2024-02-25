import requests

plato_apology = requests.get('https://www.gutenberg.org/cache/epub/1656/pg1656.txt')

# If it outputs 200 then it's a success
print(plato_apology.status_code)

print(plato_apology.headers)

# Prints the first 2000 words of the file
print(plato_apology.text[:2000])
