#General
from time import sleep
from os import system

def _handleValue_(value, allowed_types, fn) -> bool:
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


def sjekkVerdi(value, allowed_types, functionName, raiseError=True) -> bool:
    """
    Sjekker om en verdi eller liste er en av de aksepterte datatypene,
    hvis den ikke er det, kan du velge å vise en feilmelding, eller returnere veriden \"False\"
    (vis det er en liste, sjekker den om alle verdiene innenfor listen er av godkjente datatyper også, så hvis du har en liste, må list være en av de godkjente datatypene)

    Parametere:
    - value (hvilken som helst datatype): Dette er verdien eller listen du vil skjekke om møter dine aksepterte datatyper (allowed_types).
    - allowed_types (en liste med datatyper, eksempel: \'[str, list]\'. Vis du ønsker å godkjenne alle datatyper bruk: [False], som ett parameter): Dette er en liste med datatyper som er aksepterte.
    - (frivillig, standard er True) raiseError (\'True\' eller \'False\'): Dette er verdien som bestemmer om programmet skal vise en feilmelding, vis denne veriden er usann (\'False\') vil den returnere True eller False, basert på om verdien eller listen var en av de datatypene.
    
    Retunerer:
    Bool (True eller False): møtte verdien din liste med aksepterte verdier? False vis ikke, og True vis den ble godkjent.

    OBS: vis raiseError er satt til \'True\' vil programmet stoppe helt opp, og vise feilmeldingen!

    Eksempel for bruk:
    ```python
    from MultiLib import handleValue
    liste = [1, 2, 2, 3]
    print(handleValue(liste, [int, float, list], "function1", raiseError=False))
    # Output: True
    ```
    """
    if allowed_types[0] == False:
        return True

    if type(value) == list and list in allowed_types:
        for item in value:
            if (type(item) in allowed_types) == False:
                if raiseError:
                    raise Exception(f"ERROR - function: {functionName}, can ONLY take these datatypes: \n{allowed_types}\nOne of the items in your list did not meet these requirements!")
                else:
                    return False
    else:
        if (type(value) in allowed_types) == False:
            if raiseError:
                raise Exception(f"ERROR - function: {functionName}, can ONLY take these datatypes: \n{allowed_types}\nYour value did not meet the requirements for the datatype.")
            else:
                return False
    return True

def GetInput(Question, ValidResponses, ErrorMessage, readingTime=3) -> str:
    """
    Spør ett spørsmål til den får en av de riktige svarene

    Parametere:
    - Question (str): Hva funksjonen spør om.
    - ValidResponses (liste med strings, ints eller floats): Hva man kan svare for å få godkjent.
    - ErrorMessage (str): Hva funksjonen svarer hvis du skriver inn feil svar.
    - (frivillig) readingTime (int): Hvor lang tid du får på å lese feil-svar-meldingen.

    Retunerer:
    Ingenting. (None)

    Eksempel for bruk:
    ```python
    from MultiLib import GetInput
    GetInput("Nevn en hverdag:", ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"], "Det var feil!")
    # Output: (Du blir stilt det sammme spørsmålet helt til du svarer en av de rikige svarene.)
    ```
    """
    _handleValue_(Question, [str], "GetInput")
    _handleValue_(ValidResponses, [list, str], "GetInput")
    _handleValue_(ErrorMessage, [str], "GetInput")
    _handleValue_(readingTime, [int], "GetInput")
    
    for item in ValidResponses:
        str(item).capitalize()

    while True:
        input_ = str(input(Question))
        if  str(input_).capitalize() in ValidResponses:
            return
        else:
            print(str("\n"+str(ErrorMessage)))
            sleep(readingTime)
            system("cls")
            