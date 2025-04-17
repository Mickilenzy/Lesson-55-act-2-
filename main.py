#  Welcome Message

print("🎉 Welcome to the Factor Finder!")
print("Give me any number, and I'll show you all its factors!")

# ✅ Ask user for a number
num = int(input(" Enter a number:"))

print(f"\n 🔍 Finding factors of {num}...")

# 🔢Loop through numbers to find factors 
for i in range(1, num + 1):
    if num % i == 0:
        print(f" {i} is a factor of {num}")

print("\n 🎉All done! That was fun!")        