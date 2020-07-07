from secrets import token_bytes
from typing import Tuple

def random_keys(lenght: int) -> int:
	tb: bytes = token_bytes(lenght)
	return int.from_bytes(tb, 'big')

def encrypt(original: str) -> Tuple[int, int]:
	original_bytes: bytes = original.encode()
	dummy: int = random_keys(len(original_bytes))
	original_key: int = int.from_bytes(original_bytes, 'big')
	encrypted: int = original_key ^ dummy
	return dummy,encrypted

def decrpyt(key1: int, key2: int) -> int:
	decrpyted: int = key1 ^ key2
	temp: bytes = decrpyted.to_bytes((decrpyted.bit_length() + 7) // 8, 'big')
	return temp.decode()

if __name__ == '__main__':
	key1,key2 = encrypt('one Time Pad!')
	result: str = decrpyt(key1, key2)
	print(result)