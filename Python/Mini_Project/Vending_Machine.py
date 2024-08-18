import time, os, sys

products = ["coke", "pepsi", "fanta", "water", "tea"]
products_price = {
    "coke" : 1500, 
    "pepsi" :1300, 
    "fanta" : 1400, 
    "water" : 800, 
    "tea" : 1000
}
def typingPrint(text, *args, **kwargs):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
  
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value  
  
def clear_screen():
    os.system("cls")
  
typingPrint("Please select the product number\n")

def select_product():
    product_num = int(typingInput("product number :"))
    time.sleep(1)
    if product_num > len(products):
        typingPrint("Invalid input. Please select a number again\n")
        return int(input("product number :"))
    else:
        return products[product_num - 1]

selected_product = select_product()
price = products_price[selected_product]
typingPrint(f"{selected_product} - ₩ {price}\n")
typingPrint("<select a payment method>\n")

def payment_method():
    customer_choice = int(typingInput("Please select the number of the payment method you want. 1. Card 2. Cash : "))
    if customer_choice == 2:
        current_input_amount = 0
        product_price = int(price)
        while True:
            if current_input_amount < product_price:
                typingPrint("Please insert your cash\n")
                input_amount = int(typingInput("₩ "))
                current_input_amount += input_amount
                print(f"₩ {current_input_amount} / ₩ {price}\n")
            else:
                typingPrint(f"The change is ₩{current_input_amount - price}\n")
                say_goodbye()
                break
    else:
        say_goodbye()
        
def say_goodbye():
    typingPrint("The payment has been completed\n")
    time.sleep(3)
    typingPrint("Thank you for your purchase, Goodbye!\n")
    

payment_method()

def return_to_first_screen():
    typingPrint("This screen will return_to_first_screen in 3..\n")
    time.sleep(1)
    typingPrint("2..")
    time.sleep(1)
    typingPrint("1..")
    time.sleep(1)
 

return_to_first_screen()
clear_screen()