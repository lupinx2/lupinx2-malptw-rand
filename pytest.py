import os
directory = os.getcwd()
print(directory)
results = []   

for folder in os.getcwd():
    for f in os.listdir(folder):
        if f.endswith('.c'):
            results.append(f)

print (results)