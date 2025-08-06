building_list = []
result = []

for test_case in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))
    view = 0

    for building in range(len(building_list)-4):

        check_b_li = building_list[building : building + 5]

        high2 = check_b_li[0]
        main_building = check_b_li[2]
        del check_b_li[2]

        for compare in check_b_li:
            if compare > high2:
                high2 = compare

        if (main_building - high2) > 0:
            view += main_building - high2

    result.append(f"#{test_case} {view}")

for row in result:
    print(row)