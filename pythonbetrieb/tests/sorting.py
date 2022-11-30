import random
def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)):
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
        my_list[scan_pos + 1] = key_value
def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end="")
    print()
print("Selectionsort:")
my_list = []
for i in range(10):
    my_list.append(random.randrange(100))
print_list(my_list)
selection_sort(my_list)
print_list(my_list)
print("Insertionsort:")
my_list = []
for i in range(10):
    my_list.append(random.randrange(100))
print_list(my_list)
insertion_sort(my_list)
print_list(my_list)
 