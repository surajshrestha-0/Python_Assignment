"""
Write a Python Program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
"""


def replaceGoodOrPoor(givenString):
    # finding the substring not and poor, from a given string
    notInString = givenString.find('not')
    poorInString = givenString.find('poor')
    goodInString = givenString.find('good')
    # print(goodInString)

    # if not appears after not in the given string
    if poorInString > notInString and notInString > 0 and poorInString > 0:
        # replace the whole 'not'...'poor' substring with 'good'
        givenString = givenString.replace(givenString[notInString:poorInString + 4], 'good')
        return givenString
    elif goodInString > 0:
        givenString = givenString.replace(givenString[goodInString:goodInString + 4], 'poor')
        return givenString
    else:
        return givenString


print(replaceGoodOrPoor('The lyrics is not that poor!'))
print(replaceGoodOrPoor('The lyrics is good!'))
