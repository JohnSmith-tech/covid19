LOCATION = 'location'
DATE = 'date_'
TOTAL_CASES = 'total_cases'
NEW_CASES = 'new_cases'
NEW_CASES_SMOOTHED = 'new_cases_smoothed'
TOTAL_DEATHS = 'total_deaths'
NEW_DEATHS = 'new_deaths'
NEW_DEATHS_SMOOTHED = 'new_deaths_smoothed'
REPRODUCTION_RATE = 'reproduction_rate'
TOTAL_VACCINATIONS = 'total_vaccinations'
PEOPLE_VACCINATED = 'people_vaccinated'
PEOPLE_FULLY_VACCINATED = 'people_fully_vaccinated'
TOTAL_BOOSTERS = 'total_boosters'
POPULATION = 'population'
VACCINATION_RATIO = 'vaccination_ratio'
PREVALENCE = 'prevalence'
INCIDENCE = 'incidence'

DROP_TABLE_IF_EXISTS = '''drop table if exists covid19_countries'''

TABLE_NAME = 'covid19_countries'

QUERY_SELECT_ALL = f'SELECT * from {TABLE_NAME}'

QUERY_SELECT_LOCATION_GROUP = f'SELECT {LOCATION},MAX({NEW_DEATHS}) ' \
                              f'from {TABLE_NAME} ' \
                              f'GROUP BY {LOCATION}'

QUERY_SELECT_TOTAL_VACCINATIONS = f'SELECT a.{LOCATION}, a.{TOTAL_VACCINATIONS} ' \
                                  f'FROM (SELECT {LOCATION},MAX({TOTAL_VACCINATIONS}) ' \
                                  f'AS {TOTAL_VACCINATIONS} ' \
                                  f'FROM {TABLE_NAME} ' \
                                  f'GROUP BY {LOCATION}) a ' \
                                  f'ORDER BY a.{TOTAL_VACCINATIONS}'

QUERY_SELECT_TEN_DAYS = f'''SELECT {DATE},{NEW_DEATHS} ''' \
                        f'''FROM {TABLE_NAME} WHERE {LOCATION} = 'Argentina' ''' \
                        f'''ORDER BY {NEW_DEATHS} DESC LIMIT 10'''

QUERY_CREATE_TABLE_COVID19 = '''CREATE TABLE covid19_countries(
    location TEXT,
    date_ date,
    total_cases float,
    new_cases float,
    new_cases_smoothed float,
    total_deaths float,
    new_deaths float,
    new_deaths_smoothed float,
    reproduction_rate float,
    total_vaccinations float,
    people_vaccinated float,
    people_fully_vaccinated float,
    total_boosters float,
    population float,
    vaccination_ratio float,
    prevalence float,
    incidence float
    );'''
