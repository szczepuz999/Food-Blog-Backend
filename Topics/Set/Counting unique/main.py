# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'

all_students = Belov + Smith + Sarada
set_all_students = set(all_students)
print(len(set_all_students))
