#taking n inputs
n = input()
Room_list = input().split()
Room_set = set(Room_list)

for ele in list(Room_set):
    Room_list.remove(ele)

CAPTAIN_ROOM_NUM = Room_set.difference(set(Room_list)).pop()
#printing captains room number
print(CAPTAIN_ROOM_NUM)
