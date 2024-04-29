class Star_Cinema:
    _hall_list=[]
    @classmethod
    def entry_hall(cls,ob):
        cls._hall_list.append(ob)

class Hall(Star_Cinema): 
    def __init__(self,rows, cols, hall_no) -> None:
        self.rows= rows
        self.cols= cols
        self.hall_no= hall_no
        self.seats= {} 
        self.show_list= [] 
        Star_Cinema.entry_hall(self)
    
    def entry_show(self,id,movie_name,time):
        lst=(id,movie_name,time)
        self.show_list.append(lst)
        seat=[]
        for i in range(10):
            seat.append(['A','A','A','A'])
        self.seats[id] = seat


    def show_available_seats(self,id):
        for i in self.seats[id]:
            for j in i:
                print(j,end=' ')
            print()

    def book_seats(self,id,row,col):
        if self.seats[id][row][col] == 'X':
             print("This seat is already booked.")
        else:
            self.seats[id][row][col] = 'X'
            print("Booked successfully.")


    def show_available(self):
        for lst in self.show_list:  
            print(f'NAME : {lst[0]}, ID : {lst[1]}, TIME : {lst[2]}')  

Hall1=Hall(5,5,101)
Hall1.entry_show('111','Jawan maji', '11 November,2023  10.00 AM')
Hall1.entry_show('333','Sujon maji', '11 November,2023  2.00 PM')

while(True):
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAIABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXITS")
    x=int(input("ENTER OPTION :"))
    if x==1:
        print("\n-----Available Shows--------")
        Hall1.show_available()
        print() 

    elif x==2:
        x=(input("ENTER SHOW ID: "))
        if x =='111':
            print("\n-----Available SEATS--------")
            Hall1.show_available_seats(x)
            print() 
        elif x =='333':
            print("\n-----Available Shows--------") 
            Hall1.show_available_seats(x)
            print() 
        
        else:
            print("\nWrong Id. \n")

    elif x==3:
        id=(input("SHOW ID: "))
        if id !='111' and id != '333':
            print("\nWrong Id. \n")
        else:
            n=int(input("NUMBER OF TICKET: "))
            for i in range (n):
                r=int(input("ENTER SEAT ROW: "))
                c=int(input("ENTER SEAT COL: "))
                Hall1.book_seats(id,r,c)

    else:
        break