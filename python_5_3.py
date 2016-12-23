# _*_ coding: utf-8 _*_

import random
game_count = 0
all_counts = []
while True:
	game_count += 1
	guess_count = 0
	answer = random.randint(0,99)
	while True:
			guess = int(input("請猜一個數字(0-99):"))
			guess_count += 1
			if guess == answer:
				print("猜中了")
				print("共猜" + str(guess_count) + "次")
				all_counts.append(guess_count)
				break;
			elif guess > answer:
				print("too large")
			else:
				print("too small")
	onemore = input("try again(Y/N) ?")
	if onemore != 'Y' and onemore != 'y':
		print("welcome to play next time")
		break;