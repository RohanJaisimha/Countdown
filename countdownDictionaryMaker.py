def makeCountdownDictionary():
  fin=open("words.txt",'r')
  fout=open("countdownDictionary.txt",'w')
  for i in fin:
    i=i.strip()
    if(len(i)<=9):
      fout.write(i+"\n")
  fout.close()
  fin.close()

def main():
  makeCountdownDictionary()

if(__name__=="__main__"):
  main()
