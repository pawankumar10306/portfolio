from pyhtml2pdf import converter
url='https://docs.google.com/document/d/1dG2UeIWW7-paRedfL2POwSqPSAzhAXNC/edit?usp=sharing&ouid=109133290184854211953&rtpof=true&sd=true'

converter.convert(url, './website/static/docs/Pawan Kumar.pdf')