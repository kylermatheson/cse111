import df_functions as df


def main_menu():
    
    #menu options
    choose = int(input("Welcome to the Main Menu\nOptions:\n(1) Input New Data Table\n(2) Categorize Table\n(3) Monthly Expenditures\n(4) My Spending habbits\n(5) Save As CSV\n(6) Quit"))
    
    #menu logic
    match choose:
        case 1:
            df.get_file_path()
        case 2:
            df.catorgize()
        case 3:
            df.monthly()
        case 4:
            df.advice()
        case 5:
            df.save()
        case 6:
            return
        case _:
            print("INVALID REQUEST enter a value from 1-6")
          


def main():
    print("Welcome to our aplicaiton to interperate your checking data! ")
    main_menu()
    



if __name__ == "__main__":
    main()