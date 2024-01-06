# If and else statements
print("Accepting scores from students and displaying grade obtained")
print("____________________________________________________________")

score = int(input("Enter score obtained: "))

if score > 100:
    print("Enter a valid Score!")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
elif score >= 40:
    print("Grade: E")
else:
    print("YOU HAVE FAILED!!!")
