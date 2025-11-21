


def main() -> None:
    cases:int=int(input())
    for _ in range(cases):
        yab=input()
        speed, wall = yab.split(":")
        speed=float(speed)
        wall=float(wall)
        time=wall/speed
        if time <=1:
            print("SWERVE")
        elif time <=5:
            print('BRAKE')
        else:
            print('SAFE')
if __name__ == "__main__":
    main()