import os

directory = input("insert directory information...")

while True:
    while True:
        folders_st = input("insert starting folder number...")
        if folders_st.isdecimal() is True and len(folders_st) == 10:
            pass
        else:
            print("insert in 10-digit numbers")
            continue
        folders_fn = input("insert ending folder number...")
        if folders_fn.isdecimal() is True and len(folders_fn) == 10:
            break
        else:
            print("insert in 10-digit numbers")
    try:
        for i in range (int(folders_st), int(folders_fn)+1):
            os.makedirs(directory+f"/{str(i)}", exist_ok=True)
    except OSError:
        print("Failed to create directory!!!")
        raise