#4.6 match statement
"""def https_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "Im teapot"
        case _:
            return "something wrong with the internet" """

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")