def stringsplit(stringsplit):
    parts = stringsplit.split('_')
    if len(parts) != 3:
        raise ValueError("Input string should contain exactly three parts separated by underscores")
    result = {
        "name": parts[0],
        "Domain_name": parts[1],
        "Regno": parts[2]
    }
    return result
value = input("Enter the string with '_' and without spaces: ")

try:
    answer = stringsplit(value)
    print(answer)
except ValueError as e:
    print(e)
