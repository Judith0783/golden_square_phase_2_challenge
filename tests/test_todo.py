import pytest
from lib.todo import *

def test_if_string_contain_todo():
    result = includes_to_do("#TODO")
    assert result == True

def test_if_does_not_contain_to_do():
    result = includes_to_do("hello")
    assert result == False

    


"""
# golden_square_phase_2_challenge 
## 1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.
Function: def includes_to_do()
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
"""
