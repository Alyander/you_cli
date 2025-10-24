from logic.logic import Logic
import os
def App() -> None:
    print("""
    Welcome to Youtube CLI!!!
    """)
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
App()