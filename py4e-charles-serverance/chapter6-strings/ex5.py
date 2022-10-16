from functions import getDspamValue

strToParse = 'X-DSPAM-Confidence:0.8475'

dSpam = getDspamValue(strToParse)

print(f"The DSPAM Value is: {dSpam}")