age = int(input('Enter your age: '))

if (age <= 10):
  ticket_price = 'Free'
  print('The ticket is ', ticket_price, ' for you.')
elif (age > 10 and age <= 18):
  ticket_price = 20
  print('The ticket is Rs.', ticket_price)
elif (age > 18 and age < 100):
  ticket_price = 50
  print('The ticket is Rs.', ticket_price)
