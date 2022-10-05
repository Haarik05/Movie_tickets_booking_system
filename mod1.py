print("Movie Booking System")
print("--------------------")
total_shows = ["1.Titanic","2.Ironman","3.sitaram","4.thiruchitrambalam"]
shows_in_screen1 = ["1.Titanic","2.Ironman"]
shows_in_screen2 = ["3.sitaram","4.thiruchitrambalam"]
#--------------------------------------------------
screen1_first_show = "Titanic"
screen1_first_show_time = "10am"
#------------------------------------------------
screen1_second_show = "Iron man"
screen1_second_show_time = "12:30pm"
#--------------------------------------------
screen2_first_show = "Sitaram"
screen2_first_show_time = "11am"
#----------------------------------------------
screen2_second_show = "thiruchitrambalam"
screen2_second_show_time = "3pm"
#--------------------------------------------

userdatabase = {}
#-------------------------------------------
user_id = 0
no_tickets = 15
discount = ["d10","d20","d30"]
screen1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
screen2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]] 
screen3 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]] 
screen4= [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]] 
#-----------------------------------------------------
first_class = 120
second_class = 100
third_class = 60
#-----------------------------------------------
# -------------Discount------------------------- 
def dis_user(n):
    if n == "d10":
        return 10
    elif n =="d20":
        return 20
    elif n =="d30":
        return 30
    else:
        return 0
#--------------------------------------------------------------


def cancellation(id):
    
    for x in userdatabase.keys():
        if x==id:
            print("id is ",x)
            id_fetch = x
            break
    
    for x,y in userdatabase.items():
        if x==id_fetch:
            print(y)
            print(y["screen"])
            print(y["class"])
            print(y["selected seats"])
            selected_screen = y["screen"]
            selected_class=y["class"]
            selected_seat = y["selected seats"]
            y["amount"] = 0
            if selected_screen == "screen1":
                if selected_class==1:
                    
                    print("seats before restored",screen1)
                    for i in selected_seat:         #[((i-5)-1)]
                       screen1[0][(i-6)] = i   # [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
                    print("seats after restored")
                    print(screen1)
                    print("cancellation successfully")
                elif selected_class ==2:
                    print("seats before restored",screen1)
                    m=1
                    for i in selected_seat: 
                                                  # -3,8-5,9-7
                        screen1[1][-(i-m)] = i 
                        m=m+2                       #[((i-5)-1)]
                    print("seats after restored")
                    print(screen1)
                    print("cancellation successfully")
                    
                elif selected_class == 3:
                    print("seats before restored",screen1)
                    for i in selected_seat:
                        rem =i%10                   # [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
                        screen1[2][rem-1] = i                  #rem =i%10 screen1[2][rem] 
                    print("seats after restored")
                    print(screen1)
                    print("cancellation successfully")
                
            elif selected_screen == "screen2":
                if selected_class==1:
                    print("seats before restored",screen2)
                    for i in selected_seat:
                        screen2[0][(i-6)] = i 
                    print("seats after restored")
                    print(screen2)
                    print("cancellation successfully")
                    
                elif selected_class ==2:
                    print("seats before restored",screen2)
                    m=1
                    for i in selected_seat:
                        screen2[1][-(i-m)] = i 
                        m=m+2  
                    print("seats after restored")
                    print(screen2)
                    print("cancellation successfully")
                    
                elif selected_class == 3:
                    print("seats before restored",screen2)
                    for i in selected_seat:
                        rem =i%10
                        screen2[2][rem-1] = i 
                    print("seats after restored")
                    print(screen2)
                    print("cancellation successfully")
 
            elif selected_screen =="screen3":
                if selected_class==1:
                    print("seats before restored",screen3)
                    for i in selected_seat:
                        screen3[0][(i-6)] = i 
                    print("seats after restored")
                    print(screen3)
                    print("cancellation successfully")
                    
                elif selected_class ==2:
                    print("seats before restored",screen3)
                    m=1
                    for i in selected_seat:
                        screen3[1][-(i-m)] = i 
                        m=m+2  
                    print("seats after restored")
                    print(screen3)
                    print("cancellation successfully")
                    
                elif selected_class == 3:
                    print("seats before restored",screen3)
                    for i in selected_seat:
                        rem =i%10
                        screen3[2][rem-1] = i 
                    print("seats after restored")
                    print(screen3)
                    print("cancellation successfully")

            elif selected_screen == "screen4":
                if selected_class==1:
                    print("seats before restored",screen4)
                    
                    for i in selected_seat:
                        screen4[0][(i-6)] = i 
                    print("seats after restored")
                    print(screen4)
                    print("cancellation successfully")
                    
                elif selected_class ==2:
                    print("seats before restored",screen4)
                    m=1
                    for i in selected_seat:
                        screen4[1][-(i-m)] = i 
                        m=m+2 
                    print("seats after restored")
                    print(screen4)
                    print("cancellation successfully")
                elif selected_class == 3:
                    print("seats before restored",screen4)
                    for i in selected_seat:
                        rem =i%10
                        screen4[2][rem-1] = i
                    print("seats after restored")
                    print(screen4)
                    print("cancellation successfully")
         
            y["bookings"] = "cancelled"
            print(userdatabase)
            break
#--------------------------------------------------------------------------
def booking(screen_show,screen_show_time,seat_class,no_user_tikets,sss,user_discount):
    a = seat_class
    b = sss   #sss is selected screens among 4 screens
    c = no_user_tikets
    dis = dis_user(user_discount)
    if not seat_class_available(a,b,c,dis,screen_show,screen_show_time) :
        print(a,"class is not available")
        print("-------------------------------------")
    else:
        print("booking successful")
        print(userdatabase)


def seat_class_available(n,available,v,disc,d,e):
    c=0
    b=v
    values = []
    amount = 0 
    disc_amount = 0
    total_amount=0
    key = []
    dicvalues = []
    userdata = {}
    if n ==1: #n is seat class 1
        for i in range(len(available[0])): # available is the screen array
            if available[0][i]!=0:
                c =c+1            #c is count of seats for class is available
                                    #v is no of tickets
        if v <= c: 
                global user_id
                user_id = user_id+1                                   
                for i in range(len(available[0])):
                    
                        if available[0][i]!=0 and v!=0:
                            values.append(available[0][i])
                            available[0][i]=0
                            v = v-1
                            amount = amount+first_class
                disc_amount = disc/100*amount
                total_amount = amount-disc_amount
                if available==screen1:
                    t="screen1"
                elif available ==screen2:
                    t = "screen2"
                elif available == screen3:
                    t= "screen3"
                elif available == screen4:
                    t = "screen4"
                dicvalues= [d,e,t,n,b,values,disc_amount,total_amount]
                key = ["movie","time","screen","class","tickets","selected seats","discount","amount"]
                for i in range(len(key)):
                   userdata[key[i]] = dicvalues[i]
                
                userdatabase[user_id]=userdata
                userdata={}
                return 1 
        else:
            return 0  
    elif n==2:
        for i in range(len(available[1])):
            if available[1][i]!=0:
                c = c+1
        if v<=c:
            user_id = user_id+1 
            for i in range(len(available[1])):
                if available[1][i]!=0 and v!=0:
                    values.append(available[1][i])
                    available[1][i] = 0
                    v = v-1
                    amount = amount+second_class
            disc_amount = disc/100*amount
            total_amount = amount-disc_amount
            #total_amount = amount-disc_amount
            if available==screen1:
                    t="screen1"
            elif available ==screen2:
                    t = "screen2"
            elif available == screen3:
                    t= "screen3"
            elif available == screen4:
                    t = "screen4"
            dicvalues= [d,e,t,n,b,values,disc_amount,total_amount]
            key = ["movie","time","screen","class","tickets","selected seats","discount","amount"]
            for i in range(len(key)):
                userdata[key[i]] = dicvalues[i]
                
            userdatabase[user_id]=userdata
            userdata={}
           
            return 1
        else:
            return 0
    elif n ==3:
            for i in range(len(available[2])):
                if available[2][i]!=0:
                    c = c+1
            if v<=c:
                user_id = user_id+1 
                for i in range(len(available[2])):
                    if available[2][i]!=0 and v!=0:
                        values.append(available[2][i])
                        available[2][i] = 0
                        v = v-1
                        amount = amount+third_class
                disc_amount = disc/100*amount
                total_amount = amount-disc_amount
                #total_amount = amount-disc_amount
                if available==screen1:
                    t="screen1"
                elif available ==screen2:
                    t = "screen2"
                elif available == screen3:
                    t= "screen3"
                elif available == screen4:
                    t = "screen4"
                dicvalues= [d,e,t,n,b,values,disc_amount,total_amount]
                key = ["movie","time","screen","class","tickets","selected seats","discount","amount"]
                for i in range(len(key)):
                   userdata[key[i]] = dicvalues[i]
                
                userdatabase[user_id]=userdata
                userdata={}
                return 1
            else:
                return 0

# booking part done -------------------------------------------------------------------------
            
#------------------------------------------------------------------------------------------
def profitofscreen():
    screen1_profit=0
    screen2_profit=0
    screen3_profit=0
    screen4_profit=0
    
    for x,y in  userdatabase.items():
        if "bookings" not in userdatabase.values():
            temp_screen =y["screen"]
            temp_amount=y["amount"]
            if temp_screen == "screen1":
                screen1_profit = screen1_profit +temp_amount
            elif temp_screen == "screen2":
                screen2_profit = screen2_profit+temp_amount
            elif temp_screen == "screen3":
                screen3_profit = screen3_profit+temp_amount
            elif temp_screen == "screen4":
                screen4_profit = screen4_profit+temp_amount
    return [screen1_profit,screen2_profit,screen3_profit,screen4_profit]



#----------------------------------------------------------------------------------------------
while(True):
    print("1.booking")
    
    print("2.cancellation")
    
    print("3.profit")
    
    input_1 = int(input("enter choice: "))
    
    if input_1 == 1:
        print("current movies: ")
        for i in total_shows:
            print(i)
        ch = int(input("enter ur choice: "))
        if ch==1:
            s1fs = screen1_first_show
            s1fst = screen1_first_show_time 
            sc= int(input("enter 1 for first class , 2 for second class , 3 for third class: "))
            
            if sc==1 or sc==2 or sc==3:
                tickets =  int(input("enter no of tickets: "))
                if tickets!=0:
                    price_discount = input("enter discount: ")
                    booking(s1fs,s1fst,sc,tickets,screen1,price_discount)
                else:
                    print("please enter number of tickets")
            else: 
                print("there is no such class")
        elif ch ==2:
            s1ss= screen1_second_show
            s1sst= screen1_second_show_time
            sc =  int(input("enter 1 for first class , 2 for second class , 3 for third class: "))
            if sc==1 or sc==2 or sc==3:
                tickets =  int(input("enter no of tickets: "))
                if tickets!=0:
                    price_discount = input("enter discount: ")
                    booking(s1ss,s1sst,sc,tickets,screen2,price_discount)
                else:
                    print("please enter number of tickets")
            else: 
                print("there is no such class")
        elif ch ==3:
            s2fs= screen2_first_show
            s2fst= screen2_first_show_time
            sc =  int(input("enter 1 for first class , 2 for second class , 3 for third class: "))
            if sc==1 or sc==2 or sc==3:
                tickets =  int(input("enter no of tickets: "))
                if tickets!=0:
                    price_discount = input("enter discount: ")
                    booking(s2fs,s2fst,sc,tickets,screen3,price_discount)
                else:
                    print("please enter number of tickets")
            else: 
                print("there is no such class")
        elif ch ==4:
            s2ss= screen2_second_show
            s2sst= screen2_second_show_time
            sc =  int(input("enter 1 for first class , 2 for second class , 3 for third class: "))
            if sc==1 or sc==2 or sc==3:
                tickets =  int(input("enter no of tickets: "))
                if tickets!=0:
                    price_discount = input("enter discount: ")
                    booking(s2ss,s2sst,sc,tickets,screen4,price_discount)
                else:
                    print("please enter number of tickets")
            else: 
                print("there is no such class")

#-------------------------------------------------------------------------------------------
    elif input_1 ==2:
        user__id = int(input("enter user id: "))
        cancellation(user__id)

    elif input_1 == 3:
        
        pro=profitofscreen()
        print("screen1 profit is: ",pro[0])
        print("screen2 profit is: ",pro[1])
        print("screen3 profit is: ",pro[2])
        print("screen4 profit is: ",pro[3])
    else:
        print("invalid choise")
        print("enter correct choise")
        print("----------------------\n")


        
    
