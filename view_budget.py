# import the utility function that formats float to £ sterling
from to_sterling import to_sterling
# import clear_screen utility function
from clear_screen import clear_screen
# Import the Ledger instance (singleton).
from Ledger import ledger
# Import the constants storing magic strings.
from constants import INCOME, EXPENSES, ESSENTIAL, NON_ESSENTIAL

def view_budget() -> None:
      '''
      Displays a summary of the user's budget:
            - Monthly Income
            - Monthly Expenses
            - Monthly Essential Expenses
            - Monthly Non-Essential Expenses

            - Determines whether the use is:
                  - under budget and by how much
                  - reached their budget
                  - over their budget and by how much

            If the user's Essential Expenses alone exceed their income:
                  - Suggests that they recategorise one or
                    more Essential Expenses to Non-Essential Expenses

            If the user's Non-Essential Expenses but not their
            Essential Expenses are causing
            the user to exceed their budget
                  - Suggests that they remove one or more 
                    Non-Essential Expenses

      Finally, prompts the user to press enter to return to the Main Menu.
      '''
      # Clear the screen.
      clear_screen()
      # Get income from ledger
      income = ledger.get_income()

      # Display the user's monthly income
      print("---------------------------------------------\n" +
            f"Monthly {INCOME}:\n" +
            "---------------------------------------------\n" +
            f"{to_sterling(income)}\n")

      # Sum the amounts of all expenses
      sum_all_expenses = sum(expense.get_amount() or 0
                             for expense in ledger.get_all_expenses())

      # Display the sum amount of all expenses in sterling
      print("---------------------------------------------\n" +
            f"Total {EXPENSES} Amount:\n" +
            "---------------------------------------------\n" +
            f"{to_sterling(sum_all_expenses)}\n")

      # Sum the amounts of all essential expenses
      sum_essential_expenses = sum(
          expense.get_amount() or 0
          for expense in ledger.get_expenses_by_category(ESSENTIAL))

      # Display the sum amount of all essential expenses in sterling
      print("---------------------------------------------\n" +
            f"Total {ESSENTIAL} {EXPENSES}:\n" +
            "---------------------------------------------\n" +
            f"{to_sterling(sum_essential_expenses)}\n")

      # Sum the amount of all non-essential expenses
      sum_non_essential_expenses = sum(
          expense.get_amount() or 0
          for expense in ledger.get_expenses_by_category(NON_ESSENTIAL))

      # Display the sum amount of all non-essential expenses in sterling
      print("---------------------------------------------\n" +
            f"Total {NON_ESSENTIAL} {EXPENSES}:\n" +
            "---------------------------------------------\n" +
            f"{to_sterling(sum_non_essential_expenses)}\n")

      if sum_all_expenses < income:
            # Display if the user is under budget
            print("==============================================\n" +
                  "You are under budget by " +
                  f"{to_sterling(income - sum_all_expenses)}\n" +
                  "==============================================\n")

      if sum_all_expenses == income:
            # Display if the user has reached their budget
            print("==============================================\n" +
                  "You have reached your budget\n" +
                  "==============================================\n")

      if sum_all_expenses > income:
            # Display if the user is over budget and by how much
            print("==============================================\n" +
                  "You are over budget by " +
                  f"{to_sterling(sum_all_expenses - income)}\n" +
                  "==============================================\n")

            if sum_essential_expenses > income:
                  '''
                  Display if the user's essential expenses are 
                  causing their budget to be exceeded and by how much
                  '''
                  print(
                      "==============================================\n" +
                      f"Your {ESSENTIAL} {EXPENSES} alone exceed your\n" +
                      f"budget by {to_sterling(sum_essential_expenses - income)}\n"
                      + "Consider whether any of your\n" +
                      f"{ESSENTIAL} {EXPENSES}\n" +
                      f"can be recategorised to {NON_ESSENTIAL}\n" +
                      "==============================================\n")

                  # Display the user's non essential expenses
                  print("---------------------------------------------\n" +
                        f"Your {ESSENTIAL} {EXPENSES}\n" +
                        "---------------------------------------------")
                  for expense in ledger.get_expenses_by_category(ESSENTIAL):
                        print(f"{expense.get_title()}: " +
                              f"{to_sterling(expense.get_amount())}")

            if sum_all_expenses - sum_non_essential_expenses <= income:
                  '''
                  Display if the user's non esential expenses are causing
                  them to exceed their budget and by how much
                  '''
                  print("==============================================\n" +
                        "Consider whether you can remove one or more\n" +
                        f"of your {NON_ESSENTIAL} {EXPENSES}\n" +
                        "==============================================\n")

                  # Display the user's non essential expenses
                  print("---------------------------------------------\n" +
                        f"Your {NON_ESSENTIAL} {EXPENSES}\n" +
                        "---------------------------------------------")
                  '''
                  Iterate over the user's non essential expenses and 
                  print the expenses title and amount in £
                  '''
                  for expense in ledger.get_expenses_by_category(
                      NON_ESSENTIAL):
                        print(f"{expense.get_title()}: " +
                              f"{to_sterling(expense.get_amount())}")
      '''
      Prompt the user to press the Enter key to return to the Main Menu
      and await their input.
      '''
      input(
            "---------------------------------------------------------\n" + 
           "Press the ENTER key to return to the Main Menu.\n" +
           "---------------------------------------------------------\n"
      )

      # Return nothing from the function
      return None
