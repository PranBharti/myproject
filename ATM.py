import platform
password = 2703
start = 'yes'
balance = 500000
# Function to make a beep sound
def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(5000, 500)  # Frequency=1000 Hz, Duration=200 ms
    else:
        print('\a')  # System bell for Linux/macOS
while start.lower() == 'yes':
    print('<<< Welcome to ATM >>>')
    pin = int(input('Enter ATM pin:'))
    if password == pin:
        beep()
        amount = int(input('Enter your withdrawal amount:'))
        if amount % 100 != 0:
            beep()
            print('Error: ATM can dispense multiples of 100')
        else:
            a_2000 = 100
            a_1000 = 100
            a_500 = 100
            a_200 = 100
            a_100 = 100
            print('Processing your transaction...')
            beep()
            beep()
            total = amount
            take_2000 = min(amount // 2000, a_2000)
            amount -= take_2000 * 2000
            
            take_1000 = min(amount // 1000, a_1000)
            amount -= take_1000 * 1000
            
            take_500 = min(amount // 500, a_500)
            amount -= take_500 * 500
            
            take_200 = min(amount // 200, a_200)
            amount -= take_200 * 200
            
            take_100 = min(amount // 100, a_100)
            amount -= take_100 * 100
            
            # Display notes dispensed
            if take_2000 > 0:
                print('<< ₹2000 notes >>', take_2000)
            if take_1000 > 0:
                print('<< ₹1000 notes >>', take_1000)
            if take_500 > 0:
                print('<< ₹500 notes >>', take_500)
            if take_200 > 0:
                print('<< ₹200 notes >>', take_200)
            if take_100 > 0:
                print('<< ₹100 notes >>', take_100)
            
            if amount > 0:
                beep()
                print('Sorry, ATM cannot dispense the remaining amount:', amount)
            else:
                balance -= total
                beep()
                print('* Please collect your cash *')
                print('And the remaining balance is:', balance)
            
            start = input('Enter yes to withdraw more cash: ')
    else:
        beep()
        print('PIN is wrong')



    
