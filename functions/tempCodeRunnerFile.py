def multiple(num1, num2=6, strin="ABC"):
    result = num1 * num2
    return result, strin

res, word = multiple(num1=2, strin="Not ABC")
print(res, word) # 12, Not ABC