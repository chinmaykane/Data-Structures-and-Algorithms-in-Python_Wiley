"""Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike"."""
sttring = input('Enter a string')
for el in sttring:
    sttring = sttring.replace('\'','')
    sttring = sttring.replace('\"', '')
    sttring = sttring.replace(';', '')
    sttring = sttring.replace(':', '')
    sttring = sttring.replace(',', '')
    sttring = sttring.replace('.', '')
    sttring = sttring.replace('-', '')
print(sttring)