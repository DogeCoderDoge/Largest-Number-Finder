session_live = True
numbers = []
a = 0

def largest_num(arr, n):
    #Create a variable to hold the max number
    max_number = arr[0]

    #Using for loop for 1st time to check for largest number
    for i in range(1, n):
        if arr[i] > max_number:
            max_number = arr[i]

            #Returning max's value using return
    return max_number

while session_live:
    print("Tell us a number")
    num = int(input())

    numbers.insert(a, num)
    a += 1

    print("Continue? (Y/N)")
    confirm = input()


    if confirm == "Y":
        pass

    elif confirm == "N":
        session_live = False
        
        #Now I'm running the function
        arr = numbers
        n = len(arr)
        ans = largest_num(arr, n)
        print("smallest number is", ans)

    else:
        print(":/")
        session_live = False


#Another way (Million times easier):
#numbers = []

#while True:
    #print("Tell us a number")
    #numbers.append(int(input()))

    #print("Continue? (Y/N)")
    #confirm = input()
    #if confirm == "Y":
        #continue

    #if confirm == "N":
        #print("Largest number is", max(numbers))
    #else:
        #print(":/")
    #break