# program2_2.py
# Collaborators: None.

# Write a program that has the user purchase an item at a base price
# and calculate the price with shipping and taxes included in a
# receipt form.

def main():

    # Assign a variable named widget that prompts the user to enter
    # the amount of widgets they would like to purchase.
    widget = int(input('How many Widgets do you want? ==> '))

    # Assign a variable which is the base price of the widget
    widget_cost = 24.99

    # Create a print statement that centers the receipt for the user.
    print('\n\t R E C E I P T\n')

    # Assign a variable called widget_total and calculate the total cost
    # of the widget by multiplying the amountof widgets being purchased by
    # the cost of the widget.
    widget_total = widget * widget_cost

    # Print a statement that shows the user the base cost of the widget
    # along with showing the amount being purchased at the base price.
    print(f' Widgets\' base cost : ${widget_total:,.2f} ({widget:,} @ ${widget_cost})')

    # Assign a variable named shipping and calculate the shipping cost
    # per widget by the amount of widgets being purchased.
    shipping = 1 * widget

    # Assign a variable named SALES_TAX_RATE which is the widget total
    # multiplied by 7% tax.
    SALES_TAX_RATE = widget_total * 0.07

    # Print a statement showing the Shipping and handling total
    print(f' S&H : ${shipping:,.2f}')

    # Print a statement showing the tax total
    print(f' Tax : ${SALES_TAX_RATE:,.2f}')
    
    # Calculate the total by assigning a variable that calculates the
    # widget total price and adds shipping and taxes to it.
    widget_final_total = widget_total + shipping + SALES_TAX_RATE
    
    # Print a statement that shows the total price with shipping and
    # taxes.
    print(f'\n Total : ${widget_final_total:,.2f}')



main()
