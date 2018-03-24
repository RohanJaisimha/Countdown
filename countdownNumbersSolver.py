import itertools

def createPermutationsForNumbers(numbers):
  operationsWithoutOperators=[]
  for i in range(1,7):
    for j in list(set(itertools.permutations(numbers,i))):
      operationsWithoutOperators.append(list(j))
  return operationsWithoutOperators

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
  return float(t[0])

def checkOperationsAndPrint(operations,target):
  closest_operations=[]
  smallest_difference=target
  for i in operations:
    answer=evaluate(i)
    if(answer==None):
      continue
    if(int(answer)==answer):
      if(answer==target):
        if(smallest_difference!=0):
          closest_operations=[]
          closest_operations.append(i)
          smallest_difference=0
        else:
          closest_operations.append(i)
      else:
        if(abs(answer-target)<smallest_difference):
          smallest_difference=abs(answer-target)
          closest_operations=[]
          closest_operations.append(i)
        elif(abs(answer-target)==smallest_difference):
          closest_operations.append(i)
  closest_operations=list(set(tuple(i) for i in closest_operations)) #remove duplicates
  if(smallest_difference==0):
    print("Found "+str(len(closest_operations))+" operations that worked. (10 points)")
    for i in closest_operations:
      print(convertToInfix(i))
  elif(smallest_difference<=5):
    print("Found "+str(len(closest_operations))+" operations that were "+str(smallest_difference)+" away (closest I could get). (7 points)")
    for i in closest_operations:
      print(convertToInfix(i))
  elif(smallest_difference<=10):
    print("Found "+str(len(closest_operations))+" operations that were "+str(smallest_difference)+" away (closest I could get). (5 points)")
    for i in closest_operations:
      print(convertToInfix(i))
  else:
    print("Found "+str(len(closest_operations))+" operations that were within "+str(smallest_difference)+" away (closest I could get). (0 points)")
    for i in closest_operations:
      print(convertToInfix(i))

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
  return ''.join(t)[1:-1]

def getNumbersAndTarget():
  numbers=[i for i in input("Enter the 6 numbers separated by a space: ").split()]
  target=int(input("Enter the target: "))
  return numbers,target

def main():
  numbers,target=getNumbersAndTarget()
  checkOperationsAndPrint(addOperators(createPermutationsForNumbers(numbers)),target)

main()
