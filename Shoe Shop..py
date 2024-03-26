#!/usr/bin/env python
# coding: utf-8

# In[5]:


def bye(name):
    print(f"Have a great day {name}!")
    print("Welcome back and see you soon!")

    
Stock = {38:15,39:10,40:14,41:10,42:8}

def buy():
    while True:
        name = input("What's your name? ")
        size = int(input("Enter the shoe size desired:(Enter '0' to exit): "))
        if size == 0:
            bye(name)
            break
        else:
            if size not in Stock:
                print(f"The shoe size {size} is not available now.")

            else:
                print(f"you have chosen shoe size {size}.")
                number = int(input("How many pairs would you like to buy? "))
                if number <= Stock[size]:
                    print(f"You have ordered {number} pair(s) size {size}. \nThank you for your purchase!")
                    bye(name)
                    Stock[size] -=number
                    break

                else:
                    print(f"Sorry {name}! We only have {Stock[size]} pairs available.")
                    reconfirm = input("Would you like to buy the pairs available? (yes/no): ")
                    if reconfirm.lower() == "no":
                        bye(name)
                        break
                    else:
                        print(f"Congratulations {name} on your purchase!.")
                        bye(name)
                        Stock[size] = 0


# In[6]:


buy()


# In[ ]:




