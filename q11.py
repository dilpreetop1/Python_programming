n = input("Enter the day: ").lower() 

match n:
    case "s":
        print("SUNDAY")
    case "m":
        print("Monday")
    case "t":
        print("Tuesday")
    case "w":
        print("Wednesday")
    case "th":
        print("Thursday")
    case "f":
        print("Friday")
    case "sa":
        print("Saturday")
    case _:
        print("Invalid day entered.")