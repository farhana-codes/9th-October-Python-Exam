'''
Question 1: Student Marks Analysis 
A college stores students' marks in a list. Write a function that accepts a list of marks and displays the highest mark, lowest mark, average mark, and number of students who passed (marks of 40 or above). 
'''

def mark_analyze(a):
  print(f'highest mark is : {max(a)}')
  print(f'lowest mark is : {min(a)}')
  print(f'avarage marks is : {sum(a)/len(a)}')
  for _ in a:
    if _ > 40:
      print(f'avobe marks of 40 is : {_}')
  


a=[45,76,38,85,92]

mark_analyze(a)