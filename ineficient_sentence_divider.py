"""
The function works by going through the text to see if a characther should end a sentence.

This function is very inneficient, running in O(n^5) time. However, it will still split documents of several hundred pages witin a second on most machines. If time is a problem, you should use the function that is using the NTLK,  called sentence_divider.

 The reason the complexity is so high is because there are several  cases where a sentence might not actually end at a punctuation mark. These are often edge cases, and you can chose to ignore them. If you want to cut down the time complexity, you can cut down lines you don't need depending on the text you want to split. 

I included all edge cases thar present in J.D. Sallinger's Catcher in the Rye. The edge cases will depend on the document you are parsing into sentences.

If your text contains fewer individual words that the program might pick up as false sentence enders, but you want to account for those, you should consider using the regular expression module.

"""

def sentence_divider(text):

  enders=["...","!","?","."] #punctuations that end a sentence
  
  quotation_enders=[".\"","!\"","?\"","...\""] #punctuations that end the sentence. If something ends a quote, the code will not consider that the end of the sentence. You can remove this is if your document does not contain many individual words in quotes.
  
  quotation_corrected=["<period>\"<stop>","<excle>\"<stop>","<question>\"<stop>","<triple>\"<stop>"] #changes quotation ends do they won't be split as sentence enders. 

  string_punctuations=["<period>\"","<excle>\"","<question>\"","<triple>\""]

  false_enders=["JD.","Mr.","Mrs.","U.S.","U.S.A.","St.","D.B.","DB.","Dr."] #honorifics or abbrevations containing periods do not end a sentence.
  
  corrected_false_enders=["JD<dot>","Mr<dot>","Mrs<dot>","U<dot>S<dot>","U<dot>S<dot>A<dot>","St<dot>","D<dot>B<dot>","DB<dot>","Dr<dot>"] #to make sure 


  with open((str(text)),"r") as handler:
    read = handler.readlines()

  handler.close()

  read="".join(read)
  read=read.replace("\n"," ")


  for index,word in enumerate(false_enders):
    read=read.replace(word,corrected_false_enders[index]) #this is what you want to remove if you don't want to spend time looking for honorifics and abbrevations. It replcaes the abbrevations or honorifics with their spelled names so they won't be split as a sentence.

  for index,word in enumerate(quotation_enders):
    read = read.replace(word,quotation_corrected[index]) #this is what you want to remove if you want to consider full sentences within a quation as one sentence. It replaces quotation enders with spelled names of the punctuations so they won't be split as a sentence

  for ender in enders: 
    read=read.replace(ender,ender + "<stop>") #this adds a stop to all punctuations that  actually end a sentence.

  for index,word in enumerate(corrected_false_enders):
    read=read.replace(word,false_enders[index])
    #switches the spelled names of false enders to the  punctuation signs.

  for index,word in enumerate(string_punctuations):
    read=read.replace(word,quotation_enders[index])
    #switches the spelled names of the quatation enders back to the quotation enders.

  sentences=read.split("<stop>") #splits the sentence everywhere there is a <stop>. If the code accounted for all edge cases, those places will be where we want a sentence to end.


  return sentences

