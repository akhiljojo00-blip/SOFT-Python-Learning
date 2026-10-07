# Print grade based on a 10th-mark percentage/mark
# Assumption:
# 90-100 -> Grade A
# 60-89  -> Grade B
# 0-59   -> Grade C

mark = float(input("Enter your 10th mark: "))

if 0 <= mark <= 100:
    if mark >= 90:
        print("Grade A")
    elif mark >= 60:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Invalid mark. Enter a value from 0 to 100.")
