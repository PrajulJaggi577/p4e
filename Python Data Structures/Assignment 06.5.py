#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.


text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0')
print(float(text[a:]))