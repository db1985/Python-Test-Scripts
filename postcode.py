#postcode validation - does the input look like a postcode?

import re

#regex_string - just as you would build in regex101

reg_ex = "^([a-z]{1,2})([0-9]{1,2}) ?([0-9])([a-z]{2})$"

#get the postcode from the user (could come from anywhere, e.g. a file)

postcode = input("Enter postcode:")

#perform the match on the postcode using the regex and ignore case flag!

match_result = re.match(reg_ex, postcode, re.I)

#is there a match?

if match_result:
    print("valid")
else:
    print("invalid")
    
