import mysql.connector

def email_extracting_slicing():
    try:
        #connection for mysql server
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "****"
        )
        # print(mydb)
        sqlcmd = mydb.cursor()
        # print(mysql) # nothing to execute yet
        sqlcmd.execute("use emailaddr")
        sqlcmd.execute("select * from EmailAddress")

        separator = '@'
        usernames = []
        domains = []

        for person in sqlcmd:
            # print(person[2]) # extracting emails only
            email = person[2]
            position_of_separator = email.find(separator)
            # print(position_of_separator)
            user_data = email[:position_of_separator]
            # print(user_data)
            usernames.append(user_data)
            # print(usernames)
            domain_data = email[position_of_separator+1:]
            domains.append(domain_data)

        # print(sqlcmd) #CMySQLCursor: select * from EmailAddress

        # printing the data
        i = 0 
        print()
        print("----------------List of Usernames---------------")
        for user_name in usernames:
            i += 1
            print(str(i)+'. '+user_name)
            
        i = 0
        print()
        print("-----------------List of Domains----------------")    
        for domain_info in domains:
            i += 1
            print(str(i)+'. '+domain_info)    
    except Exception:
        print("internal error!!")

if __name__ == "__main__":
    email_extracting_slicing()