gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())

result = gryffindor | ravenclaw | slytherin | hufflepuff
print(result)