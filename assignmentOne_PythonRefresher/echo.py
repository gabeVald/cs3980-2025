# This script contains the first function that is required for the first homework assignment;
# The function, echo, works as follows:
# The first argument, text, is required and dictates the string that will echo back to the user.
# The second argument, repetitions, is not required, but if specified will dictate the number of times the string echos back before fading fully. If no argument is given, 3 is used.
# Based on the given outputs, I decided to implement the function works as follows:
# Echo back the initial string index [-repetitions], subtracting 1 from the value for repetitions for each subsequent echo.
# In the default case, that results in [-3:]


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    while repetitions > 0:
        print(text[-repetitions:])
        repetitions -= 1
    return "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

"""
Sample outputs based on assignment example:
First Example:
(base) Gabes-MacBook-Air-7:assignmentOne:PythonRefresher gabe$ python echo.py
Yell something at a mountain: Helloooo
ooo
oo
o
.

Second Example:
(base) Gabes-MacBook-Air-7:assignmentOne:PythonRefresher gabe$ python echo.py
Yell something at a mountain: echo 123
123
23
3
.
"""
