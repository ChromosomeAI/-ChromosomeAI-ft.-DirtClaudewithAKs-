#!/data/data/com.termux/files/usr/bin/python3

def process_card_number():
    while True:
        try:
            number = input("Enter 16-digit number (or 'q' to quit): ").replace(" ", "")
            if number.lower() == 'q':
                break
            if len(number) != 16 or not number.isdigit():
                print("Please enter exactly 16 digits")
                continue
                
            total = 0
            for i, digit in enumerate(reversed(number)):
                digit = int(digit)
                if i % 2 == 1:  # every second digit
                    doubled = digit * 2
                    total += doubled if doubled < 10 else doubled - 9
                else:
                    total += digit
                    
            result = total * 3
            print(f"Sum: {total}")
            print(f"Result (sum × 3): {result}")
            
        except ValueError:
            print("Numbers only! Try again or 'q' to quit")

if __name__ == "__main__":
    print("Card Number Sum×3 Calculator - Enter 'q' to quit")
    process_card_number()
