import os





def replaceName(path,before,after):
    for filename in os.listdir(path):
        rName = filename.replace(before,after)
        print(f'in {path}\n{filename} => {rName}')
        os.rename(f'{path}/{filename}',rName)

while True:
    path_input = input('where is the working directory?...')
    os.chdir(path_input)
    path = os.path.abspath(os.getcwd())
    while True:
        before = input('from what?...')
        if before :
            pass
        else :
            break
        after = input('to what?...')
        replaceName(path,before,after)
