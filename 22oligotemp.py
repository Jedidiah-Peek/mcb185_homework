# 22oligotemp.py by Jedidiah_Peek

def temp_melt(a, c, g, t):
	nt_count = a + c + g + t
	if a < 0 or c < 0 or g < 0 or t < 0:
		return 'Error: negative nucliotide count'
		
	elif nt_count == 0:
		return 'Error: no nucliotides'
		
	elif nt_count <= 13:
		return (a + t) * 2 + (g + c) * 4
		
	else:
		return 64.9 + 41 * (g + c - 16.4) /nt_count
		
		
print(temp_melt(1, 1, 1, 1))
print(temp_melt(5, 10, 12, 14))
print(temp_melt(23, -5, 18, 16))
print(temp_melt(0, 0, 0, 0))