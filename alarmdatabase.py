import sqlite3


class Datebase:
    def __init__(self):
        self.con=sqlite3.connect("Alarm_database.db")
        self.cursor=self.con.cursor()
    

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result=self.cursor.execute(query)
        alarms=result.fetchall()
        return alarms
    

    
    def add_new_alarm(self , new_title, new_time):

        try:
            query=f"INSERT INTO alarms(title , time) VALUES ('{new_title}' , '{new_time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False


    def edit_alarms(self,id,text):
        query=f"UPDATE alarms SET title='{text}' WHERE id='{id}'"
        self.cursor.execute(query)
        self.con.commit()
        # choose=0
        # id=input("enter the id product: ")
        # print("1- name")
        # print("2- price")
        # print("3- count")
        # choose=int(input("which one do you wanna edit? "))
        # if choose==1:
        #     global new_name
        #     new_name=input("Enter new name of this product: ")
        #     my_cursor.execute(f"UPDATE products SET name='{new_name}' WHERE id='{id}'")
        #     connection.commit()
        #     print("update succesfully")
            
        # elif choose==2:
        #     global new_price
        #     new_price=input("Enter new price of this product: ")
        #     my_cursor.execute(f"UPDATE products SET price='{new_price}' WHERE id='{id}'")
        #     connection.commit() 
        #     print("update succesfully")  
        
        # elif choose==3:
        #     global new_count
        #     new_count=input("Enter new count of this product: ")
        #     my_cursor.execute(f"UPDATE products SET count='{new_count}' WHERE id='{id}'")
        #     connection.commit() 
        #     print("update succesfully")
            
        # else:
        #     print("the code not found")

    def remove_alarms(self,id):
        query=f"DELETE FROM alarms WHERE id='{id}'"
        self.cursor.execute(query)
        self.con.commit()

    
       
