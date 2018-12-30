  
"""
input_file: name of of the text file.
word: which word you are looking for.
count: how many sentences before and after the target word you want to write in the file.
output_name: the name of the output file.
"""
def paragrapher(input_file,word,count,output_name):

  if count == None: #if the user does not specify a count, the code will asume they wonly want the sentences with the word, and no preceeding or succeeding sentence
    count =0

  text_list=sentencer(input_file)
  #makes a list of all sentences in the file. You will need to use one of the sentencer functions. Alternatively, you can just put in a list of sentences yourself.

  sentences=[]#the sentences that will be added to the output will be stored in this file. You can just directly write the code to the files if you work with very large fiels and want save space, but I'm leaving it like this in case someone needs the sentences in an array. 

  counter = 0 #the file will show which count of the occurence of the word a section is

  position = 0 #this is to keep track of the position of the sentence within the text

  for sentence in text_list:

    if word.lower() in sentence.lower(): #if the sentence includes the word

      counter += 1 #increase occurence time of the word


      if (position-count)<0: #in case there aren't enough sentences before the sentence to incldue enough sentences before the sentence with our word, it will just start from the first sentence. If the count is always going to be zero, you can remove this part.  

        section="".join(text_list[0:position+count+1])
        section = str(counter) +"\n" + section+ "\n"
        
      elif position+count+1>len(text_list)-count: #in case there aren't enough sentences to include after the sentence including our word, it will just end after the last sentence. If the count is always going to be zero, you can remove this part. 


        section="".join(text_list[position-count:])
        section = str(counter) +"\n" + section + "\n"
        
      else: #if there are enough sentences to include before and after the sentence with our word.

        section="".join(text_list[position-count:position+count+1])
        section =  str(counter) +"\n" + section + "\n"
      sentences.append(section)

      section=""
    position+=1

  output_text=open(str(output_name),"w+") #creates output file

  for lines in sentences: #writes output file.
    output_text.write(lines)
  output_text.close()
