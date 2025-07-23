score = float(input("Enter student's score: "))

if score >= 90:
    print("Excellent")  # 90 or above
elif score >= 75:
    print("Good")       # 75-89
elif score >= 60:
    print("Pass")       # 60-74
else:
    print("Fail")       # Below 60