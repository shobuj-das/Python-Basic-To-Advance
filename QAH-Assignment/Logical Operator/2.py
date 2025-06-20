def is_eligible_for_vote(age, voting_age):
    return True if age >= voting_age else False

voting_age = 8
age = int(input("Enter age: "))

if(is_eligible_for_vote(age, voting_age)):
    print("Eligible of vote")
else:
    print("Not eligible for vote")