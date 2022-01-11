#4.6 match statement
def https_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "Im teapot"
        case _:
            return "something wrong with the internet"