products = ["coke", "pepsi", "fanta", "water", "tea"]
products_price = {
    "coke" : 1500, 
    "pepsi" :1300, 
    "fanta" : 1400, 
    "water" : 800, 
    "tea" : 1000
}
print("Please select the product number")

def select_product():
    product_num = int(input("product number :"))
    if product_num > len(products):
        print("Invalid input. Please select a number again")
        return int(input("product number :"))
    else:
        return products[product_num - 1]

selected_product = select_product()
print(selected_product,"-", "₩", products_price[selected_product])
print("Please select a payment method")

def payment_method():
    customer_choice = int(input("Please select the number of the payment method you want. 1. Card 2. Cash : "))
    if customer_choice == 2:
        current_input_amount = 0
        product_price = int(products_price[selected_product])
        while True:
            if current_input_amount < product_price:
                print("Please insert your cash")
                input_amount = int(input("₩ "))
                current_input_amount += input_amount
                print("₩", current_input_amount, "/", "₩", products_price[selected_product])
            else:
                print(f"The change is ₩{current_input_amount - products_price[selected_product]}")
                say_goodbye()
                break
    else:
        say_goodbye()
        
def say_goodbye():
    print("The payment has been completed")
    print("Thank you for your purchase, Goodbye!")

payment_method()