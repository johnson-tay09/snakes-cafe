print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
response = input(">")
n = 0
order_amounts = {

}
while response != "quit":
    if response in order_amounts:
        order_amounts[response] += 1
    else:
        order_amounts[response] = 1

    if order_amounts[response] > 1:
        reply = f"** {order_amounts[response]} orders of {response} have been added to your meal **"
        print(reply)
        response = input(">")
    else:
        reply = f"** {order_amounts[response]} order of {response} have been added to your meal **"
        print(reply)
        response = input(">")
