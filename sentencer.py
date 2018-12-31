from nltk import sent_tokenize
def sentencer(text):

  with open((str(text)),"r") as handler:
    text=handler.read()
  handler.close()

  sentences= sent_tokenize(text)


  return sentences

