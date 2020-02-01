#!/usr/bin/python3
"""Functions for handling of requests, auxiliaries for the app server
"""
from word2number import w2n

"""This one could be a more elaborated database"""
database_valid_names = {'Colombia': ['Amazonas', 'Antioquia', 'Arauca',
                                     'Atlántico', 'Bolívar', 'Boyacá',
                                     'Tunja', 'Caldas', 'Caquetá', 'Casanare',
                                     'Cauca', 'Cesar', 'Chocó', 'Córdoba',
                                     'Cundinamarca', 'Guainía', 'Guaviare',
                                     'Huila', 'La Guajira', 'Magdalena',
                                     'Meta', 'Nariño', 'Norte de Santander',
                                     'Putumayo', 'Quindío', 'Risaralda',
                                     'San Andrés y Providencia', 'Santander',
                                     'Sucre', 'Tolima', 'Valle del Cauca',
                                     'Vaupés', 'Vichada']}

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
           "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
           "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
           "hundred", "and", "thousand", "million"]


def is_valid_jurisdiction(name, country):
    """ Returns true if the name is a valid jurisdiction for a given country
    """
    try:
        valid_names = database_valid_names[country]
        if name in valid_names:
            return True
    except:
        return False


def words_to_number(words):
    """Takes an string and converts it into integer, or None on error
    """
    try:
        words = words.strip()
        value = int(words)
        return value
    except:
        pass

    for number in numbers:
        idx = words.find(number)
        if idx > 0:
            words = words[:idx] + "-" + words[idx:]
        try:
            return w2n.word_to_num(words)
        except:
            return None
