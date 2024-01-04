import os
lst = os.listdir(os.getcwd())
for filename in lst:
    if filename.endswith('.py'):
        print(filename)