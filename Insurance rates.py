# Denzel Coleman COP1000
# Insurance_rates.py
# Collaborators: None.
# Create a program that calculates the cost of an automotive insurance policy
# by prompting the user to enter their age and how many accidents they have been involved in
def main():

    # Assign a variable age that prompts the user to enter their age
    age = int(input('Enter age of insured: '))

    # Assign a variable accidents that prompts the user to enter how many accidents they have
    accidents = int(input('Enter the number of Accidents: '))

    # Assign a constant variable BASE_CHARGE to equal the price for the
    # base charge for all ages and accidents, if eligible.
    BASE_CHARGE = 500.0

    # Assign a constant variable AGE_FEE to equal the price for the age for
    # for all users under the age of 25.
    AGE_FEE = 100.0
    

    # Create an if statement that determines if the user is eligible for insurancce.
    # If the user is over the age of 25 and has more than 3 accidents, deny them with
    # a Boolean variable insurance_eligible.
    if age > 25 and accidents > 3:
        insurance_eligible = False
        print('You are not eligible for insurance!')
        
    # Create and if-elif block that determines if the user is eligible for insurance.
    # If the user is over the age of 25 and has 3 accidents, they are eligible
    # but must pay a surcharge of $600.
    if age > 25 and accidents == 3:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + 600.0 # Calculate the policy amount for the user by adding the base charge and surcharge of $600.0
        print(f'Policy Amount: ${policy_amt:,.0f}') 

    # Elif the user is over the age of 25 and has 2 accidents, they are eligible
    elif age > 25 and accidents == 2:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + 400.0 # Calculate the policy amount for the user by adding the base charge and surcharge of $400.0
        print(f'Policy Amount: ${policy_amt:,.0f}')

    # Elif the user is over the age of 25 and has 1 accident, they are eligible
    elif age > 25 and accidents == 1:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + 200.0 # Calculate the policy amount for the user by adding the base charge and surcharge of $200.0
        print(f'Policy Amount: ${policy_amt:,.0f}')

    # Elif the user is over the age of 25 and has 0 accidents, they are eligible
    elif age > age and accidents == 0:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + 0.0 # Calculate the policy amount for the user by adding the base charge and no surcharge.
        print(f'Policy Amount: ${policy_amt:,.0f}')




        

    # If the user is under the age of 25 and has more than 2 accidents they are not eligible for insurance.
    if age < 25 and accidents > 2:
        insurance_eligible = False
        print('You are not eligible for insurance!')

    # If the user is under the age of 25 and has less than or equal to 2 accidents, they are eligible for insurance
    if age < 25 and accidents == 2:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + AGE_FEE + 400.0
        print(f'Policy Amount: ${policy_amt:,.0f}')

    # If the user is under the age of 25 and has less than or equal to 1 accident, they are eligible for insurance
    elif age < 25 and accidents == 1:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + AGE_FEE + 200.0
        print(f'Policy Amount: ${policy_amt:,.0f}')
        
    # If the user is under the age of 25 and has less than or equal to 0 accidents, they are eligible for insurance
    elif age < 25 and accidents == 0:
        insurance_eligible = True
        policy_amt = BASE_CHARGE + AGE_FEE
        print(f'Policy Amount: ${policy_amt:,.0f}')
    
    

main()
