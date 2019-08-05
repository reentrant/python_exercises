from collections import Counter
from collections import OrderedDict


def query_student_average():
    '''
    You have a record of  students. Each record contains the student's name, and
    their percent marks in Maths, Physics and Chemistry. The marks can be floating
    values. The user enters some integer  followed by the names and marks for
    students. You are required to save the record in a dictionary data type.
    The user then enters a student's name. Output the average percentage marks
    obtained by that student, correct to two decimal places.

    Example:
    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh
    '''
    student_marks = {}
    # n = int(input())
    # print()
    # for _ in range(n):
    #     name, *line = input().split()
    #     print(name)
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    #     print(student_marks)
    # query_name = input().strip()
    query_name = 'Avril'
    student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
    if student_marks.get(query_name):
        marks = float(len(student_marks[query_name]))
        return "{0:.2f}".format(sum(student_marks[query_name]) / marks)


def group_by_owners():
    """
    exercise from https://www.testdome.com/
    :param files: (files) a dictionary containing the file owner name for each file name.
    :returns: (result) a dictionary containing a list of file names for each owner name,
    in any order.
    """
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    result = {}
    for k, v in files.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result


class LeagueTable:
    """
    The LeagueTable class tracks the score of each player in a league. After each game, the player
    records their score with the record_result function.
    """
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        """
        a) The player with the highest score is ranked first (rank 1).
            The player with the lowest score is ranked last.
        b) If two players are tied on score, then the player who has played the fewest games is
            ranked higher.
        c) If two players are tied on score and number of games played, then the player who was
            first in the list of players is ranked higher.
        :param rank:
        :return: returns the player at the given rank.
        """
        def sortByScore(d):
            return d.get("score")
        scores = {}
        n_games = {}
        max = 0
        print(self.standings)
        print(self.standings.keys())
        print(self.standings.values())

        # for player, v in self.standings.items():
        #     print(player, v['score'], v['games_played'])

        for player, v in self.standings.items():
            if v['score'] > max:
                max = v['score']
                scores[max] = [player]
                n_games[v['games_played']] = [player]
            elif v['score'] == max:
                scores[max].append(player)
                if v['games_played'] in n_games:
                    n_games[v['games_played']].append(player)
                else:
                    n_games[v['games_played']] = [player]

        if scores:
            print(scores)
            rank_one = scores.get(max)
            if len(rank_one) == 1:
                higher_rank = rank_one.pop()
            else:
                rank_one = n_games.get(min(n_games.keys()))
                if len(rank_one) == 1:
                    higher_rank = rank_one.pop()
                else:
                    for player in self.standings.keys():
                        if player in rank_one:
                            higher_rank = player
                            break
        return higher_rank


if __name__ == '__main__':
    # print(query_student_average())
    # print(group_by_owners())
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))

