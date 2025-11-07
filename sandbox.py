def main() -> None:
    num=int(input())
    for _ in range(num):
        x, y=input().split(" ")
        x=int(x)
        y=int(y)
        print(f'{x+y} {x*y}')
if __name__ == "__main__":
    main()