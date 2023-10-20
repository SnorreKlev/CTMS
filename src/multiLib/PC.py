#PC
from time import sleep
from os import system, getcwd
import importlib, subprocess
import messagebox
CanUsePyperclip = False
try:
    import pyperclip
except:
    None
else:
    CanUsePyperclip = True
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

def wait(time: int | float) -> None:
    """
    Venter før programmet fortsetter med koden.

    Parametere:
    - time (int eller float): Dette er hvor mange sekunder programmet skal vente.

    Retunerer:
    Ingenting. (None)

    Eksempel for bruk:
    ```python
    from MultiLib import wait
    wait(1)
    print("Hello world")
    # Output: (Etter 1 sekund) Hello world
    ```
    Merk:
    - Denne funksjonen forventer at _list_ (parameteret) er en liste, og inneholder bare tall og desimaler.
    """
    _handleValue_(time, [int, float], "wait")
    sleep(time)

def cmd(arg: str) -> None:
    """
    Sender ett argument til ledetekst (Der programmet kjører, også kaldt \'CMD\')

    Parametere:
    - arg (str): Dette hva programmet skal sende til cmd

    Retunerer:
    Ingenting. (None)

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import cmd
    cmd("color 4")
    # Output: (Tekst fargen til programmet blir rød)
    ```
    Merk:
    - Denne funksjonen forventer at arg (parameteret) er en string, og inneholder bare tekst og symboler.
    """
    _handleValue_(arg, [str], "cmd")
    try:
        system(arg)
    except Exception as exc:
        raise Exception(f"ERROR - function: cmd, An error occured while tring to execute the command: \'{arg}\'\nError received: {exc}")

def installPipe(module_name: str) -> bool:
    """
    Installerer en pipe (modul), men vis den er installert fra før, gjør den ingen ting.

    Parametere:
    - module_name (str): Dette er hvilken modul som skal installeres, for eksempel: \'pygame\'

    Retunerer:
    \'True\' hvis pip\'en er installert fra før.

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import installPipe
    installPipe("pygame")
    # Output: (pygame blir installert hvis den ikke var det fra før)
    ```
    Merk:
    - Denne funksjonen forventer at arg (parameteret) er en string, og inneholder bare tekst og noen få symboler.
    """
    _handleValue_(module_name, [str], "installerModul")
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        print(f"The module '{module_name}' is not installed. Attempting to install...")
        try:
            subprocess.check_call(["pip", "install", module_name])
            print(f"The module '{module_name}' has been successfully installed.")
        except Exception as e:
            raise Exception(f"Failed to install the module '{module_name}'. Error: {str(e)}")
        
def copy(arg: str) -> None:
    """
        OBS: Hvis pyperclip ikke er installert på forhånd, kan ikke denne funksjonen brukes!

        Kopierer tekst til utklippstavla. (ctrl + v får å lime inn, eller win + v for å vise historikk)

        Parametere:
        - arg (str): Dette hva funksjonen skal kopiere.

        Retunerer:
        Ingenting. (None)

        OBS: Programmet sender en feilmelding hvis prosessen feiler!

        Eksempel for bruk:
        ```python
        from MultiLib import copy
        copy("Hello world")
        # Output: (Hvis du gjør ctrl + v limer den inn \'Hello world\'. Den har dermed kopiert \'Hello world\' til utkippstavla)
        ```
        Merk:
        - Denne funksjonen forventer at arg (parameteret) er en string, og inneholder bare tekst og symboler.
        """
    if CanUsePyperclip == False:
        raise Exception("ERROR - function: limInn, Pyperclip is not installed or is accessible! (to install it, run \'pip install pyperclip\' in cmd)")
    else:
        _handleValue_(arg, [str], "kopier")
        try: pyperclip.copy(arg)
        except Exception as Exc:
            raise Exception("ERROR - function: kopier, when trying to copy text to clipboard, this error occured:\n", + str(Exc))

def paste() -> str:
    """
    OBS: Hvis pyperclip ikke er installert på forhånd, kan ikke denne funksjonen brukes!

    limer inn tekst fra utklippstavla. (ctrl + v får å lime inn, eller win + v for å vise historikk)

    Parametere:
    Ingen.

    Retunerer:
    - Str: Hva som var på utklippstavla (det som ble limt inn).

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import paste
    print(paste())
    # Output: (den printer ut hva som var på utklippstavla)
    ```
    """
    if CanUsePyperclip == False:
        raise Exception("ERROR - function: limInn, Pyperclip is not installed or is accessible! (to install it, run \'pip install pyperclip\' in cmd)")
    else:
        return pyperclip.paste()

def shutdown(mode, delay, reason):
    """
    Skrur av eller restarter pc'en

    Parametere:
    - mode (str, OBS: Denne verdien kan bare være \'shutdown\' eller \'restart\'!): Denne verdien bestemmer om pc'en skal restarte eller skru seg av.
    - delay (int): Dette er hvor lang tid det tar fra meldingen (reason) vises til marskinen skrur seg av eller restarter.
    - reason (str, OBS: Du kan ikke ha symboler som \" eller \' i meldingen! ): Dette er meldingen som vises rett etter funksjonen kjøres.

    Retunerer:
    Ingenting. (None)

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import shutdown
    shutdown("shutdown", 5, "Dette er en test.")
    # Output: (pc'en skrur seg av etter fem sekunder, mens den viser meldingen \'Dette er en test.\')
    ```
    """
    _handleValue_(mode, [str], "shutdown")
    _handleValue_(delay, [int], "shutdown")
    _handleValue_(reason, [str], "shutdown")
    match mode:
        case "shutdown":
            MODE = "s"
        case "restart":
            MODE = "r"
        case _:
            raise Exception("ERROR - function: shutdown, mode can only be \'shutdown\' or \'restart\'!")
    system(f"shutdown /{MODE} /t {delay} /c \"{reason}\"")

def cancelShutdown():
    """
    Stopper pc'en fra ett planlagt restart eller avsluttelse.
    Parametere:
    Ingen.

    Retunerer:
    Ingenting. (None)

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import shutdown, cancelShutdown
    shutdown("shutdown", 5, "Dette er en test.")
    cancelShutdown()
    # Output: (pc'en skrur seg av etter fem sekunder, mens den viser meldingen \'Dette er en test.\', men blir avbrutt av cancelShutdown funksjonen som hindrer den fra å skru seg av.)
    ```
    """
    system("shutdown /a")

class yes_no: ...
class retry_cancel: ...
class yes_no_cancel: ...
class ok_cancel: ...

def messageBox(title: str, question: str, mode: yes_no | retry_cancel | yes_no_cancel | ok_cancel = yes_no) -> str:
    """
    Spør brukeren om ett spørsmål via ett annet vindu
    Parametere:
    - title (str): Dette er hva tittelen på spørsmålet skal være.
    - question (str): Dette er hva du vil spørre om.
    - mode (frivillig, men må være enten: yes_no, retry_cancel, yes_no_cancel eller ok_cancel og er yes_no som standard)

    Retunerer:
    - svar (str): Hva brukeren svarte, hvis de trykker \'No\' returnerer den \'no\', mens hvis brukeren svarer retry for eksempel, returnerer den det.

    OBS: Programmet sender en feilmelding hvis prosessen feiler!

    Eksempel for bruk:
    ```python
    from MultiLib import messageBox
    a=messageBox("Warning", "Do you want to continue?!")
    if a == \"no\":
        exit()
    # Output: (Hvis du trykker no, stopper programmet)
    ```
    """
    if mode == yes_no:
        a= messagebox.askyesno(title, question)
        if a==True:
            return "yes"
        else:
            return "no"
    elif mode == retry_cancel:
        a= messagebox.askretrycancel(title, question)
        if a==True:
            return "retry"
        else:
            return "cancel"
    elif mode == yes_no_cancel:
        a= messagebox.askyesnocancel(title, question)
        if a==True:
            return "yes"
        elif a==None:
            return "cancel"
        else:
            return "no"
    elif mode == ok_cancel:
        a= messagebox.askokcancel(title, question)
        if a==True:
            return "yes"
        else:
            return "cancel"

