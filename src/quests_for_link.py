import csv
import os
import ast


def run():
    quest = []
    file_location = os.path.abspath("quests_for_question.csv")
    with open(file_location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                quest[:line_count] = {'Quest': {row[0]}, 'Start Date': {row[1]}, 'Duration': {row[2]},
                                      'Reward': {row[3]},
                                      'Difficulty': {row[4]}, 'Location': {row[5]}, 'Quest Giver': {row[6]}}

    print(quest[:1])
