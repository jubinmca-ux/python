
age = int(input("\nEnter your age: "))

vote = lambda age: "\nEligible to vote" if age >= 18 else "\nNot eligible to vote"

print(vote(age))


