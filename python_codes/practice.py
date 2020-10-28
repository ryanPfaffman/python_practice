import textract
text = textract.process('Test this.docx')
text = text.decode('utf-8')
print(test)
