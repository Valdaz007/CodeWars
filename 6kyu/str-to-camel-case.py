# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case). The next words should be always capitalized.

def to_camel_case(text):
    #? Soln 1.0 ******************************************************************************************
    # case_flag = 0
    # if text == "": return ""
    # else:
    #     for i in text:
    #         if i == "-" or i == "_":
    #             text = text.replace(i, "", 1)
    #             case_flag = 1
    #         elif case_flag == 1:
    #             text = text.replace(i, i.upper(), 1)
    #             case_flag = 0
    #         elif i.isupper():
    #             i.lower()
    #     return text


    #? Soln 2.0 ***************************************************************************************
    # temp=[]
    # for elmt in text.split('-'):
    #     if "_" in elmt: 
    #         for i in el.split('_'): temp.append(i)
    #     else: temp.append(elmt)
    
    # temp2 = []
    # temp2.append(temp[0])
    # for i in temp[1:]:
    #     temp2.append(i.capitalize())
    # return "".join(temp2)

    #? Soln 2.1 ****************************************************************************************
    text = text.replace('_', '-').split('-')
    return "".join([text[indx].capitalize() if indx > 0 else text[indx] for indx in range(len(text))])

# Test
print(to_camel_case("the-stealth_warrior"))