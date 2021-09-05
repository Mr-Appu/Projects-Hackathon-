import mysql.connector
import time
sqlpassword =input("Sql password : ")

#Structure of the program
def main():
    while True:
        intro_art()
        print("1. Log in ")
        print("2. Sign up ")
        print("3. Log in as a Guest ")
        print("4. Exit")
        choice=input("Enter :")
        print()
        
        if choice=='1':
             data=log_in()
             if data == 0:
                 clear()
                 continue 
             else:
                 clear()
                 pass
                
             if data[0][5]=="ADMIN": # check whether the user is customer or admin
                 while True:
                     intro_art()
                     print("1.Alter Instrument table " )
                     print("2.View Billing Log ")
                     print("3.Delete account ")
                     print("4.Log out ")
                     choice =input("Enter : ")
                     print()
                     if choice=='1':
                         print("1.Add instrument to the table ")
                         print("2.Update values  ")
                         print("3.Delete instrument from the table")
                         choice =input("Enter :")
                         print()
                         if choice=='1':
                             addrow()
                             time.sleep(2)
                             clear()
                         elif choice=='2':
                             updtrow()
                             time.sleep(2)
                             clear()
                         elif choice=='3':
                             delrow()
                             time.sleep(2)
                             clear()

                                 
                     elif choice=='2':
                         print("1.View all Purchases ")
                         print("2.View  Purchases  by specific User  ")
                         print("3.View  Purchases on specific Date   ")
                         choice =input("Enter :")
                         print()
                         if choice=='1':
                             log_all()
                             clear()
                         elif choice=='2':
                             log_user()
                             clear()
                         elif choice=='3':
                             log_date()
                             clear()
                             


                     elif choice=='3':
                         V=deluser(data[0][0])
                         if V =='deleted':
                             clear()
                             break
                         else:
                             clear()

 
                     elif choice=='4':
                         data=0
                         print()
                         clear()
                         break
                    
                     else:
                         print("Enter valid option")
                         print()
                         

                 
             elif data [0][5]=="USER": # check whether the user is customer or admin
                 while True:
                     intro_art()
                     print("1.View Instruments ")
                     print("2.Buy Instruments ")
                     print("3.Alter account ")
                     print("4.Delete account ")
                     print("5.Log out ")
                     choice =input("Enter : ")
                     if choice=='1':
                         menu()
                     elif choice=='2':
                         buyinstruments(data[0][0])
                         print()
                     elif choice=='3':
                         alter_acc(data[0][0])
                         time.sleep(2)
                         clear()
                         print()
                     elif choice=='4':
                         V=deluser(data[0][0])
                         if V== 'deleted':
                             print()
                             print("Deleted ")
                             time.sleep(2)
                             clear()
                             break
                         else :
                             print()
                             clear()
                            
                     elif choice=='5':
                         print()
                         clear()
                         break
                    
                     else:
                         print("Enter valid option ")
                         print()
                         time.sleep(2)
                         clear()
                     
        elif choice=='2':
            clear()
            intro_art()
            sign_up()
            clear()
            continue
             
        elif choice=='3':
            data=[]
            while True:
                clear()
                intro_art()
                print("1.View Instruments ") 
                print("2.Buy Instruments ")
                print("3.Exit")
                choice =input("Enter : ")
                if choice=='1':
                    menu()
                    
                elif choice=='2':
                    print("  Please log in or sign up to buy ")
                    print("  Guest can only view the products :)")
                    print()
                    time.sleep(4)
                    clear()
                    break
                
                elif choice=='3':
                    print()
                    clear()
                    break
                
                else:
                    print("Enter valid option")
                    print()
                    time.sleep(2)
                    clear()


            

        elif choice=='4':
            print("Bye")
            time.sleep(2)
            break
         
        else:
             print("Enter valid option ")
             print()
             continue
            
#log in function
def log_in():
    import mysql.connector
    import stdiomask
    n=0
    while True:
        try:
            Id=int(input("Enter User Id:"))
        except:
            print("Enter valid user id ")
            print()
            continue
        Name=input("Enter Name:")
        Password=stdiomask.getpass(prompt="Enter Password: ",mask="*")
        print()
        
        mydb=mysql.connector.connect(user="root",host="localhost",passwd=sqlpassword,database="musicstore")
        cursor=mydb.cursor()
        cursor.execute("SELECT * FROM USER \
                                      WHERE ID = %d AND USERNAME = '%s' AND PASSWORD='%s' "
                                      %(Id,Name,Password))
        data=cursor.fetchall()
        cursor.close()
        if data != [] and len(data)==1 : # data verification
            print("User",Name,"sucessfully loged in :) ")
            print()
            return data
            break
        else:
            n+=1
            print()
            print("Try Again.............. :(")
            print()
            if n==3:
                print()
                print("Failed to log in 3 times , BYE :(")
                time.sleep(2)
                return 0
                break

#Sign up function
            
def sign_up():
    import mysql.connector
    
    Admin_password="12345" #password for admin's to create an account 
    print("1.Admin")
    print("2.User")
    print("3.Exit ")
    while True:
        choice=input("Enter:")
        print()
        if choice=='1':
            A=input("Enter Admin password to create Account: ")
            if A==Admin_password:
                pass
            else:
                print("incorrect Admin password ")
                print()
                continue
            Name=input("Enter Name: ")
            print("Enter Contact No : ",end ='')
            Contact_no=contactn0()
            print("Enter Password : ",end ="")
            Password=passwd()         
            mydb=mysql.connector.connect(user="root",host="localhost",passwd=sqlpassword,database="musicstore")
            cursor=mydb.cursor()
            while True:
                try:
                   cursor.execute(" insert into USER(USERNAME,CONTACTNO,PASSWORD,ROLE)\
                                            values ('%s','%s','%s','ADMIN')"%(Name,Contact_no,Password))
                   mydb.commit()
                   print("Sucssfully registered :)")
                   print()
                   break
                except:
                   print( "User name",Name ," is already taken " )
                   Name=input("Enter Name again : ")
                   print()
                   continue
            cursor.execute("Select ID from USER\
                                           where USERNAME='%s' and CONTACTNO= '%s' and PASSWORD='%s' "%(Name,Contact_no,Password))
            Id=cursor.fetchall()
            mydb.close()
            print("This is your User ID : ",Id[0][0])
            print("Log in to activate your account")
            nxt=input()
            print()
            break
        
        elif choice=='2':
            import mysql.connector
            Name=input("Enter Name: ")
            print("Enter Contact No : ",end ='')
            Contact_no=contactn0()
            Shipping_add=input("Enter Shipping address: ")
            Billing_add=input("Enter Billing address: ")
            Profession=input("Enter Profession: ")
            print("Enter Password : " ,end = '')
            Password=passwd()
            mydb=mysql.connector.connect(user="root",host="localhost",passwd=sqlpassword,database="musicstore")
            cursor=mydb.cursor()
            while True:
                try:
                    cursor.execute(" insert into USER(USERNAME,CONTACTNO,BILLINGADDRESS,SHIPPINGADDRESS,PROFESSION,PASSWORD)\
                                            values('%s','%s','%s','%s','%s','%s') "
                                           %(Name,Contact_no,Billing_add,Shipping_add,Profession,Password))
                    mydb.commit()
                    print("Sucssfully registered :)")
                    print()
                    break
                except:
                    print( "User name",Name ," is already taken " )
                    Name=input("Enter Name again : ")
                    print()
                    continue
            cursor.execute("Select ID from USER\
                                           where USERNAME='%s' and CONTACTNO= '%s' and PASSWORD='%s' "%(Name,Contact_no,Password))
            Id=cursor.fetchall()
            mydb.close()
            print("Your User ID is : ",Id[0][0])
            print("Log in to activate your account")
            nxt=input()
            print()
            break

        elif choice=='3':
            print()
            clear()
            break
               
        else:
            print("Invalid Input ")
            print()
           
#password validation function            
def passwd():
    import stdiomask
    while True:
        password=stdiomask.getpass(prompt="",mask="*")
        if len(password)<5:
            print("Password should contain atleast 5 character ")
        else:
            digit=0
            special=0
            alpha=0
            uppercase=0
            for i in password:
                if i.isdigit():
                    digit+=1
                elif i.isupper():
                    uppercase+=1
                elif i.isalpha():
                    alpha+=1
                else:
                    special+=1
            if alpha==0:
                print("Password should contain atleast alphabetic value  ")       
            elif uppercase==0:
                print("Password should contain atleast one capital letter ")
            elif digit==0:
                print("Password should contain atleast one digit ")    
            elif special==0:
                print("Password should contain atleast one special character ")
            else:
                print("Password approved ")
                break
    return password

#contact no validation function
def contactn0():
    while True:
        try:
            contact=int(input())
        except:
            print("Enter 10 digit valid Contact No: ")
            continue
        l=str(contact)
        if len(l)==10:
            return l
            break
        else:
            print("Enter 10 digit valid Contact No: ")

#instrument menu function
def menu():
    while True:
        print()
        print("Enter 1 to find various wind instruments")
        print("Enter 2 to find various brass instruments")
        print("Enter 3 to find various percussion instruments")
        print("Enter 4 to find various string instruments")
        print("Enter 5 to find various electronic instruments")
        print("Enter 6 to find various electronic devices")
        print("Enter 7 to find various music accessories \n")
        user_option=input("enter the category : ")
        print()
        if user_option=='1':
            wind_instrument()
            
        elif user_option=='2':
            brass_instrument()
            
        elif user_option=='3':
            percussion_instrument()

        elif user_option=='4':
            string_instrument()

        elif user_option=='5':
            electronic_instrument()

        elif user_option=='6':
            electronic_devices()
              
        elif user_option=='7':
            music_accessories()

        else:
            print("you have entered wrong input! \n")
            continue

        con=input("Wanna view more catogories (yes/no)?")
        if con=='N' or con=='n' or con=='no' or con=='NO' or con=='No':
            clear()
            break
        elif con=='Y' or con=='y' or con=='yes' or con=='YES' or con=='Yes':
            continue 
        else:
            print("Enter yes or no ")    
            
            
def wind_instrument():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='wind instrument'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()
         
def brass_instrument():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='brass instrument'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t\t', i[3])
    mydb.close()

         
def percussion_instrument():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='percussion instrument'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()
        
def string_instrument():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='string instrument'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()
    
def electronic_instrument():
    import mysql.conector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='electronic instrument'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()

         
def electronic_devices():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='electronic devices'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()
    
def music_accessories():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select instrument_name,price,quantity,description from instrument where category='music accessories'")
    print("Instrument Name\t","Price\t","Quantity Available\t","Description")
    for i in mycursor:
        print(i[0],'\t', i[1],'\t', i[2],'\t\t', i[3])
    mydb.close()


# Instrument table functions
# add instruments
def addrow():           
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword, database="musicstore")
    cursor=mydb.cursor()

    while True:
        #user defenition to add row details
        ins_nm=input("Enter instrument name : ")
        ins_code=int(input("Enter an unique 3 or 4 digit code for instrument : "))
        print("Select Instrument Category from the list given below ")
        print("1.Wind Instrument ")
        print("2.Brass Instrument ")
        print("3.Percussion Instrument ")
        print("4.String Instrument ")
        print("5.Electronic Instrument ")
        print("6.Music Accessories ")
        while True :
            choice = input("Enter No of the Instrument Category : ")
            print()
            if choice == '1':
                catg='wind instrument'
                break
            
            elif choice == '2':
                catg='brass instrument'
                break
            
            elif choice == '3':
                catg='percussion instrument'
                break

            elif choice == '4':
                catg='string instrument'
                break

            elif choice == '5':
                catg='electronic instrument'
                break

            elif choice == '6':
                catg='music accessories'
                break

            else:
                print("Invalid Input ,Enter valid option no ")
                print()
                
                
        prc=int(input("Enter price of instrument : "))
        qnt=int(input("Enter quantity of instrument : "))
        sal=input("Enter is discount available(yes/no) : ")
        descr=input("Enter product description : " )

        #Adding gathered details to table
        cursor.execute("insert into INSTRUMENT values(%d,'%s','%s',%d,%d,'%s','%s')"%(ins_code,ins_nm,catg,prc,qnt,sal,descr))
        mydb.commit()
        print("info added ;)")
        mydb.close()

        #continue row addition (user defined)
        con=input("Wanna add anymore instruments(yes/no)?")

        if con=='N' or con=='n' or con=='no' or con=='NO' or con=='No':
            break
        elif con=='Y' or con=='y' or con=='yes' or con=='YES' or con=='Yes':
            continue 
        else:
            print("Enter yes or no ")    


def delrow():
    #importing module
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword, database="musicstore")
    cursor=mydb.cursor()

    while True:
        #user defenition to delete rows
        id_usin=int(input("Enter instrument code to delete : "))

        #deleting
        cursor.execute("delete from instrument where code=%d"%(id_usin,))
        mydb.commit()
        mydb.close()
        print("Successfully deleted ")

        #continue row deletion (user defined)
        con=input("Wanna delete anymore instruments(yes/no)?")

        if con=='N' or con=='n' or con=='no' or con=='NO' or con=='No':
            break
        elif con=='Y' or con=='y' or con=='yes' or con=='YES' or con=='Yes':
            continue 
        else:
            print("Enter yes or no ")
            
def updtrow():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword, database="musicstore")
    cursor=mydb.cursor()

    while True:
        #user defenition to update
        id_usin=int(input("Enter Code of the Instrument which you want to update : "))

        #Checking if entered ID exists in instrument table
        cursor.execute("select CODE from instrument")
        id_dt=cursor.fetchall()
        
        if (id_usin,) in id_dt:
            pass
        else:
            print("You entered an Code not in the list :( .Enter a valid Code ")
            break

        print("Select your choice that you want to update ")
        print("1.Instrument name ")
        print("2.Category")
        print("3.Price ")
        print("4.Quantity ")
        print("5.Sale ")
        print("6.Description ")
        ch=input("Select choice : ")

        #updating instrument name
        if ch=='1':
            try:
                ins_nm=input("Enter new Instrument Name to be Updated : ")
                cursor.execute("update instrument set INSTRUMENT_NAME='%s' where code=%d"%(ins_nm,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
            except:
                print("Try again :(")
                continue

        #updating category
        elif ch==2:
            
            try:
                print("Select Instrument Category from the list given below ")
                print("1.Wind Instrument ")
                print("2.Brass Instrument ")
                print("3.Percussion Instrument ")
                print("4.String Instrument ")
                print("5.Electronic Instrument ")
                print("6.Music Accessories ")
                
                while True :
                    choice = input("Enter No of the Instrument Category : ")
                    print()
                    if choice == '1':
                        catg='wind instrument'
                        break
            
                    elif choice == '2':
                        catg='brass instrument'
                        break
            
                    elif choice == '3':
                        catg='percussion instrument'
                        break

                    elif choice == '4':
                        catg='string instrument'
                        break

                    elif choice == '5':
                        catg='electronic instrument'
                        break

                    elif choice == '6':
                        catg='music accessories'
                        break

                    else:
                        print("Invalid Input ,Enter valid option no ")
                        print()
        
                cursor.execute("Update instrument set CATEGORY='%s' where code=%d"%(catg,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
                            
            except:
                print("Try again :(")
                continue    

        #updating price
        elif ch=='3':
            try:
                prc=input("Enter new price : ")
                cursor.execute("update instrument set PRICE='%s' where code=%d"%(prc,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
            except:
                print("Try again :(")
                continue
            
        #updating quantity
        elif ch=='4':
            try:
                qnt=input("Enter new quantity : ")
                cursor.execute("update instrument set QUANTITY='%s' where code=%d"%(qnt,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
            except:
                print("Try again :( ")
                continue
                
        #updating sale
        elif ch=='5':
            try:
                sle=input("Sale? yes/no : ")
                cursor.execute("update instrument set SALE='%s' where code=%d"%(sle,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
            except:
                print("Try again :( ")
                continue
            
        #updating description
        elif ch=='6':
            try:
                des=input("Enter description")
                cursor.execute("update instrument set DESCRIPTION='%s' where code=%d"%(des,id_usin))
                mydb.commit()
                mydb.close()
                print("Successfully updated ")
            except:
                print("Try again :( ")
                continue
         
        else:
            print("Invalid choice entered. Please select a valid choice ")
            print()
            

        #continue updation (user defined)
        con=input("\nUpdate anymore rows(yes/no)? ")
        print()
        
        if con=='N' or con=='n' or con=='no' or con=='NO' or con=='No':
            break
        elif con=='Y' or con=='y' or con=='yes' or con=='YES' or con=='Yes':
            continue 
        else:
            print("Enter yes or no ")
            print()

#deleting user function
def deluser(Id):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword, database="musicstore")
    cursor=mydb.cursor()

    while True:

        confirm=input("Do you want to delete to account permanently (yes/no) : ")
        print()

        if confirm=='N' or confirm=='n' or confirm=='no' or confirm=='NO' or confirm=='No':
            break
        elif confirm=='Y' or confirm=='y' or confirm=='yes' or confirm=='YES' or confirm=='Yes':
            cursor.execute("UPDATE user SET PASSWORD = 'deleted' where ID=%d"%(Id,))
            mydb.commit()
            mydb.close()
            print("Bye  ")
            time.sleep(2)
            print()
            return "deleted"
            break

        else:
            print("Enter yes or no ")
            
            

# buying instruments and billing
def buyinstruments(ID):
    import mysql.connector
    import datetime
    while True:
        print()
        code=input("Enter Code or Name of the instrument you want to buy : ")
        print()
    
        #instrument code
        if code.isdigit():
            code=int(code)
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
            mycursor=mydb.cursor()
            try:
                mycursor.execute("select code,instrument_name,quantity,price,sale from instrument where code = %d " % (code))
                idata=mycursor.fetchall()
                mycursor.close()
                print("  Instrument Code : ", idata[0][0])
                print("  Instrument Name : ", idata[0][1])
                print("  Quantity : ", idata[0][2])
                print("  Price  : ", idata[0][3])
                print()
                break
            except:
                print("Enter correct Instrument Code")
                continue
            
        
        # instrument name   
        else :
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
            mycursor=mydb.cursor()
            try:
                mycursor.execute("select code,instrument_name,quantity,price,sale from instrument where instrument_name= '%s' ;" % (code))
                idata=mycursor.fetchall()
                mycursor.close()
                print("  Instrument Code : ", idata[0][0])
                print("  Instrument Name : ", idata[0][1])
                print("  Available Quantity : ", idata[0][2])
                print("  Price  : ", idata[0][3])
                print()
                break
            except:
                print("Enter correct Instrument Name ")
                continue

    print()   
    quantity=int(input("Enter number of items you want :"))
    if quantity > idata[0][2]:
        print()
        print("required stock unavailable please try again later :( ")
        print()
        time.sleep(2)
        clear()
    else :
        t_price=(quantity*idata[0][3])
        if idata[0][4].lower()=="yes":
            print("The instrument",idata[0][1],"is on special offer of 20 % discount ")
            t_price=int(0.8*t_price)
        else:
            pass
        print("Total bill amount is :",t_price)
        while True:
            print()
            print("1.Sumbit Order ")
            print("2.Exit ")
            print()
            choice = int(input("Enter :"))
            if choice==1:
                #update instrument table
                mycursor=mydb.cursor()
                mycursor.execute(" update instrument set  quantity = %d where code= %s ;" % (idata[0][2]-quantity,idata[0][0]))
                mydb.commit()
                #generating  bill no 
                mycursor.execute("select * from log ;")
                bill_no=len(mycursor.fetchall())+1
                date=datetime.datetime.today().strftime("%Y-%m-%d")
                #adding values to log table
                mycursor.execute(" insert into LOG(BILL_NO,CODE,ID,T_PRICE,QUANTITY,DATE) \
                                                      values (%d,%d,%d,%d,%d,'%s');"%(bill_no,idata[0][0],ID,t_price,quantity,date))
                mydb.commit()
                print("Order placed successfully  ͡❛ ͜ʖ ͡❛ ")
                print()
                mycursor.execute(" select BILL_NO,LOG.ID,USERNAME,CONTACTNO,BILLINGADDRESS,SHIPPINGADDRESS,INSTRUMENT_NAME,T_PRICE,LOG.QUANTITY,DATE \
                                                      from USER,INSTRUMENT,LOG \
                                                      where LOG.ID=USER.ID and LOG.CODE=INSTRUMENT.CODE and BILL_NO=%d ;"%(bill_no))
                bill=mycursor.fetchall()
                print("**********************************************")
                print()
                print("Date:",date,"         Bill No:",bill[0][0])
                print("User Id :",bill[0][1])
                print("Customer Name :",bill[0][2])
                print("Product :",bill[0][6],"    Quantity :",bill[0][8])
                print("Total Price :",bill[0][7])
                print()
                print("Shipping Address :",bill[0][4])
                print("Billing Address :",bill[0][5])
                print("**********************************************")
                print()

                f=open(str(bill_no)+"BILL.txt","w")
                f.writelines("Date : "+ date+'\n')
                f.writelines("Bill No : " + str(bill[0][0])+'\n')
                f.writelines("User Id :" +str(bill[0][1])+'\n')
                f.writelines("Customer Name :" +bill[0][2]+'\n')
                f.writelines("Product : "+bill[0][6]+'\n')
                f.writelines("Quantity : "+str(bill[0][8])+'\n')
                f.writelines("Total Price : "+str(bill[0][7])+'\n')
                f.writelines("Shipping Address : "+bill[0][4]+'\n')
                f.writelines("Billing Address : "+bill[0][5]+'\n')
                f.close()

                print("Bill has been downloaded")
                mycursor.close()
                mydb.close()
                time.sleep(3)
                clear()
                break

                                               
            elif choice==2:
                mydb.close()
                print()
                clear()
                break
            else:
                print("Enter Valid option ")
                

#log table functions

def log_user():
    import mysql.connector
    import datetime
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    user=input("Enter User Id or Name of the Customer : ")

    if user.isdigit():
        user=int(user)
        mycursor.execute("select BILL_NO,LOG.ID,USERNAME,CONTACTNO,BILLINGADDRESS,SHIPPINGADDRESS,INSTRUMENT_NAME,T_PRICE,LOG.QUANTITY,DATE,PROFESSION \
                                                      from USER,INSTRUMENT,LOG \
                                                      where LOG.ID=USER.ID and LOG.CODE=INSTRUMENT.CODE and USER.ID=%d ;"%(user)) 
        data=mycursor.fetchall()
        mycursor.close()
        if data ==[]: #validation 
            print("User doesn't exist (or) No purchased history ")
        else:
            print()
            print("User Id: ",data[0][1])
            print("User Name: ",data[0][2])
            print("Contact No: ",data[0][3])
            print("Billing Address: ",data[0][4])
            print("Shipping Address: ",data[0][5])
            print("Profession: ",data[0][10])
            print()
            print("Date\t\t","Instrument\t","Quantity\t","Bill Amount ")
            for i in data:
                print(i[9],'\t',i[6],'\t\t',i[8],'\t\t',i[7])
            nxt=input()    
            
    else :
        mycursor.execute("select BILL_NO,LOG.ID,USERNAME,CONTACTNO,BILLINGADDRESS,SHIPPINGADDRESS,INSTRUMENT_NAME,T_PRICE,LOG.QUANTITY,DATE,PROFESSION \
                                                      from USER,INSTRUMENT,LOG \
                                                      where LOG.ID=USER.ID and LOG.CODE=INSTRUMENT.CODE and USERNAME='%s' ;"%(user)) 
        data=mycursor.fetchall()
        mycursor.close()
        if data ==[]: #validation 
            print("User doesn't exist (or) No purchased history ")
        else:
            print()
            print("User Id: ",data[0][1])
            print("User Name: ",data[0][2])
            print("Contact No: ",data[0][3])
            print("Billing Address: ",data[0][4])
            print("Shipping Address: ",data[0][5])
            print("Profession: ",data[0][10])
            print()
            print("Date\t\t","Instrument\t","Quantity\t","Bill Amount ")
            for i in data:
                print(i[9],'\t',i[6],'\t\t',i[8],'\t\t',i[7])
            nxt=input()    


def log_all():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    mycursor.execute("select BILL_NO,LOG.ID,USERNAME,INSTRUMENT_NAME,T_PRICE,LOG.QUANTITY,DATE\
                                                      from USER,INSTRUMENT,LOG \
                                                      where LOG.ID=USER.ID and LOG.CODE=INSTRUMENT.CODE  ;") 
    data=mycursor.fetchall()
    mycursor.close()
    if data==[]:
        print("No Values Found ")
        print()
        return
    print("Date\t\t","Bill No\t","User ID\t","User Name\t","Instrument\t","Quantity\t","Bill Amount ")
    for i in data:
        print(i[6],'\t',i[0],'\t',i[1],'\t',i[2],'\t\t',i[3],'\t\t',i[5],'\t',i[4])
    print()
    nxt=input()


def log_date():
    import mysql.connector
    import datetime
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    date=input("Enter Date 'yyyy-mm-dd'  : ")
    mycursor.execute("select BILL_NO,LOG.ID,USERNAME,INSTRUMENT_NAME,T_PRICE,LOG.QUANTITY,DATE\
                                                      from USER,INSTRUMENT,LOG \
                                                      where LOG.ID=USER.ID and LOG.CODE=INSTRUMENT.CODE  and DATE='%s' ;"%(date,)) 
    data=mycursor.fetchall()
    mycursor.close()
    if data==[]:
        print("No Values Found   ")
        print()
        return
    print("Date\t\t","Bill No\t","User ID\t","User Name\t","Instrument\t","Quantity\t","Bill Amount ")
    for i in data:
        print(i[6],'\t',i[0],'\t',i[1],'\t',i[2],'\t\t',i[3],'\t\t',i[5],'\t',i[4])
    print()    
    nxt=input()

def alter_acc(Id):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    mycursor=mydb.cursor()
    print()
    print("Select your choice that you want to update ")
    print("1.User Name ")
    print("2.Password ")
    print("3.Contact no ")
    print("4.Billing Address ")
    print("5.Shipping Address ")
    print("6.Exit ")

    while True:             
        choice=input("Enter Choice : ")
        print()
        if choice == '1':
            Name = input("Enter New User Name : ")
            while True:
                try:
                    mycursor.execute("update USER set USERNAME='%s' where ID=%d ;"%(Name,Id))
                    mydb.commit()
                    print("Sucssfully Updated :)")
                    break
                except:
                    print( "User name",Name ," is already taken " )
                    Name=input("Enter Name again : ")
                    continue
            break
        
        elif choice == '2':
            print("Enter New password : ",end ="")
            Password=passwd()
            mycursor.execute("update USER set PASSWORD='%s' where ID=%d ;"%(Password,Id))
            mydb.commit()
            print("Sucssfully Updated :)")
            break
        
        elif choice == '3':
            print("Enter New Contact No : ")
            Contact_no=contactno()
            mycursor.execute("update USER set CONTACTNO='%s' where ID=%d ;"%(Contact_no,Id))
            mydb.commit()
            print("Sucssfully Updated :)")
            break
        

        elif choice == '4':
            Billing_Address=input("Enter New Billing Address : ")
            mycursor.execute("update USER set BILLINGADDRESS ='%s' where ID=%d ;"%(Billing_Address,Id))
            mydb.commit()
            print("Sucssfully Updated :)")
            break
         
        elif choice == '5':
            Shipping_Address=input("Enter New Shipping Address : ")
            mycursor.execute("update USER set SHIPPINGADDRESS ='%s' where ID=%d ;"%(Shipping_Address,Id))
            mydb.commit()
            print("Sucssfully Updated :)")
            break

        elif choice == '6':
            break

        else:
            print("Enter Valid Option No ")
            continue

# Table Creation Functions

def database_creation(name):
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",passwd=sqlpassword)
    cursor=mydb.cursor()
    cursor.execute("create database if not exists  %s ;" % (name))
    mydb.commit()
    mydb.close()
   
def user_table():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",passwd=sqlpassword,database="musicstore")
    cursor=mydb.cursor()
    cursor.execute("create table if not exists USER \
                                   (ID int not null unique AUTO_INCREMENT,\
                                    USERNAME varchar(100)not null unique,\
                                    CONTACTNO char(15) not null ,\
                                    BILLINGADDRESS varchar(255) ,\
                                    SHIPPINGADDRESS varchar(255),\
                                    ROLE varchar(10) not null default'USER',\
                                    PROFESSION varchar(50) ,\
                                    PASSWORD varchar(50) not null,\
                                    primary key(ID));") 
    mydb.commit()
    mydb.close()
    
def instrument_table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    cursor=mydb.cursor()
    cursor.execute("create table if not exists INSTRUMENT\
                                        (CODE int(5)primary key not null unique,\
                                        INSTRUMENT_NAME varchar(30)not null unique,\
                                        CATEGORY varchar(45) not null,\
                                        PRICE int(6)not null,\
                                        QUANTITY int(3)not null,\
                                        SALE varchar(3)default 'no',\
                                        DESCRIPTION varchar(500))")
    mydb.commit()
    cursor.execute("select * from INSTRUMENT")
    data=cursor.fetchall()
    if data==[]:
        cursor.execute("""insert into INSTRUMENT(CODE,INSTRUMENT_NAME,CATEGORY,PRICE,QUANTITY,SALE,DESCRIPTION)
                     values(11,'flute','wind instrument',250,10,'yes','blue colour, wooden flute 12 inches'),
                     (30,'clarinet','wind instrument',2750,8,'no','latest model single reed brown clarinet'),
                     (21,'saxophone','wind instrument',7950,7,'no','model 5.5 gold colour'),
                     (09,'bagpipe','wind instrument',8500,6,'no','red and black colour B4 model'),
                     (13,'trumpet','brass instrument',3150,8,'no','model 3.7 gold colour'),
                     (23,'french horn','brass instrument',4500,8,'no','blue and yellow colour'),
                     (47,'trombone','brass instrument',3750,10,'no','model 6.2 bronze colour'),
                     (07,'xylophone','percussion instrument',6950,8,'no','maple 3.5 model with a case'),
                     (10,'tubular bells','percussion instrument',450,10,'no','pack of two bells'),
                     (14,'triangle','percussion instrument',1050,12,'no','pack of triangle and stick'),
                     (19,'tambourine','percussion instrument',350,8,'no','different colours available'),
                     (22,'rattle','percussion instrument',400,8,'no','pack of three music rattles'),
                     (28,'acoustic guitar','string instrument',8050,15,'no','latest wooden guitar with picks'),
                     (38,'electric guiatr','string instrument',9150,15,'no','bright blue colour with adjustable strap'),
                     (26,'violin','string instrument',5250,10,'no','windsor model set'),
                     (16,'cello','string instrument',1500,12,'no','latest wooden 7.0 model'),
                     (41,'banjo','string instrument',7950,10,'no','colourful with adjustable strap'),
                     (33,'double bass','string instrument',10150,15,'no','bass guitar with case and cords'),
                     (37,'piano','electronic instrument',10100,10,'no','latest model comes with a case'),
                     (29,'keyboard','electronic instrument',4500,12,'no','portable and with a case'),
                     (36,'synthesizers','electronic instrument',9450,8,'no','colour coordinated model comes with a stand'),
                     (44,'rhythm machine','electronic instrument',8950,10,'no','latest easy to use model'),
                     (35,'orchestral stand','music accessories',1150,10,'no','suitable for all purposes'),
                     (31,'microphone stand','music accessories',1050,10,'no','adjustable height suitable for all models'),
                     (08,'guitar picks','music accessories',150,15,'no','pack of five different guitar picks'),
                     (05,'song book','music accessories',300,25,'no','easy to understand beginner friendly'),
                     (04,'mircrophone','electronic devices',950,15,'no','different colours available with two meter wire'),
                     (24,'bluetooth speakers','electronic devices',2700,25,'no','great sound range'),
                     (12,'headphones','electronic devices',800,20,'no','good quality wireless noise cancelling'),
                     (03,'earphones','electronic devices',400,20,'no','good quality with one meter wire'),
                     (45,'music player','electronic devices',2500,20,'no','black colour model cd player with radio option')""")
        mydb.commit()
    else:
        pass
    mydb.close()

def log_table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword,database="musicstore")
    cursor=mydb.cursor()
    cursor.execute("create table if not exists LOG\
                                        (BILL_NO int(5)primary key not null unique,\
                                        CODE int(5) not null ,\
                                        ID int(5) not null,\
                                        T_PRICE int(6) not null,\
                                        QUANTITY int(3)not null,\
                                        DATE date not null,\
                                        FOREIGN KEY (ID) REFERENCES USER(ID),\
                                        FOREIGN KEY (CODE) REFERENCES INSTRUMENT(CODE) );")
    mydb.commit()
    mydb.close()

def intro_art():
    print(
"""

███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░  ░██████╗██╗░░██╗░█████╗░██████╗░
████╗░████║██║░░░██║██╔════╝██║██╔══██╗  ██╔════╝██║░░██║██╔══██╗██╔══██╗
██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝  ╚█████╗░███████║██║░░██║██████╔╝
██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗  ░╚═══██╗██╔══██║██║░░██║██╔═══╝░
██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝  ██████╔╝██║░░██║╚█████╔╝██║░░░░░
╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░
""")

def clear():
    import os
    os.system('cls')
    #project
try:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=sqlpassword)
    database_creation('musicstore')
    user_table()
    instrument_table()
    log_table()
    main()
except:
    print("Can't Connect to the Server ")
    time.sleep(2)





















    
