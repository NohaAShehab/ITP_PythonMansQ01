# regex valid if input string, follow pattern
import re
# # check password 8 letters
# password  = input("plz enter password")
# if not password.isspace() and len(password)> 0:
#     print("valid")

# email = "dfff@ffff.com"
# # #pattern
# myemailpattern="^[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
# print(re.match(myemailpattern,"nsheh@iti.gov.eg"))
# # # \w{8}
# #
# # x = re.match(myemailpattern,"Nohaiti@iti67r6erer.com")  # return none if string doesn't match pattern
# # # if string matches the pattern , match object
# # print(x)
# # #
# # # match =---> return match if part of the string follwed the pattern
# # # full match --> will scan all scan string S
#
# memail = "qwjhejwegej@gkljfklgjklfd.comnshehab@iti.com"
# mailpattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# print(re.match(mailpattern, memail))
# print(re.match(mailpattern,"nsheh@iti.gov.eg"))


# object ---> re.Match object, else None object
print(f"{memail}")
