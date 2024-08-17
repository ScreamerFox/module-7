class Match:
    def __init__(self, count_t, t1, t2, score1, score2, t1_t, t2_t):
        self.count_t = count_t
        self.t1 = t1
        self.t2 = t2
        self.score1 = score1
        self.score2 = score2
        self.t1_t = t1_t
        self.t2_t = t2_t

    def prt_count_t(self):
        for key, value in self.t1.items():
            for key1, value1 in self.t2.items():
                print('В команде %s - %s участников.' % (key, value))
                print('В команде %s - %s участников.' % (key1, value1))
                print('И того в командах участников %(count)s против %(count1)s.\n' % {'count': value, 'count1': value1})

    def t_score(self):
        for key, value in self.t1.items():
            for key1, value1 in self.t2.items():
                print('Команда  {}, решили - {} задачи, за {} минут'
                        .format(key, self.score1, round(self.t1_t / 60, 1)))
                print('Команда  {}, решили - {} задачи, за {} минут\n'
                        .format(key1, self.score2, round(self.t2_t / 60, 1)))

    def challenge_result(self):
        if isinstance(self.score1, (int, float)) > 0 and isinstance(self.score2, (int, float)) > 0:
            total_task1 = self.t1_t / self.score1
            total_task2 = self.t2_t / self.score2
            if self.score1 == self.score2 and total_task1 == total_task2:
                print('Счёт команд равный, поэтому объявляется НИЧЬЯ!')
            elif self.score1 > self.score2 or (self.score1 == self.score2 and total_task1 < total_task2):
                print(f'Победила команда {list(self.t1.keys())[0]}!')
            else:
                print(f'Победила команда {list(self.t2.keys())[0]}!')
            print(f'Количество решенных задач по командам: {self.score1} и {self.score2}')

    def tasks_total(self):
        tasks_total = self.score1 + self.score2
        time_avg = ((self.t1_t + self.t2_t) / tasks_total)
        if round(time_avg, 1) > 100:
            print('Сегодня было решено: %(tasks_total)s, в среднем по %(times)s минут на задачу' % {'tasks_total': tasks_total, 'times': round(time_avg, 1) / 60})
        else:
            print('Сегодня было решено: {}, в среднем по {} секунд на задачу'.format(tasks_total, round(time_avg, 1)))




match1 = Match(2, {'Мастера кода': 5}, {'Волшебники данных': 6}, 40, 40, 1261, 2523)

match1.prt_count_t()
match1.t_score()
match1.challenge_result()
match1.tasks_total()
