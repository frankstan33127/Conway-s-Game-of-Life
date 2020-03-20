import random, time, sys, copy

wIn = int(input())
hIn = int(input())
Size = wIn * hIn
li = []
pr = []
bu = []
reset = []


def prin():
    x9 = -1
    for i4 in range(0, hIn):
        for i6 in range(0, wIn):
            x9 += 1
            print(pr[x9] + " ", end="")
        print()


def IN2():
    for i2 in range(0, Size):
        y = random.randint(0, 1)
        if y == 1:
            x1 = "■"
            pr.append(x1)
            li.append(y)
        else:
            x1 = "□"
            pr.append(x1)
            li.append(y)


def IN1():
    for i1 in range(0, Size):
        while True:
            y = int(input())
            if y == 1:
                x1 = "■"
                li.append(y)
                pr.append(x1)
                break
            elif y == 0:
                x1 = "□"
                pr.append(x1)
                li.append(y)
                break
            else:
                print("The number should be either 1 or 0")
                continue


def res():
    for i5 in range(0, Size):
        reset.append(0)


def IN3():
    while True:
        print(
            "For manual input type M and press ENTER. For automatic random input type A and press ENTER"
        )
        ININ = input()
        if ININ == "M":
            return IN1()
            break
        elif ININ == "A":
            return IN2()
            break
        else:
            print("Invalid")
            continue


res()
IN3()
bu = copy.deepcopy(li)
prin()
while True:
    time.sleep(1)
    for x in range(0, len(li)):
        # Corner
        if x == 0 or x == wIn * (hIn - 1) or x == wIn - 1 or x == len(li) - 1:
            if x == 0:
                if li[x] == 1:
                    if (li[x + 1] + li[x + wIn] + li[x + wIn + 1] == 2) or (
                        li[x + 1] + li[x + wIn] + li[x + wIn + 1] == 3
                    ):
                        bu[0] = 1
                        pr[0] = "■"
                    else:
                        bu[0] = 0
                        pr[0] = "□"
                else:
                    if li[x + 1] + li[x + wIn] + li[x + wIn + 1] == 3:
                        bu[0] = 1
                        pr[0] = "■"
                    else:
                        bu[0] = 0
                        pr[0] = "□"
            elif x == wIn * (hIn - 1):
                if li[x] == 1:
                    if (
                        li[(wIn * (hIn - 1)) + 1]
                        + li[(wIn * (hIn - 1)) - wIn]
                        + li[((wIn * (hIn - 1)) - wIn) + 1]
                        == 2
                    ) or (
                        li[(wIn * (hIn - 1)) + 1]
                        + li[(wIn * (hIn - 1)) - wIn]
                        + li[((wIn * (hIn - 1)) - wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[(wIn * (hIn - 1)) + 1]
                        + li[(wIn * (hIn - 1)) - wIn]
                        + li[((wIn * (hIn - 1)) - wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
            elif x == wIn - 1:
                if li[x] == 1:
                    if (
                        li[wIn - 2] + li[(wIn - 1) + (wIn - 1)] + li[(wIn - 1) + wIn]
                        == 2
                    ) or (
                        li[wIn - 2] + li[(wIn - 1) + (wIn - 1)] + li[(wIn - 1) + wIn]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[wIn - 2] + li[(wIn - 1) + (wIn - 1)] + li[(wIn - 1) + wIn]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
            elif x == len(li) - 1:
                if li[x] == 1:
                    if (
                        li[len(li) - 2]
                        + li[(len(li) - 1) - wIn]
                        + li[(len(li) - 1) - wIn - 1]
                        == 2
                    ) or (
                        li[len(li) - 2]
                        + li[(len(li) - 1) - wIn]
                        + li[(len(li) - 1) - wIn - 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[len(li) - 2]
                        + li[(len(li) - 1) - wIn]
                        + li[(len(li) - 1) - wIn - 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
        # Upper Edge and Lower Edge
        elif (x >= 1 and x <= wIn - 2) or (
            x >= (wIn * hIn) - (wIn - 1) and x <= (wIn * hIn) - 2
        ):
            if x >= 1 and x <= wIn - 2:
                if li[x] == 1:
                    if (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x + wIn) - 1]
                        + li[x + wIn]
                        + li[(x + wIn) + 1]
                        == 2
                    ) or (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x + wIn) - 1]
                        + li[x + wIn]
                        + li[(x + wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x + wIn) - 1]
                        + li[x + wIn]
                        + li[(x + wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
            else:
                if li[x] == 1:
                    if (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x - wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) + 1]
                        == 2
                    ) or (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x - wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[x - 1]
                        + li[x + 1]
                        + li[(x - wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) + 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
        # Left Edge
        elif x % wIn == 0 and x != 0 and x <= wIn * (hIn - 2):
            if li[x] == 1:
                if (
                    li[x + 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    == 2
                ) or (
                    li[x + 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    == 3
                ):
                    bu[x] = 1
                    pr[x] = "■"
                else:
                    bu[x] = 0
                    pr[x] = "□"
            else:
                if (
                    li[x + 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    == 3
                ):
                    bu[x] = 1
                    pr[x] = "■"
                else:
                    bu[x] = 0
                    pr[x] = "□"
        # Right Edge
        elif (x + 1) % wIn == 0:
            if (x + 1) != wIn and x != ((wIn * hIn) - 1):
                if li[x] == 1:
                    if (
                        li[x - 1]
                        + li[x + wIn]
                        + li[(x + wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) - 1]
                        == 2
                    ) or (
                        li[x - 1]
                        + li[x + wIn]
                        + li[(x + wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) - 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
                else:
                    if (
                        li[x - 1]
                        + li[x + wIn]
                        + li[(x + wIn) - 1]
                        + li[x - wIn]
                        + li[(x - wIn) - 1]
                        == 3
                    ):
                        bu[x] = 1
                        pr[x] = "■"
                    else:
                        bu[x] = 0
                        pr[x] = "□"
        # Center
        else:
            if li[x] == 1:
                if (
                    li[x + 1]
                    + li[x - 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[(x + wIn) - 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    + li[(x - wIn) - 1]
                    == 2
                ) or (
                    li[x + 1]
                    + li[x - 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[(x + wIn) - 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    + li[(x - wIn) - 1]
                    == 3
                ):
                    bu[x] = 1
                    pr[x] = "■"
                else:
                    bu[x] = 0
                    pr[x] = "□"
            else:
                if (
                    li[x + 1]
                    + li[x - 1]
                    + li[x + wIn]
                    + li[x + wIn + 1]
                    + li[(x + wIn) - 1]
                    + li[x - wIn]
                    + li[(x - wIn) + 1]
                    + li[(x - wIn) - 1]
                    == 3
                ):
                    bu[x] = 1
                    pr[x] = "■"
                else:
                    bu[x] = 0
                    pr[x] = "□"
    li = bu
    bu = copy.deepcopy(reset)
    print(" ")
    prin()
