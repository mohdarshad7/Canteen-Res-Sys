from conn_db import *


class Menu:
    def __init__(self, fname, price, type, addedBy, creationDate, e_id=None):
        self.id = e_id
        self.fname = fname
        self.price = price
        self.type = type
        self.addedBy = addedBy
        self.creationDate = creationDate

    def menu_add(self):
        conn = Database()
        sql = "INSERT INTO `menu`(`fname`, `price`, `type`, `addedBy`, `creationDate`) VALUES (%s,%s,%s,%s,%s)"
        values = (self.fname, self.price, self.type, self.addedBy, self.creationDate)
        try:
            exec = conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
            return "Failed to Create Menu, Please Verify whether Menu already Exists"
        finally:
            conn.close()
        return "New Menu Created"

    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM menu")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def menu_delete(table_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM menu WHERE id = %s", (table_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()
