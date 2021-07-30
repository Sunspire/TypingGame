from functions.database import get_query


def get_random_words(limit):
    return get_query(
        "SELECT DISTINCT word " \
        "FROM entries "\
        "ORDER BY RANDOM() LIMIT " + str(limit))