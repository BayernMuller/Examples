from flask import Flask, request, jsonify
from datetime import datetime
import database
import json
app = Flask(__name__)

def log(msg):
    print('\n' + datetime.now().strftime('%H:%M:%S'))
    print('>>', msg)
    print()

@app.route('/user_login', methods=['POST'])
def user_login():
    params = request.json
    db = database.DataBase('./data.db')
    info = db.GetUserInfo(params['user'])
    if info:
        if info[1] == params['password']:
            log(params['user'] + ' has logined')
            return jsonify({'status' : 200}), 200
    return jsonify({'status' : 500}), 500

@app.route('/user_info', methods=['POST'])
def user_info():
    params = request.json
    print(params)
    db = database.DataBase('./data.db')
    info = db.GetUserInfo(params['user'])
    if info:
        dic = {
            'user' : info[5],
            'school' : info[3],
            'grade' : info[2],
            'class' : info[4],
            'team' : info[6],
            'name' : info[5][4:]
        }
        log(params['user'] + '\'s info is taken')
        return jsonify(dic), 200
    return '', 500

@app.route('/user_team', methods=['POST'])
def user_team():
    params = request.json
    db = database.DataBase('./data.db')
    teams = db.GetTeamsByName(params['user'])
    return jsonify(teams), 200


@app.route('/teacher_login', methods=['POST'])
def teacher_login():
    params = request.json
    db = database.DataBase('./data.db')
    info = db.GetTeacherInfo(params['name'])
    if info:
        if info[2] == params['password']:
            log(params['name'] + ' has logined')
            return jsonify({'status' : 200}), 200
    return jsonify({'status' : 500}), 500

@app.route('/teacher_info', methods=['POST'])
def teacher_info():
    params = request.json
    db = database.DataBase('./data.db')
    info = db.GetTeacherInfo(params['user'])
    log(info)
    if info:
        dic = {
            'user' : info[1],
            'room' : info[3],
        }
        log(params['user'] + '\'s info is taken')
        return jsonify(dic), 200
    return '', 500

@app.route('/room_info', methods=['POST'])
def room_info():
    params = request.json
    db = database.DataBase('./data.db')
    info = db.GetRoomInfo(params['name'])
    if info:
        dic = {
            'charge' : info[4],
            'name' : info[1],
            'acceptable' : info[5],
            'state' : 'ableToBook',
            'beem' : info[2],
            'board' : info[3],
            'school' : info[6]
        }
        log('room ' + params['name'] + '\'s info is taken')
        return jsonify(dic), 200
    return '', 500

@app.route('/room_list', methods=['POST'])
def room_list():
    db = database.DataBase('./data.db')
    params = request.json
    return jsonify(db.GetRoomList(params['school'], params['date'])), 200

@app.route('/team_info', methods=['POST'])
def team_info():
    db = database.DataBase('./data.db')
    params = request.json
    team = db.GetTeamInfo(params['name'])
    dic = {
        'name' : team[1],
        'leader' : team[2],
        'members' : team[3].split()
    }
    return jsonify(dic), 200

@app.route('/team_add', methods=['POST'])
def team_add():
    db = database.DataBase('./data.db')
    params = request.json
    db.AddTeamInfo(params['name'], params['leader'], params['members'])
    return jsonify({'status' : 200}), 200

@app.route('/room_book', methods=['POST'])
def room_book():
    db = database.DataBase('./data.db')
    params = request.json
    print(params)
    ret = db.BookRoom(params['team'], params['room'], params['date'], params['reason'])
    code = 200 if ret else 500
    return jsonify({'status' : code}), code

@app.route('/room_state', methods=['POST'])
def room_state():
    db = database.DataBase('./data.db')
    params = request.json
    ret = db.GetRoomState(params['room'], params['date'])
    code = 200 if ret else 500
    return jsonify({'status' : ret}), code

@app.route('/room_accept', methods=['POST'])
def room_accept():
    db = database.DataBase('./data.db')
    params = request.json
    db.AcceptRoom(params['team'], params['room'], params['date'], params['accept'])
    return jsonify({'status' : 200}), 200

@app.route('/book_list', methods=['POST'])
def book_list():
    db = database.DataBase('./data.db')
    params = request.json
    ret = db.GetBookList()
    return jsonify(ret), 200

@app.route('/booked_list', methods=['POST'])
def booked_list():
    db = database.DataBase('./data.db')
    params = request.json
    ret = db.GetBookedListByUser(params['user'])
    return jsonify(ret), 200

@app.route('/book_cancel', methods=['POST'])
def book_cancel():
    db = database.DataBase('./data.db')
    params = request.json
    db.CancelBook(params['team'], params['room'], params['date'])
    return jsonify({'state' : 200}), 200

@app.route('/book_change', methods=['POST'])
def book_change():
    db = database.DataBase('./data.db')
    params = request.json
    db.ChangeBook(params['team'], params['room'], params['old_date'], params['new_date'])
    return jsonify({'state' : 200}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)