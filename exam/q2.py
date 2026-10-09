'''
Question 2: Online Mobile Store An online store maintains a list of mobile prices. Write a function to display all mobiles costing more than ₹20,000, calculate the total inventory value, and find the most expensive mobile price. 
'''

def mobile_store(a):
  for _ in a:
    if _ >20000:
      print(f'mobile above 20k is : {_}')

  print(f'total inventory of the mobile store is {sum(a)}')
  print(f'total inventory of the mobile store is {max(a)}')

a=[30643,45000,15999,80999,56000]

mobile_store(a)