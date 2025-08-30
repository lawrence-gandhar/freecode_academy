"""
Build a Budget App Project
Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example usage:

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits, and it should be the percentage of the amount spent for each category to the total spent for all categories. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g    
"""
class Category:
    
    def __init__(self, category=None):
        self.ledger = []
        self.category = category
        self.deposited_amount = 0
        self.balance = 0
        self.withdrawl = 0

    def deposit(self, amount=0, description = ""):
        self.ledger.append(
            {
                'amount': self.deposited_amount + amount, 
                'description': description
            }
        )
        self.deposited_amount += amount

    def withdraw(self, amount=0, description = ""):
        self.ledger.append(
            {
                'amount': 0-amount, 
                'description': description
            }
        )

        if self.check_funds(amount):
            self.deposited_amount -= amount
            self.balance = self.deposited_amount 
            self.withdrawl += amount
            return True
        return False

    def get_balance(self, amount=0, description = ""):
        return self.deposited_amount


    def transfer(self, amount=0, category = None):

        description_to = f'Transfer to {category.category.title()}'
        description_from = f'Transfer from {self.category.title()}'
        if self.check_funds(amount):
            if(self.withdraw(amount, description_to)):
                category.deposit(amount, description_from)
                return True
            else:
                return False
        else:
            return False

    def check_funds(self, amount):
        if self.deposited_amount >= amount:
            return True
        return False

    def __str__(self):
        title = f"{self.category:*^30}\n"  # Title line centered with stars
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]  # only first 23 chars
            amt = f"{entry['amount']:.2f}"    # format amount to 2 decimals
            items += f"{desc:<23}{amt:>7}\n"  # left desc, right amount
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
        


def create_spend_chart(categories):

    category_len = len(categories)
    max_len = max([len(x.category) for x in categories])

    chart_title = "Percentage spent by category\n"
    
    # Creator the separator
    # Convert Category Name to title case 
    separator = []
    total_spent = 0

    for x in range(category_len):
        separator.append("---")
        total_spent += categories[x].withdrawl
        

    separator = (''.join(separator)) + "-"
    width = len(separator) + 4
    separator = f'{separator:>{width}}\n'

    # Create the percent block
    # append blank spaces for categories
    data_grid = []

    for x in range(0, 101, 10):
        percent = f"{str(x)+'|':>4}"

        inner_data = [percent] 
        for x in range(len(categories)):
            inner_data.append(" "*3)
        data_grid.append(inner_data)

    # Create a mxn array
    for x in range(category_len):

        spent_percent = ((
            int((categories[x].withdrawl / total_spent) * 100) // 10
        ) * 10)/10

        print(spent_percent)

        j = 0
        for i in range(0,11):
            if j <= spent_percent:
                data_grid[i][x+1] = ' o '
            j += 1

        categories[x] = categories[x].category.title()

    # Create a mxn array
    category_name = []

    for x in range(max_len):
        inner_space = []
        for y in range(category_len): 
            try:
                inner_space.append(f' {categories[y][x]} ')
            except:
                inner_space.append(" "*3)
        inner_space = ''.join(inner_space)+" \n"
        category_name.append(f'{(" "*4)}{inner_space}')

    category_name = (''.join(category_name)).strip("\n")

    # Main Output
    str_f = ""
    for x in range(len(data_grid), -1, -1):
        try:
            str_f += ''.join(data_grid[x])+" \n"
        except:
            pass
    
    return chart_title + str_f + separator + category_name

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(105.55, "groceries")
food.withdraw(33.40, "restaurant and more food")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "deposit")
entertainment.withdraw(15)

business = Category("Business")
business.deposit(1000, "deposit")
business.withdraw(10.99)

print(create_spend_chart([food, entertainment, business]))