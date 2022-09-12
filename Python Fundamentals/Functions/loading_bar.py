def loading_bar(num):
    bar = []

    percent = "%" * (num // 10)
    dots = "." * (10 - num // 10)
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        bar.append(percent)
        bar.append(dots)
        final = "".join(bar)
        print(f"{num}% [{final}] ")
        print("Still loading...")


number = int(input())
loading_bar(number)