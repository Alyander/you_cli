from logic.logic import Logic
import os
print("""
    Welcome to Youtube CLI!!!
    """)
def App() -> None:
    logic = Logic("https://inv.nadeko.net")
    query = input("Search: ")
    data = logic.query(query, 1)
    urls = data[0]
    names = data[1]
    channel_names = data[3]
    i = 0
    for name in names:
        print(f"{i}. {name} - {channel_names[i]}")
        i+=1
    num = input("Type Number:")
    os.system(f"mpv {urls[int(num)]} >> /dev/null")
    choose = input("Another(1) video or search(2) or quit(3): ")
    if choose == "1":
        i = 0
        for name in names:
            print(f"{i}. {name} - {channel_names[i]}")
            i+=1
    elif choose == "2":
        App()
    else:
        quit()
App()