import random, time
import bext

def print_instructions():
    print("Welcome in The Llama Game!")
    print("The goal is to have llamas")
    print("New llamas are born each night, but there are also diseases.")
    print("If all llamas die, game ends.")
    print("Good luck!")
    print("")

def roll_dice(n):
    return random.randint(1, n)

def play_game(num_lam):
    days = 0
    lam_alive = num_lam
    simspeed=2.5
    simspeedsetting=input("Enter simulation speed(0.5 - 5 or 'light')")
    if simspeedsetting=='light':
        simspeed=0
    else:
        try:
            simspeedsetting=float(simspeedsetting)
        except ValueError:
            print("Enter number")
        if simspeedsetting>=0.5 and simspeedsetting<=5:
            simspeed/=simspeedsetting
        else:
            print("Podałeś za wysoką lub za niską prędkość.")
            play_game(num_lam)

    print("Enter game mode((H)ard, (N)ormal, (E)asy, (S)andbox")
    setting=input()
    if setting=='H':
        diffborn=4
        diffdied=5
    elif setting=='N':
        diffborn=4
        diffdied=4
    elif setting=='E':
        diffborn=4
        diffdied=2
    elif setting=='S':
        diffborn=4
        diffdied=1

    while lam_alive > 0:
        days += 1
        bext.fg('yellow')
        print("Day", days)
        
        lam_born = roll_dice(diffborn)
        lam_died = roll_dice(diffdied)
        lam_yesterday=lam_alive

        if lam_born > 1:
            bext.fg('green')
            print("Urodziły się {} małe lamy!".format(lam_born))
            lam_alive += lam_born
        elif lam_born == 1:
            bext.fg('green')
            print("Urodziła się mała lama!")
            num_lam += 1
        else:
            print("Żadne lamy się nie urodziły.")
            
        if lam_died > 0:
            bext.fg('purple')
            print("Pojawiła się choroba!")
            bext.fg('red')
            if lam_died>1 and lam_died<5:
                print(lam_died, "lamy zmarły.")
            elif lam_died>4:
                print(lam_died, "lam zmarło.")
            else:
                print("1 lama zmarła")
            lam_alive -= lam_died
        
        if lam_alive>lam_yesterday:
            bext.fg('green')
        elif lam_alive==lam_yesterday:
            bext.fg('yellow')
        else:
            bext.fg('red')
        print("Aktualna liczba lam:", lam_alive)
        print()
        time.sleep(simspeed)
    print("Koniec gry! Przetrwałeś", days, "dni, a Twoje lamy umarły :(")

def main():
    print_instructions()
    play_game(random.randint(5,10))

a=True
while a:
    bext.fg('yellow')
    main()
    a=input("Czy chcesz zagrać jeszcze raz?1-tak,0-nie")
