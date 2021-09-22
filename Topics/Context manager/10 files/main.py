# write your code here

n_files = 10
files = []

for i in range(n_files):
    with open(f'file{i+1}.txt', 'w') as f:
        f.write(f'{i+1}')

