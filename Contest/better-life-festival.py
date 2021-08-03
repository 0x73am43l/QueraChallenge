r, c = map(int, input().split())

s = ""

if c <= 10:
	s = "Right"
else:
	s = "Left"

row = (10 - r) + 1

col = c if s == "Right" else (20 - c) + 1

print(s, row, col)
