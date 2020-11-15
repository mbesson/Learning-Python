# Interacting with files

# File is someting that implements read and write
#d ocs.python.org/3
my_file = open('xmen.txt', 'w+')

my_file.write('Beaste\n')
my_file.write('Phoenix\n')
my_file.writelines(['Cyclops\n','Bishop\n','Nightcrawler\n'])


my_file =open('xmen.txt', 'r')
print(my_file.read())
print('Reading again')
print(my_file.read()) # gives nothing due to cursor moving from de beginning to the end
my_file.seek(0)
my_file.close() # also call flush

# with statement to avoid closing
with open('xmen.txt') as my_file:
    #blablab