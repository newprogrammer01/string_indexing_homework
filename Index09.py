def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=len(s)
    if (s=="0" or s=="1" or s=='2' or s=='3' or s=='4' or s=='5' or s=='6' or s=='7' or s=='8' or s=='9') and x==1:
     return s
    else:
        return "False"
print(main("4k"))
