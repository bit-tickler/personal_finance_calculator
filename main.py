# import built in time module
import time 

# import the main_menu subroutine
from main_menu import main_menu

# Display the welcome message to the user
print(
  "==========================================\n" +
  "Welcome to Personal Finance Calculator...\n" +
  "==========================================\n"
)

time.sleep(2)

# Run the main_menu subroutine
main_menu()
