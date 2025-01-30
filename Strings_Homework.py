text = """tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

lower_text = text.lower()
result = ""
for s in lower_text.split('.'):
    result = result + s.strip().capitalize() + '. '
result = result.replace("iz", "is")
print("Count of zeros is:" + str(result.count(" ")))
print(result)