n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
alice = cards[0::2]
bob = cards[1::2]
print(sum(alice) - sum(bob))
