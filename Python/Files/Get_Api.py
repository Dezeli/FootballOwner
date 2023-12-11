import requests
from datetime import datetime
import sqlite3

API_KEY = "vt3RYmcPrf4zdoIQLYtV51cx58szBpFL10D757Bc"


###########################################################################
# 리그 API id 가져오기
###########################################################################
def get_league_id():
    r = requests.get(
        "https://data.football-api.com/v3/competitions?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
    )
    data = r.json()

    db = sqlite3.connect("../Database/FO_API_datafile_200705.db")
    cursor = db.cursor()

    for i in range(len(data)):
        leauge_data = data[i]
        leauge_id = leauge_data["id"]
        leauge_name = leauge_data["name"]
        leauge_region = leauge_data["region"]
        insert_query = f"INSERT INTO Leagues VALUES('{leauge_id}', '{leauge_name}', '{leauge_region}')"
        cursor.execute(insert_query)
        db.commit()


###########################################################################
# 팀 API id 가져오기
###########################################################################


def get_team_id():
    db = sqlite3.connect("../Database/FO_API_datafile_200705.db")
    cursor = db.cursor()
    leauge_id = 1163
    r = requests.get(
        f"https://data.football-api.com/v3/standings/{leauge_id}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
    )
    data = r.json()
    for i in range(len(data)):
        r = requests.get(
            f"https://data.football-api.com/v3/standings/{leauge_id}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
        )
        data = r.json()
        Team_data = data[i]

        Team_country = Team_data["country"]
        Team_id = Team_data["team_id"]
        Team_name = Team_data["team_name"]
        Team_form = Team_data["recent_form"]
        Team_position = Team_data["position"]
        Team_home_match = Team_data["home_gp"]
        Team_home_win = Team_data["home_w"]
        Team_home_draw = Team_data["home_d"]
        Team_home_lose = Team_data["home_l"]
        Team_home_goal = Team_data["home_gs"]
        Team_home_goal_lost = Team_data["home_ga"]
        Team_away_match = Team_data["away_gp"]
        Team_away_win = Team_data["away_w"]
        Team_away_draw = Team_data["away_d"]
        Team_away_lose = Team_data["away_l"]
        Team_away_goal = Team_data["away_gs"]
        Team_away_goal_lost = Team_data["away_ga"]
        Team_goal_dif = Team_data["gd"]
        Team_points = Team_data["points"]
        r = requests.get(
            f"https://data.football-api.com/v3/teams/{Team_id}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
        )
        data = r.json()[0]
        Team_stadium = data["venue_name"]
        Team_coach = data["coach_name"]
        insert_query = f'INSERT INTO China_Teams VALUES("{Team_country}", "{Team_id}", "{Team_name}","{Team_coach}", "{Team_form}", "{Team_position}", "{Team_home_match}",\
                                            "{Team_home_win}", "{Team_home_draw}", "{Team_home_lose}", "{Team_home_goal}", "{Team_home_goal_lost}",\
                                            "{Team_away_match}", "{Team_away_win}", "{Team_away_draw}", "{Team_away_lose}", "{Team_away_goal}",\
                                            "{Team_away_goal_lost}", "{Team_goal_dif}", "{Team_points}","{Team_stadium}")'
        cursor.execute(insert_query)
        db.commit()


###########################################################################
# 팀 API 정보 가져오기
###########################################################################


def get_team_data():
    db = sqlite3.connect("../Database/FO_API_datafile_200705.db")
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM SerieA_Teams")
    Team_range = cursor.fetchone()[0]
    Teams = []
    Teams_id = []

    cursor.execute("SELECT Team_name FROM SerieA_Teams ORDER BY Rank")
    for i in range(Team_range):
        Teams.append(cursor.fetchone()[0])

    cursor.execute("SELECT Team_id FROM SerieA_Teams")
    for i in range(Team_range):
        Teams_id.append(cursor.fetchone()[0])

    for i in range(Team_range):
        print(Teams[i])
        r = requests.get(
            f"https://data.football-api.com/v3/teams/{Teams_id[i]}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
        )
        player_datas = r.json()[0]["squad"]
        for j in range(len(player_datas)):

            data = player_datas[j]
            Player_id = data["id"]
            Player_name = data["name"]
            Player_number = data["number"]
            Player_age = data["age"]
            Player_position = data["position"]
            Player_injured = data["injured"]
            Player_minutes = data["minutes"]
            Player_appearences = data["appearences"]
            Player_goals = data["goals"]
            Player_assists = data["assists"]
            Player_yellowcards = data["yellowcards"]
            Player_yellowred = data["yellowred"]
            Player_redcards = data["redcards"]

            insert_query = f'INSERT INTO Players VALUES("{Teams[i]}",  "{Player_id}", "{Player_name}", "{Player_number}", "{Player_age}",\
                                                "{Player_position}", "{Player_injured}", "{Player_minutes}", "{Player_appearences}",\
                                                "{Player_goals}", "{Player_assists}", "{Player_yellowcards}", "{Player_yellowred}", "{Player_redcards}")'
            cursor.execute(insert_query)
            db.commit()


###########################################################################
# 팀 API 전술 정보 가져오기
###########################################################################
def get_team_statistics():
    db = sqlite3.connect("../Database/FO_API_datafile_200705.db")
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM Team_Datas")
    Team_range = cursor.fetchone()[0]
    Teams = []
    Teams_id = []

    cursor.execute("SELECT name FROM Team_Datas ORDER BY position")
    for i in range(Team_range):
        Teams.append(cursor.fetchone()[0])

    cursor.execute("SELECT id FROM Team_Datas")

    for i in range(Team_range):
        Teams_id.append(cursor.fetchone()[0])

    for i in range(16, Team_range):
        r = requests.get(
            f"https://data.football-api.com/v3/teams/{Teams_id[i]}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b"
        )
        data = r.json()[0]["statistics"]
        Player_id = data["avg_goals_per_game_scored_home"]
        Player_name = data["avg_goals_per_game_scored_away"]
        Player_number = data["avg_goals_per_game_conceded_home"]
        Player_age = data["avg_goals_per_game_conceded_away"]
        Player_position = data["scoring_minutes_0_15_pct"]
        Player_injured = data["scoring_minutes_15_30_pct"]
        Player_minutes = data["scoring_minutes_30_45_pct"]
        Player_appearences = data["scoring_minutes_45_60_pct"]
        Player_goals = data["scoring_minutes_60_75_pct"]
        Player_assists = data["scoring_minutes_75_90_pct"]

        insert_query = f"INSERT INTO Statistics VALUES('{Teams[i]}',  '{Player_id}', '{Player_name}', '{Player_number}', '{Player_age}',\
                                            '{Player_position}', '{Player_injured}', '{Player_minutes}', '{Player_appearences}',\
                                            '{Player_goals}', '{Player_assists}')"
        cursor.execute(insert_query)
        db.commit()
    # 예외 처리;;;
    # insert_query = \
    #     f"INSERT INTO Statistics VALUES('Everton',  '1.26', '1.18', '1', '1.93',\
    #                                         '15.5%', '5.4%', '12.6%', '15.3%',\
    #                                         '19.1%', '32.1%')"
    # cursor.execute(insert_query)
    # db.commit()


if __name__ == "__main__":
    get_team_data()
