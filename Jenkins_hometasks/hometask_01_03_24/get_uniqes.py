def get_uniques(mstr1,mstr2):
    ms1 = ""
    for el in mstr1:
        if el not in mstr2:
            ms1 += el
    for el in mstr2:
        if el not in mstr1:
            ms1 += el
    return ms1


def main():
    mst1 = input("write a first string: ")
    mst2 = input("write a second string: ")
    print(get_uniques(mst1,mst2))
if __name__ == '__main__':
    print("Hello world")
    print("The uniques are")
    main()
