import matplotlib.pyplot as plt
import random
import sqlite3
import ast
import matplotlib.patches as mpatches

# connect to database
con = sqlite3.connect('baseball.db')
cur = con.cursor()
# creates table if there is no table
cur.execute("""CREATE TABLE IF NOT EXISTS
            pitcherStats(college, fName, lName, xCord, yCord, color)""")

# stores the values of the point clicked on the plot
def onclick(event):
    newx.append(round(event.xdata, 1))
    newy.append(round(event.ydata, 1))
    fig.canvas.mpl_disconnect(cid)

# create the original plot and labels for the strike zone
plt.axes()
fig = plt.figure()
rectangle = plt.Rectangle((-50, -125), 150, 250, fc='w', ec="black")
plt.gca().add_patch(rectangle)
a = mpatches.Patch(color='b', label='Fastball')
b = mpatches.Patch(color='g', label='Curveball')
c = mpatches.Patch(color='r', label='Changeup')
d = mpatches.Patch(color='c', label='Slider')
e = mpatches.Patch(color='m', label='Other')
plt.legend(handles=[a,b,c,d,e])
plt.xlim([-175, 175])
plt.ylim([-175, 175])
plt.xticks([])
plt.yticks([])

# global variable used to end the program
done = False

# loop through the user options
while(done == False):
    userIn = input("\nWhat would you like to do?\n[1] Add points\n[2] Plot points\n[3] Exit\n")

    # Adding points path
    if (userIn == "1"):
        done1 = False
        while(done1 == False):
            userIn = input("\n[1] New Player\n[2] Search for Player\n[3] Cancel\n")
            # create new player
            if (userIn == "1"):
                college = input("Enter a college: ")
                fName = input("Enter a First Name: ")
                lName = input("Enter a Last Name: ")
                newx = []
                newy = []
                color = []
                # receive click input
                cid = fig.canvas.mpl_connect('button_press_event', onclick)
                plt.waitforbuttonpress()
                pitch = input(
                    "What type of pitch was it?\n[1] Fastball\n[2] Curveball\n[3] Changeup\n[4] Slider\n[5] Other\n")
                if (pitch == "1"):
                    color.append('b')
                elif (pitch == "2"):
                    color.append('g')
                elif (pitch == "3"):
                    color.append('r')
                elif (pitch == "4"):
                    color.append('c')
                elif (pitch == "5"):
                    color.append('m')
                color = repr(color)
                newx = repr(newx)
                newy = repr(newy)
                # store new data into .db file
                cur.execute("""
                INSERT INTO pitcherStats(college, fName, lName, xCord, yCord, color)
                VALUES (?,?,?,?,?,?)
                """, (college, fName, lName, newx, newy, color))
            # search for player
            elif (userIn == "2"):
                userIn = input("Search by...\n[1] College\n[2] First Name\n[3] Last Name\n[4] Display all\n[5] Cancel\n")
                # search by college
                if (userIn == "1"):
                    college = input("Enter a college: ")
                    cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE college=?', (college,))
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    rowid = input("Enter row ID: ")
                    cur.execute('SELECT xCord, yCord FROM pitcherStats WHERE rowid=?', (rowid,))
                    newrows = cur.fetchone()
                    newx = newrows[0]
                    newy = newrows[1]
                    color = newrows[2]
                    color = ast.literal_eval(color)
                    newx = ast.literal_eval(newx)
                    newy = ast.literal_eval(newy)
                    # search for click input
                    cid = fig.canvas.mpl_connect('button_press_event', onclick)
                    plt.waitforbuttonpress()
                    pitch = input("What type of pitch was it?"
                                  "\n[1] Fastball\n[2] Curveball\n[3] Changeup\n[4] Slider\n[5] Other\n")
                    if (pitch == "1"):
                        color.append('b')
                    elif (pitch == "2"):
                        color.append('g')
                    elif (pitch == "3"):
                        color.append('r')
                    elif (pitch == "4"):
                        color.append('c')
                    elif (pitch == "5"):
                        color.append('m')
                    newx = repr(newx)
                    newy = repr(newy)
                    color = repr(color)
                    # store new info
                    cur.execute('UPDATE pitcherStats SET xCord=? WHERE rowid=?', (newx, rowid))
                    cur.execute('UPDATE pitcherStats SET yCord=? WHERE rowid=?', (newy, rowid))
                    cur.execute('UPDATE pitcherStats SET color=? WHERE rowid=?', (color, rowid))
                    con.commit()
                # search by first name
                elif (userIn == "2"):
                    fName = input("Enter a first name: ")
                    cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE fName=?', (fName,))
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    rowid = input("Enter row ID: ")
                    cur.execute('SELECT xCord, yCord FROM pitcherStats WHERE rowid=?', (rowid,))
                    newrows = cur.fetchone()
                    newx = newrows[0]
                    newy = newrows[1]
                    color = newrows[2]
                    color = ast.literal_eval(color)
                    newx = ast.literal_eval(newx)
                    newy = ast.literal_eval(newy)
                    # search for click event
                    cid = fig.canvas.mpl_connect('button_press_event', onclick)
                    plt.waitforbuttonpress()
                    pitch = input("What type of pitch was it?"
                                  "\n[1] Fastball\n[2] Curveball\n[3] Changeup\n[4] Slider\n[5] Other\n")
                    if (pitch == "1"):
                        color.append('b')
                    elif (pitch == "2"):
                        color.append('g')
                    elif (pitch == "3"):
                        color.append('r')
                    elif (pitch == "4"):
                        color.append('c')
                    elif (pitch == "5"):
                        color.append('m')
                    color = repr(color)
                    newx = repr(newx)
                    newy = repr(newy)
                    # store new info
                    cur.execute('UPDATE pitcherStats SET xCord=? WHERE rowid=?', (newx, rowid))
                    cur.execute('UPDATE pitcherStats SET yCord=? WHERE rowid=?', (newy, rowid))
                    cur.execute('UPDATE pitcherStats SET color=? WHERE rowid=?', (color, rowid))
                    con.commit()
                # search by last name
                elif(userIn == "3"):
                    lName = input("Enter a last name: ")
                    cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE lName=?', (lName,))
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    rowid = input("Enter row ID: ")
                    cur.execute('SELECT xCord, yCord FROM pitcherStats WHERE rowid=?', (rowid,))
                    newrows = cur.fetchone()
                    newx = newrows[0]
                    newy = newrows[1]
                    color = newrows[2]
                    color = ast.literal_eval(color)
                    newx = ast.literal_eval(newx)
                    newy = ast.literal_eval(newy)
                    cid = fig.canvas.mpl_connect('button_press_event', onclick)
                    plt.waitforbuttonpress()
                    pitch = input("What type of pitch was it?"
                                  "\n[1] Fastball\n[2] Curveball\n[3] Changeup\n[4] Slider\n[5] Other\n")
                    if (pitch == "1"):
                        color.append('b')
                    elif (pitch == "2"):
                        color.append('g')
                    elif (pitch == "3"):
                        color.append('r')
                    elif (pitch == "4"):
                        color.append('c')
                    elif (pitch == "5"):
                        color.append('m')
                    newx = repr(newx)
                    newy = repr(newy)
                    color = repr(color)
                    cur.execute('UPDATE pitcherStats SET xCord=? WHERE rowid=?', (newx, rowid))
                    cur.execute('UPDATE pitcherStats SET yCord=? WHERE rowid=?', (newy, rowid))
                    cur.execute('UPDATE pitcherStats SET color=? WHERE rowid=?', (color, rowid))
                    con.commit()
                # displays all of the players
                elif (userIn == "4"):
                    cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    rowid = input("Enter row ID: ")
                    cur.execute('SELECT xCord, yCord, color FROM pitcherStats WHERE rowid=?', (rowid,))
                    newrows = cur.fetchone()
                    newx = newrows[0]
                    newy = newrows[1]
                    color = newrows[2]
                    color = ast.literal_eval(color)
                    newx = ast.literal_eval(newx)
                    newy = ast.literal_eval(newy)
                    # search for click event
                    cid = fig.canvas.mpl_connect('button_press_event', onclick)
                    plt.waitforbuttonpress()
                    pitch = input("What type of pitch was it?"
                                  "\n[1] Fastball\n[2] Curveball\n[3] Changeup\n[4] Slider\n[5] Other\n")
                    if (pitch == "1"):
                        color.append('b')
                    elif (pitch == "2"):
                        color.append('g')
                    elif (pitch == "3"):
                        color.append('r')
                    elif (pitch == "4"):
                        color.append('c')
                    elif (pitch == "5"):
                        color.append('m')
                    color = repr(color)
                    newx = repr(newx)
                    newy = repr(newy)
                    # store new info
                    cur.execute('UPDATE pitcherStats SET xCord=? WHERE rowid=?', (newx, rowid))
                    cur.execute('UPDATE pitcherStats SET yCord=? WHERE rowid=?', (newy, rowid))
                    cur.execute('UPDATE pitcherStats SET color=? WHERE rowid=?', (color, rowid))
                    con.commit()
                # cancel searching for player
                elif (userIn == "5"):
                    print("Cancelling...\n")
                    done1 = True
                else:
                    print("Invalid Input\n")
                # cancel adding points
            elif (userIn == "3"):
                print("Cancelling...\n")
                done1 = True
            else:
                print("Invalid Input\n")
    # plotting points path
    elif (userIn == "2"):
        userIn = input("Search by...\n[1] College\n[2] First Name\n[3] Last Name\n[4] Display all\n[5] Cancel\n")
        # search for player by college
        if (userIn == "1"):
            college = input("Enter a college: ")
            cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE college=?', (college,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            rowid = input("Enter row ID: ")
            cur.execute('SELECT xCord, yCord, color FROM pitcherStats WHERE rowid=?', (rowid,))
            newrows = cur.fetchone()
            newx = newrows[0]
            newy = newrows[1]
            color = newrows[2]
            color = ast.literal_eval(color)
            newx = ast.literal_eval(newx)
            newy = ast.literal_eval(newy)
            # plot stored points
            for i in range(len(newx)):
                plt.plot(newx[i], newy[i], 'ro', c=color[i], marker=".", markersize=30)
                plt.draw()
                plt.pause(0.01)
        # search for player by first name
        elif (userIn == "2"):
            fName = input("Enter a first name: ")
            cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE fName=?', (fName,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            rowid = input("Enter row ID: ")
            cur.execute('SELECT xCord, yCord, color FROM pitcherStats WHERE rowid=?', (rowid,))
            newrows = cur.fetchone()
            newx = newrows[0]
            newy = newrows[1]
            color = newrows[2]
            color = ast.literal_eval(color)
            newx = ast.literal_eval(newx)
            newy = ast.literal_eval(newy)
            # plot stored points
            for i in range(len(newx)):
                plt.plot(newx[i], newy[i], 'ro', c=color[i], marker=".", markersize=30)
                plt.draw()
                plt.pause(0.01)
        # search by first name
        elif (userIn == "3"):
            lName = input("Enter a last name: ")
            cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats WHERE lName=?', (lName,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            rowid = input("Enter row ID: ")
            cur.execute('SELECT xCord, yCord, color FROM pitcherStats WHERE rowid=?', (rowid,))
            newrows = cur.fetchone()
            newx = newrows[0]
            newy = newrows[1]
            color = newrows[2]
            color = ast.literal_eval(color)
            newx = ast.literal_eval(newx)
            newy = ast.literal_eval(newy)
            # plot stored points
            for i in range(len(newx)):
                plt.plot(newx[i], newy[i], 'ro', c=color[i], marker=".", markersize=30)
                plt.draw()
                plt.pause(0.01)
        # displays all of the players
        elif (userIn == "4"):
            cur.execute('SELECT rowid, college, fName, lName FROM pitcherStats')
            rows = cur.fetchall()
            for row in rows:
                print(row)
            rowid = input("Enter row ID: ")
            cur.execute('SELECT xCord, yCord, color FROM pitcherStats WHERE rowid=?', (rowid,))
            newrows = cur.fetchone()
            newx = newrows[0]
            newy = newrows[1]
            color = newrows[2]
            color = ast.literal_eval(color)
            newx = ast.literal_eval(newx)
            newy = ast.literal_eval(newy)
            # plot stored points
            for i in range(len(newx)):
                plt.plot(newx[i], newy[i], 'ro', c=color[i], marker=".", markersize=30)
                plt.draw()
                plt.pause(0.01)
        # cancel plotting points
        elif (userIn == "5"):
            print("Cancelling...\n")
        else:
            print("Invalid Input\n")
    # exiting path
    elif (userIn == "3"):
        print("Exiting...\n")
        done = True
    # error exception
    else:
        print("Invalid Input\n")


plt.show()
con.commit()
con.close()
