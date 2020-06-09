#this is global scope variable
my_name = 'john'

def print_name():
    global my_name
    my_name = 'ryu'
    print(f'my name is {my_name}')

print_name()
print('my name is', my_name)