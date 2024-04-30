import random
import string
length=int(input("Enter len of the password you want: "))
characters=string.ascii_letters + string.digits + string.punctuation
password=''.join(random.choice(characters) for _ in range(length))
print(password)
