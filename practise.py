class Star_Cinema:
    hall_list = []

    def __init__(self, name, id, time):
        self.name = name
        self.id = id
        self.time = time

    def show_list(self, name, id, time):
        movie = Star_Cinema(name, id, time)
        self.hall_list.append(movie)


class Hall(Star_Cinema):
    show_list = []

    def __init__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.initialize_seats()

    def initialize_seats(self):
        for _ in range(self.rows):
            row = ['A'] * self.cols
            self.seats[_ + 1] = row

    def entry_show(self):
        id = input("Enter the Id: ")
        movie_name = input("Movie Name: ")
        time = input("Movie Time: ")
        show = Star_Cinema(movie_name, id, time)
        self.show_list.append(show)

    def available_seat(self, id):
        seats = []
        for _ in range(self.rows):
            row = ['A'] * self.cols
            seats.append(row)
        self.seats[id] = seats

    def show_available_seats(self, id):
        for row in self.seats[id]:
            for seat in row:
                print(seat, end=' ')
            print()

    def book_seats(self, id, n, row, col):
        for _ in range(n):
            if self.seats[id][row - 1][col - 1] == 'X':
                print("This seat is already booked.")
            else:
                self.seats[id][row - 1][col - 1] = 'X'
                print("Booked successfully.")

    @staticmethod
    def show_available():
        for show in Hall.show_list:
            print(f'NAME: {show.name}, ID: {show.id}, TIME: {show.time}')


show = Star_Cinema("javan", "dgefuy", "dchubkuf")
show.show_list("Pathan", "111", "11 November, 2023")
show.show_list("javan", "333", "11 November, 2023")

while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    x = int(input("ENTER OPTION: "))

    if x == 1:
        Hall.show_available()

    elif x == 2:
        id = input("ENTER SHOW ID: ")
        if id == "111" or id == "333":
            Hall.show_available_seats(id)
        else:
            print("Wrong ID.")

    elif x == 3:
        id = input("SHOW ID: ")
        n = int(input("NUMBER OF TICKETS: "))
        R = int(input("ENTER SEAT ROW: "))
        C = int(input("ENTER SEAT COLUMN: "))
        Hall.book_seats(id, n, R, C)

    elif x == 4:
        break
