# a-z  srkkhan@gmail.com
# 0-9
#. _ time 1
# @ time 1
# . 2 position and 3 position
# ^ useing for start
# [] using for range
# + using for merge condition 
# \ using for searching carecter in string
# ? working between 0 and 1 condition (True & False condition) ,given at a time one carecter
# In RegEx @ is a special corecter serching by \w
# In RegEx if any condition search on any position useing by {} sign
# In RegEx . behind the search with using $ sign

import re
email_condition="^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email= input("Enter your email: ")

if re.search(email_condition,user_email):
    print('right email')
else:
    print("wrong email")