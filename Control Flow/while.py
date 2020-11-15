# Mastering the while loop

while True:
    print("looping") # Becareful, this gives an infinite loop

count = 1
while count <4:
    print("Looping")
    count+=1

count = 0
while count <10:
    if count % 2 ==0:
        count += 1
        continue # Back to the top
    print(f"We're counting odd numbers: {count}")
    count+=1

count = 1
while count< 10:
    if count % 2 == 0:
        break # Stop the loop entirelrly
    print(f"We're counting odd numbers: {count}")
    count +=1