from conn_db import *


class Table:
    def __init__(self, tableNumber, addedBy, creationDate, e_id=None):
        self.id = e_id
        self.tableNumber = tableNumber
        self.addedBy = addedBy
        self.creationDate = creationDate

    def table_add(self):
        conn = Database()
        sql = "INSERT INTO `tables` (`table_number`, `added_by`, `creation_date`) VALUES (%s,%s,%s)"
        values = (int(self.tableNumber), self.addedBy, self.creationDate)
        try:
            exec = conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
            return "Failed to Create Table, Please Verify whether Table already Exists"
        finally:
            conn.close()
        return "New Table Created"

    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM tables")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def table_delete(table_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM tables WHERE id = %s", (table_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()
