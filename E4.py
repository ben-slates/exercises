import random
import string
letters = string.ascii_lowercase

print ("Welcome to Language Encryptor")
choice=int(input("Select an option to continue\n 1.Encoder.\n 2.Decoder.\n 3.Exit\n"))

if choice == 1:
	text = input("enter message here:")
	word=[]
	word = text.split(' ')
	encoded_message = []
	for w in word:
		if len(w) < 3:
			encoded = w[::-1]
		else:
			rand =  ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
			rand2 =  ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
			encoded = (rand + w + rand2)
		encoded_message.append(encoded)
	final = ' ' .join(encoded_message)
	print(final)
elif choice == 2:
    text = input("enter message here:")
    word=[]
    word = text.split(' ')
    decoded_message=[]
    for w in word:
        if len(w) < 3:
            decode = w[::-1]
        else:
            decode = w[3:-3]
        decoded_message.append(decode)
    final = ' '.join(decoded_message)
    print(final)
elif choice == 3:
    print("Exiting the program.\nGood bye.")
    exit()
else:
    exit()
