# Matching a sequence of characters with character classes
import re

pattern = r"[Hh]ello"
text = "Hello world"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
    
'''
This will search the 'text' string for the regular expression pattern 
[Hh]ello, which matches either "Hello" or "hello", and print "Match 
found!" if a match is found.
'''

# Matching a specific number of characters with a quantifier
pattern = r"[0-9]{3}"
text = "The pin is 1234."

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
    
'''
This will search the text string for the regular expression pattern 
[0-9]{3}, which matches any sequence of three digits, and print "Match 
found!" if a match is found.
'''

# Using grouping constructs and backreferences
pattern = r"([A-Za-z]+) (\d+)"
text = "John 1234"

match = re.search(pattern, text)

if match:
    name = match.group(1)
    number = match.group(2)
    print(f"Name: {name}, Number: {number}")
else:
    print("Match not found.")
'''
This will search the text string for the regular expression pattern 
([A-Za-z]+) (\d+), which matches a sequence of one or more letters 
followed by a sequence of one or more digits, and defines two capture
groups for the name and number. It then prints the name and number
using the group() method.
'''

# Using lookahead assertions
pattern = r"cat(?=fish)"
text = "catfish"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
'''
This will search the text string for the regular expression pattern
cat(?=fish), which matches the word "cat" only if it is immediately 
followed by the word "fish", and print "Match found!" if a match is 
found.
'''
target_string = "Emma is a basketball player who was born on June 17"
result = re.match(r"\w{4}", target_string) #

# printing the Match object
print("Match object: ", result)
# Output re.Match object; span=(0, 4), match='Emma'

# Extract match value
print("Match value: ", result.group())
# Output 'Emma'
