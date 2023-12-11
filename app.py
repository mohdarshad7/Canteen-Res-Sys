from aifc import Error

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from table import Table
from menu import Menu
from bookings import Bookings
from datetime import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/')
def logout():  # put application's code here
    return render_template("index.html")

@app.route('/home')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route("/viewtodaymenu")
def viewtodaymenu():
    tablesList = Menu.view_all()
    return render_template('studentviewmenu.html', rows=tablesList)

@app.route("/addMenuPage")
def addMenuPage():
    return render_template("addmenu.html")


@app.route("/addMenu", methods=['POST', 'GET'])
def addMenu():
    if request.method == 'POST':
        try:
            fname = request.form['fname']
            price = request.form['price']
            type = request.form['type']
            menu = Menu(fname, price, type, "Admin", datetime.now())
            msg = menu.menu_add()
        except:
            msg = "Error in the INSERT"
    return render_template('addmenu.html', msg=msg)



@app.route("/menu")
def menu():
    tablesList = Menu.view_all()
    return render_template('viewmenu.html', rows=tablesList)


@app.route("/deletemenu", methods=['POST', 'GET'])
def deletemenu():
    if request.method == 'POST':
        rowid = request.form['id']
        Menu.menu_delete(rowid)
    tablesList = Menu.view_all()
    return render_template('viewmenu.html', msg="record deleted", rows=tablesList)



@app.route("/addTablesPage")
def addTablesPage():
    return render_template("addTable.html")


@app.route("/addTable", methods=['POST', 'GET'])
def addTable():
    if request.method == 'POST':
        try:
            tableNumber = request.form['tableNumber']

            table = Table(tableNumber, "Admin", datetime.now())
            msg = table.table_add()
        except:
            msg = "Error in the INSERT"
    return render_template('addTable.html', msg=msg)





@app.route("/tables")
def tables():
    tablesList = Table.view_all()
    return render_template('viewTables.html', rows=tablesList)


@app.route("/deletetables", methods=['POST', 'GET'])
def deleteTables():
    if request.method == 'POST':
        rowid = request.form['id']
        Table.table_delete(rowid)
    tablesList = Table.view_all()
    return render_template('viewTables.html', msg="record deleted", rows=tablesList)


@app.route("/createBooking")
def createBooking():
    return render_template("createBookings.html")


@app.route("/addBooking", methods=['POST', 'GET'])
def addBooking():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            contactno = request.form['contactno']
            bookingDate = request.form['bookingDate']
            bookingTime = request.form['bookingTime']
            adult = request.form['adult']
            children = request.form['children']
            type = request.form['type']

            booking = Bookings(name, email, contactno, bookingDate, bookingTime, adult, children, type, 'Pending', None)
            msg = booking.booking_add()

        except:
            msg = "Error in the INSERT"
    return render_template('createBookings.html', msg=msg)


@app.route("/bookings")
def bookings():
    bookingList = Bookings.view_all()
    return render_template('bookings.html', rows=bookingList)


@app.route("/modifyBooking", methods=['POST', 'GET'])
def modifyBooking():
    if request.method == 'POST':
        id = request.form['id']
        rows = Bookings.booking_single(id)
        tablesList = Table.view_all()
        return render_template('modifyBooking.html', rows=rows, list=tablesList)


@app.route("/editBooking", methods=['POST', 'GET'])
def editBooking():
    print("test")
    if request.method == 'POST':
        try:
            id = request.form['id']
            status = request.form['status']
            tableNumber = request.form['tableNumber']
            remarks = request.form['remarks']
            Bookings.bookings_edit(id, status, tableNumber, remarks)
        except:
            msg = "Error while updating"

    return render_template('bookings.html', rows=Bookings.view_all())


@app.route("/bookingStatus", methods=['POST', 'GET'])
def bookingStatus():
    if request.method == 'POST':
        contactno = request.form['contactno']
        rows = Bookings.booking_number(contactno)
        return render_template('viewstatus.html', rows=rows)


@app.route("/viewbookingStatus")
def viewbookingStatus():
    return render_template('viewstatus.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if (name == 'admin' and password == 'admin'):
            return redirect(url_for('bookings'))

        return render_template('login.html', msg="Enter Valid Details")


@app.route("/adminlogin", methods=['POST', 'GET'])
def adminLogin():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
