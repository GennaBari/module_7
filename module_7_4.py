def print_team_num(team1_num, team2_num):
    if team1_num:
        print("В команде Мастера кода участников: %s!" % (team1_num))
    if team1_num and team2_num:
        print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

def team2_score_result(score_2, team2_time):
    print("Команда Волшебники данных решила задач: {}".format(score_2))
    print("Волшебники данных решили задачи за {}".format(team2_time))

def total_score(score1, score2):
    print(f"Команды решили {score1} и {score2} задач.")

def challenge_result(score1, score2, team1_time, team2_time):
    if score1 > score2 or score1 == score2 and team1_time < team2_time:
        print(f'Победа команды Мастера кода!')
    elif score1 < score2 or score1 == score2 and team1_time > team2_time:
        print(f'Победа команды Волшебники данных!')
    else:
        print(f'Ничья!')

def current_score(tasks_total, time_avg):
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Вызов функций
print_team_num(team1_num, team2_num)
team2_score_result(score2, team2_time)
total_score(score1, score2)
challenge_result(score1, score2, team1_time, team2_time)
current_score(tasks_total, time_avg)


