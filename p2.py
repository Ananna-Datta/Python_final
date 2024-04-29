class Star_Cinema:
    # Ei class a shudhu "hall list" r "entry_hall" ei duita jinish e rakhte bolsilo.
    __hall_list=[]
    @classmethod
    def entry_hall(cls,ob):
        cls.__hall_list.append(ob) # Hall class theke Hall er ekta object ashbe jeta hall_list a append hobe.
   
   # show_list holo ekta tuple. function/method na. jeta Hall class er moddhe thakbe. so eta purata kete diyen. ami apatoto comment kore rakhlam. 
    '''def show_list(self,name,id,time):
        list=Star_Cinema(name,id,time)
        self.hall_list.append(list)''' 



class Hall(Star_Cinema):
     # init eivabe likhte hoy " __init__"....
     # 2 no. question er last a bola ase je " rows, cols, hall_no" diye Hall class er object initialized korte. 
    def __init__(self,rows, cols, hall_no) -> None:
        self.__rows= rows
        self.__cols= cols
        self.__hall_no= hall_no
        self.__seats= {} # 2 er a te bola ase je seats holo ekta dictinary and eita hall class a thakbe.
        self.__show_list= [] # eitai holo show_list jeta apni Star_Cinema class likhsilen function hishebe, kintu eta hobe ekta tuple
        Star_Cinema.entry_hall(self) # eikhane 'self' holo Hall class er ekta object jeta purata Star_Cinema class er entry hall a jabe.


    # eigula upore likhsi. eikhane hobe na, kete diyen. karon prottek ta Hall object er e ekta show_list r seats thakbe.
    '''show_list=[]
    seats={}'''

    # 3 no. question a bola ache je show list ta entry_show method er maddhome nite hobe. kintu apni niche direct show_list er moddhe niye nicchen.
    # oikhane apni just show_list er jaygay entry_show likhben tailei hobe(ami likhe diyechi).
    def entry_show(self,id,movie_name,time): #niche ei method ta jokhon call korechi tokon id, movie_name, time gula send korechi tai eigula eikhane likhechi
        '''id=input("Enter the Id :")
        movie_name=input("Movie Name :") #eigula kete diyen
        time=input("Movie Time :")'''
        lst=(id,movie_name,time)
        self.__show_list.append(lst)
        __seat=[]
        for i in range(10):
            __seat.append(['A','A','A','A'])
        self.__seats[id] = __seat # prottek ta movie er jonno seat list eikhanei niye nisi. niche apni jei method likhsen oitar jonno apnake
                                # alada kore available_seat function call kora lagto(r apni oi function kothao call o koren nai dekhlam). akhn r oi function lagbe na. 


    '''def available_seat(self,id):
        seat = []
        for i in range(10):
            seat.append(['A','A','A','A'])
        self.seats[id] = seat'''

    def show_available_seats(self,id):
        for i in self.seats[id]:
            for j in i:
                print(j,end=' ')
            print()

    def book_seats(self,id,row,col):
        # row = int(input("Enter row : "))
        # col = int(input("Enter coloumn : "))

        #eikhane for loop ta chalale ektu jhamela hobe. sudu ekta book korte parben baki gula parben na. karon row r col ekbar e ashtese.
        # ei for loop ta main function a chalate hobe.
        '''for i in n:'''
        if self.__seats[id][row][col] == 'X':
             print("This seat is already booked.")
        else:
            self.__seats[id][row][col] = 'X'
            print("Booked successfully.")


    # def show_available(self):
    #     # list = Star_Cinema(n,id,time)
    #     # self.train_list.append(list)
    #     for lst in self.hall_list:
    #         print(f'NAME : {lst.name}, ID : {lst.id}, TIME : {lst.time}')

    def show_available(self):
        # list = Star_Cinema(n,id,time)
        # self.train_list.append(list)
        for lst in self.show_list:  # show thakbe show list a. hall_list a show paben na to!!!!
            print(f'NAME : {lst[0]}, ID : {lst[1]}, TIME : {lst[2]}')  # list er value index diye access korte hoy. lst.name diye access kora jabe na to!!!


# show=Star_Cinema("aknx","ckmd","ssssssssssd")
# show.show_list("Pathan","111","11 November,2023")
# show.show_list("javan","333","11 November, 2023")

Hall1=Hall(5,5,101)
Hall1.entry_show('111','Pathan', '11 November,2023')
Hall1.entry_show('333','javan', '11 November,2023')

while(True):
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAIABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXITS")
    x=int(input("ENTER OPTION :"))
    if x==1:
        print("\n-----Available Shows--------") # eita ektu shundor korar jonno disi
        Hall1.show_available()
        print() # ekta new line print korar jonno disi.

    elif x==2:
        # id = int(input("ENTER SHOW ID : "))
        x=(input("ENTER SHOW ID: "))
        if x =='111':
            print("\n-----Available SEATS--------") # eita ektu shundor korar jonno disi
            Hall1.show_available_seats(x)
            print() # ekta new line print korar jonno disi.
            #print("Correct password which is 111")
        elif x =='333':
            print("\n-----Available Shows--------") # eita ektu shundor korar jonno disi
            Hall1.show_available_seats(x)
            print() # ekta new line print korar jonno disi.
            #print("Correct password which is 333")
        else:
            print("\nWrong Id. \n")
            #eikhane break hobe na. break dile to pura file tai bondho hye jabe
            # break
        # Hall.book_seats(x) # seat booking 3 te hobe. eikhane kno disen jani na.....


    elif x==3:
        id=(input("SHOW ID: "))
        if id !='111' and id != '333':
            print("\nWrong Id. \n")
        else:
            n=int(input("NUMBER OF TICKET: "))
            for i in range (n):  # ei loop ta book_seats function a na chaliye eikhane chalalam. Ekhn n ta seat book korte parbe
                r=int(input("ENTER SEAT ROW: "))
                c=int(input("ENTER SEAT COL: "))
                Hall1.book_seats(id,r,c)

    else:
        break