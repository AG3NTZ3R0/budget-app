class Category:
  """Represent a category within a budget."""

  def __init__(self, cat_name):
    """Initialize attributes of the category."""
    self.cat_name = cat_name
    self.ledger = []

  def __str__(self):
    """String representation of class."""
    name_len = len(self.cat_name)
    stars = int((30 - name_len) / 2)
    title_line = "*" * stars + self.cat_name + "*" * stars

    ledger = ''
    for object in self.ledger:
      object_description = object["description"] 
      whitespace1 = 23 - len(object_description[:23]) 
      object_amount = '%.2f' % object["amount"]
      whitespace2 =  7 - len(object_amount[:7]) 

      ledger += object_description[:23] + " " * whitespace1 + " " * whitespace2 + object_amount + '\n'
    
    
    output = title_line + '\n' + ledger + f"Total: {self.get_balance()}"
    return output

  def deposit(self, amount, description=''):
    """Append and object to the ledger list."""
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    """Return True or False if the withdrawal took place or not."""
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  def get_balance(self):
    """Returns the balance of the budget category."""
    balance = 0
    if self.ledger != None:
      for object in self.ledger:
        balance += object["amount"]
    return balance
  
  def transfer(self, amount, cat_name2):
    """Return True or False if the transfer took place or not."""
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {cat_name2.cat_name}")
      cat_name2.deposit(amount, f"Transfer from {self.cat_name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    """Returns True or False if the amount is greater than the balance."""
    if amount > self.get_balance():
      return False
    else:
      return True

def create_spend_chart(categories):
  title = "Percentage spent by category"
  output = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
  return output