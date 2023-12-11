import requests
from bs4 import BeautifulSoup
import sqlite3

###########################################################################################################
# 리그 가져오기
###########################################################################################################


def Get_Leauge():
    Con_URLs = []
    League_list = []
    Country_list = []
    Clubs_list = []
    Value_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    continents = [
        "europa",
        "europa/wettbewerbe?ajax=yw1&page=2",
        "europa/wettbewerbe?ajax=yw1&page=3",
        "europa/wettbewerbe?ajax=yw1&page=4",
        "asien",
        "asien/wettbewerbe?ajax=yw1&page=2",
        "amerika",
        "afrika",
    ]

    for continent in continents:
        Con_URLs.append(f"https://www.transfermarkt.com/wettbewerbe/{continent}")

    for Con_URL in Con_URLs:
        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, "html.parser")
        for League in Con_soup.find_all("table", {"class": "inline-table"}):
            if League.text[8:] == "3. Liga\n\n\n":
                break
            if League.text[8:] == "K3 League\n\n\n":
                break
            if League.text[8:] == "Série B\n\n\n":
                break
            if League.text[8:] == "Nedbank Cup\n\n\n":
                break
            League_list.append(League.text[8:])
        T = "".join(League_list)
        League_list = T.split("\n\n\n")
        League_list.pop(-1)
        i = 0
        for League in Con_soup.find_all("td", {"class": "zentriert"}):
            i = i + 1
            if i % 6 == 1:
                Country_list.append(League.find("img")["title"])
            elif i % 6 == 2:
                Clubs_list.append(League.text)
                if len(Clubs_list) == 99:
                    break
                if len(Clubs_list) == 132:
                    break
                if len(Clubs_list) == 155:
                    break
                if len(Clubs_list) == 162:
                    break

        for League in Con_soup.find_all("td", {"class": "rechts hauptlink"}):
            Value_list.append(League.text)
            if len(Value_list) == 99:
                break
            if len(Value_list) == 132:
                break
            if len(Value_list) == 155:
                break
            if len(Value_list) == 162:
                break

    db = sqlite3.connect("../Database/FO_datafile.db")
    cursor = db.cursor()
    for i in range(len(League_list)):
        insert_query = f'INSERT INTO Leagues VALUES("{League_list[i]}","{Country_list[i]}", "{Clubs_list[i]}","{Value_list[i]}")'
        cursor.execute(insert_query)
        db.commit()


###########################################################################################################
# 팀 가져오기
###########################################################################################################


def Get_Team():
    Con_URLs = []
    League_list = []
    Country_list = []
    Base_URLs = []
    First_URL = "https://www.transfermarkt.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    continents = [
        "europa",
        "europa/wettbewerbe?ajax=yw1&page=2",
        "europa/wettbewerbe?ajax=yw1&page=3",
        "europa/wettbewerbe?ajax=yw1&page=4",
        "asien",
        "asien/wettbewerbe?ajax=yw1&page=2",
        "amerika",
        "afrika",
    ]

    for continent in continents:
        Con_URLs.append(f"https://www.transfermarkt.com/wettbewerbe/{continent}")

    for Con_URL in Con_URLs:
        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, "html.parser")
        for League in Con_soup.find_all("table", {"class": "inline-table"}):
            if League.text[8:] == "3. Liga\n\n\n":
                break
            if League.text[8:] == "K3 League\n\n\n":
                break
            if League.text[8:] == "Série B\n\n\n":
                break
            if League.text[8:] == "Nedbank Cup\n\n\n":
                break
            League_list.append(League.text[8:])

        i = 0
        for League in Con_soup.find_all("td", {"class": "zentriert"}):
            i = i + 1
            if i % 6 == 1:
                Country_list.append(League.find("img")["title"])
                if len(Country_list) == 99:
                    break
                if len(Country_list) == 132:
                    break
                if len(Country_list) == 155:
                    break
                if len(Country_list) == 162:
                    break

        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, "html.parser")
        for href in Con_soup.find_all("table", {"class": "inline-table"}):
            League_URL = href.find_all("a")[1]["href"]
            if League_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
                break
            if (
                League_URL
                == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2"
            ):
                break
            if League_URL == "/k3-league/startseite/wettbewerb/K3L":
                break
            if League_URL == "/3-liga/startseite/wettbewerb/L3":
                break
            Base_URLs.append(First_URL + League_URL)

    T = "".join(League_list)
    League_list = T.split("\n\n\n")
    League_list.pop(-1)

    r = 0
    for Base_URL in Base_URLs:
        Base_html = requests.get(Base_URL, headers=headers).text
        Base_soup = BeautifulSoup(Base_html, "html.parser")
        Team_list = []
        Value_list = []
        Age_list = []
        for Team in Base_soup.find_all(
            "td", {"class": "hauptlink no-border-links hide-for-small hide-for-pad"}
        ):
            Teama = Team
            try:
                Teama = Team.text.replace("\xa0", "")
            except:
                pass
            Teama = Teama.rstrip()
            Team_list.append(Teama)

        for Value in Base_soup.find_all(
            "td", {"class": "rechts hide-for-small hide-for-pad"}
        ):
            Value_list.append(Value.text)
        for Age in Base_soup.find_all(
            "td", {"class": "zentriert hide-for-small hide-for-pad"}
        ):
            Age_list.append(Age.text)
        db = sqlite3.connect("../Database/FO_datafile.db")
        cursor = db.cursor()
        for i in range(len(Team_list)):
            try:
                insert_query = f'INSERT INTO Teams VALUES("{League_list[r]}","{Country_list[r]}", "{Team_list[i]}","{Value_list[i*2+2]}","{Age_list[i+1]}")'
                cursor.execute(insert_query)
                db.commit()
            except:
                insert_query = f'INSERT INTO Teams VALUES("{League_list[r]}","{Country_list[r]}", "{Team_list[i]}","","{Age_list[i+1]}")'
                cursor.execute(insert_query)
                db.commit()
        r = r + 1


###########################################################################################################
# 선수 가져오기
###########################################################################################################


def Get_Player():
    Base_URLs = []
    Con_URLs = []
    continents = [
        "europa",
        "europa/wettbewerbe?ajax=yw1&page=2",
        "europa/wettbewerbe?ajax=yw1&page=3",
        "europa/wettbewerbe?ajax=yw1&page=4",
        "asien",
        "asien/wettbewerbe?ajax=yw1&page=2",
        "amerika",
        "afrika",
    ]
    for continent in continents:
        Con_URLs.append(f"https://www.transfermarkt.com/wettbewerbe/{continent}")

    URLs = []
    First_URL = "https://www.transfermarkt.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    for Con_URL in Con_URLs:
        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, "html.parser")
        for href in Con_soup.find_all("table", {"class": "inline-table"}):
            Team_URL = href.find_all("a")[1]["href"]
            if Team_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
                break
            if Team_URL == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2":
                break
            if Team_URL == "/k3-league/startseite/wettbewerb/K3L":
                break
            if Team_URL == "/3-liga/startseite/wettbewerb/L3":
                break
            Base_URLs.append(First_URL + Team_URL)

    for Base_URL in Base_URLs:
        Base_html = requests.get(Base_URL, headers=headers).text
        Base_soup = BeautifulSoup(Base_html, "html.parser")
        for href in Base_soup.find_all(
            "td", class_="hauptlink no-border-links show-for-small show-for-pad"
        ):
            Team_URL = href.find("a")["href"]
            URLs.append(First_URL + Team_URL)

    for URL in URLs:
        html = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")

        Team_soup = soup.find("h1", {"itemprop": "name"})
        Team_name = Team_soup.text.strip()

        Player_list = []
        Player_soup = soup.find_all("span", {"class": "hide-for-small"})
        for Player in Player_soup:
            Player_list.append(Player.text)
        T = "!".join(Player_list)
        Player_list = T.split("!!")
        T = "!".join(Player_list)
        Player_list = T.split("!")
        if Player_list[0] == "":
            Player_list.pop(0)

        Player_num_list = []
        Player_num_soup = soup.find_all("div", {"class": "rn_nummer"})
        for Player_num in Player_num_soup:
            Player_num_list.append(Player_num.text)
        T = "-".join(Player_num_list)
        Player_num_list = T.split("--")
        T = "-".join(Player_num_list)
        Player_num_list = T.split("-")

        Player_soup_list1 = []
        Player_pos_list = []
        Player_pos_soup = soup.find_all("tr")
        for Player_pos in Player_pos_soup:
            Player_soup_list1.append(Player_pos.text)
        for i in range(len(Player_soup_list1)):
            if i % 6 == 4:
                Player_pos_list.append(Player_soup_list1[i])
            if i % 6 == 1:
                Player_pos_list.append(Player_soup_list1[i])
        a = len(Player_list) + 1
        Player_pos_list = Player_pos_list[1:a]

        Player_soup_list2 = []
        Player_age_list = []
        Player_age_soup = soup.find_all("td", {"class": "zentriert"})
        for Player_age in Player_age_soup:
            Player_soup_list2.append(Player_age.text)

        for i in range(len(Player_soup_list2)):
            if i % 3 == 1:
                Player_age_list.append(Player_soup_list2[i])
        a = len(Player_list)
        Player_age_list = Player_age_list[0:a]

        Player_value_list = []
        Player_value_soup = soup.find_all("td", {"class": "rechts hauptlink"})
        for Player_value in Player_value_soup:
            Player_value_list.append(Player_value.text)
        T = "".join(Player_value_list)
        Player_value_list = T.split("\xa0")
        T = "!".join(Player_value_list)
        T = T.replace("!!!!", "!!!!!!")
        Player_value_list = T.split("!!")
        T = "!".join(Player_value_list)
        Player_value_list = T.split("!")
        if len(Player_list) < len(Player_value_list):
            Player_value_list.pop(-1)

        db = sqlite3.connect("../Database/FO_datafile.db")
        cursor = db.cursor()
        for i in range(len(Player_list)):
            try:
                insert_query = f'INSERT INTO Players VALUES("{Player_list[i]}","{Team_name}", "{Player_num_list[i]}", "{Player_pos_list[i]}","{Player_age_list[i]}", "{Player_value_list[i]}")'
                cursor.execute(insert_query)
                db.commit()
            except:
                insert_query = f'INSERT INTO Players VALUES("{Player_list[i]}","{Team_name}", "{Player_num_list[i]}", "{Player_pos_list[i]}","{Player_age_list[i]}", "")'
                cursor.execute(insert_query)
                db.commit()


###########################################################################################################
# 스텝 가져오기
###########################################################################################################


def Get_Coach():
    Con_URLs = []
    Base_URLs = []
    URLs = []
    Team_Coach_URLs = []

    First_URL = "https://www.transfermarkt.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    continents = [
        "europa",
        "europa/wettbewerbe?ajax=yw1&page=2",
        "europa/wettbewerbe?ajax=yw1&page=3",
        "europa/wettbewerbe?ajax=yw1&page=4",
        "asien",
        "asien/wettbewerbe?ajax=yw1&page=2",
        "amerika",
        "afrika",
    ]

    db = sqlite3.connect(f"../Database/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Coach_Link")
    for i in range(2137):
        Team_Coach_URLs.append(cursor.fetchone()[0])

    # db = sqlite3.connect(f"../Database/FO_datafile.db")
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM Team_link")
    # for i in range(2216):
    #     URLs.append(cursor.fetchone()[0])

    # for continent in continents:
    #     Con_URLs.append(
    #         f'https://www.transfermarkt.com/wettbewerbe/{continent}')

    # for Con_URL in Con_URLs:
    #     Con_html = requests.get(Con_URL, headers=headers).text
    #     Con_soup = BeautifulSoup(Con_html, 'html.parser')
    #     for href in Con_soup.find_all("table", {"class": 'inline-table'}):
    #         Team_URL = href.find_all("a")[1]["href"]
    #         if Team_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
    #             break
    #         if Team_URL == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2":
    #             break
    #         if Team_URL == "/k3-league/startseite/wettbewerb/K3L":
    #             break
    #         if Team_URL == "/3-liga/startseite/wettbewerb/L3":
    #             break
    #         Base_URLs.append(First_URL+Team_URL)

    # for Base_URL in Base_URLs:
    #     Base_html = requests.get(Base_URL, headers=headers).text
    #     Base_soup = BeautifulSoup(Base_html, 'html.parser')
    #     for href in Base_soup.find_all("td", {"class": 'hauptlink no-border-links show-for-small show-for-pad'}):
    #         Team_URL = href.find("a")["href"]
    #         URLs.append(First_URL+Team_URL)

    # for URL in URLs:
    #     html = requests.get(URL, headers=headers).text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     for href in soup.find_all("div", {"class": 'c2action-footer bxPagerParent'}):
    #         Team_Coach_URL = href.find("a")["href"]
    #         if Team_Coach_URL[-4:] == '2019':
    #             continue
    #         if 'geruechte' in Team_Coach_URL:
    #             continue
    #         Team_Coach_URLs.append(First_URL+Team_Coach_URL)
    #         print(First_URL+Team_Coach_URL)
    #         db = sqlite3.connect("../Database/FO_datafile.db")
    #         cursor = db.cursor()
    #         insert_query = \
    #             f'INSERT INTO Coach_Link VALUES("{First_URL+Team_Coach_URL}")'
    #         cursor.execute(insert_query)
    #         db.commit()

    for URL in Team_Coach_URLs:
        html = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")
        Team = soup.find("h1", {"itemprop": "name"})
        Team_name = Team.text.strip()
        for coach in soup.find_all("tbody")[1:]:
            coach = coach.text.strip()
            coach_infos = coach.split("\n")
            coach_name_list = []
            coach_position_list = []
            coach_age_list = []
            i = 0
            for coach_info in coach_infos:
                if i % 22 == 0:
                    coach_name_list.append(coach_info.strip())
                if i % 22 == 3:
                    coach_position_list.append(coach_info)
                if i % 22 == 7:
                    coach_age_list.append(coach_info)
                i += 1

            for i in range(len(coach_name_list)):
                db = sqlite3.connect("../Database/FO_datafile.db")
                cursor = db.cursor()
                insert_query = f'INSERT INTO Staffs VALUES("{coach_name_list[i]}","{Team_name}","{coach_position_list[i]}","{coach_age_list[i]}")'
                cursor.execute(insert_query)
                db.commit()


########################################################################################
if __name__ == "__main__":
    Get_Coach()
