import sqlite3

class DataBase:
    def __init__(self, path):
        self.con = sqlite3.connect(path, uri=True)

    def GetUserInfo(self, name):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM user WHERE name=?', (name,))
        user = list(cur.fetchone())
        if user:
            user[6] = self.GetTeamsByName(user[5])
        return user
        
    def GetTeacherInfo(self, name):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM teacher WHERE name=?', (name,))
        return cur.fetchone()

    def GetRoomInfo(self, name):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM room WHERE name=?', (name,))
        return cur.fetchone()

    def GetRoomList(self, school, date):
        cur = self.con.cursor()
        if school == 'all':
            cur.execute('SELECT * FROM room')
        else:
            cur.execute('SELECT * FROM room WHERE school=?', (school,))
        ls = cur.fetchall()
        for i, info in enumerate(ls):
            dic = {
                'charge' : info[4],
                'name' : info[1],
                'acceptable' : info[5],
                'beem' : info[2],
                'board' : info[3],
                'school' : info[6],
                'state' : self.GetRoomState(info[1], date)
            }
            ls[i] = dic
        return ls

    def GetTeamsByName(self, name):
        cur = self.con.cursor()
        cur.execute(f'SELECT * FROM team WHERE members LIKE "%{name}%"')
        ls = cur.fetchall()
        cur.execute(f'SELECT * FROM team WHERE leader LIKE "%{name}%"')
        ls += cur.fetchall()
        names = [team[1] for team in ls]
        return names

    def GetTeamInfo(self, team):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM team WHERE name=?', (team,))
        return cur.fetchone()

    def GetBookList(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM book WHERE status="waitForAccept"')
        ls = cur.fetchall()
        for i, info in enumerate(ls):
            dic = {
                'team' : info[1],
                'room' : info[2],
                'date' : info[3],
                'reason' : info[5]
            }
            ls[i] = dic
        return ls

    def GetBookedListByUser(self, user):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM book WHERE status="waitForAccept"')
        rooms = cur.fetchall()
        cur.execute('SELECT * FROM book WHERE status="accepted"')
        rooms += cur.fetchall()
        
        booked = []

        user_team = self.GetTeamsByName(user)
        for room in rooms:
            if room[1] in user_team:
                booked.append({'team' : room[1], 'room' : room[2], 'status' : room[4], 'date' : room[3]})
        
        return booked
    
    def BookRoom(self, team, room, date, reason):
        if self.IsAbleToBook(room, date) is not None:
            print('denined')
            return False
        cur = self.con.cursor()
        cur.execute('INSERT INTO book(team, room, date, status, reason) VALUES(?,?,?,?, ?)',\
            (team, room, date, 'waitForAccept', reason))
        self.con.commit()
        return True

    def AcceptRoom(self, team, room, date, accept):
        cur = self.con.cursor()
        if accept:
            cur.execute('UPDATE book SET status="accepted" WHERE room=? AND date=?', (room, date,))
        else:
            cur.execute('DELETE FROM book WHERE room=? AND date=?', (room, date,))
        self.con.commit()


    def GetRoomState(self, room, date):
        ret = self.IsAbleToBook(room, date)
        print(ret)
        if ret:
            return ret[4]
        return 'ableToBook'

    def IsAbleToBook(self, room, date):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM book WHERE room=? AND date=?', (room, date,))
        return cur.fetchone()

    def AddTeamInfo(self, name, leader, members):
        cur = self.con.cursor()
        str_members = ''
        for i in members:
            str_members += i + ' '
        cur.execute('INSERT INTO team(name, leader, members) VALUES(?,?,?)', (name, leader, str_members))
        self.con.commit()
        cur.close()

    def CancelBook(self, team, room, date):
        cur = self.con.cursor()
        cur.execute('DELETE FROM book WHERE room=? AND date=? AND team=?', (room, date, team,))
        self.con.commit()
        cur.close()

    def ChangeBook(self, team, room, old_date, new_date):
        cur = self.con.cursor()
        cur.execute('UPDATE book SET date=? WHERE room=? AND date=? AND team=? AND status="waitForAccept"', \
            (new_date, room, old_date, team))
        self.con.commit()
        cur.close()

    def close(self):
        self.con.close()
