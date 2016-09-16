import csv
import operator

def read_data(data):
    with open(data, 'r') as fh:
        result = [line for line in csv.reader(fh)]
    return result

def get_min_difference_on_score(parsed_data):
    parsed_data.pop(0)    # throw away the header
    teams = [line[0] for line in parsed_data]
    goals = [line[5] for line in parsed_data]
    goals_allowed = [line[6] for line in parsed_data]
    lines = [(t, int(g) - int(g_a)) for t, g, g_a in zip(teams, goals, goals_allowed)]
    #right_on = min(lines, key=lambda t: t[1])
    right_on = min(lines, key=operator.itemgetter(1))
    return right_on

def get_min_difference_on_temperature(parsed_data):
    parsed_data.pop(0)    # throw away the header
    days = [line[0] for line in parsed_data]
    highs = [line[1] for line in parsed_data]
    lows = [line[2] for line in parsed_data]
    lines = [(d, int(h) - int(l)) for d, h, l in zip(days, highs, lows)]
    #right_on = min(lines, key=lambda t: t[1])
    right_on = min(lines, key=operator.itemgetter(1))
    return right_on

def get_target_with_min_difference(parsed_data, **kwargs):
    parsed_data.pop(0)    # toss the header
    TARGET_INDEX = int(kwargs.get('target_col'))
    HIGH = int(kwargs.get('high'))
    LOW = int(kwargs.get('low'))
    targets = [line[TARGET_INDEX] for line in parsed_data]
    highs = [line[HIGH] for line in parsed_data]
    lows = [line[LOW] for line in parsed_data]
    lines = [(t, int(h) - int(l)) for t, h, l in zip(targets, highs, lows)]
    return min(lines, key=operator.itemgetter(1))

if __name__ == '__main__':
    football_data = read_data('Data/football.csv')
    print(get_min_difference_on_score(football_data))

    days_data = read_data('Data/weather.csv')
    print(get_min_difference_on_temperature(days_data))

    print(get_target_with_min_difference(football_data,
                                   target_col=0,
                                   high=5,
                                   low=6))

    print(get_target_with_min_difference(days_data,
                                         target_col=0,
                                         high=1,
                                         low=2))
