def rot(num):
    num_list = list(str(num))
    for i in range(len(num_list) + 1):
        if num_list[i] == '6':
            num_list.insert(i, '9')
            num_list.pop(i + 1)
            break
        elif '6' not in num_list:
            return num
    return int("".join([str(l) for l in num_list]))
if __name__ == "__main__":
    print(rot(9696))
