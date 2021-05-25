# age=int(input("Enter Your Age\n"))

year=int(input("Enter Your Birth Year\n"))

if year<=9999:
    y = int(input("In Which year You Want to cheack your age \n"))
    if y in range(year,9999):
        s = y - year
        print(f" Your Age in {y} is {s}")
    else:
        print("Enter Your Correct Birth Year ")
exit("Thank You")

