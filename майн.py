blocks = int(input())
stacks = blocks // 64
remainder = blocks % 64
print(f"{stacks} stacks, {remainder} blocks")
