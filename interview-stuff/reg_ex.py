"""
Regular Expressions

Regular expressions

A regular expression (shortened as regex [...]) is a sequence of characters that specifies a search pattern in text. [...] used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

    1.Import the regex module with import re.
    2.Create a Regex object with the re.compile() function. (Remember to use a raw string.)
    3.Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
    4.Call the Match object’s group() method to return a string of the actual matched text.
"""

import re
reg_obj = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_obj = reg_obj.search("Hi this is my phone 234-123-4567")
print(match_obj.group())

email_reg = re.compile(r'^\s@.com$')
email = email_reg.search("gtm@gmail.com")
# print(email.group())

# \d is a metacharacter that matches any digit from 0 to 9.
regex_json={
    'po_number':r'[4-5]5\d{8}',
    'mat_code':r'[a-wy-z]+[0-9]+\d'
}
clean_po='jdjd4567823456'
po=re.search(regex_json['po_number'], clean_po)
print(po.group())