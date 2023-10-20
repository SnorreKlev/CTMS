#Advanced math
from statistics import median as Med

def _handleValue_(value, allowed_types, fn) -> None:
    if allowed_types[0] == False:
        return True

    if type(value) == list and list in allowed_types:
        for item in value:
            if (type(item) in allowed_types) == False:
                raise Exception(f"ERROR - function: {fn}, can ONLY take these datatypes: \n{allowed_types}\nOne of the items in your list did not meet these requirements!")
                return False
    else:
        if (type(value) in allowed_types) == False:
            raise Exception(f"ERROR - function: {fn}, can ONLY take these datatypes: \n{allowed_types}\nYour value did not meet the requirements for the datatype.")
            return False
    return True

def kvadratrot(num: int | float) -> int or float:
    """
    Regner ut kvadratroten av ett tall (int eller float)

    Parametere:
    - num (int eller float): Dette er tallet du vil regne ut kvadratroten på

    Retunerer:
    int eller float: kvadratroten av parametere (num)

    Eksempel for bruk:
    ```python
    from MultiLib import kvadratrot
    print(kvadratrot(25))
    # Output: 5
    ```
    Merk:
    - Denne funksjonen forventer at num (parameteret) er ett tall.
    """
    _handleValue_(num, [int, float], "kvadratrot")
    return num**0.5
def typetall(_list_: list) -> object:
    """
    Regner ut typetallet av en liste (uansett datatype)

    Parametere:
    - _list_ (uansett datatype): Dette er listen som funksjonen regner ut typetallet på.

    Retunerer:
    most_mentioned_item (datatype varierer basert på hva du bruker som parametere): Dette er det objektet som ble nevnt flest ganger i listen.

    Eksempel for bruk:
    ```python
    from MultiLib import typetall
    liste = [1, 2, 2, 3]
    print(typetall(liste))
    # Output: 2 (som int, fordi det var den datatypen som listen brukte)
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste.
    """
    _handleValue_(_list_, [False], "typetall")
    mentions = {}
    for item in _list_:
        if item in mentions.keys:
            mentions[item] += 1
        else:
            mentions[item] = 1
    most_mentioned_item = max(mentions, key=mentions.get)
    return most_mentioned_item
def variasjonsbredde(_list_: list) -> int or float:
    """
    Regner ut variasjonsbredden av en liste (int eller float)

    Parametere:
    - _list_ (uansett datatype): Dette er listen som funksjonen regner ut variasjonsbredden på.

    Retunerer:
    int eller float (kan variere på hvilken av typene som brukes i listen): Dette er det største tallet minus det minste tallet, altså variasjonsbredden.

    Eksempel for bruk:
    ```python
    from MultiLib import variasjonsbredde
    liste = [1, 2, 2, 3]
    print(variasjonsbredde(liste))
    # Output: 2 (som int, fordi det var den datatypen som listen brukte)
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste, og inneholder bare tall og desimaler.
    """
    _handleValue_(_list_, [int, float, list], "variasjonsbredde")
    return max(_list_) - min(_list_)
def gjennomsnitt(_list_: list) -> int or float:
    """
    Regner ut gjennomsnittet av en liste (int eller float)

    Parametere:
    - _list_ (int eller float): Dette er listen som funksjonen regner ut gjennomsnittet på.

    Retunerer:
    gjennomsnitt (datatype varierer basert på hva du bruker som parametere): Dette er kvotienten til summen av alle tallene i listen, delt på hvor mange tall det var (gjennomsnittet).

    Eksempel for bruk:
    ```python
    from MultiLib import gjennomsnitt
    liste = [1, 2, 2, 3]
    print(gjennomsnitt(liste))
    # Output: 2 (som int, fordi det var den datatypen som listen brukte)
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste, og inneholder bare tall og desimaler.
    """
    _handleValue_(_list_, [int, float, list], "gjennomsnitt")
    sum = 0
    for item in _list_:
        sum += item
def median(_list_: list) -> int or float:
    """
    Regner ut medianet av en liste (int eller float)

    Parametere:
    - _list_ (int eller float): Dette er listen som funksjonen regner ut medianet på.

    Retunerer:
    medianet (datatype varierer basert på hva du bruker som parametere): Dette er medianet til listen (tallet i midten).

    Eksempel for bruk:
    ```python
    from MultiLib import median
    liste = [1, 2, 2, 3]
    print(median(liste))
    # Output: 2 (som int, fordi det var den datatypen som listen brukte)
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste, og inneholder bare tall og desimaler.
    """
    _handleValue_(_list_, [int, float, list], "median")
    return Med(_list_)
def potens(base: int | float, exponent: int | float) -> int or float:
    """
    Regner ut en potensen (int eller float)

    Parametere:
    - _list_ (int eller float): Dette er listen som funksjonen regner ut medianet på.

    Retunerer:
    int eller float (datatype varierer basert på hva du bruker som parametere): Dette er slutt verdien til potensen.

    Eksempel for bruk:
    ```python
    from MultiLib import potens
    print(potens(2, 1))
    # Output: 2 (som int, fordi det var den datatypen som listen brukte)
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste, og inneholder bare tall og desimaler.
    """
    _handleValue_(base, [int, float], "potens")
    _handleValue_(exponent, [int, float], "potens")
    try:
        pow(base, exponent)
    except:
        raise Exception("ERROR - function: potens,\nDuring the calculation, the number went over the max allowed value, to fix this, use:\nimport sys\nsys.set_int_max_str_digits(0)")
