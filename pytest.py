import os
directory = os.getcwd()
print(directory)
results = []

for folder in gamefolders:
    for f in os.listdir(folder):
        if f.endswith('.c'):
            results.append(f)

print results