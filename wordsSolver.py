#goes through the dictionary and checks each word against the letters
def wordsSolver(letters):
  fin=open("countdownDictionary.txt",'r')
  longest_word=""
  for i in fin:
    i=i.strip()
    if(len(i)>len(longest_word) and lettersMatch(letters,i)):
      longest_word=i
  return longest_word

#checks if the all the letters in word are in letters
#Eg. lettersMatch(["a","b","e","c","i","o","r","s","a"],"rabies")
#After the first loop, count = {'a':2,'b':1,'c':1,'e':1,'i':1,'o':1,'r':1,'s':1}
#After the second loop, count = {'a':1,'b':0,'c':1,'e':0,'i':0,'o':1,'r':0,'s':0}
#As none of the numbers are negative, it returns true

#Eg. lettersMatch(["a","b","e","c","i","o","r","s","a"],"babies")
#After the first loop, count = {'a':2,'b':1,'c':1,'e':1,'i':1,'o':1,'r':1,'s':1}
#After the second loop, count = {'a':1,'b':-1,'c':1,'e':0,'i':0,'o':1,'r':1,'s':0}
#As count['b'] < 0, word has too many b
#Therefore, it returns False
def lettersMatch(letters,word):
  count={}
  for i in letters:
    if(i in count.keys()):
      count[i]+=1
    else:
      count[i]=1

  for i in word:
    if(i not in count.keys()):
      return False
    count[i]-=1
  
  for i in count.keys():
    if(count[i]<0):
      return False

  return True

def main():
  print(wordsSolver(list(input("Enter the letters (no spaces): "))))

if(__name__=="__main__"):
  main()
