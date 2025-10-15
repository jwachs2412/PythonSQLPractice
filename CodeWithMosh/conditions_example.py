# If applicant has high income AND good credit, they are eligible for a loan
high_income = False
good_credit = True
criminal_record = True

if high_income and good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

# If applicant has high income OR good credit, they are eligible for a loan
if high_income or good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

# If applicant has good credit and no criminal record, they are eligible for a loan
if good_credit and not criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')
