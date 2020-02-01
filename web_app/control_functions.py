#!/usr/bin/python3
"""Functions for handling of requests, auxiliaries for the app server
"""
#from word2number import w2n

#This one could be a more elaborated database
database_valid_names = {'Colombia': ['Amazonas', 'Antioquia', 'Arauca',
                        'Atlántico', 'Bolívar', 'Boyacá', 'Tunja', 'Caldas',
                        'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Chocó',
                        'Córdoba', 'Cundinamarca', 'Guainía', 'Guaviare',
                        'Huila', 'La Guajira', 'Magdalena', 'Meta', 'Nariño',
                        'Norte de Santander', 'Putumayo', 'Quindío',
                        'Risaralda', 'San Andrés y Providencia', 'Santander',
                        'Sucre', 'Tolima', 'Valle del Cauca', 'Vaupés',
                        'Vichada']}

def is_valid_jurisdiction(name, country):
    """ Returns true if the name is a valid jurisdiction for a given country
    """
    try:
        valid_names = database_valid_names[country]
        if name in valid_names:
            return True
    except:
        return False
