from config import *

def main():
    while True:
        page = "Menu"
        title_cmd(name, version, page)
        clear()
        print(f"""
{p}======{red}Menu{r}======{m}{red}
|{r} {b}1{r}- {b}Programs    {red}|
|{r} {b}2{r}- {b}Options     {red}|
|{r} {b}3{r}- {b}Exit        {red}|
{p}================{m}
        """)
        choice = input(choiceinput)
        if choice == "1":
            programs()
        elif choice == "2":
            pass
        elif choice == "3":
            exit()
        else:
            invalidchoice()
            pass

def programs():
    while True:
        page = "Programs"
        title_cmd(name, version, page)
        clear()
        print(f"""
{p}========={red}Programs{r}========={m}{red}
|{r} {b}1{r}- {b}Post-It               {red}|
|{r} {b}2{r}- {b}                      {red}|
|{r} {b}3{r}- {b}                      {red}|
|{r} {b}4{r}- {b}                      {red}|
|{r}{o}B{c}-{cy}Back {o}M{c}-{cy}Menu {o}N{c}-{cy}Next{red}|
{p}=========================={m}
        """)
        choice = input(choiceinput)
        if choice == "1":
            post_it()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "M" or choice == "m":
            main()
        else:
            invalidchoice()
            pass


if __name__ == '__main__':
    main()