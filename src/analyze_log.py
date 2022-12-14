import os
import csv
from statistics import mode

def analyze_log(path_to_file):
    filename, ext = os.path.splitext(path_to_file)

    if ext != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{filename}{ext}'")

    try:
        with open(path_to_file, "r") as file:
            orders = list(csv.reader(file))
            all_foods = set([
                order[1]
                for order in orders
            ])

            working_days = set([
                order[2]
                for order in orders
            ])

            maria_most_ordered = mode([
            order[1]
            for order in orders
            if order[0] == 'maria'
            ])

            hamburgers_eaten_by_arnaldo = len([
                order[1]
                for order in orders
                if order[0] == 'arnaldo' and order[1] == 'hamburguer'
            ])

            dishes_joao_never_ordered = all_foods.difference(set([
                order[1]
                for order in orders
                if order[0] == 'joao'
            ]))

            days_arnaldo_never_attended = working_days.difference(set([
                order[2]
                for order in orders
                if order[0] == 'arnaldo'
            ]))

            lines = [maria_most_ordered, hamburgers_eaten_by_arnaldo, dishes_joao_never_ordered, days_arnaldo_never_attended]
            with open('data/mkt_campaign.txt', "w") as txt:
                for line in lines:
                    txt.write(f'{line}\n')

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{filename}{ext}'")
