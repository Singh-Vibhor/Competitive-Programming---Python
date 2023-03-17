t = int(input())
def ask (x):
	print('-', x)
	return int(input())
for i in range(t):
	cur = int(input())
	add = 0
	ans = 0
	while cur > 0:
		x = ask(add + 1)
		back = x - cur + 1
		add = 2 ** back - 1
		ans += 2 ** back
		cur = x - back
	print('!', ans)
