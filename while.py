banana = 5

i = 0

while i < banana:
    print("Banana:{}".format(i))
    i += 1  # increment by +1

    if i == 3:
        continue
        print("hye three")

    if i == 4:
        break
        print("hye two")
