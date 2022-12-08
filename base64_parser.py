import re

# Define a regular expression that matches a base64 string
regex = re.compile(r'[A-Za-z0-9+/]{4}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?')

# Sample string that contains multiple base64 strings
sample_string = 'The base64 strings are: YWJjZA== and ZXhlZA== and ZXhlZGFjZGFl'

# Find all base64 strings using the regular expression
matches = regex.findall(sample_string)
if matches:
    # Find the longest base64 string using the max() function
    longest_base64 = max(matches, key=len)

    print(matches) # my addition
    # Print the longest base64 string
    print(longest_base64)