from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
	yield 0
	if n > 0: yield 1
	Last: int = 0
	Next: int = 1
	for m in range(1,n):
		Last, Next = Next, Next + Last
		yield  Next

if __name__ == "__main__":
	for i in fib(7):
		print(i)
from compression import CompressedGene
comp = CompressedGene('AAATTTGGG')
org = comp.decompress()
print(org)