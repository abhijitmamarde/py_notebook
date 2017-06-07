'''
Regex with Python is easy

Steps required:

- import standard module `re`
- write your regex pattern and compile it
- call the one of methods - findall, match, search, sub etc.

'''
import re

number_input_text = "the numbers are: 12 34 56 and 78, others numbers are: 33 78 and 0."
number_regex_pattern = r"(\d+)"
r = re.compile(number_regex_pattern)

# findall occurences/matches for pattern
matched_numbers = r.findall(number_input_text)
print("Input text:", repr(number_input_text))
print("Matched numbers:", matched_numbers)

# replace all the matches/occurences with some string
masked_numbers = r.sub('XX', number_input_text)
print("Numbers masked:", masked_numbers)

'''
search() 

- searches for the first pattern match
- returns the MATCH object, not a string
- on matched object either run, group() or groups()
'''
search_numbers = r.search(number_input_text)
print("Match object:", search_numbers)
print("match.group():", search_numbers.group())
print("match.groups():", search_numbers.groups())
