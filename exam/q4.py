'''
Question 4: Employee Salary Analysis A company stores employee salaries in a list.
 Write a function to calculate the average salary,
   display salaries above the average,
     and increase every salary by 10%. 
'''
def salary(a):
  num=sum(a)/len(a)
  print(f'average salary is {num}')
  
  for _ in a:
    if _ > num:
      print(f'above the avg salary is : {_}')
def inc(a):
  for i in range(len(a)):
    a[i] = a[i] * 1.10
  print("Salary after 10% increase:", a)
    


a=[20000,30000,55000,25000,35999]
salary(a)
inc(a)
