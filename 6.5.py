text = "X-DSPAM-Confidence:    0.8475";
s=text.find('0')
f=text.strip()
print(f)
print(s)
p=text[s:]
print(float(p))