# golden_square_phase_2_challenge
## 1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.
Function: def checks_if_includes_to_do()
Parameter: String
Return Value: Boolean (True/False)

## 3. Create Examples as Tests
Make a list of examples of what the function will take and return.
Scenarios
- If string contains #TODO. == return true.
- If string doesnt contain #TODO == return false.
- if empty string return == false
- if string contains #todo.lower == return false
- error
#COMPLETED - this task has already been done
"I am going #todo this today"

## 4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

