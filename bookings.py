from conn_db import *


class Bookings:
    def __init__(self, name, email, contactno, bookingDate, bookingTime, adults, children, type, bookingStatus, table, e_id=None):
        self.id = e_id
        self.name = name
        self.email = email
        self.contactno = contactno
        self.bookingdate = bookingDate
        self.bookingtime = bookingTime
        self.adults = adults
        self.children = children
        self.type = type
        self.bookingstatus = bookingStatus
        self.table = table
      

    def booking_add(self):
        conn = Database()
        sql = "INSERT INTO `bookings` (`name`, `email`, `contactno`,`bookingdate`, `bookingtime`, `adults`,`children`, `type`, `bookingstatus`, `tableNumber`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            self.name, self.email, self.contactno, self.bookingdate, self.bookingtime, int(self.adults),
            int(self.children), self.type,
            self.bookingstatus, self.table);
        try:
            exec = conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
            return "Failed to Create Booking"
        finally:
            conn.close()
        return "New Table Booking Created"

    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM bookings")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def booking_single(b_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM bookings WHERE id = %s", (b_id,))
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    def bookings_edit(id, status, tableNumber, remarks):
        conn = Database()
        try:
            conn.cursor.execute(
                "UPDATE bookings SET bookingstatus=%s, tableNumber=%s, remarks=%s WHERE id=%s",
                (status, tableNumber, remarks, id)
            )
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def booking_number(b_number):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM bookings WHERE contactno = %s", (b_number,))
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()
