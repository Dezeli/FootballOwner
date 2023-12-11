from Make_label import Get_label
from Use_data import *
from Manage_data import *
from tkinter import *
import time
import random
from tkinter import messagebox
import threading
import os

img_path = os.path.join(os.getcwd())


class Screen:
    def __init__(self, Gui):
        self.Gui = Gui
        self.Menu_Screen()

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()

    def no_action(self):
        pass

    def destroy(self):
        list1 = self.Gui.Gui.place_slaves()
        for l in list1:
            l.destroy()

    ############################################################
    # 첫 메뉴 화면
    ############################################################
    def Menu_Screen(self):
        Menu_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Title_Screen_bg.png"), 0, 0
        )
        Game_Start_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Game_Start_btn.png"),
            20,
            350,
            self.loadfiles_Screen,
        )
        HowToPlay_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/HowToPlay_btn.png"),
            20,
            450,
            self.HowToPlay_Screen,
        )
        Settings_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Settings_btn.png"),
            20,
            550,
            self.Incomplete_Screen,
        )
        Exit_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Exit_btn.png"),
            20,
            650,
            self._quit,
        )
        Version_label = Label(
            self.Gui.Gui,
            text="Version 1.0 BETA",
            fg="yellow",
            bg="purple",
            font=("맑은 고딕", 12),
            height=1,
        )
        self.contract_data = 0
        Version_label.place(x=1050, y=5)

    ############################################################
    # 미완성 화면
    ############################################################
    def Incomplete_Screen(self):
        self.destroy()
        Incomplete_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Incomplete_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Return_btn.png"),
            920,
            10,
            self.Menu_Screen,
        )
        reset_datas_btn = Button(
            self.Gui.Gui,
            text="세이브 파일 리셋하기",
            bg="yellowgreen",
            fg="blue",
            font=("맑은 고딕", 45),
            command=reset_datas,
        )
        reset_datas_btn.place(x=10, y=10)

    def Loading_Screen(self, thread):
        self.destroy()

        def loading(num, thread):

            if num == 9:
                num = 1
            if thread.is_alive() == False:
                self.Main_Screen()
                return 0
            Loading_Screen_background = Get_label.image_label(
                self.Gui, os.path.join(img_path, f"../../Images/로딩{num}.png"), 0, 0
            )
            Loading_Screen_background.after(200, lambda: loading(num + 1, thread))

        loading(1, thread)

    def cant_use_Screen(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/cantuse_bg.png"), 0, 0
        )
        game_button = self.game_buttons()

    ############################################################
    # 설명 화면
    ############################################################
    def HowToPlay_Screen(self):
        self.destroy()
        HowToPlay_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/HowToPlay_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Return_btn.png"),
            920,
            10,
            self.Menu_Screen,
        )

    ############################################################
    # 세이브 화면
    ############################################################

    def Savefiles_Screen(self):
        self.destroy()
        time_save = time_auto_save()

        def save1():
            save = Save1_data()
            MainScreen = self.Main_Screen()

        def save2():
            save = Save2_data()
            MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Savefiles_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Return_btn.png"),
            885,
            44,
            self.Main_Screen,
        )
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                198,
                save1,
                f"+",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            first_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                198,
                save1,
                f"☆ 구단주 이름 : {Save_check1[0]}     ☆ 현재 자금 : {Save_check1[3]}만원\n☆ 소속 팀 : {Save_check1[1]}\n☆ 저장 날짜 : {Save_check1[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )
        if Save_check2 == None:
            second_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                398,
                save2,
                f"+",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            second_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                398,
                save2,
                f"☆ 구단주 이름 : {Save_check2[0]}     ☆ 현재 자금 : {Save_check2[3]}만원\n☆ 소속 팀 : {Save_check2[1]}\n☆ 저장 날짜 : {Save_check2[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )
        if Save_check3 == None:
            third_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                598,
                self.no_action,
                f"자동 저장 된 정보가 없습니다",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            third_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                82,
                598,
                self.no_action,
                f"☆ 구단주 이름 : {Save_check3[0]}     ☆ 현재 자금 : {Save_check3[3]}만원\n☆ 소속 팀 : {Save_check3[1]}\n☆ 저장 날짜 : {Save_check3[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )

    ############################################################
    # 불러오기 화면
    ############################################################
    def loadfiles_Screen(self):
        self.destroy()
        time_save = time_auto_save()

        def load1():
            load = load1_data()
            MainScreen = self.Main_Screen()

        def load2():
            load = load2_data()
            MainScreen = self.Main_Screen()

        def first():
            name_save = input_Names1()
            if name_save != "No":
                data = Auto_save_get_data(1)
                load = load1_data()
                MainScreen = self.Main_Screen()

        def second():
            name_save = input_Names2()
            if name_save != "No":
                data = Auto_save_get_data(2)
                load = load2_data()
                MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Loadfiles_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/Return_btn.png"),
            45,
            44,
            self.Menu_Screen,
        )
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                198,
                first,
                f"+",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            first_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                198,
                load1,
                f"☆ 구단주 이름 : {Save_check1[0]}     ☆ 현재 자금 : {Save_check1[3]}만원\n☆ 소속 팀 : {Save_check1[1]}\n☆ 저장 날짜 : {Save_check1[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )
        if Save_check2 == None:
            second_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                398,
                second,
                f"+",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            second_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                398,
                load2,
                f"☆ 구단주 이름 : {Save_check2[0]}     ☆ 현재 자금 : {Save_check2[3]}만원\n☆ 소속 팀 : {Save_check2[1]}\n☆ 저장 날짜 : {Save_check2[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )
        if Save_check3 == None:
            third_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                598,
                self.no_action,
                f"자동 저장 된 정보가 없습니다",
                "#407F7F",
                ("1훈떡볶이 Regular", 26),
            )
        else:
            third_save_btn = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Save_label.png"),
                395,
                598,
                self.Main_Screen,
                f"☆ 구단주 이름 : {Save_check3[0]}     ☆ 현재 자금 : {Save_check3[3]}만원\n☆ 소속 팀 : {Save_check3[1]}\n☆ 저장 날짜 : {Save_check3[2]}",
                "#407F7F",
                ("1훈떡볶이 Regular", 24),
            )

    ############################################################
    # 메인 게임 화면
    ############################################################

    def Main_Screen(self):
        self.destroy()
        Menu_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        self.game_buttons()
        self.message()

    def game_buttons(self):
        Logo_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/logo_btn.png"),
            31,
            33,
            self.logo_com,
        )
        Save_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/save_btn.png"),
            121,
            33,
            self.Savefiles_Screen,
        )
        if check_gamer_team() == False:
            Go_button = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/go_btn.png"),
                1090,
                33,
                self.no_action,
            )
        else:
            Go_button = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/go_btn.png"),
                1090,
                33,
                self.continue_btn,
            )
        self.menu1_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu1.png"),
            34,
            140,
            self.message,
        )
        if check_gamer_team() == False:
            self.menu2_button = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/menu2.png"),
                34,
                210,
                lambda: self.cant_use_Screen(),
            )
        else:
            self.menu2_button = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/menu2.png"),
                34,
                210,
                lambda: self.situation(0, 10, get_myteam_table()),
            )
        self.menu3_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu3.png"),
            34,
            280,
            self.acquisition,
        )
        self.menu4_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu4.png"),
            34,
            350,
            self.financial,
        )
        self.menu5_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu5.png"),
            34,
            420,
            self.Team_Player_Screen,
        )
        self.menu6_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu6.png"),
            34,
            490,
            self.Team_Coach_Screen,
        )
        self.menu7_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu7.png"),
            34,
            560,
            self.Team_Staff_Screen,
        )
        self.menu8_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu8.png"),
            34,
            630,
            self.cant_use_Screen,
        )
        self.menu9_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/menu9.png"),
            34,
            700,
            self.cant_use_Screen,
        )

    def logo_com(self):
        time_save = time_auto_save()
        answer = messagebox.askyesno("확인", "정말 메인화면으로 돌아가시겠습니까?")
        if answer == True:
            screen = self.Menu_Screen()

    ############################################################
    # 게임 진행 버튼
    ############################################################

    def continue_btn(self):
        event = random.randrange(0, 100)
        if event < 20:
            self.match_play()
        elif 20 <= event < 25:
            self.injury()
        elif 25 <= event < 35:
            self.buy_player()
        elif 35 <= event < 45:
            self.sell_player()
        elif 45 <= event < 47:
            self.sell_team()
        elif 47 <= event < 67:
            self.secretary()
        elif 67 <= event < 77:
            self.contract()
        elif 77 <= event < 90:
            self.ability_change()
        elif 90 <= event < 95:
            self.fan_res()
        elif 95 <= event < 100:
            self.player_res()

    def match_play(self):
        Match_Play_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/simulation_bg.png"), 0, 0
        )
        next_match = search_calander()
        if next_match != 0:
            self.result = my_match_progress(next_match[0], next_match[1])
            self.team_squad("Home")
            self.team_squad("Away")
            self.home_score = 0
            self.away_score = 0
            self.match_result(0)
        else:
            simulate_last()
            self.Main_Screen()

    def team_squad(self, pos):
        if pos == "Home":
            team = 0
            x = 49
            scorex = 295

        elif pos == "Away":
            team = 1
            x = 928
            scorex = 810

        Team_label = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, f"../../Images/{pos}_name.png"),
            x,
            67,
            f"{self.result[team+3]}",
            "#0051C9",
            ("1훈떡볶이 Regular", 14),
        )
        Score_label = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, f"../../Images/{pos}_score.png"),
            scorex,
            60,
            f"0",
            "#0051C9",
            ("1훈떡볶이 Regular", 20),
        )
        if self.result[team][-1] == None:
            coach_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach.png"),
                x,
                152,
                f"No Coach",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )
        else:
            coach_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach.png"),
                x,
                152,
                f"{self.result[team][-1][1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )
        for i in range(1):
            player_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player.png"),
                x,
                152 + ((i + 1) * 49),
                f"{self.result[team][0][i][1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )
        for i in range(4):
            player_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player.png"),
                x,
                152 + ((i + 2) * 49),
                f"{self.result[team][1][i][1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )
        for i in range(3):
            player_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player.png"),
                x,
                152 + ((i + 6) * 49),
                f"{self.result[team][2][i][1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )
        for i in range(3):
            player_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player.png"),
                x,
                152 + ((i + 9) * 49),
                f"{self.result[team][3][i][1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 12),
            )

    def match_result(self, num):
        locnum = num % 10
        if self.result[2][num][1][-1] == "1":
            match_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Home_hi.png"),
                320,
                152 + (locnum * 59),
                f"{self.result[2][num][0]}",
                "#9563E0",
                ("1훈떡볶이 Regular", 14),
            )
            if self.result[2][num][1][0] == "골":
                self.home_score += 1
                Score_label = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, f"../../Images/Home_score.png"),
                    295,
                    60,
                    f"{self.home_score}",
                    "#ed1c24",
                    ("1훈떡볶이 Regular", 20),
                )
            elif self.result[2][num][1][0] == "ㄴ":
                self.home_score -= 1
                Score_label = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, f"../../Images/Home_score.png"),
                    295,
                    60,
                    f"{self.home_score}",
                    "#ed1c24",
                    ("1훈떡볶이 Regular", 20),
                )
        elif self.result[2][num][1][-1] == "2":
            match_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/Away_hi.png"),
                320,
                152 + (locnum * 59),
                f"{self.result[2][num][0]}",
                "#DAE3D6",
                ("1훈떡볶이 Regular", 14),
            )
            if self.result[2][num][1][0] == "골":
                self.away_score += 1
                Score_label = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, f"../../Images/Away_score.png"),
                    810,
                    60,
                    f"{self.away_score}",
                    "#ed1c24",
                    ("1훈떡볶이 Regular", 20),
                )
            elif self.result[2][num][1][0] == "ㄴ":
                self.away_score -= 1
                Score_label = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, f"../../Images/Away_score.png"),
                    810,
                    60,
                    f"{self.away_score}",
                    "#ed1c24",
                    ("1훈떡볶이 Regular", 20),
                )
        if self.result[2][num][1][-1] == "3":
            match_label = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/hi.png"),
                320,
                152 + (locnum * 59),
                f"{self.result[2][num][0]}",
                "#E07988",
                ("1훈떡볶이 Regular", 14),
            )
        if locnum != 9:
            match_label_reset = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/hi.png"),
                320,
                152 + ((locnum + 1) * 59),
                f"",
                "#E07988",
                ("1훈떡볶이 Regular", 10),
            )
        if num < len(self.result[2]) - 1:
            match_label.after(1000, lambda: self.match_result(num + 1))
        else:
            match_label.after(5000, lambda: self.Main_Screen())

    def injury(self):
        get_injury()
        make_thread = threading.Thread(target=make_player_data)
        make_thread.daemon = True
        make_thread.start()
        self.Main_Screen()

    def buy_player(self):
        later("선수 영입")
        self.Main_Screen()

    def sell_player(self):
        later("선수 판매")
        self.Main_Screen()

    def sell_team(self):
        later("구단 매각")
        self.Main_Screen()

    def secretary(self):
        later("비서")
        self.Main_Screen()

    def contract(self):
        self.contract_data = msg_contact()
        self.Main_Screen()

    def ability_change(self):
        ability_ran_change()
        self.Main_Screen()

    def fan_res(self):
        fan_msg_res()
        self.Main_Screen()

    def player_res(self):
        pla_msg_Res()
        self.Main_Screen()

    ############################################################
    # 메세지 화면
    ############################################################
    def message(self):
        self.destroy()
        Menu_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_btn = self.game_buttons()
        check_mon = check_money()
        if check_mon == "-":
            self.menu1_button.config(state="disabled")
            self.menu2_button.config(state="disabled")
            self.menu3_button.config(state="disabled")
            self.menu4_button.config(state="disabled")
            self.menu5_button.config(state="disabled")
            self.menu6_button.config(state="disabled")
            self.menu7_button.config(state="disabled")
            self.menu8_button.config(state="disabled")
            self.menu9_button.config(state="disabled")
            self.get_first_money()
        else:
            Message_Screen_background = Get_label.image_label(
                self.Gui,
                os.path.join(img_path, "../../Images/message_box_bg.png"),
                0,
                0,
            )
            self.game_buttons()
            data = get_message_data()
            message_notice1 = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/message_notice_btn.png"),
                219,
                130,
                lambda: self.message_content(0),
                f"{data[0][1]}\n{data[0][2]}\n{data[0][3]}\n{data[0][4]}",
                "#564AF7",
                ("타이포_헬로피오피 테두리B", 15),
            )
            message_notice2 = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/message_notice_btn.png"),
                219,
                260,
                lambda: self.message_content(1),
                f"{data[1][1]}\n{data[1][2]}\n{data[1][3]}\n{data[1][4]} ",
                "#564AF7",
                ("타이포_헬로피오피 테두리B", 15),
            )
            message_notice3 = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/message_notice_btn.png"),
                219,
                390,
                lambda: self.message_content(2),
                f"{data[2][1]}\n{data[2][2]}\n{data[2][3]}\n{data[2][4]}",
                "#564AF7",
                ("타이포_헬로피오피 테두리B", 15),
            )
            message_notice4 = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/message_notice_btn.png"),
                219,
                520,
                lambda: self.message_content(3),
                f"{data[3][1]}\n{data[3][2]}\n{data[3][3]}\n{data[3][4]}",
                "#564AF7",
                ("타이포_헬로피오피 테두리B", 15),
            )
            message_notice5 = Get_label.image_button_text(
                self.Gui,
                os.path.join(img_path, "../../Images/message_notice_btn.png"),
                219,
                650,
                lambda: self.message_content(4),
                f"{data[4][1]}\n{data[4][2]}\n{data[4][3]}\n{data[4][4]}",
                "#564AF7",
                ("타이포_헬로피오피 테두리B", 15),
            )

    def message_content(self, num):
        data = get_message_data()
        msg_content1 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/msg1.png"),
            460,
            135,
            f"{data[num][1]}\n{data[num][2]}\n{data[num][3]}\n{data[num][4]}",
            "#003D35",
            ("타이포_헬로피오피 테두리B", 18),
        )
        content = data[num][5]
        con_list = content.split("\\n")
        for i in range(10):
            con_list.append("")
        msg_content1 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/msg2.png"),
            460,
            315,
            f"{con_list[0]}\n{con_list[1]}\n{con_list[2]}\n{con_list[3]}",
            "#003D35",
            ("1훈떡볶이 Regular", 18),
        )
        if data[num][1] == "재계약 추천" and num == 0 and self.contract_data != 0:
            contract_label1 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/contract.png"),
                1022,
                150 + (50 * 0),
                lambda: do_contract(
                    self.contract_data[0][0],
                    self.contract_data[0][1],
                    self.contract_data[0][2],
                    "Players",
                ),
            )
            contract_label2 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/contract.png"),
                1022,
                150 + (50 * 1),
                lambda: do_contract(
                    self.contract_data[1][0],
                    self.contract_data[1][1],
                    self.contract_data[1][2],
                    "Coaches",
                ),
            )
            contract_label3 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/contract.png"),
                1022,
                150 + (50 * 2),
                lambda: do_contract(
                    self.contract_data[2][0],
                    self.contract_data[2][1],
                    self.contract_data[2][2],
                    "Staffs",
                ),
            )

    ############################################################
    # 미니게임 화면
    ############################################################
    def get_first_money(self):
        self.money = 10000
        self.win = 0
        Name = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Name_Tag.png"), 250, 40
        )
        Intro1 = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/intro1.png"), 245, 170
        )
        Intro2 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/intro2.png"),
            250,
            345,
            f"                {self.win}번",
            "#ed1c24",
            ("1훈떡볶이 Regular", 32),
        )
        Intro3 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/intro3.png"),
            600,
            345,
            f"             {self.money}원",
            "#ed1c24",
            ("1훈떡볶이 Regular", 32),
        )
        start = self.MINI_Game()

    def MINI_Game(self):
        self.first_player = mini_game()
        self.first_value = int(self.first_player[6])
        self.second_player = mini_game()
        self.second_value = int(self.second_player[6])
        self.bg1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            250,
            445,
            self.select1,
            f"\n이름 : {self.first_player[1]}\n팀 : {self.first_player[2]}\n등번호 : {self.first_player[3]}\n포지션 {self.first_player[4]}\n나이 : {self.first_player[5]}\n",
            "#472f91",
            ("타이포_헬로피오피 테두리B", 19),
        )
        self.bg2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            720,
            445,
            self.select2,
            f"\n이름 : {self.second_player[1]}\n팀 : {self.second_player[2]}\n등번호 : {self.second_player[3]}\n포지션 {self.second_player[4]}\n나이 : {self.second_player[5]}\n",
            "#472f91",
            ("타이포_헬로피오피 테두리B", 19),
        )

    def select1(self):
        self.bg1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            250,
            445,
            self.no_action,
            f"\n이름 : {self.first_player[1]}\n\n선수가치 : {self.first_value}\n",
            "#28a44a",
            ("타이포_헬로피오피 테두리B", 21),
        )
        self.bg2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            720,
            445,
            self.no_action,
            f"\n이름 : {self.second_player[1]}\n\n선수가치 : {self.second_value}\n",
            "#28a44a",
            ("타이포_헬로피오피 테두리B", 21),
        )

        if self.first_value >= self.second_value:
            self.bg2.after(2000, self.wait_answer)
        else:
            self.bg1.config(state="disabled")
            self.bg2.config(state="disabled")
            self.finished()

    def select2(self):
        self.bg1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            250,
            445,
            self.no_action,
            f"\n이름 : {self.first_player[1]}\n\n선수가치 : {self.first_value}\n",
            "#28a44a",
            ("타이포_헬로피오피 테두리B", 21),
        )
        self.bg2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/bg1.png"),
            720,
            445,
            self.no_action,
            f"\n이름 : {self.second_player[1]}\n\n선수가치 : {self.second_value}\n",
            "#28a44a",
            ("타이포_헬로피오피 테두리B", 21),
        )

        if self.first_value <= self.second_value:
            self.bg2.after(3000, self.wait_answer)
        else:
            self.bg1.config(state="disabled")
            self.bg2.config(state="disabled")
            self.finished()

    def wait_answer(self):
        self.money *= 2
        self.win += 1
        Intro2 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/intro2.png"),
            250,
            345,
            f"                {self.win}번",
            "#472f91",
            ("1훈떡볶이 Regular", 32),
        )
        Intro3 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/intro3.png"),
            600,
            345,
            f"             {self.money}원",
            "#472f91",
            ("1훈떡볶이 Regular", 32),
        )
        restart = self.MINI_Game()

    def finished(self):
        if self.money <= 40000:
            self.money = 40000
        update_money = give_money(self.money)

        self.bg2.after(4000, self.Main_Screen)

    ############################################################
    # 현재 상황 화면
    ############################################################
    def situation(self, start, finish, league_data):
        self.league_data = league_data
        self.start_rank = start
        self.finish_rank = finish
        self.destroy()
        Menu_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        self.game_buttons()
        self.sel1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn1.png"),
            232,
            148,
            self.no_action,
            f"팀 순위 보기",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn1.png"),
            462,
            148,
            self.no_action,
            f"선수 순위 보기",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn2.png"),
            692,
            148,
            lambda: self.situation(0, 10, get_EPL_table()),
            f"EPL 상황",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn2.png"),
            922,
            148,
            lambda: self.situation(0, 10, get_LaLiga_table()),
            f"라리가 상황",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn2.png"),
            232,
            238,
            lambda: self.situation(0, 10, get_Bundes_table()),
            f"분데스리가 상황",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel6 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn2.png"),
            462,
            238,
            self.no_action,
            f"타 리그 상황",
            "#472f91",
            ("고도 M", 12),
        )
        self.sel7 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit_btn3.png"),
            692,
            238,
            lambda: self.situation(0, 10, get_myteam_table()),
            f"현 소속 리그 보기",
            "#472f91",
            ("고도 M", 12),
        )
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            1060,
            258,
            self.sit_right_btn,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            980,
            258,
            self.sit_left_btn,
        )
        if self.finish_rank == len(self.league_data):
            right_button.config(state="disabled")
        if self.start_rank == 0:
            left_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit1-1.png"),
            227,
            333,
            self.no_action,
            f"순위",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit2-1.png"),
            287,
            333,
            self.no_action,
            f"팀 이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            527,
            333,
            self.no_action,
            f"경기",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            607,
            333,
            self.no_action,
            f"승",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            687,
            333,
            self.no_action,
            f"무",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            767,
            333,
            self.no_action,
            f"패",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            847,
            333,
            self.no_action,
            f"득점",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro8 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            927,
            333,
            self.no_action,
            f"실점",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro9 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            1007,
            333,
            self.no_action,
            f"득실",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro10 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/sit3-1.png"),
            1087,
            333,
            self.no_action,
            f"점수",
            "#472f91",
            ("고도 M", 12),
        )
        self.show_rank()

    def sit_left_btn(self):
        if self.finish_rank - self.start_rank != 10:
            self.finish_rank = self.start_rank + 10

        if self.start_rank != 0:
            self.start_rank -= 10
            self.finish_rank -= 10
            self.situation(self.start_rank, self.finish_rank, self.league_data)

    def sit_right_btn(self):
        if self.finish_rank + 10 <= len(self.league_data):
            self.start_rank += 10
            self.finish_rank += 10
            self.situation(self.start_rank, self.finish_rank, self.league_data)
        else:
            self.start_rank += 10
            self.finish_rank = len(self.league_data)
            self.situation(self.start_rank, self.finish_rank, self.league_data)

    def show_rank(self):
        for i in range(self.start_rank, self.finish_rank):
            sit1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit1-2.png"),
                227,
                373 + (40 * (i - self.start_rank)),
                f"{i+1}",
                "#472f91",
                ("고도 M", 12),
            )
            sit2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit2-2.png"),
                287,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                527,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                607,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][5]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                687,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][6]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                767,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][7]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                847,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][8]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                927,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][9]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit9 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                1007,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][10]}",
                "#472f91",
                ("고도 M", 12),
            )
            sit10 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/sit3-2.png"),
                1087,
                373 + (40 * (i - self.start_rank)),
                f"{self.league_data[i][11]}",
                "#472f91",
                ("고도 M", 12),
            )

    ############################################################
    # 인수 / 매각 화면
    ############################################################

    def acquisition(self):
        self.destroy()
        Message_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/acquisition_bg.png"), 0, 0
        )
        self.game_buttons()
        money = int(check_money())
        myteam = check_myteam()
        self.myteam_info = my_team_ac()
        self.acquisition_list = ran_team_ac(money)
        self.Intro1 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac1.png"),
            302,
            138,
            f"팀 이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac2.png"),
            572,
            138,
            f"인수 가격",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac3.png"),
            722,
            138,
            f"속한 나라",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac4.png"),
            952,
            138,
            f"속한 리그",
            "#472f91",
            ("고도 M", 12),
        )
        for i in range(7):
            team1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac1-1.png"),
                302,
                188 + (50 * i),
                f"{self.acquisition_list[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            team2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac2-1.png"),
                572,
                188 + (50 * i),
                f"{self.acquisition_list[i][4]} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            team3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac3-1.png"),
                722,
                188 + (50 * i),
                f"{self.acquisition_list[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            team4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac4-1.png"),
                952,
                188 + (50 * i),
                f"{self.acquisition_list[i][1]}",
                "#472f91",
                ("고도 M", 10),
            )
        Team_label1 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 0),
            self.buy1,
        )
        Team_label2 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 1),
            self.buy2,
        )
        Team_label3 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 2),
            self.buy3,
        )
        Team_label4 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 3),
            self.buy4,
        )
        Team_label5 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 4),
            self.buy5,
        )
        Team_label6 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 5),
            self.buy6,
        )
        Team_label7 = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/acquisition_btn1.png"),
            222,
            188 + (50 * 6),
            self.buy7,
        )

        self.Intro5 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac1.png"),
            302,
            575,
            f"팀 이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac2.png"),
            572,
            575,
            f"인수 가격",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac3.png"),
            722,
            575,
            f"속한 나라",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro8 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/ac4.png"),
            952,
            575,
            f"속한 리그",
            "#472f91",
            ("고도 M", 12),
        )
        for i in range(myteam):
            team1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac1-1.png"),
                302,
                625 + (50 * i),
                f"{self.myteam_info[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            team2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac2-1.png"),
                572,
                625 + (50 * i),
                f"{self.myteam_info[i][4]} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            team3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac3-1.png"),
                722,
                625 + (50 * i),
                f"{self.myteam_info[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            team4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/ac4-1.png"),
                952,
                625 + (50 * i),
                f"{self.myteam_info[i][1]}",
                "#472f91",
                ("고도 M", 10),
            )
        if myteam == 1:
            Team_label8 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 0),
                self.sell1,
            )
        elif myteam == 2:
            Team_label8 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 0),
                self.sell1,
            )
            Team_label8 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 1),
                self.sell2,
            )
        else:
            Team_label8 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 0),
                self.sell1,
            )
            Team_label9 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 1),
                self.sell2,
            )
            Team_label10 = Get_label.image_button(
                self.Gui,
                os.path.join(img_path, "../../Images/acquisition_btn2.png"),
                222,
                625 + (50 * 2),
                self.sell3,
            )

    def buy1(self):
        save_buy_team(self.acquisition_list[0])
        self.acquisition()

    def buy2(self):
        save_buy_team(self.acquisition_list[1])
        self.acquisition()

    def buy3(self):
        save_buy_team(self.acquisition_list[2])
        self.acquisition()

    def buy4(self):
        save_buy_team(self.acquisition_list[3])
        self.acquisition()

    def buy5(self):
        save_buy_team(self.acquisition_list[4])
        self.acquisition()

    def buy6(self):
        save_buy_team(self.acquisition_list[5])
        self.acquisition()

    def buy7(self):
        save_buy_team(self.acquisition_list[6])
        self.acquisition()

    def sell1(self):
        save_sell_team(self.myteam_info[0])
        self.acquisition()

    def sell2(self):
        save_sell_team(self.myteam_info[1])
        self.acquisition()

    def sell3(self):
        save_sell_team(self.myteam_info[2])
        self.acquisition()

    ############################################################
    # 재정 관리 화면
    ############################################################

    def financial(self):
        self.destroy()
        financial_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/financial_bg.png"), 0, 0
        )
        self.game_buttons()
        gamer_data = get_gamer_team()
        self.Intro1 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1.png"),
            232,
            148,
            f"구단주 이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1.png"),
            232,
            218,
            f"구단 이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1.png"),
            232,
            288,
            f"현재 자금",
            "#472f91",
            ("고도 M", 12),
        )
        self.con1 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-1.png"),
            402,
            148,
            f"{gamer_data[0]}",
            "#472f91",
            ("고도 M", 12),
        )
        self.con2 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-1.png"),
            402,
            218,
            f"{gamer_data[1]}",
            "#472f91",
            ("고도 M", 12),
        )
        self.con3 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-1.png"),
            402,
            288,
            f"{gamer_data[3]}",
            "#472f91",
            ("고도 M", 12),
        )
        money = team_money()
        self.Intro4 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi2.png"),
            232,
            398,
            f"선수 주급",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi2.png"),
            232,
            468,
            f"코치 주급",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi2.png"),
            232,
            538,
            f"직원 주급",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi2.png"),
            232,
            608,
            f"이적료 지출",
            "#472f91",
            ("고도 M", 12),
        )
        self.con4 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-2.png"),
            402,
            398,
            f"{money[0]} 만원",
            "#472f91",
            ("고도 M", 12),
        )
        self.con5 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-2.png"),
            402,
            468,
            f"{money[1]} 만원",
            "#472f91",
            ("고도 M", 12),
        )
        self.con6 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-2.png"),
            402,
            538,
            f"{money[2]} 만원",
            "#472f91",
            ("고도 M", 12),
        )
        self.con7 = Get_label.image_label_text(
            self.Gui,
            os.path.join(img_path, "../../Images/fi1-2.png"),
            402,
            608,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        if get_gamer_team()[1] != "무직":
            player_think = pla_Res()
            fan_think = fan_res()
            self.Intro1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi5.png"),
                782,
                148,
                f"팀 명성",
                "#472f91",
                ("고도 M", 12),
            )
            self.Intro2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi5.png"),
                782,
                218,
                f"팀 내 평가",
                "#472f91",
                ("고도 M", 12),
            )
            self.Intro3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi5.png"),
                782,
                288,
                f"팬 평가",
                "#472f91",
                ("고도 M", 12),
            )
            self.con1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi5-1.png"),
                922,
                148,
                f"",
                "#472f91",
                ("고도 M", 12),
            )
            if player_think[1] == 0:
                self.con2 = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, "../../Images/fi5-2.png"),
                    922,
                    218,
                    f"{player_think[0]}",
                    "#472f91",
                    ("고도 M", 12),
                )
            else:
                self.con2 = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, "../../Images/fi5-1.png"),
                    922,
                    218,
                    f"{player_think[0]}",
                    "#472f91",
                    ("고도 M", 12),
                )
            if fan_think[1] == 0:
                self.con3 = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, "../../Images/fi5-2.png"),
                    922,
                    288,
                    f"{fan_think[0]}",
                    "#472f91",
                    ("고도 M", 12),
                )
            else:
                self.con3 = Get_label.image_label_text(
                    self.Gui,
                    os.path.join(img_path, "../../Images/fi5-1.png"),
                    922,
                    288,
                    f"{fan_think[0]}",
                    "#472f91",
                    ("고도 M", 12),
                )

            match = match_money()

            self.Intro4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi3.png"),
                712,
                398,
                f"경기당 수익",
                "#472f91",
                ("고도 M", 12),
            )
            self.Intro5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi3.png"),
                712,
                468,
                f"대회 수익",
                "#472f91",
                ("고도 M", 12),
            )
            self.Intro6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi3.png"),
                712,
                538,
                f"스폰서 수익",
                "#472f91",
                ("고도 M", 12),
            )
            self.Intro7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi3.png"),
                712,
                608,
                f"이적료 수익",
                "#472f91",
                ("고도 M", 12),
            )
            self.con4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1-2.png"),
                882,
                398,
                f"{match}",
                "#472f91",
                ("고도 M", 12),
            )
            self.con5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1-2.png"),
                882,
                468,
                f"",
                "#472f91",
                ("고도 M", 12),
            )
            self.con6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1-2.png"),
                882,
                538,
                f"{(money[0]+money[1]+money[2])*9//10} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            self.con7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1-2.png"),
                882,
                608,
                f"",
                "#472f91",
                ("고도 M", 12),
            )

            self.Intro8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1.png"),
                232,
                688,
                f"넷 스펜딩",
                "#472f91",
                ("고도 M", 12),
            )
            self.con8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/fi1-3.png"),
                402,
                688,
                f"",
                "#472f91",
                ("고도 M", 12),
            )

    ############################################################
    # 팀 선수단 화면
    ############################################################

    def Team_Player_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Player_Screen_background = Get_label.image_label(
                self.Gui, os.path.join(img_path, "../../Images/cantuse_bg.png"), 0, 0
            )
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.players = team_players("Position", self.sort_num)
            fir = self.first_player_scr()

    def first_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.second_player_scr,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.no_action,
        )
        left_button.config(state="disabled")
        self.len_player = len(self.players)
        if self.len_player < 16:
            right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player1.png"),
            222,
            133,
            self.sortpla1,
            f"번호",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player2.png"),
            282,
            133,
            self.sortpla2,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player3.png"),
            542,
            133,
            self.sortpla3,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player4.png"),
            742,
            133,
            self.sortpla4,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player5.png"),
            802,
            133,
            self.sortpla5,
            f"선수 가치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player6.png"),
            932,
            133,
            self.sortpla6,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player7.png"),
            992,
            133,
            self.sortpla7,
            f"잠재력",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro8 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player8.png"),
            1052,
            133,
            self.sortpla8,
            f"선수 주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        first_len = 0
        if self.len_player > 14:
            first_len = 15
        else:
            first_len = self.len_player
        for i in range(first_len):
            pla1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player1-1.png"),
                222,
                173 + (40 * i),
                f"{self.players[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player2-1.png"),
                282,
                173 + (40 * i),
                f"{self.players[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player3-1.png"),
                542,
                173 + (40 * i),
                f"{self.players[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player4-1.png"),
                742,
                173 + (40 * i),
                f"{self.players[i][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player5-1.png"),
                802,
                173 + (40 * i),
                f"{self.players[i][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            pla6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player6-1.png"),
                932,
                173 + (40 * i),
                f"{self.players[i][6]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player7-1.png"),
                992,
                173 + (40 * i),
                f"{self.players[i][7]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player8-1.png"),
                1052,
                173 + (40 * i),
                f"{self.players[i][8]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def second_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.third_player_scr,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.first_player_scr,
        )
        second_len = 0
        if self.len_player > 29:
            second_len = 15
        else:
            second_len = self.len_player - 15
            right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player1.png"),
            222,
            133,
            self.sortpla1,
            f"번호",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player2.png"),
            282,
            133,
            self.sortpla2,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player3.png"),
            542,
            133,
            self.sortpla3,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player4.png"),
            742,
            133,
            self.sortpla4,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player5.png"),
            802,
            133,
            self.sortpla5,
            f"선수 가치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player6.png"),
            932,
            133,
            self.sortpla6,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player7.png"),
            992,
            133,
            self.sortpla7,
            f"잠재력",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro8 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player8.png"),
            1052,
            133,
            self.sortpla8,
            f"선수 주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        for i in range(second_len):
            pla1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player1-1.png"),
                222,
                173 + (40 * i),
                f"{self.players[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player2-1.png"),
                282,
                173 + (40 * i),
                f"{self.players[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player3-1.png"),
                542,
                173 + (40 * i),
                f"{self.players[i+15][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player4-1.png"),
                742,
                173 + (40 * i),
                f"{self.players[i+15][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player5-1.png"),
                802,
                173 + (40 * i),
                f"{self.players[i+15][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            pla6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player6-1.png"),
                932,
                173 + (40 * i),
                f"{self.players[i+15][6]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player7-1.png"),
                992,
                173 + (40 * i),
                f"{self.players[i+15][7]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player8-1.png"),
                1052,
                173 + (40 * i),
                f"{self.players[i+15][8]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def third_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.second_player_scr,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.second_player_scr,
        )

        right_button.config(state="disabled")
        third_len = self.len_player - 30

        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player1.png"),
            222,
            133,
            self.sortpla1,
            f"번호",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player2.png"),
            282,
            133,
            self.sortpla2,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player3.png"),
            542,
            133,
            self.sortpla3,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player4.png"),
            742,
            133,
            self.sortpla4,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player5.png"),
            802,
            133,
            self.sortpla5,
            f"선수 가치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro6 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player6.png"),
            932,
            133,
            self.sortpla6,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro7 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player7.png"),
            992,
            133,
            self.sortpla7,
            f"잠재력",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro8 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/player8.png"),
            1052,
            133,
            self.sortpla8,
            f"선수 주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        for i in range(third_len):
            pla1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player1-1.png"),
                222,
                173 + (40 * i),
                f"{self.players[i+30][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player2-1.png"),
                282,
                173 + (40 * i),
                f"{self.players[i+30][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player3-1.png"),
                542,
                173 + (40 * i),
                f"{self.players[i+30][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player4-1.png"),
                742,
                173 + (40 * i),
                f"{self.players[i+30][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player5-1.png"),
                802,
                173 + (40 * i),
                f"{self.players[i+30][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )
            pla6 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player6-1.png"),
                932,
                173 + (40 * i),
                f"{self.players[i+30][6]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla7 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player7-1.png"),
                992,
                173 + (40 * i),
                f"{self.players[i+30][7]}",
                "#472f91",
                ("고도 M", 12),
            )
            pla8 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/player8-1.png"),
                1052,
                173 + (40 * i),
                f"{self.players[i+30][8]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def sortpla1(self):
        self.players = team_players("Number", self.sort_num)
        self.sort_color = 1
        fir = self.first_player_scr()

    def sortpla2(self):
        self.players = team_players("Name", self.sort_num)
        self.sort_color = 2
        fir = self.first_player_scr()

    def sortpla3(self):
        self.players = team_players("Position", self.sort_num)
        self.sort_color = 3
        fir = self.first_player_scr()

    def sortpla4(self):
        self.players = team_players("Age", self.sort_num)
        self.sort_color = 4
        fir = self.first_player_scr()

    def sortpla5(self):
        self.players = team_players("Market_Value", self.sort_num)
        self.sort_color = 5
        fir = self.first_player_scr()

    def sortpla6(self):
        self.players = team_players("Ability", self.sort_num)
        self.sort_color = 6
        fir = self.first_player_scr()

    def sortpla7(self):
        self.players = team_players("Potential", self.sort_num)
        self.sort_color = 7
        fir = self.first_player_scr()

    def sortpla8(self):
        self.players = team_players("Money", self.sort_num)
        self.sort_color = 8
        fir = self.first_player_scr()

    def change_pla_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")
        self.Intro6.config(fg="#472f91")
        self.Intro7.config(fg="#472f91")
        self.Intro8.config(fg="#472f91")

    ############################################################
    # 팀 코치단 화면
    ############################################################

    def Team_Coach_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Coach_Screen_background = Get_label.image_label(
                self.Gui, os.path.join(img_path, "../../Images/cantuse_bg.png"), 0, 0
            )
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.coaches = team_coaches("Position", self.sort_num)
            fir = self.first_coach_scr()

    def first_coach_scr(self):
        self.destroy()
        Team_Coach_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.second_coach_scr,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.no_action,
        )
        left_button.config(state="disabled")
        self.len_coach = len(self.coaches)
        if self.len_coach < 16:
            right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach1.png"),
            222,
            133,
            self.sortcoa1,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach2.png"),
            552,
            133,
            self.sortcoa2,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach3.png"),
            832,
            133,
            self.sortcoa3,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach4.png"),
            912,
            133,
            self.sortcoa4,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach5.png"),
            992,
            133,
            self.sortcoa5,
            f"주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_coa_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_coa_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_coa_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_coa_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_coa_sortnum()
            self.Intro5.config(fg="#B30000")
        first_len = 0
        if self.len_coach > 14:
            first_len = 15
        else:
            first_len = self.len_coach
        for i in range(first_len):
            coa1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach1-1.png"),
                222,
                173 + (40 * i),
                f"{self.coaches[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach2-1.png"),
                552,
                173 + (40 * i),
                f"{self.coaches[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach3-1.png"),
                832,
                173 + (40 * i),
                f"{self.coaches[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach4-1.png"),
                912,
                173 + (40 * i),
                f"{self.coaches[i][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach5-1.png"),
                992,
                173 + (40 * i),
                f"{self.coaches[i][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def second_coach_scr(self):
        self.destroy()
        Team_Coach_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.no_action,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.first_coach_scr,
        )
        second_len = self.len_coach - 15
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach1.png"),
            222,
            133,
            self.sortcoa1,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach2.png"),
            552,
            133,
            self.sortcoa2,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach3.png"),
            832,
            133,
            self.sortcoa3,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach4.png"),
            912,
            133,
            self.sortcoa4,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach5.png"),
            992,
            133,
            self.sortcoa5,
            f"주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_coa_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_coa_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_coa_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_coa_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_coa_sortnum()
            self.Intro5.config(fg="#B30000")
        for i in range(second_len):
            coa1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach1-1.png"),
                222,
                173 + (40 * i),
                f"{self.coaches[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach2-1.png"),
                552,
                173 + (40 * i),
                f"{self.coaches[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach3-1.png"),
                832,
                173 + (40 * i),
                f"{self.coaches[i+15][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach4-1.png"),
                912,
                173 + (40 * i),
                f"{self.coaches[i+15][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            coa5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach5-1.png"),
                992,
                173 + (40 * i),
                f"{self.coaches[i+15][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def sortcoa1(self):
        self.coaches = team_coaches("Name", self.sort_num)
        self.sort_color = 1
        fir = self.first_coach_scr()

    def sortcoa2(self):
        self.coaches = team_coaches("Position", self.sort_num)
        self.sort_color = 2
        fir = self.first_coach_scr()

    def sortcoa3(self):
        self.coaches = team_coaches("Age", self.sort_num)
        self.sort_color = 3
        fir = self.first_coach_scr()

    def sortcoa4(self):
        self.coaches = team_coaches("Ability", self.sort_num)
        self.sort_color = 4
        fir = self.first_coach_scr()

    def sortcoa5(self):
        self.coaches = team_coaches("Money", self.sort_num)
        self.sort_color = 5
        fir = self.first_coach_scr()

    def change_coa_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")

    ############################################################
    # 팀 직원 화면
    ############################################################

    def Team_Staff_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Staff_Screen_background = Get_label.image_label(
                self.Gui, os.path.join(img_path, "../../Images/cantuse_bg.png"), 0, 0
            )
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.staffs = team_staffs("Position", self.sort_num)
            fir = self.first_staff_scr()

    def first_staff_scr(self):
        self.destroy()
        Team_Staff_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.second_staff_scr,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.no_action,
        )
        left_button.config(state="disabled")
        self.len_staff = len(self.staffs)
        if self.len_staff < 16:
            right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach1.png"),
            222,
            133,
            self.sortsta1,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach2.png"),
            552,
            133,
            self.sortsta2,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach3.png"),
            832,
            133,
            self.sortsta3,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach4.png"),
            912,
            133,
            self.sortsta4,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach5.png"),
            992,
            133,
            self.sortsta5,
            f"주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sta_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sta_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sta_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sta_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sta_sortnum()
            self.Intro5.config(fg="#B30000")
        first_len = 0
        if self.len_staff > 14:
            first_len = 15
        else:
            first_len = self.len_staff
        for i in range(first_len):
            sta1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach1-1.png"),
                222,
                173 + (40 * i),
                f"{self.staffs[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach2-1.png"),
                552,
                173 + (40 * i),
                f"{self.staffs[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach3-1.png"),
                832,
                173 + (40 * i),
                f"{self.staffs[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach4-1.png"),
                912,
                173 + (40 * i),
                f"{self.staffs[i][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach5-1.png"),
                992,
                173 + (40 * i),
                f"{self.staffs[i][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def second_staff_scr(self):
        self.destroy()
        Team_Staff_Screen_background = Get_label.image_label(
            self.Gui, os.path.join(img_path, "../../Images/Main_Screen_bg.png"), 0, 0
        )
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/right.png"),
            980,
            43,
            self.no_action,
        )
        left_button = Get_label.image_button(
            self.Gui,
            os.path.join(img_path, "../../Images/left.png"),
            900,
            43,
            self.first_staff_scr,
        )
        second_len = self.len_staff - 15
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach1.png"),
            222,
            133,
            self.sortsta1,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach2.png"),
            552,
            133,
            self.sortsta2,
            f"포지션",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach3.png"),
            832,
            133,
            self.sortsta3,
            f"나이",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach4.png"),
            912,
            133,
            self.sortsta4,
            f"능력치",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.Gui,
            os.path.join(img_path, "../../Images/coach5.png"),
            992,
            133,
            self.sortsta5,
            f"주급",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sta_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sta_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sta_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sta_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sta_sortnum()
            self.Intro5.config(fg="#B30000")
        for i in range(second_len):
            sta1 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach1-1.png"),
                222,
                173 + (40 * i),
                f"{self.staffs[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta2 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach2-1.png"),
                552,
                173 + (40 * i),
                f"{self.staffs[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta3 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach3-1.png"),
                832,
                173 + (40 * i),
                f"{self.staffs[i+15][3]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta4 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach4-1.png"),
                912,
                173 + (40 * i),
                f"{self.staffs[i+15][4]}",
                "#472f91",
                ("고도 M", 12),
            )
            sta5 = Get_label.image_label_text(
                self.Gui,
                os.path.join(img_path, "../../Images/coach5-1.png"),
                992,
                173 + (40 * i),
                f"{self.staffs[i+15][5]} 만원",
                "#472f91",
                ("고도 M", 12),
            )

    def sortsta1(self):
        self.staffs = team_staffs("Name", self.sort_num)
        self.sort_color = 1
        fir = self.first_staff_scr()

    def sortsta2(self):
        self.staffs = team_staffs("Position", self.sort_num)
        self.sort_color = 2
        fir = self.first_staff_scr()

    def sortsta3(self):
        self.staffs = team_staffs("Age", self.sort_num)
        self.sort_color = 3
        fir = self.first_staff_scr()

    def sortsta4(self):
        self.staffs = team_staffs("Ability", self.sort_num)
        self.sort_color = 4
        fir = self.first_staff_scr()

    def sortsta5(self):
        self.staffs = team_staffs("Money", self.sort_num)
        self.sort_color = 5
        fir = self.first_staff_scr()

    def change_coa_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")
