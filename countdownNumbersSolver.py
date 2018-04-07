import itertools,time

#generates all possible combinations and permutations of the 6 numbers
def createPermutationsForNumbers(numbers):
  operationsWithoutOperators=[]
  for i in range(1,7):
    for j in list(set(itertools.permutations(numbers,i))):
      operationsWithoutOperators.append(list(j))
  return operationsWithoutOperators

#adds operators to operations, completing the operation
def addOperators(operationsWithoutOperators):
  operators=['+','-','/','*']
  operations=[]
  for i in range(len(operationsWithoutOperators)):
    if(len(operationsWithoutOperators[i])==1):
      operations.append(operationsWithoutOperators[i])
    if(len(operationsWithoutOperators[i])==2):
      for j in operators:
        operations.append(operationsWithoutOperators[i]+[j])
    if(len(operationsWithoutOperators[i])==3):
      for j1 in operators:
        for j2 in operators:
          operations.append(operationsWithoutOperators[i]+[j1,j2])
    if(len(operationsWithoutOperators[i])==4):
      for j1 in operators:
        for j2 in operators:
          for j3 in operators:
            operations.append(operationsWithoutOperators[i]+[j1,j2,j3])
    if(len(operationsWithoutOperators[i])==5):
      for j1 in operators:
        for j2 in operators:
          for j3 in operators:
            for j4 in operators:
              operations.append(operationsWithoutOperators[i]+[j1,j2,j3,j4])
    if(len(operationsWithoutOperators[i])==6):
      for j1 in operators:
        for j2 in operators:
          for j3 in operators:
            for j4 in operators:
              for j5 in operators:
                operations.append(operationsWithoutOperators[i]+[j1,j2,j3,j4,j5])
  return operations

#evaluates an operation in RPN notation
#Eg. evaluate(["2","3","+","7","**"])=35
def evaluate(operation):
  t=[]
  operators=['+','-','/','*']	
  for i in operation:
    if(i in operators):
      num1=t.pop(-1)
      num2=t.pop(-1)
      if((num1=='0' or num1=='0.0') and i=='/'):
        return None
      else:
        t.append(str(eval(num2+i+num1)))
    else:
      t.append(i)
  return int(float(t[0])) if(int(float(t[0]))==float(t[0])) else None

def checkOperationsAndPrint(operations,target):
  smallest_difference=2**31-1
  for i in operations:
    answer=evaluate(i)
    if(answer==None):
      continue
    if(answer==target):
      print(convertToInfix(i),"=",evaluate(i))
      return
    elif(abs(answer-target)<smallest_difference):
      smallest_difference=abs(answer-target)
      print(convertToInfix(i),"=",evaluate(i))

#converts an operation in RPN form to infix form
def convertToInfix(operation):
  t=[]
  operators=['+','-','/','*']
  for i in operation:
    if(i in operators):
      num1=t.pop(-1)
      num2=t.pop(-1)
      t.append("("+num2+" "+i+" "+num1+")")
    else:
      t.append(i)
  if("(" in t[0]):
    return ''.join(t)[1:-1]
  else:
    return ''.join(t[0])

def getNumbersAndTarget():
  numbers=[i for i in input("Enter the 6 numbers separated by a space: ").split()]
  target=int(input("Enter the target: "))
  return numbers,target

def main():
  numbers,target=getNumbersAndTarget()
  start_time=time.time()
  checkOperationsAndPrint(addOperators(createPermutationsForNumbers(numbers)),target)
  print("And that was as close as I could get")
  print("Took ",time.time()-start_time,"\bs to run")

main()
