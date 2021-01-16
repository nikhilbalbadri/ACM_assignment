def reverseNumber(number):    #function to reverse a number
    revs_number = 0
    while (number > 0):
        remainder = number%10
        revs_number = (revs_number * 10) + remainder
        number = number // 10
    return revs_number

def main():
    num_cases = int(input())
    for i in range(num_cases):
        request = input()    #reads input as request
        if len(request.split()) < 2:    # returns 0 if input only contains 1 integer.
            print(0)
        else:
            num1, num2 = request.split()    #splits string input into two integer seperated by space.
            if not num1.isdigit() or not num2.isdigit():
                print(0)
            else:
                revnum1 = reverseNumber(int(num1)) #reverse num1
                revnum2 = reverseNumber(int(num2)) #reverse num2
                Sum = revnum1 + revnum2
                revsum = reverseNumber(Sum) #reverse Sum
                print(revsum)
if __name__== "__main__" :
    main()