def caesar_cipher_numbers(numbers: list):
    return[''.join([(str(((int(x)+3))%10)) for x in i]) for i in numbers]

print(caesar_cipher_numbers(input("Sonlarni kiriting: ").split()))