def process_input(selected, expression):
    if selected == "C":
        return ""
    elif selected == "DEL":
        return expression[:-1]
    elif selected == "=":
        try:
            return str(eval(expression))
        except:
            return "Error"
    return expression + selected
