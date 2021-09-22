amount = int(input())

multip = 1
for i in range(amount):
    width = amount * 2 -1
    printable = multip*"#"
    print(printable.center(width))
    multip += 2
