import random, time, sys, copy, os

clear = lambda: os.system("cls")
# Fixed width for animation
wIn = 15
# Fixed height for animation
hIn = 15
Size = wIn * hIn
li = []
pr = []
bu = []
reset = []


def res():
    for i5 in range(0, Size):
        reset.append(0)


li = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
for i10 in range(0, len(li)):
    if li[i10] == 1:
        G = "■"
        pr.append(G)
    else:
        G = "□"
        pr.append(G)


def prin():
    x9 = -1
    for i4 in range(0, hIn):
        for i6 in range(0, wIn):
            x9 += 1
            print(pr[x9] + " ", end="")
        print()


prin()
clear()
res()
bu = copy.deepcopy(li)


def cls1():
    print("\n" * hIn)


while True:
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
    clear()
