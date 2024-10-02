from mysql.connector import errorcode
import mysql.connector


class SQL():

    def  __init__(self, database):
        self.database = database

    def close(self):
        self.database.close()

    def create_user(self, username, role, email, password, created_date):
        cursor = self.database.cursor()
        try:
                

            sql_str = """
            insert into users (user_name, role_name, email, password, created_date)
            values ("{username}", "{role}", "{email}", "{password}", "{created_date}");
            """

            print(sql_str.format(username=username, role= role, email= email, password=password, created_date= created_date))
            cursor.execute(sql_str.format(username=username, role= role, email= email, password=password, created_date= created_date))

            self.database.commit()

        except mysql.connector.Error as err:
            # if err.errno == errorcode.ER_
            print(err)
            exit(1)
        finally:
            cursor.close()
            return sql_str.format(username=username, role= role, email= email, password=password, created_date= created_date)
            


    def create_role(self, name, description, enable_block, enable_reset_pwd, enable_sql):
        
        cursor = self.database.cursor()

        try:
            sql_str = """
            insert into user_roles (role_name, enable_block, enable_reset_pwd,enable_sql)
            values ("{name}", {enable_block}, {enable_reset_pwd}, {enable_sql});
            """

            print(sql_str.format(name=name,enable_block=enable_block, enable_reset_pwd=enable_reset_pwd, enable_sql=enable_sql))
            cursor.execute(sql_str.format(name=name,enable_block=enable_block, enable_reset_pwd=enable_reset_pwd, enable_sql=enable_sql))

            self.database.commit()

            print("item for "+ description + ": has been created")
        except mysql.connector.Error as err:
            print(err)
            exit(1)

        finally:
            cursor.close()
            
    def get_user(self, username, password):

        cursor = self.database.cursor()

        try:
            sql_str = """
                SELECT * from users WHERE user_name = "{username}" AND password = "{password}";
            """
            print(sql_str.format(username= username, password= password))
            
            cursor.execute(sql_str.format(username= username, password= password))
            user = cursor.fetchone()
            cursor.close()

            print(sql_str.format(username= username, password= password))

            return user

        except mysql.connector.Error as err:
            print(err)
            exit(1)

        finally:
            cursor.close()  

