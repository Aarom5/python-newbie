text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
extracted_d=text[pos:]
print(float(extracted_d))