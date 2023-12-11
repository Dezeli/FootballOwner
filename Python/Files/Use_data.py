import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time
import random
import threading
from timer import testtime

table_list = [
    "Coaches",
    "Leagues",
    "Players",
    "Staffs",
    "Teams",
    "Gamer_Team",
    "League_Calander",
    "League_table",
    "Message_box",
    "Player_Stat",
]

timercheck = testtime()
###############################################################################
# 게이머 생성
###############################################################################


def input_Names1():
    name = askstring("구단주 생성", "구단주 이름을 입력하세요.")
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    if name == None:
        return "No"
    else:
        db = sqlite3.connect("../../Database/FO_savefile1.db")
        cursor = db.cursor()
        insert_query = f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}','-')"
        cursor.execute(insert_query)
        db.commit()


def input_Names2():
    name = askstring("구단주 생성", "구단주 이름을 입력하세요.")
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    if name == None:
        return "No"
    else:
        db = sqlite3.connect("../../Database/FO_savefile2.db")
        cursor = db.cursor()
        insert_query = f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}','-')"
        cursor.execute(insert_query)
        db.commit()


###############################################################################
# 데이터 저장
###############################################################################
def Save1_data():
    Warning_message = tkinter.messagebox.askokcancel("경고", "정말 데이터 파일을 덮어씌우시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"../../Database/FO_savefile1.db")
        cursor = db.cursor()
        for table in table_list:
            cursor.execute(f"DELETE FROM {table}")
        cursor.execute("DELETE FROM Gamer")
        db.commit()
        db_load = sqlite3.connect(f"../../Database/FO_savefile3.db")
        l_cursor = db_load.cursor()
        db_save = sqlite3.connect(f"../../Database/FO_savefile1.db")
        s_cursor = db_save.cursor()
        for table in table_list:
            l_cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = l_cursor.fetchone()[0]
            l_cursor.execute(f"SELECT * FROM {table}")
            for i in range(count):
                Save_list = l_cursor.fetchone()
                s_cursor.execute(f"INSERT INTO {table} VALUES{Save_list}")
        l_cursor.execute(f"SELECT * FROM Gamer")
        Save_list = l_cursor.fetchone()
        now = time.localtime()
        Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
            now.tm_year,
            now.tm_mon,
            now.tm_mday,
            now.tm_hour,
            now.tm_min,
            now.tm_sec,
        )
        s_cursor.execute(
            f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')"
        )
        db_save.commit()
        Save_message = tkinter.messagebox.showinfo("저장 완료", "데이터 파일을 저장했습니다.")


def Save2_data():
    Warning_message = tkinter.messagebox.askokcancel("경고", "정말 데이터 파일을 덮어씌우시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"../../Database/FO_savefile2.db")
        cursor = db.cursor()
        for table in table_list:
            cursor.execute(f"DELETE FROM {table}")
        cursor.execute("DELETE FROM Gamer")
        db.commit()
        db_load = sqlite3.connect(f"../../Database/FO_savefile3.db")
        l_cursor = db_load.cursor()
        db_save = sqlite3.connect(f"../../Database/FO_savefile2.db")
        s_cursor = db_save.cursor()
        for table in table_list:
            l_cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = l_cursor.fetchone()[0]
            l_cursor.execute(f"SELECT * FROM {table}")
            for i in range(count):
                Save_list = l_cursor.fetchone()
                s_cursor.execute(f"INSERT INTO {table} VALUES{Save_list}")
        l_cursor.execute(f"SELECT * FROM Gamer")
        Save_list = l_cursor.fetchone()
        now = time.localtime()
        Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
            now.tm_year,
            now.tm_mon,
            now.tm_mday,
            now.tm_hour,
            now.tm_min,
            now.tm_sec,
        )
        s_cursor.execute(
            f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')"
        )
        db_save.commit()
        Save_message = tkinter.messagebox.showinfo("저장 완료", "데이터 파일을 저장했습니다.")


def Auto_save_get_data(num):
    db_load = sqlite3.connect(f"../../Database/FO_datafile.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"../../Database/FO_savefile{num}.db")
    s_cursor = db_save.cursor()
    for table in table_list[0:5]:
        l_cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(f"INSERT INTO {table} VALUES{Save_list}")
    db_load.commit()
    db_save.commit()

    def makethread():
        make_messages(3)
        make_messages(num)
        make_calander(num)
        make_calander(3)
        make_player_stats(num)
        make_player_stats(3)
        make_league_table(num)
        make_league_table(3)

    make_thread = threading.Thread(target=makethread)
    make_thread.daemon = True
    make_thread.start()


def make_messages(num):
    db = sqlite3.connect(f"../../Database/FO_savefile{num}.db")
    cursor = db.cursor()
    for i in range(4):
        cursor.execute(f"INSERT INTO Message_box VALUES('{i+1}','','','','','')")
    cursor.execute(
        f"INSERT INTO Message_box VALUES('5','Football Owner','오신것을','환영합니다','','Football Owner은 축구 시뮬레이션 게임입니다.\n 아직 많이 부족하지만,\n 재밌게 즐겨주세요.')"
    )
    db.commit()


def time_auto_save():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    cursor.execute(f"UPDATE Gamer Set Date= '{Date}'")
    db.commit()


###############################################################################
# 데이터 불러오기
###############################################################################
def load1_data():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    for table in table_list:
        cursor.execute(f"DELETE FROM {table}")
    cursor.execute("DELETE FROM Gamer")
    db.commit()
    db_load = sqlite3.connect(f"../../Database/FO_savefile1.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"../../Database/FO_savefile3.db")
    s_cursor = db_save.cursor()
    for table in table_list:
        l_cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(f"INSERT INTO {table} VALUES{Save_list}")
    l_cursor.execute(f"SELECT * FROM Gamer")
    Save_list = l_cursor.fetchone()
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    s_cursor.execute(
        f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')"
    )
    db.commit()
    db_load.commit()
    db_save.commit()


def load2_data():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    for table in table_list:
        cursor.execute(f"DELETE FROM {table}")
    cursor.execute("DELETE FROM Gamer")
    db.commit()
    db_load = sqlite3.connect(f"../../Database/FO_savefile2.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"../../Database/FO_savefile3.db")
    s_cursor = db_save.cursor()
    for table in table_list:
        l_cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(f"INSERT INTO {table} VALUES{Save_list}")
    l_cursor.execute(f"SELECT * FROM Gamer")
    Save_list = l_cursor.fetchone()
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    s_cursor.execute(
        f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')"
    )
    db.commit()
    db_load.commit()
    db_save.commit()


###############################################################################
# 데이터 리셋
###############################################################################
def reset_datas():
    Warning_message = tkinter.messagebox.askokcancel("경고", "정말 모든 데이터 파일을 삭제하시겠습니까?")
    if Warning_message == True:
        for i in range(3):
            db = sqlite3.connect(f"../../Database/FO_savefile{i+1}.db")
            cursor = db.cursor()
            for table in table_list:
                cursor.execute(f"DELETE FROM {table}")
            cursor.execute("DELETE FROM Gamer")
            db.commit()
    reset_message = tkinter.messagebox.showinfo("리셋 완료", f"정보를 모두 리셋했습니다.")


###############################################################################
# 데이터 체크
###############################################################################
def Check_Savefiles(savefile):
    db = sqlite3.connect(f"../../Database/FO_savefile{savefile}.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Gamer ORDER BY Date DESC")
    Save_list = cursor.fetchone()
    return Save_list


def check_money():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Gamer")
    Save_list = cursor.fetchone()[3]
    return Save_list


def check_myteam():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Gamer_Team")
    count = cursor.fetchone()[0]
    return int(count)


###############################################################################
# 데이터 변경
###############################################################################
def give_money(money):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE Gamer SET Money ='{money}'")
    db.commit()
    return 0


def save_buy_team(Team):
    Warning_message = tkinter.messagebox.askokcancel("인수", "정말 팀을 인수하시겠습니까?")
    if Team[3] == "돈을 더 모으고 오세요":
        return
    if Warning_message == True:
        db = sqlite3.connect(f"../../Database/FO_savefile3.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM Gamer_Team")
        count = cursor.fetchone()[0]
        cursor.execute(f"SELECT Money From Gamer")
        money = cursor.fetchone()[0]
        sale = int(Team[4])
        if count < 1 and money > sale:
            cursor.execute(f"INSERT INTO Gamer_Team VALUES{Team}")
            db.commit()
            Save_message = tkinter.messagebox.showinfo("인수 완료", f"{Team[3]} 팀을 인수했습니다.")
            cursor.execute(f'UPDATE Gamer SET Money ="{money-sale}"')
            cursor.execute(f'UPDATE Gamer SET Team ="{Team[3]}"')
            db.commit()
        else:
            no_message = tkinter.messagebox.showinfo(
                "인수 불가", f"돈이 부족하거나 1팀 이상 인수 불가합니다."
            )


def save_sell_team(Team):
    Warning_message = tkinter.messagebox.askokcancel("매각", "정말 팀을 매각하시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"../../Database/FO_savefile3.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM Gamer_Team")
        count = cursor.fetchone()[0]
        cursor.execute(f"SELECT Money From Gamer")
        money = cursor.fetchone()[0]
        sale = int(Team[4])
        Seq = int(Team[0])
        cursor.execute(f'DELETE FROM Gamer_Team WHERE Seq=="{Seq}"')
        db.commit()
        Save_message = tkinter.messagebox.showinfo("매각 완료", f"{Team[3]} 팀을 매각했습니다.")
        cursor.execute(f'UPDATE Gamer SET Money ="{money+sale}"')
        if count == 1:
            cursor.execute(f'UPDATE Gamer SET Team ="무직"')
        else:
            cursor.execute(f"SELECT Team From Gamer_Team")
            team_name = cursor.fetchone()[0]
            cursor.execute(f'UPDATE Gamer SET Team ="{team_name}"')
        db.commit()


def get_injury():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Seq, Market_Value FROM Players WHERE Injury =='0' ORDER BY random()"
    )
    ran_length = random.randrange(5, 3000)
    injury_list = []
    for i in range(ran_length):
        injury_list.append(cursor.fetchone())
    for i in range(ran_length):
        ran_injury = random.randrange(1, 50)
        for j in range(7):
            new_injury = random.randrange(1, 50)
            if ran_injury > new_injury:
                ran_injury = new_injury
        cursor.execute(
            f'UPDATE Players SET Injury ="{ran_injury}" WHERE Seq == "{injury_list[i][0]}"'
        )
        db.commit()
    player_Data = []
    famous = 0
    for j in range(5):
        num = 0
        famous = 0
        for i in range(len(injury_list)):
            if famous < int(injury_list[i][1]):
                famous = int(injury_list[i][1])
                num = i
        player_Data.append(injury_list[num][0])
        injury_list.pop(num)
    return_list = []
    for i in player_Data:
        cursor.execute(f"SELECT * FROM Players WHERE Seq =='{i}'")
        return_list.append(cursor.fetchone())
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT * FROM Players WHERE Team = '{my_team}' AND Injury != '0' Order by Market_Value DESC"
    )
    return_list += cursor.fetchall()
    for i in range(3):
        return_list.append(["", "선수 없음", "", "", "", "0"])
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","부상 안내","{return_list[0][1]}","{return_list[1][1]}","{return_list[2][1]}" ,"{return_list[0][2]} 소속 {return_list[0][1]} 선수가\n 부상당하여 {return_list[0][-1]}경기 출전불가입니다.\
        \n{return_list[1][2]} 소속 {return_list[1][1]} 선수가\n 부상당하여 {return_list[1][-1]}경기 출전불가입니다.\n{return_list[2][2]} 소속 {return_list[2][1]} 선수가\n 부상당하여 {return_list[2][-1]}경기 출전불가입니다.\
        \n{return_list[3][2]} 소속 {return_list[3][1]} 선수가\n 부상당하여 {return_list[3][-1]}경기 출전불가입니다.\n{return_list[4][2]} 소속 {return_list[4][1]} 선수가\n 부상당하여 {return_list[4][-1]}경기 출전불가입니다.\
        \n {my_team} 부상자는\n {return_list[5][1]}, {return_list[6][1]}, {return_list[7][1]}등으로\n각각 {return_list[5][-1]}, {return_list[6][-1]}, {return_list[7][-1]} 경기 출전불가입니다 ")'
    cursor.execute(insert_query)
    db.commit()


###############################################################################
# 데이터 SELECT
###############################################################################


def mini_game():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    ran = random.randrange(1, 3001)
    cursor.execute(f"SELECT * FROM Players Where Seq = '{ran}'")
    a = cursor.fetchone()
    return a


def ran_team_ac(money):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Teams WHERE Value<='{money}' ORDER BY random()")
    acquistion_list = []
    for i in range(7):
        content = cursor.fetchone()
        if type(content) == tuple:
            acquistion_list.append(content)
        else:
            acquistion_list.append(["", "", "", "돈을 더 모으고 오세요", "", ""])
    return acquistion_list


def my_team_ac():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Gamer_Team")
    count = cursor.fetchone()[0]
    cursor.execute(f"SELECT * FROM Gamer_Team")
    acquistion_list = []
    for i in range(count):
        acquistion_list.append(cursor.fetchone())
    return acquistion_list


def team_players(sort, desc):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(f'SELECT COUNT(*) FROM Players Where Team =="{my_team}"')
    count_player = cursor.fetchone()[0]
    player_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Players Where Team =="{my_team}" Order By "{sort}"'
        )
    else:
        cursor.execute(
            f'SELECT * FROM Players Where Team =="{my_team}" Order By "{sort}" DESC'
        )

    for i in range(count_player):
        player = cursor.fetchone()[1:]
        player_list.append(player)
    return player_list


def team_coaches(sort, desc):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(f'SELECT COUNT(*) FROM Coaches Where Team =="{my_team}"')
    count_coaches = cursor.fetchone()[0]
    coach_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Coaches Where Team =="{my_team}" Order By "{sort}"'
        )
    else:
        cursor.execute(
            f'SELECT * FROM Coaches Where Team =="{my_team}" Order By "{sort}" DESC'
        )

    for i in range(count_coaches):
        coach = cursor.fetchone()[1:]
        coach_list.append(coach)
    return coach_list


def team_staffs(sort, desc):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(f'SELECT COUNT(*) FROM Staffs Where Team =="{my_team}"')
    count_staffs = cursor.fetchone()[0]
    staff_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Staffs Where Team =="{my_team}" Order By "{sort}"'
        )
    else:
        cursor.execute(
            f'SELECT * FROM Staffs Where Team =="{my_team}" Order By "{sort}" DESC'
        )

    for i in range(count_staffs):
        staff = cursor.fetchone()[1:]
        staff_list.append(staff)
    return staff_list


def team_manager_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Coaches Where Position ==(?) AND Team ==(?)",
        ("Manager", my_team),
    )
    Ability = cursor.fetchone()
    return Ability


def team_keeper_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == (?) ORDER By Ability DESC",
        (my_team, "0", "Goalkeeper"),
    )
    return cursor.fetchall()


def team_defender_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == (?) ORDER By Ability DESC",
        (my_team, "0", "Defender"),
    )
    return cursor.fetchall()


def team_midfielder_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players Where Team ==(?) AND Injury ==(?) AND Position == (?) ORDER By Ability DESC",
        (my_team, "0", "Midfielder"),
    )
    return cursor.fetchall()


def team_forward_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players Where Team ==(?) AND Injury ==(?) AND Position == (?) ORDER By Ability DESC",
        (my_team, "0", "Forward"),
    )
    return cursor.fetchall()


def team_ability(my_team):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players Where Team ==(?) AND Injury ==(?) ORDER By Ability DESC",
        (my_team, "0"),
    )
    return cursor.fetchall()


def team_coaches_ability():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT COUNT(*) AVG(Ablility) FROM Coaches Where Team ==(?)", (my_team,)
    )
    Data = cursor.fetchone()
    count_coaches = int(Data[0])
    avg_ability = int(Data[1])
    return int(count_coaches + avg_ability)


def team_staffs_ability():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT COUNT(*) AVG(Ablility) FROM Staffs Where Team ==(?)", (my_team,)
    )
    Data = cursor.fetchone()
    count_staffs = int(Data[0])
    avg_ability = int(Data[1])
    return int(count_staffs + avg_ability)


def rec_players(ability):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players WHERE Potential <= (?) ORDER BY random()", (ability,)
    )
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def rec_coaches(ability):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Coaches WHERE Ability <= (?) ORDER BY random()", (ability,)
    )
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def rec_staffs(ability):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Staffs WHERE Ability <= (?) ORDER BY random()", (ability,)
    )
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def ran_sell_player():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Players ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def ran_sell_coach():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Coaches ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def ran_sell_staff():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Staffs ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def sell_my_team():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(f"SELECT Value FROM Teams Where Team ==(?)", (my_team))
    Team_value = int(cursor.fetchone()[0])
    minus_value = int(Team_value * (0.5))
    plus_value = int(Team_value(0.3))
    result = random.randrange(Team_value - minus_value, Team_value + plus_value)
    return result


def ability_ran_change():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT * FROM Players Where Team ==(?) ORDER BY random()", (my_team,)
    )
    player_list = []
    random_list = []
    players = cursor.fetchall()
    for i in range(3):
        player = players[i]
        player_seq = int(player[0])
        player_ability = int(player[7])
        player_potential = int(player[8])
        ran = 0
        while ran == 0:
            ran = random.randrange(-2, 2)
        if player_ability + ran > player_potential:
            cursor.execute(
                f"UPDATE Players SET ability = (?) Where Seq == (?)",
                (player_potential, player_seq),
            )
        else:
            cursor.execute(
                f"UPDATE Players SET ability = (?) Where Seq == (?)",
                (player_ability + ran, player_seq),
            )
        db.commit()
        player_list.append(player)
        random_list.append(ran)

    def random_pick():
        cursor.execute(
            f"SELECT * FROM Players Where Team !=(?) ORDER BY random()", (my_team,)
        )
        players = cursor.fetchall()
        for i in range(1000):
            player = players[i]
            player_seq = int(player[0])
            player_ability = int(player[7])
            player_potential = int(player[8])
            ran = random.randrange(-2, 2)
            if player_ability + ran > player_potential:
                cursor.execute(
                    f"UPDATE Players SET ability = (?) Where Seq == (?)",
                    (player_potential, player_seq),
                )
            else:
                cursor.execute(
                    f"UPDATE Players SET ability = (?) Where Seq == (?)",
                    (player_ability + ran, player_seq),
                )
            db.commit()
            player_list.append(player)
            random_list.append(ran)

    make_thread = threading.Thread(target=lambda: random_pick)
    make_thread.daemon = True
    make_thread.start()
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","능력치 변화","{player_list[0][1]}","{player_list[1][1]}","{player_list[2][1]}" ,"{player_list[0][1]} 선수의 능력치가 {random_list[0]} 만큼 변화하였습니다.\n{player_list[1][1]} 선수의 능력치가 {random_list[1]} 만큼 변화하였습니다.\n{player_list[2][1]} 선수의 능력치가 {random_list[2]} 만큼 변화하였습니다.\n")'
    cursor.execute(insert_query)
    db.commit()


def fan_res():
    minus = team_money()
    minus = (minus[0] + minus[1] + minus[2]) // 20
    plus = int(match_money()[2:-3])
    score = plus - minus
    if score >= 50000:
        return ("최상", 0)
    elif 50000 > score >= 40000:
        return ("상", 0)
    elif 40000 > score >= 20000:
        return ("보통", 0)
    elif 20000 > score >= 10000:
        return ("하", 1)
    else:
        return ("최하", 1)


def fan_msg_res():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    minus = team_money()
    minus = (minus[0] + minus[1] + minus[2]) // 20
    plus = int(match_money()[2:-3])
    score = plus - minus
    if score >= 50000:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","팬 반응","","","" ,"최근 {my_team}은 경기당 {score} 만원 이익을 냈으며 \n 팬들은 이에 대하여 매우 기뻐하고 있습니다. \n 앞으로도 구단을 재정적으로 잘 이끌어 주세요.")'
    elif 50000 > score >= 40000:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","팬 반응","","","" ,"최근 {my_team}은 경기당 {score} 만원 이익을 냈으며 \n 팬들은 이에 대하여 만족하고 있습니다. \n 하지만 아직 발전할 가능성은 충분합니다.")'

    elif 40000 > score >= 20000:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","팬 반응","","","" ,"최근 {my_team}은 경기당 {score} 만원 이익을 냈으며 \n 팬들은 이에 대하여 아무 생각이 없습니다. \n 조금 더 열심히 하여 좋은 결과를 낼 필요가 있습니다.")'

    elif 20000 > score >= 10000:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","팬 반응","","","" ,"최근 {my_team}은 경기당 {score} 만원 이익을 냈으며 \n 팬들은 이에 대하여 실망하고 있습니다. \n 조금 이익을 위해 분발해주세요.")'

    else:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","팬 반응","","","" ,"최근 {my_team}은 경기당 {score} 만원 이익을 냈으며 \n 팬들은 이에 대하여 매우 절망하고 있습니다. \n 구단을 매각하고 다른 구단을 찾아보는 것도...")'
    cursor.execute(insert_query)
    db.commit()


def pla_Res():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT count(*) From League_Calander Where result != (?) AND (Home == (?) OR Away == (?))",
        ("0", my_team, my_team),
    )
    count = int(cursor.fetchone()[0])
    if count < 5:
        return ("미정", 0)
    else:
        cursor.execute(
            f"SELECT * FROM League_Calander Where result != (?) AND (Home == (?) OR Away == (?)) ORDER BY Seq DESC",
            ("0", my_team, my_team),
        )
        score = 0
        for i in range(5):
            Data = cursor.fetchone()
            Home = str(Data[4])
            Away = str(Data[5])
            home_result = int(Data[6][0])
            away_result = int(Data[6][2])
            if home_result == away_result:
                score += 1
            elif home_result >= away_result:
                if Home == my_team:
                    score += 3
            elif home_result <= away_result:
                if Away == my_team:
                    score += 3

        if score >= 13:
            return ("최상", 0)
        elif 13 > score >= 10:
            return ("상", 0)
        elif 10 > score >= 7:
            return ("보통", 0)
        elif 7 > score >= 4:
            return ("하", 1)
        else:
            return ("최하", 1)


def pla_msg_Res():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT count(*) From League_Calander Where result != (?) AND (Home == (?) OR Away == (?))",
        ("0", my_team, my_team),
    )
    count = int(cursor.fetchone()[0])
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    if count < 5:
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 치룬 경기가 아직 부족합니다. \n 선수들은 경기를 열심히 준비하고 있습니다. \n 5경기를 치룬 이후에 선수들의 반응이 나올 것입니다.")'

    else:
        cursor.execute(
            f"SELECT * FROM League_Calander Where result != (?) AND (Home == (?) OR Away == (?)) ORDER BY Seq DESC",
            ("0", my_team, my_team),
        )
        score = 0
        for i in range(5):

            Data = cursor.fetchone()
            Home = str(Data[4])
            Away = str(Data[5])
            home_result = int(Data[6][0])
            away_result = int(Data[6][2])
            if home_result == away_result:
                score += 1
            elif home_result >= away_result:
                if Home == my_team:
                    score += 3
            elif home_result <= away_result:
                if Away == my_team:
                    score += 3

        if score >= 13:
            insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 승점 {score}점을 획득했으며 \n 선수들은 이에 대하여 매우 기뻐하고 있습니다. \n 앞으로도 이를 유지하면 될 것 같습니다.")'

        elif 13 > score >= 10:
            insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 승점 {score}점을 획득했으며 \n 선수들은 이에 대하여 나름 만족하고 있습니다. \n 하지만 아직 발전 할 가능성은 충분합니다.")'

        elif 10 > score >= 7:
            insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 승점 {score}점을 획득했으며 \n 선수들은 이에 대하여 아무생각이 없습니다. \n 조금 더 열심히 하여 좋은 결과를 낼 필요가 있습니다.")'

        elif 7 > score >= 4:
            insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 승점 {score}점을 획득했으며 \n 선수들은 이에 대하여 실망하고 있습니다. \n 새로운 변화가 필요할 것 같습니다.")'

        else:
            insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","선수단 반응","","","" ,"최근 {my_team}은 승점 {score}점을 획득했으며 \n 선수들은 이에 대하여 매우 절망하고 있습니다. \n 최악의 상황에서 분위기를 반전시켜야 합니다.")'

    cursor.execute(insert_query)
    db.commit()


###############################################################################
# 그 외
###############################################################################


def make_calander(num):
    db = sqlite3.connect(f"../../Database/FO_savefile{num}.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM League_Calander")
    db.commit()
    cursor.execute(f"SELECT count(*) From Leagues")
    league_count = cursor.fetchone()[0]
    cursor.execute(f"SELECT Name, Country From Leagues")
    league_list = []
    for i in range(league_count):
        league_list.append(cursor.fetchone())
    seq = 0
    for k in range(league_count):
        cursor.execute(
            f"SELECT count(*) From Teams Where League == (?) AND Country == (?)",
            (
                league_list[k][0],
                league_list[k][1],
            ),
        )
        count = cursor.fetchone()[0]
        cursor.execute(
            f"SELECT Team From Teams WHERE League == (?) AND Country == (?)",
            (
                league_list[k][0],
                league_list[k][1],
            ),
        )
        Team_list = []
        for i in range(count):
            Team_list.append(cursor.fetchone()[0])
        calander_list = []
        for i in range(len(Team_list)):
            for j in range(1, len(Team_list)):
                inter = i + j
                if inter > len(Team_list) - 1:
                    inter -= len(Team_list)
                calander_list.append((Team_list[i], Team_list[inter]))
        calander_sort_list = []
        for i in range(len(Team_list) - 1):
            ran_num = [i + 1 for i in range(len(Team_list))]
            for j in range(len(Team_list)):
                choicenum = random.choice(ran_num)
                ran_num.remove(choicenum)
                result = choicenum * (len(Team_list) - 1) - len(Team_list) + i - 1
                calander_sort_list.append(calander_list[result])
        for i in range(len(calander_sort_list)):
            seq += 1
            cursor.execute(
                f'INSERT INTO League_Calander VALUES("{seq}", "{league_list[k][1]}", "{league_list[k][0]}", "{i+1}", "{calander_sort_list[i][0]}", "{calander_sort_list[i][1]}","0","0")'
            )
        db.commit()


def make_player_stats(num):
    db = sqlite3.connect(f"../../Database/FO_savefile{num}.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM Player_Stat")
    db.commit()
    cursor.execute(f"SELECT count(*) From Leagues")
    league_count = cursor.fetchone()[0]
    cursor.execute(f"SELECT Name, Country From Leagues")
    league_list = []
    for i in range(league_count):
        league_list.append(cursor.fetchone())
    seq = 0
    all_team = []
    for k in range(league_count):
        cursor.execute(
            f"SELECT count(*) From Teams Where League == (?) AND Country == (?)",
            (
                league_list[k][0],
                league_list[k][1],
            ),
        )
        count = cursor.fetchone()[0]
        cursor.execute(
            f"SELECT Team From Teams WHERE League == (?) AND Country == (?)",
            (
                league_list[k][0],
                league_list[k][1],
            ),
        )
        Team_list = []
        for i in range(count):
            Team_list.append(cursor.fetchone()[0])
        all_team += Team_list
        player_list = []
        for i in range(len(Team_list)):
            cursor.execute(
                f"SELECT count(*) From Players WHERE Team == (?)", (Team_list[i],)
            )
            player_cnt = cursor.fetchone()[0]
            cursor.execute(
                f"SELECT Team, Name From Players WHERE Team == (?)", (Team_list[i],)
            )
            for i in range(player_cnt):
                player_list.append(cursor.fetchone())
        for i in range(len(player_list)):
            seq += 1
            cursor.execute(
                f'INSERT INTO Player_Stat VALUES("{seq}", "{league_list[k][1]}", "{league_list[k][0]}","{player_list[i][0]}","{player_list[i][1]}","0","0","0","0")'
            )
        db.commit()


def play_my_game(Home, Away, db):
    Home_Team_manager = team_manager_ability(Home)
    Away_Team_manager = team_manager_ability(Away)
    if Home_Team_manager == None:
        H_manager_ability = 50
    else:
        H_manager_ability = int(Home_Team_manager[5])
    if Away_Team_manager == None:
        A_manager_ability = 50
    else:
        A_manager_ability = int(Away_Team_manager[5])
    H_try = H_manager_ability - A_manager_ability + 20
    A_try = A_manager_ability - H_manager_ability + 20
    H_keeper = team_keeper_ability(Home)
    A_keeper = team_keeper_ability(Away)
    H_defender = team_defender_ability(Home)
    A_defender = team_defender_ability(Away)
    H_midfielder = team_midfielder_ability(Home)
    A_midfielder = team_midfielder_ability(Away)
    H_forward = team_forward_ability(Home)
    A_forward = team_forward_ability(Away)
    H1_k_abil = int(H_keeper[0][7])
    A1_k_abil = int(A_keeper[0][7])
    H4_d_abil = (
        int(H_defender[0][7])
        + int(H_defender[1][7])
        + int(H_defender[2][7])
        + int(H_defender[3][7])
    )

    A4_d_abil = (
        int(A_defender[0][7])
        + int(A_defender[1][7])
        + int(A_defender[2][7])
        + int(A_defender[3][7])
    )
    H3_m_abil = (
        int(H_midfielder[0][7]) + int(H_midfielder[1][7]) + int(H_midfielder[2][7])
    )
    A3_m_abil = (
        int(A_midfielder[0][7]) + int(A_midfielder[1][7]) + int(A_midfielder[2][7])
    )
    H3_f_abil = int(H_forward[0][7]) + int(H_forward[1][7]) + int(H_midfielder[2][7])
    A3_f_abil = int(A_forward[0][7]) + int(A_forward[1][7]) + int(A_forward[2][7])

    H_Team = H_keeper, H_defender, H_midfielder, H_forward, Home_Team_manager
    A_Team = A_keeper, A_defender, A_midfielder, A_forward, Away_Team_manager
    highlight = []

    if H_try < 10:
        H_try = 10
    if A_try < 10:
        A_try = 10
    if H_try > 27:
        H_try = 27
    if A_try > 27:
        A_try = 27
    order = []
    for i in range(H_try):
        order.append("H")
    for i in range(A_try):
        order.append("A")
    random.shuffle(order)
    goal1 = 0
    goal1per = 101
    goal2 = 0
    goal2per = 101
    for i in order:
        if i == "H":
            chance_dif = int((H3_m_abil - A3_m_abil) / 4)
            if chance_dif < 0:
                chance_dif = int(chance_dif / 2)
            ran = random.randrange(1, goal1per)
            if 60 + chance_dif < ran:
                highlight.append([f"{Home} 앞으로 나아갑니다", "1"])
                highlight.append([f"아, 패스가 끊겼어요", "1"])
                continue
            pk_chance = int(H3_f_abil / 100)
            ran = random.randrange(1, goal1per)
            if 1 + pk_chance >= ran:
                highlight.append([f"아 이게 뭔가요, {Home}팀 선수가 페널티 박스에서 넘어졌는데요...", "1"])
                highlight.append(["PK가 선언됩니다.", "1"])
                ran = random.randrange(1, goal1per)
                if ran <= 70:
                    highlight.append(["슛~~", "1"])
                    highlight.append([f"PK는 놓치면 안돼죠, {Home}의 골이 들어갑니다", "골1"])
                    goal1per += 15
                    goal1 += 1
                    continue
                else:
                    highlight.append(["슛~~", "1"])
                    highlight.append([f"아 이 좋은 기회를 실축으로 날려버리나요...", "1"])
                    continue
            supersave_chance = int(A1_k_abil / 10)
            ran = random.randrange(1, goal1per)
            if 1 + supersave_chance >= ran:
                highlight.append([f"{Home} 벼락같은 슛!", "1"])
                highlight.append(["엄청난 슈퍼세이브가 나옵니다", "2"])
                continue
            goal_dif = int(((H3_f_abil + H3_m_abil) - (A4_d_abil + (A1_k_abil))) / 16)
            ran = random.randrange(1, goal1per)
            if goal_dif + 20 >= ran:
                highlight.append([f"{Home} 앞으로 나아갑니다", "1"])
                highlight.append([f"좋은 패스죠", "1"])
                highlight.append([f"그대로 슛!!!", "1"])
                highlight.append([f"골~~~~ {Home} 팀이 골을 터트립니다.", "골1"])
                goal1per += 15
                goal1 += 1
            else:
                highlight.append([f"{Home} 앞으로 나아갑니다", "1"])
                highlight.append([f"좋은 패스죠", "1"])
                highlight.append([f"그대로 슛!!!", "1"])
                highlight.append(["아 이걸 날려먹나요...", "1"])
                continue
            ran = random.randrange(1, goal1per)
            if ran <= 2:
                goal1per -= 15
                goal1 -= 1
                highlight.append(["어? VAR 체크를 하는데요.. 아 노골이에요...", "ㄴ1"])
        else:
            chance_dif = int((A3_m_abil - H3_m_abil) / 4)
            if chance_dif < 0:
                chance_dif = int(chance_dif / 2)
            ran = random.randrange(1, goal2per)
            if 50 + chance_dif < ran:
                highlight.append([f"{Away} 앞으로 나아갑니다", "2"])
                highlight.append([f"아, 패스가 끊겼어요", "2"])
                continue
            pk_chance = int(A3_f_abil / 100)
            ran = random.randrange(1, goal2per)
            if 1 + pk_chance >= ran:
                highlight.append([f"아 이게 뭔가요, {Away}팀 선수가 페널티 박스에서 넘어졌는데요...", "2"])
                highlight.append(["PK가 선언됩니다.", "2"])
                ran = random.randrange(1, goal2per)
                if ran <= 70:
                    highlight.append(["슛~~", "2"])
                    highlight.append([f"PK는 놓치면 안돼죠, {Away}의 골이 들어갑니다", "골2"])
                    goal2per += 15
                    goal2 += 1
                else:
                    highlight.append(["슛~~", "2"])
                    highlight.append([f"아 이 좋은 기회를 실축으로 날려버리나요...", "2"])
                    continue
            supersave_chance = int(H1_k_abil / 10)
            ran = random.randrange(1, goal2per)
            if 1 + supersave_chance >= ran:
                highlight.append([f"{Away} 벼락같은 슛!", "2"])
                highlight.append(["엄청난 슈퍼세이브가 나옵니다", "1"])
                continue
            goal_dif = int(((A3_f_abil + A3_m_abil) - (H4_d_abil + (H1_k_abil))) / 16)
            ran = random.randrange(1, goal2per)
            if goal_dif + 10 >= ran:
                highlight.append([f"{Away} 앞으로 나아갑니다", "2"])
                highlight.append([f"좋은 패스죠", "2"])
                highlight.append([f"그대로 슛!!!", "2"])
                highlight.append([f"골~~~~ {Away} 팀이 골을 터트립니다.", "골2"])
                goal2per += 15
                goal2 += 1
            else:
                highlight.append([f"{Away} 앞으로 나아갑니다", "2"])
                highlight.append([f"좋은 패스죠", "2"])
                highlight.append([f"그대로 슛!!!", "2"])
                highlight.append(["아 이걸 날려먹나요...", "2"])
                continue
            ran = random.randrange(1, goal2per)
            if ran <= 2:
                goal1per -= 15
                goal2 -= 1
                highlight.append(["어? VAR 체크를 하는데요.. 아 노골이에요...", "ㄴ2"])
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE League_Calander SET result=(?) WHERE Home == (?) AND Away == (?)",
        (f"{goal1}:{goal2}", Home, Away),
    )
    db.commit()
    highlight.append([f"경기{goal1}:{goal2}로 종료됩니다. ", "3"])

    cursor.execute(f"SELECT Team FROM Gamer")
    my_team = cursor.fetchone()[0]
    ticket = (
        H_manager_ability
        + A_manager_ability
        + H3_f_abil
        + A3_f_abil
        + H3_m_abil
        + A3_m_abil
        + H4_d_abil
        + A4_d_abil
        + H1_k_abil
        + A1_k_abil
    )
    ticket //= 2
    ticket = ticket ** 7
    if my_team == Home:
        ticket *= 2
        if goal1 > goal2:
            ticket *= 3
        elif goal1 == goal2:
            ticket *= 2
    else:
        if goal1 < goal2:
            ticket *= 3
        elif goal1 == goal2:
            ticket *= 2
    money = team_money()
    money = (money[0] + money[1] + money[2]) // 20
    cursor.execute(
        f"UPDATE Gamer SET Money=Money+{(ticket//60000000000000000-money) + 2000}"
    )
    db.commit()
    return H_Team, A_Team, highlight, Home, Away


def match_money():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer")
    my_team = cursor.fetchone()[0]
    Home_Team_manager = team_manager_ability(my_team)
    if Home_Team_manager == None:
        H_manager_ability = 50
    else:
        H_manager_ability = int(Home_Team_manager[5])
    H_keeper = team_keeper_ability(my_team)
    H_defender = team_defender_ability(my_team)
    H_midfielder = team_midfielder_ability(my_team)
    H_forward = team_forward_ability(my_team)
    H1_k_abil = int(H_keeper[0][7])
    H4_d_abil = (
        int(H_defender[0][7])
        + int(H_defender[1][7])
        + int(H_defender[2][7])
        + int(H_defender[3][7])
    )
    H3_m_abil = (
        int(H_midfielder[0][7]) + int(H_midfielder[1][7]) + int(H_midfielder[2][7])
    )
    H3_f_abil = int(H_forward[0][7]) + int(H_forward[1][7]) + int(H_midfielder[2][7])
    ticket = H_manager_ability + H3_f_abil + H3_m_abil + H4_d_abil + H1_k_abil
    ticket = ticket ** 7
    ticket *= 3
    ticket *= 2
    return f"약 {(ticket//60000000000000000)+2000} 만원"


def team_money():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer")
    my_team = cursor.fetchone()[0]
    cursor.execute(f'SELECT Sum(Money) FROM Players Where Team =="{my_team}"')
    player_money = cursor.fetchone()[0]
    cursor.execute(f'SELECT Sum(Money) FROM Coaches Where Team =="{my_team}"')
    coach_money = cursor.fetchone()[0]
    cursor.execute(f'SELECT Sum(Money) FROM Staffs Where Team =="{my_team}"')
    staff_money = cursor.fetchone()[0]
    if player_money == None:
        player_money = 0
    if coach_money == None:
        coach_money = 0
    if staff_money == None:
        staff_money = 0
    return player_money, coach_money, staff_money


def play_simulation_game(Home, Away, db):
    Home_Team_manager = team_manager_ability(Home)
    Away_Team_manager = team_manager_ability(Away)
    Home_Team_players = team_ability(Home)
    Away_Team_players = team_ability(Away)
    if Home_Team_manager == None:
        Home_ability = 50
    else:
        Home_ability = int(Home_Team_manager[5])
    if Away_Team_manager == None:
        Away_ability = 50
    else:
        Away_ability = int(Away_Team_manager[5])
    Home_ability = 0
    Away_ability = 0
    for i in range(11):
        Home_ability += int(Home_Team_players[i][7])
        Away_ability += int(Away_Team_players[i][7])
    ran_goal = 10
    for i in range(3):
        ran_goal1 = random.randrange(0, 11)
        if ran_goal1 < ran_goal:
            ran_goal = ran_goal1
    if ran_goal == 0:
        ran_goal = random.randrange(0, 3)

    if Home_ability < Away_ability:
        minus_ability = Home_ability - 75
    else:
        minus_ability = Away_ability - 75
    Home_ability -= minus_ability
    Away_ability -= minus_ability
    Home_ability += 30

    H_goal = 0
    A_goal = 0
    for i in range(ran_goal):
        goal = random.randrange(0, Home_ability + Away_ability)
        if goal < Home_ability:
            H_goal += 1
        else:
            A_goal += 1
    # return f"{H_goal}:{A_goal}"
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE League_Calander SET result=(?) WHERE Home == (?) AND Away == (?)",
        (f"{H_goal}:{A_goal}", Home, Away),
    )
    db.commit()


def my_match_progress(sta, fin):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT Home, Away FROM League_Calander WHERE (Home==(?) OR Away==(?)) AND result==(?) ORDER BY Date",
        (my_team, my_team, "0"),
    )
    my_team_match = cursor.fetchone()
    result = play_my_game(my_team_match[0], my_team_match[1], db)
    make_thread = threading.Thread(target=lambda: other_match_progress(sta, fin))
    make_thread.daemon = True
    make_thread.start()
    return result


def simulate_last():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT count(*) FROM League_Calander WHERE result==(?) ORDER BY Date",
        ("0"),
    )
    result = cursor.fetchone()[0]
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    if result != 0:
        other_match_progress(1, 651)
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","리그 종료","","","" ,"리그가 모두 종료되었습니다.\n남은 잔여리그가 처리되고 있습니다 \n 다음 경기 진행시 새 시즌이 시작됩니다.")'
        cursor.execute(insert_query)
        db.commit()
    else:
        cursor.execute(f"DELETE FROM League_Calander")
        cursor.execute(f"DELETE FROM League_table")
        db.commit()
        make_calander(3)
        make_league_table(3)
        insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","새 시즌 시작","","","" ,"새 시즌이 다시 시작됩니다.\n지난 시즌보다 좋은 결과가 되길...")'
        cursor.execute(insert_query)
        db.commit()


def other_match_progress(sta, fin):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Home, Away FROM League_Calander WHERE Date>=(?) AND Date<=(?) AND result==(?)",
        (sta, fin, "0"),
    )
    li = cursor.fetchall()
    for i in range(len(li)):
        play_simulation_game(li[i][0], li[i][1], db)
    update_league_table()


def search_calander():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT * FROM League_Calander WHERE result==(?) AND (Home ==(?) or Away ==(?))",
        (
            "0",
            my_team,
            my_team,
        ),
    )
    try:
        fin = cursor.fetchone()[3]
        cursor.execute(
            f"SELECT * FROM League_Calander WHERE result==(?) Group By Date",
            ("0",),
        )
        sta = cursor.fetchone()[3]
        return [sta, fin]
    except:
        return 0


def one_position():
    db = sqlite3.connect(f"../../Database/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(
        f'UPDATE Players Set Position= "Defender" Where Position like "%Back" OR Position =="Defender"'
    )
    db.commit()
    cursor.execute(
        f'UPDATE Players Set Position= "Midfielder" Where Position like "%Midfield" OR Position == "Midfielder"'
    )
    db.commit()
    cursor.execute(
        f'UPDATE Players Set Position= "Forward" Where Position like "Second%" OR Position like "%Forward"'
    )
    db.commit()
    cursor.execute(f"SELECT * FROM Players Group by Position")


def make_league_table(num):
    db = sqlite3.connect(f"../../Database/FO_savefile{num}.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Teams")
    pla_list = cursor.fetchall()
    for i in range(len(pla_list)):
        insert_query = f'INSERT INTO League_table VALUES("{pla_list[i][0]}", "{pla_list[i][2]}", "{pla_list[i][1]}", "{pla_list[i][3]}","0","0","0","0","0","0","0","0")'
        cursor.execute(insert_query)
    db.commit()


def update_league_table():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM League_Calander WHERE upd ==(?) AND result != (?)", ("0", "0")
    )
    update_list = cursor.fetchall()
    for i in update_list:
        Seq = i[0]
        Country = i[1]
        League = i[2]
        Home = i[4]
        Away = i[5]
        result = i[6].split(":")

        cursor.execute(
            f"UPDATE League_Calander SET upd = (?) WHERE Seq ==(?)", ("1", Seq)
        )
        if int(result[0]) > int(result[1]):
            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Win=Win+1, Score=Score+{result[0]}, Conceded =Conceded+{result[1]}, GD = GD+{result[0]}-{result[1]}, Point =Point+3 WHERE Team = "{Home}"'
            )

            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Lose=Lose+1, Score=Score+{result[1]}, Conceded =Conceded+{result[0]}, GD = GD+({result[1]}-{result[0]}) WHERE Team = "{Away}"'
            )

        elif int(result[0]) == int(result[1]):
            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Draw=Draw+1, Score=Score+{result[0]}, Conceded =Conceded+{result[1]}, Point =Point+1 WHERE Team = "{Home}"'
            )

            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Draw=Draw+1, Score=Score+{result[1]}, Conceded =Conceded+{result[0]}, Point =Point+1 WHERE Team = "{Away}"'
            )

        else:
            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Win=Win+1, Score=Score+{result[1]}, Conceded =Conceded+{result[0]}, GD = GD+({result[1]}-{result[0]}), Point =Point+3 WHERE Team = "{Away}"'
            )

            cursor.execute(
                f'UPDATE League_table SET Match=Match+1, Lose=Lose+1, Score=Score+{result[0]}, Conceded =Conceded+{result[1]}, GD = GD+({result[0]}-{result[1]}) WHERE Team = "{Home}"'
            )
        db.commit()


def get_myteam_table():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Gamer")
    my_team = cursor.fetchone()
    cursor.execute(
        f"SELECT Country, League FROM League_table Where Team ==(?)", (my_team)
    )
    myCountry, myLeague = cursor.fetchone()
    cursor.execute(
        f"SELECT * FROM League_table Where Country ==(?) AND League ==(?) Order by Point DESC",
        (myCountry, myLeague),
    )
    return cursor.fetchall()


def get_EPL_table():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM League_table Where Country ==(?) AND League ==(?) Order by Point DESC",
        ("England", "Premier League"),
    )
    return cursor.fetchall()


def get_LaLiga_table():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM League_table Where Country ==(?) AND League ==(?) Order by Point DESC",
        ("Spain", "LaLiga"),
    )
    return cursor.fetchall()


def get_Bundes_table():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM League_table Where Country ==(?) AND League ==(?) Order by Point DESC",
        ("Germany", "Bundesliga"),
    )
    return cursor.fetchall()


def get_message_data():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Message_box Order by Seq DESC")
    messages = cursor.fetchall()
    return messages[0:5]


def check_gamer_team():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Gamer")
    player_team = cursor.fetchone()[1]
    if player_team == "무직":
        return False
    else:
        return True


def get_gamer_team():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Gamer")
    player_team = cursor.fetchone()
    return player_team


def msg_contact():
    team = get_gamer_team()[1]
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT * FROM Players WHERE Team=="{team}" AND Contract=="1" ORDER BY random()'
    )
    player = cursor.fetchone()
    if player == None:
        player = [0, "없음", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        mon1 = 0
    else:
        mon1 = player[9] + random.randint(0, int(player[9]) // 2)
    cursor.execute(
        f'SELECT * FROM Coaches WHERE Team=="{team}" AND Contract=="1" ORDER BY random()'
    )
    coach = cursor.fetchone()
    if coach == None:
        coach = [0, "없음", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        mon2 = 0
    else:
        mon2 = coach[6] + random.randint(0, int(coach[6]) // 2)
    cursor.execute(
        f'SELECT * FROM Staffs WHERE Team=="{team}" AND Contract=="1" ORDER BY random()'
    )
    staff = cursor.fetchone()
    if staff == None:
        staff = [0, "없음", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        mon3 = 0
    else:
        mon3 = staff[6] + random.randint(0, int(staff[6]) // 2)
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    con1 = random.randint(3, 6)
    con2 = random.randint(3, 6)
    con3 = random.randint(3, 6)
    insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","재계약 추천","{player[1]}","{coach[1]}","{staff[1]}" ,"다음은 계약이 1년 남은 선수, 코치, 스탭입니다.\
        \n다음과 같은 재계약을 추천합니다.\n\n <선수 {player[1]}> {mon1}만원 재계약 {con1}년 \n <코치 {coach[1]}> {mon2}만원 재계약 {con2}년 \n <스탭 {staff[1]}> {mon3}만원 재계약 {con3}년 \n\n 재계약 하려면 옆에 계약 버튼을 눌러주세요.")'
    cursor.execute(insert_query)
    db.commit()

    return [player[0], con1, mon1], [coach[0], con2, mon2], [staff[0], con3, mon3]


def do_contract(seq, con, mon, type):
    Warning_message = tkinter.messagebox.askokcancel("계약", "정말 재계약 하시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"../../Database/FO_savefile3.db")
        cursor = db.cursor()
        cursor.execute(
            f'UPDATE {type} SET Contract="{con}", Money="{mon}" WHERE Seq=="{seq}"'
        )
        db.commit()
        Save_message = tkinter.messagebox.showinfo("계약 완료", "재계약을 완료했습니다.")


def later(name):
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count(*) FROM Message_box")
    cnt = cursor.fetchone()[0]
    insert_query = f'INSERT INTO Message_box VALUES("{cnt+1}","{name}","","","" ,"죄송합니다\n Beta에서는 지원되지 않습니다.")'
    cursor.execute(insert_query)
    db.commit()


if __name__ == "__main__":
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f'UPDATE League_Calander SET result="0:0", upd="1" WHERE Date<=370')
    db.commit()
