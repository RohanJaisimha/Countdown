def wordsSolver(letters):
  fin=open("countdownDictionary.txt",'r')
  longest_word=""
  for i in fin:
    i=i.strip()
    if(len(i)>len(longest_word) and lettersMatch(letters,i)):
      longest_word=i
  return longest_word

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
