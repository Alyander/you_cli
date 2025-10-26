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
    print(urls)
    print(names)
    render(urls, names)
    choose = input("Another video(1) or search(2) or quit(3): ")
    if choose == "1":
        render(urls, names)
    elif choose == "2":
        App()
    else:
        quit()
def render(urls,names):
    i = 0
    for name in names:
        print(f"{i}. {name}")
        i+=1
    num = input("Type Number:")
    os.system(f"mpv {urls[int(num)]} >> /dev/null")
App()