import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dewlee#$20",
    database="crud_op"
)

mycursor=mydb.cursor()
print("Establish connection")

# streamlit run login.py

def main():
    st.title("CRUD OPERATIONS WITHIN MYSQL");
    
    #display options for CRUD operations
    option = st.sidebar.selectbox("Select an opertaiion",("Create","Read","Delete","Update"))
    
    #perform select operation
    if option == "Create":
        st.subheader("Create a Record")
        
        name =st.text_input("Enter your name")
        email =st.text_input("Enter your email")
        
        if st.button("Create"):
            sql = "insert into users (name,email) values(%s,%s)"
            val = (name,email)
            mycursor.execute(sql,val)  
            mydb.commit()      
            st.success("Successfully Record Updated")
    
    #perform read operation
       
    elif option == "Read":
        st.subheader("Read a Record")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    #perform update operation
       
    elif option == "Update":
        st.subheader("Update a Record")
        
        id=st.number_input("Enter ID you want to change",min_value=1)
        name =st.text_input("Enter your new name")
        email =st.text_input("Enter your new email")
        
        if st.button("Update"):
            sql = "update users set name=%s,email=%s where id=%s"
            val = (name,email,id)
            mycursor.execute(sql,val)  
            mydb.commit()      
            st.success("Successfully Record Updated")
            
        
    #perform delete operation  
      
    elif option == "Delete":
        st.subheader("Delete a Record")
        
        id=st.number_input("Enter ID you want to delete",min_value=1)
        
        if st.button("Delete"):
            sql="delete from users where id=%s"
            val = (id,)
            mycursor.execute(sql,val)  
            mydb.commit()      
            st.success("Successfully Record Deleted")
    
#call to the main function

if __name__ =="__main__":
    main()