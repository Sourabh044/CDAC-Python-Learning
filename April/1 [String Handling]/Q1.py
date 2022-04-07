# # Investment Report
principle = float(input('Enter the investment amount: '))
time = int(input('Enter the Number of years: '))
rate = float(input('Enter the rate as %: '))
ending_balance = principle
total_interest = 0.00
print('Year'.rjust(4), 'Starting Balance'.rjust(22),
      'Interest'.rjust(12), 'Ending balance'.rjust(20))
# exit()
for i in range(1, time+1):
    interest = (ending_balance*rate*time/100)/5
    print(str(i).rjust(4), ('%.2f' % ending_balance).rjust(22), ('%.2f' %
          interest).rjust(12), ('%.2f' % (ending_balance+interest)).rjust(20))
    ending_balance += interest
    total_interest += interest
    
print('Ending balance: Rs.%.2f' % ending_balance)
print('Total interest earned: Rs.%.2f' % total_interest)
