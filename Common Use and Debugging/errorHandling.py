# How can we manage error handling
# TRY CATCH ELSE FINALLY
import sys

file_name = 'recipies.txt'

try:
    my_file = open('recipies.txt', 'x') # x is mode for creation the second time it will fail
    my_file.write(f'Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists.")
    #sys.exit(1)
except:
    print(f'unable to write to the file')
    #sys.exit(1)
else:
    print(f"Wrote to {file_name}.")
finally:
    print(f"Execution completed.")
