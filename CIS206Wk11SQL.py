import  sqlite3

def connectToDB(dbName):
    connection = sqlite3.connect(dbName)
    return connection

def getTables(connection):
    cursor = connection.cursor()
    cursor.execute("Select name from sqlite_master where type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def displayTableRecords(connection, tableName):
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({tableName});")
    columns = [col[1] for col in cursor.fetchall()]

    print(f"Displaying records from table: {tableName}")
    print(f"columns: {', '.join(columns)}\n")

    cursor.execute(f"Select * From {tableName}")
    rows = cursor.fetchall()

    for index, row in enumerate(rows, start=1):
        print(f"Row {index}: {', '.join(str(x) for x in row)}")

def insertRecord(connection, tableName):
    cursor = connection.cursor()

    cursor.execute(f"PRAGMA table_info({tableName});")
    columns = [col[1] for col in cursor.fetchall()]

    print(f"Insert a new record into table '{tableName}'")
    values = []
    for col in columns:
        value = input("Enter value for {col}: ")
        values.append(value)

    placeHolders = ", ".join(["?" for _ in columns])
    cursor.execute(f"INSERT INTO {tableName} ({', '.join(columns)}) VALUES ({placeHolders})", values)
    connection.commit()
    print(f"Record inserted into '{tableName}'.")

def updateRecord(connection, tableName):
    cursor = connection.cursor()
    
    cursor.execute(f"PRAGMA table_info({tableName});")
    columns = [col[1] for col in cursor.fetchall()]
    
    displayTableRecords(connection, tableName)
    
    rowNum = int(input(f"Enter the row number to update (1 - {len(columns)}): "))
    columnName = input(f"Enter the column name to update from {', '.join(columns)}: ")
    
    newValue = input(f"Enter the new value for {columnName}: ")
    
    cursor.execute(f"UPDATE {tableName} SET {columnName} = ? WHERE rowid = ?", (newValue, rowNum))
    connection.commit()
    print(f"Record updated in '{tableName}'.")

def deleteRecord(connection, tableName):
    cursor = connection.cursor()
    
    displayTableRecords(connection, tableName)
    
    rowNum = int(input(f"Enter the row number to delete (1 - {len(tableName)}): "))
    
    cursor.execute(f"DELETE FROM {tableName} WHERE rowid = ?", (rowNum,))
    connection.commit()
    print(f"Record deleted from '{tableName}'.")

def main():
   
    dbName = 'Northwind.sqlite'  
    connection = connectToDB(dbName)
    
    while True:
        tables = getTables(connection)
        print("Tables in the Northwind database:")
        for index, table in enumerate(tables, start=1):
            print(f"{index}. {table}")
        
        tableChoice = int(input("Select a table by number: ")) - 1
        if tableChoice < 0 or tableChoice >= len(tables):
            print("Invalid table number. Exiting.")
            break
        
        selectedTable = tables[tableChoice]
        displayTableRecords(connection, selectedTable)
        
        action = input("Choose an action - (I)nsert, (U)pdate, (D)elete, or (Q)uit: ").upper()
        
        if action == 'I':
            insertRecord(connection, selectedTable)
        elif action == 'U':
            updateRecord(connection, selectedTable)
        elif action == 'D':
            deleteRecord(connection, selectedTable)
        elif action == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main() 
