import re

#Define a pattern to search for, this means search for any length number (d represents digits and the + shows that there is no limit to the number of digits in a row)
pattern = r'\d+'

# Search the string for the pattern, this will return the first instance
match = re.search(pattern, 'The price is 100 dollars and 200 euros')
print(match.group())


# Search the string for the pattern, this will return the all instances
match_all = re.findall(pattern, 'The price is 100 dollars and 200 euros')
print(match_all)

# This will replace the pattern with the designated text
replace = re.sub(pattern, 'XX', 'The price is 100 dollars and 200 euros')
print(replace)
