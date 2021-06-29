print("Shivam Kirana")
sum = 0
while (True):
    user = input("Enter The Price Of The Product:  \n")
    if (user != 'q'):
        sum = sum + int(user)
        print(f"Your Order Total is {sum}")
    else:
        print(f"Your Bill is {sum} \n Visit Again :) ")
        break
