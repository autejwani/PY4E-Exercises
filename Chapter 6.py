# Chapter 6, Exercise 5
#Solution to Programming Exercise 5 of Chapter 6 of Python For Everybody:
#Python For Everybody, Dr. Charles R. Severance

str = 'X-DSPAM-Confidence:0.8475'
colon_pos = str.find(':')
sliced_str = str[(colon_pos + 1):len(str)]
print('%g' % float(sliced_str))
                 

# Chapter 6, Exercise 6
#Solution to Programming Exercise 6 of Chapter 6 of Python For Everybody:
#Python For Everybody, Dr. Charles R. Severance

# Leading and Trailing spaces are removed below
phrase = '     Twinkle Twinkle Little Star How I Wonder What You Are     '
phrase_stripped = phrase.strip()
print(phrase_stripped)

# Replace spaces with null
phrase_replaced = phrase.replace(' ','')
print(phrase_replaced)

# Returns index of first occurance of substring specified
print(phrase_replaced.find('How'))

