from os import system, getcwd, mkdir, path, remove

class data:
    """
    Dette er en enkel måte å lagre data i programmet ditt på,
    for å starte, importer multilib (en * for å importere alle funksjoner derfra)\nlag en variabel og kall den hva du vil at datasettet skal hete\nog skriv data(), husk å bruke navnet på variablen som det første parameteret:
    ```python
    from multiLib import *
    myData = data("myData")
    ```
    Eller du kan for eksempel skru på automatisk lagring, sånn at hver gang du oppdaterer dataen, lagres den uten at du trenger\nå bruke save() funksjonen:
    ```python
    from multiLib import *
    myData = data("myData", autoSave=True)
    ```
    Deretter kan du bruke funksjoner som myData.save() eller myData.content("Hello world")
    """
    instances = []
    content_ = []

    def __init__(self, filename: str, autoSave: bool = False) -> None:
        self.deleted = False
        self.filename = filename
        tempData = __file__.removesuffix(".py")
        self.dirPath = str(path.join(getcwd(), f"{tempData}_pydata"))
        self.autoSave = autoSave
        self.data: str = ""
        try: mkdir(self.dirPath)
        except Exception as ex: ...
        try:
            f = open(
                str(path.join(self.dirPath, f"{str(self.filename)}.pydata")),
                "a")
            f.write("")
            f.close()
        except Exception as Ex:
            raise Exception("ERROR : Function: data() -", Ex)
        self.storePath = str(path.join(self.dirPath, f"{str(self.filename)}.pydata"))
        data.instances.append(str(self.storePath))
        data.content_.append(self.data)

    def save(self) -> None:
        """
        Lagrer data for klassen \'data\'

        Parametere:
        Ingen.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.content("Hello world")
        myData.save()
        # Output: (Dataen er lagret)
        ```
        """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        f = open(
                str(path.join(self.dirPath, f"{str(self.filename)}.pydata")),
                "w")
        f.write(str(self.data))
        f.close()
    
    def read(self) -> str:
        """
        Leser data for klassen \'data\'

        Parametere:
        Ingen.

        Retunerer:
        - string: Hva som var lagret

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.content("Hello world")
        myData.save()
        print(myData.read())
        # Output: \"Hello world\"
        ```
        """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        f = open(str(self.storePath), "r")
        a = f.read()
        f.close()
        return a

    def append(self, content: str) -> None:

        """
        Legger til data for klassen \'data\' uten å fjerne det gammle

        Parametere:
        - content (str): Dette er hva du vil legge til.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.content("Hello world")
        myData.append(\"Bye world\")
        myData.save()
        # Output: (Dataen er lagret, og det står to linjer med tekst: \'Hello world\', og \'Bye world\')
        ```
    """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        index = data.content_.index(str(self.data))
        self.data += f"\n{str(content)}"
        data.content_[index] = str(self.data)
        if self.autoSave:
            self.save()
    
    def content(self, content: str) -> None:
        
        """
        Overskriver data for klassen \'data\'

        Parametere:
        - content (str): Dette er hva du vil sette den nye dataen til.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.content("Hello world")
        myData.save()
        # Output: (Dataen er lagret)
        ```
        """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        index = data.content_.index(str(self.data))
        self.data = str(content)
        data.content_[index] = str(self.data)
        if self.autoSave:
            self.save()
    
    def delete(self) -> None:
        """
        sletter data for klassen \'data\'
        
        OBS! Etter ett datasett er slettet, kan 
        ikke samme navn bli brukt igjen
        
        Parametere:
        Ingen.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.delete()
        # Output: (Dataen er som var lagret før, blir slettet (hvis det var lagret noe fra før))
        ```
        """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        self.deleted = True
        data.content_.remove(str(self.data))
        data.instances.remove(str(self.storePath))
        remove(self.storePath)
        return
    
    def openWithNotepad(self) -> None:

        """
        Åpner data for klassen \'data\' i notepad (ett program i windows)

        Parametere:
        Ingen.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData = data("myData")
        myData.content("Hello world")
        myData.save()
        myData.openWithNotepad()
        # Output: (Dataen åpnes i notepad.exe)
        ```
    """
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        system("notepad " + str(self.storePath))

    def getPath(self) -> str:
        if self.deleted:
            raise Exception("ERROR - You can not use the data you have deleted!")
        return str(self.storePath)

def saveAll():
    """
        Lagrer all data for klassen \'data\'

        Parametere:
        Ingen.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData1 = data("myData1")
        myData1.content("Hello world")

        #data 2
        myData2 = data("myData2")
        myData2.content("Hello world again")

        saveAll()
        # Output: (Dataen er lagret)
        ```
    """
    for instance in data.instances:
        f = open(
                str(instance),
                "w")
        f.write(str(data.content_[data.instances.index(instance)]))
        f.close()
    
def deleteAll():
    """
        SLETTER *ALL* data for klassen \'data\'

        Parametere:
        Ingen.

        Retunerer:
        Ingenting. (None)

        Eksempel for bruk:
        ```python
        from MultiLib import data
        myData1 = data("myData1")
        myData1.content("Hello world")

        #data 2
        myData2 = data("myData2")
        myData2.content("Hello world again")

        deleteAll()
        # Output: (Dataen er lagret)
        ```
        """
    
    for instance in data.instances:
        remove(str(instance))
    data.instances = data.content_ = []

