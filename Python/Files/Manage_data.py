import sqlite3
import random
import names


def change_ages():
    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute("SELECT Seq, Age From Staffs")
    for i in range(56297):
        a = cursor.fetchone()
        Seq = a[0]
        Age = str(a[1])
        ran = random.randrange(30, 70)
        if len(Age) != 2:
            cursor1.execute(f"UPDATE Staffs SET Age='{ran}'  WHERE Seq == '{Seq}'")
            db.commit()


def change_values():
    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor1.execute(f'UPDATE Leagues SET Value="0"')
    db.commit()
    # cursor.execute(
    #     "SELECT Seq, Age, Ability, Potential From Players")
    # for i in range(56297):
    #     a = cursor.fetchone()
    #     Seq = a[0]
    #     Age = int(a[1])
    #     Ability = int(a[2])
    #     Potential = int(a[3])
    #     Value = int(((Ability-Age+10)**3) *
    #                 ((Ability-45)**3)*(Potential**2)/20000000)
    #     cursor1.execute(
    #         f"UPDATE Players SET Market_Value='{Value}'  WHERE Seq == '{Seq}'")
    #     db.commit()

    # cursor.execute(
    #     "SELECT Team, sum(Market_Value) Value FROM Players GROUP By Team")
    # for i in range(2093):
    #     a = cursor.fetchone()
    #     Team = a[0]
    #     Value = a[1]
    #     print(Team, Value)
    #     cursor1.execute(
    #         f'UPDATE Teams SET Value="{Value}" WHERE Team=="{Team}"')
    #     db.commit()

    cursor.execute("SELECT League,Country, sum(Value) Value FROM Teams GROUP By League")
    for i in range(2093):
        a = cursor.fetchone()
        League = a[0]
        Country = a[1]
        Value = a[2]
        cursor1.execute(
            f'UPDATE Leagues SET Value="{Value}" WHERE Name=="{League}" AND Country=="{Country}"'
        )
        db.commit()


# SELECT Team, sum(Market_Value) Value
# FROM Players
# GROUP By Team
# ORDER By Value
# ;


def delete_same():
    name = []
    team = []
    number = []
    position = []
    age = []
    market_value = []

    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM(SELECT Name, Team, Position, Age, Count(*) Cnt	FROM Staffs GROUP by Name, Team) WHERE Cnt>1"
    )
    for i in range(176):
        a = cursor.fetchone()
        name.append(a[0])
        team.append(a[1])
        position.append(a[2])
        age.append(a[3])
    for i in range(176):
        cursor.execute(
            f'DELETE FROM Staffs WHERE Name=="{name[i]}" and Team=="{team[i]}" and Age=="{age[i]}"'
        )
        db.commit()
    for i in range(176):
        insert_query = f'INSERT INTO Staffs VALUES("","{name[i]}", "{team[i]}","{position[i]}","{age[i]}")'
        cursor.execute(insert_query)
        db.commit()


def make_ablity():
    Ability_data = []
    Value_data = []

    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    # cursor.execute(
    #     f"UPDATE Players SET Ability='0'")
    # db.commit()
    cursor.execute("SELECT Market_Value From Players Group BY Market_Value")
    for i in range(116):
        a = cursor.fetchone()[0][1:-2]
        Value_data.append(a)
    for i in Value_data:
        i = float(i)
        if i == 0:
            Ability_data.append(52)
        elif 1 <= i < 2:
            Ability_data.append(55)
        elif 2 <= i < 3:
            Ability_data.append(57)
        elif 3 <= i < 4:
            Ability_data.append(60)
        elif 4 <= i < 5:
            Ability_data.append(63)
        elif 5 <= i < 8:
            Ability_data.append(65)
        elif 8 <= i < 12:
            Ability_data.append(67)
        elif 12 <= i < 20:
            Ability_data.append(69)
        elif 20 <= i < 25:
            Ability_data.append(71)
        elif 25 <= i < 30:
            Ability_data.append(74)
        elif 30 <= i < 40:
            Ability_data.append(77)
        elif 40 <= i < 50:
            Ability_data.append(80)
        elif 50 <= i < 60:
            Ability_data.append(83)
        elif 60 <= i < 70:
            Ability_data.append(85)
        elif 70 <= i < 80:
            Ability_data.append(86)
        elif 80 <= i < 100:
            Ability_data.append(87)
        elif 100 <= i < 120:
            Ability_data.append(88)
        elif 120 <= i <= 140:
            Ability_data.append(89)
        elif 140 <= i <= 180:
            Ability_data.append(90)
    for i in range(26, 31):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-23+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'"
            )
            db.commit()
    for i in range(31, 36):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-26+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'"
            )
            db.commit()
    for i in range(36, 55):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{56-i+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'"
            )
            db.commit()
    for i in range(22, 26):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{27-i+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'"
            )
            db.commit()
    for i in range(14, 22):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{25-i+Ability_data[r]-7}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'"
            )
            db.commit()


def make_potential():
    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute("SELECT Seq, Age, Ability, Market_Value From Players")
    for i in range(56297):
        a = cursor.fetchone()
        Seq = a[0]
        Age = int(a[1])
        Ability = int(a[2])
        potential = Ability
        if 31 <= Age:
            ranpot = random.randrange(Ability, Ability + 2)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability + 2)
            if potential < ranpot:
                potential = ranpot
        elif 28 <= Age < 31:
            ranpot = random.randrange(Ability, Ability + 3)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability + 3)
            if potential < ranpot:
                potential = ranpot
        elif 25 <= Age < 28:
            ranpot = random.randrange(Ability, Ability + 4)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability + 4)
            if potential < ranpot:
                potential = ranpot
        elif 22 <= Age < 25:
            ranpot = random.randrange(Ability, 94)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, 94)
            if potential < ranpot:
                potential = ranpot
        else:
            ranpot = random.randrange(Ability, 96)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, 96)
            if potential < ranpot:
                potential = ranpot

        cursor1.execute(
            f"UPDATE Players SET Potential='{potential}'  WHERE Seq == '{Seq}'"
        )
        db.commit()


def make_staff_ability():
    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute("SELECT Team FROM Teams Order By Value")
    rank = {}
    for i in range(2203):
        a = cursor.fetchone()
        Team = a[0]
        Value = i + 1
        if Value <= 1000:
            Value = 1000
        rank[Team] = Value

    # for key in rank:
    #     cursor1.execute(
    #         f'UPDATE Staffs SET Ability="1"  WHERE Team == "{key}"')
    #     db.commit()
    cursor.execute("SELECT Seq, Team FROM Staffs")
    for i in range(6552):
        a = cursor.fetchone()
        Seq = a[0]
        Team = a[1]
        ability = 93
        while True:
            ranpot = random.randrange(30000)
            if rank[Team] <= ranpot:
                ability -= 1
            else:
                break
        if ability < 20:
            ability = random.randrange(20, 40)
        cursor1.execute(f"UPDATE Staffs SET Ability='{ability}'  WHERE Seq == '{Seq}'")
        db.commit()


def make_money():
    db = sqlite3.connect(f"../../Database/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    # cursor.execute(
    #     "SELECT Seq,Position,Age,Ability FROM Staffs")
    # for i in range(6552):
    #     a = cursor.fetchone()
    #     Seq = int(a[0])
    #     Position = str(a[1])
    #     Age = 50 - int(a[2])
    #     if Age < 0:
    #         Age = -Age
    #     Age = 55 - Age
    #     Ability = int(a[3])
    #     money = Age*Ability
    #     if Position == 'Owner':
    #         money = 0
    #     if Seq < 500:
    #         money = money*2
    #     cursor1.execute(
    #         f'UPDATE Staffs Set Money="{int(money/8)}" Where Seq=="{Seq}"')
    #     db.commit()
    cursor.execute("SELECT Seq,Age,Ability,Potential,Position FROM Players")
    for i in range(56297):
        a = cursor.fetchone()
        Seq = a[0]
        Age = int(a[1])
        if Age >= 35:
            Age = 35
        Ability = int(a[2])
        Potential = int(a[3])
        Position = str(a[4])
        money = Age * Ability * Potential / 5
        if Position == "Goalkeeper":
            money = money * 4 / 5
        if Ability < 70:
            money = money / 2
        if Ability < 65:
            money = money / 3
        if Ability < 60:
            money = money / 4
        if Ability < 55:
            money = money / 5
        if Ability < 50:
            money = money / 6
        cursor1.execute(f'UPDATE Players Set Money="{int(money)}" Where Seq=="{Seq}"')
        db.commit()


def make_contract():
    db = sqlite3.connect(f"../../Database/FO_datafile.db")
    cursor = db.cursor()
    for i in range(56297):
        contract = random.randrange(1, 6)
        cursor.execute(
            f'UPDATE Coaches Set Contract="{int(contract)}" Where Seq=="{i+1}"'
        )
        db.commit()


def no_injury():
    db = sqlite3.connect(f"../../Database/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE Players SET Injury ='0'")
    db.commit()
    return 0


def missed_leagues():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    data_db = sqlite3.connect(f"../../Database/FO_datafile.db")
    d_cursor = data_db.cursor()
    cursor.execute(
        f"SELECT League, Country, sum(Value), count(*) From Teams Group By League"
    )
    lost = []
    seq = 142
    for i in range(12):
        lost.append(cursor.fetchone())
    for i in range(12):
        d_cursor.execute(
            f'INSERT INTO Leagues VALUES("{seq+i}", "{lost[i][0]}", "{lost[i][1]}","{lost[i][3]}","{lost[i][2]}")'
        )
        data_db.commit()


def make_row_num():
    db = sqlite3.connect(f"../../Database/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Coaches")
    row_list = cursor.fetchall()
    for i in range(len(row_list)):
        a = row_list[i]
        Name = a[1]
        Team = a[2]
        Position = a[3]
        Money = a[6]

        cursor.execute(
            f'UPDATE Coaches SET Seq = {i+1} Where Name = "{Name}" AND Team = "{Team}" AND Position = "{Position}" AND Money = "{Money}"'
        )
        db.commit()


def missed_players():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team, Name From Player_Stat")
    lost = []
    for i in range(53516):
        lost.append(cursor.fetchone())
    for i in range(53516):
        cursor.execute(
            f'DELETE FROM Players WHERE Team = "{lost[i][0]}" AND Name = "{lost[i][1]}"'
        )
        db.commit()

    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    data_db = sqlite3.connect(f"../../Database/FO_datafile.db")
    d_cursor = data_db.cursor()
    cursor.execute(f"SELECT Team From Players Group By Team")
    lost = []
    for i in range(105):
        lost.append(cursor.fetchone()[0])
    for i in range(105):
        d_cursor.execute(f'DELETE FROM Players WHERE Team =="{lost[i]}"')
        data_db.commit()


def del_ghost_team():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team From Players GROUP BY Team")
    a = cursor.fetchall()
    for i in range(len(a)):
        cursor.execute(f'DELETE FROM Teams WHERE Team = "{a[i][0]}"')
        db.commit()
    cursor.execute(f"SELECT Team From Teams")
    b = cursor.fetchall()
    db = sqlite3.connect(f"../../Database/FO_datafile.db")
    cursor = db.cursor()
    for i in range(len(b)):
        cursor.execute(f'DELETE FROM Teams WHERE Team = "{b[i][0]}"')
        db.commit()


def make_player_data():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT Team FROM Teams")
    teams = cursor.fetchall()
    for team in teams:
        team = str(team[0])
        cursor.execute(
            f"SELECT Count(*) FROM Players WHERE Team ==(?) AND Position ==(?) AND Injury ==(?)",
            (team, "Goalkeeper", 0),
        )
        goalkeeper_cnt = cursor.fetchone()[0]
        if goalkeeper_cnt < 4:
            for i in range(4 - goalkeeper_cnt):
                make_new_player(team, "Goalkeeper")
        cursor.execute(
            f"SELECT Count(*) FROM Players WHERE Team ==(?) AND Position ==(?) AND Injury ==(?)",
            (team, "Defender", 0),
        )
        defender_cnt = cursor.fetchone()[0]
        if defender_cnt < 6:
            for i in range(6 - defender_cnt):
                make_new_player(team, "Defender")
        cursor.execute(
            f"SELECT Count(*) FROM Players WHERE Team ==(?) AND Position ==(?) AND Injury ==(?)",
            (team, "Midfielder", 0),
        )
        midfielder_cnt = cursor.fetchone()[0]
        if midfielder_cnt < 6:
            for i in range(6 - midfielder_cnt):
                make_new_player(team, "Midfielder")
        cursor.execute(
            f"SELECT Count(*) FROM Players WHERE Team ==(?) AND Position ==(?) AND Injury ==(?)",
            (team, "Forward", 0),
        )
        forward_cnt = cursor.fetchone()[0]
        if forward_cnt < 5:
            for i in range(5 - forward_cnt):
                make_new_player(team, "Forward")


def make_new_player(team, position):
    ran_name = str(names.get_full_name(gender="male"))
    position = str(position)
    seq = get_player_seq()
    ran_age = random.randint(21, 33)
    ran_ability = random.randint(49, 63)
    ran_potential = random.randint(ran_ability, 68)
    money = ran_age * ran_ability * ran_potential / 5
    contract = random.randint(1, 6)
    if position == "Goalkeeper":
        money = money * 4 / 5
    if ran_ability < 70:
        money = money / 2
    if ran_ability < 65:
        money = money / 3
    if ran_ability < 60:
        money = money / 4
    if ran_ability < 55:
        money = money / 5
    if ran_ability < 50:
        money = money / 6
    money = int(money)
    Value = int(
        ((ran_ability - ran_age + 10) ** 3)
        * ((ran_ability - 45) ** 3)
        * (ran_potential ** 2)
        / 20000000
    )
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'INSERT INTO Players VALUES("{seq+1}", "{ran_name}", "{team}","0", "{position}","{ran_age}", "{Value}", "{ran_ability}", "{ran_potential}", "{money}", "{contract}", "0")'
    )
    db.commit()


def get_player_seq():
    db = sqlite3.connect(f"../../Database/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count(*) FROM Players")
    players = cursor.fetchone()[0]
    return int(players)
