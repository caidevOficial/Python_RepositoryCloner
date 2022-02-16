# GNU General Public License V3
# 
# Copyright (c) 2022 [FacuFalcone]
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

import requests
from DataFrameHandler_Mod.DFHandler import DataFrameHandler as DFH
from pandas import DataFrame
from PrintMessage_Mod.CloneMessenger import CloneMessenger as CM


class DataManager:
    #!TODO: Implement Pandas
    """[summary]\n
    Class in charge of the file management to read and process the \n
    data of the students in order to clone their repositorys.\n
    Returns:
        [class]: [DataManager].\n
    """
    #########? START ATTRIBUTES #########
    __configAPIURL = ''
    __name = ''
    __version = ''
    __commands: list = []
    __Messenger: CM = CM()
    __studentsInfo: DataFrame = DataFrame()
    __APIResponse = None
    __cloningMessages:list = []
    ########? END ATTRIBUTES #########

    def __init__(self):
        pass

    def InitialConfig(self, name:str, version:str, APIURL:dict):
        """[summary]\n
        Initialize the config of the class.\n
        Args:
            name (str): [The name of the program].\n
            version (str): [The version of the program].\n
            APIURL (dict): [The API URL of the program].\n
        """
        self.SetAppName(name)
        self.SetAppVersion(version)
        self.SetAPIURL(APIURL)
        self.APIResponse = self.GetAPIURL()

    #########? SETTERS #########

    def SetFilename(self, fileName:str)->None:
        """[summary]\n
        Set the name of the file to read.\n
        Args:
            fileName (str): [The name of the file to read].\n
        """
        self.fileName = fileName
    
    def SetAppName(self, name:str)->None:
        """[summary]\n
        Set the name of the file.\n
        Args:
            name (str): [The name of the file].\n
        """
        self.__name = name
    
    def SetAppVersion(self, version:str)->None:
        """[summary]\n
        Set the version of the file.\n
        Args:
            version (str): [The version of the file].\n
        """
        self.__version = version

    def SetAPIURL(self, api:dict)->None:
        """[summary]\n
        Set the URL of the API.\n
        Args:\n
            api (str): [The URL of the API]\n
            "URL": "https://api.github.com/repos",\n
            "USER": "CaidevOficial",\n
            "REPO": "Python_Udemy_DataManipulation",\n
            "BRANCH": "main" \n
            Example: "https://api.github.com/repos/CaidevOficial/Python_Udemy_DataManipulation/commits/main".\n
        """
        self.__configAPIURL = f'{api["URL"]}/{api["USER"]}/{api["REPO"]}/commits/{api["BRANCH"]}'

    def AddComand(self, command:str)->None:
        """[summary]\n
        Add a command to the list of the commands.\n
        Args:
            command (str): [The command to add].\n
        """
        self.__commands.append(command)

    def SetStudentsDF(self, students: DataFrame)->None:
        """[summary]\n
        Sets the dataframe of students to work with.\n
        Args:
            students (DataFrame): The dataframe of students to work.\n
        """
        self.__studentsInfo = students

    ########? GETTERS #########

    def GetCommands(self)->list:
        """[summary]\n
        Get the commands to clone the repositories of the students.\n
        Returns:
            list: [The list of the commands to execute].\n
        """
        return self.__commands
    
    def GetAppName(self)->str:
        """[summary]\n
        Get the name of the application.\n
        Returns:
            str: [The name of the application].\n
        """
        return self.__name
    
    def GetAppVersion(self)->str:
        """[summary]\n
        Get the version of the application.\n
        Returns:
            str: [The version of the application].\n
        """
        return self.__version

    def GetFilename(self)->str:
        """[summary]\n
        Get the name of the file.\n
        Returns:
            str: [The name of the file].\n
        """
        return self.fileName

    def GetAPIURL(self)->str:
        """[summary]\n
        Get the URL of the API.\n
        Returns:
            str: [The URL of the API].\n
        """
        return self.__configAPIURL

    def GetDate(self)->str:
        """[summary]\n
        Get the date from the API.\n
        Returns:
            str: [The date formatted without the dashes].\n
        """
        date = self.APIResponse.json()["commit"]["author"]["date"]
        date = date[:10]
        return date.replace("-","")

    def GetStudentsDF(self)->DataFrame:
        """[summary]\n
        Gets the Students DataFrame of the class to work with.\n
        Returns:
            DataFrame: The Actual DataFrame of the students.\n
        """
        return self.__studentsInfo

    #########? END GETTERS #########
    
    #########? PROPERTIES #########

    @property
    def Messenger(self)->CM:
        """[summary]\n
        Get the Messenger of the class.\n
        Returns:
            CM: [The Messenger of the class].\n
        """
        return self.__Messenger

    @property
    def Commands(self):
        """[summary]\n
        Get the commands to clone the repositories of the students.\n
        Returns:
            list: [The list of the commands to execute].\n
        """
        return self.__commands
    
    @Commands.setter
    def Commands(self, commands:list):
        """[summary]\n
        Set the commands to clone the repositories of the students.\n
        Args:
            commands (list): [The list of the commands to execute].\n
        """
        self.__commands = commands

    @property
    def APIResponse(self)->str:
        """[summary]\n
        Get the API Response.\n
        Returns:
            str: [The API Response].\n
        """
        return self.__APIResponse
    
    @APIResponse.setter
    def APIResponse(self, APILink:str):
        """[summary]\n
        Set the API Response by sending a request trough the API link.\n
        Args:
            APILink (str): [The Link of the API].\n
        """
        self.__APIResponse = requests.get(APILink)

    @property
    def CloningMessages(self)->list:
        """[summary]\n
        Get the list of the cloning messages.\n
        Returns:
            list: [The list of the cloning messages].\n
        """
        return self.__cloningMessages
    
    @CloningMessages.setter
    def CloningMessages(self, cloningMessage:str):
        """[summary]\n
        Adds a message to the cloning messages.\n
        Args:
            cloningMessage (str): [The message to add].\n
        """
        self.__cloningMessages.append(cloningMessage)

    ########? END PROPERTIES #########

    #########? METHODS #########

    def NormalizeURL(self, url:str)->str:
        """[summary]\n
        Normalize the URLs of the git's repositorys of the students,\n
        adding the .git at the end if it is not already there.\n
        Args:
            url (str): [The crudal url of the git's repository].\n
        Returns:
            str: [The normalized url].\n
        """
        if not ".git" in url:
            url = url.replace('\n','')
            url = f'{url}.git'
        return url.replace("\\n","")

    def NormalizeCourse(self, course:str)->str:
        """[summary]\n
        Normalize the course name, removing the spaces.\n
        Args:
            course (str): [The course name].\n
        Returns:
            str: [The normalized course name].\n
        """
        return course.replace(' - ', '-').replace(" ","_")

    def FormatFullnameDate(self, surname:str, name:str)->str:
        """[summary]\n
        Format the surname of the student, removing the spaces and replacing them with '_'\n
        Args:
            surname (str): [The surname of the student].\n
            name (str): [The name of the student].\n
            date (str): [The date of the student].\n
            Returns:
                str: [The formatted Fullname like this: surname_name_date].\n
        """
        surname = surname.replace(",","_").replace(" ","").replace("\n","")
        name = name.replace(",","_").replace(" ","").replace("\n","")
        
        return f'{surname}_{name}_{self.GetDate()}'
    
    def FormatCourse(self, fieldList:str)->str:
        """[summary]\n
        Format the course of the student, removing the line jumps and replacing them with '_'\n
        Args:
            fieldList (str): [The field of the course. It is the second field of the csv file].\n
        Returns:
            str: [The formatted course].\n
        """
        return self.NormalizeCourse(fieldList.replace("\n",""))

    def MakeCloneCommands(self, dfHandler: DFH)->None:
            """[summary]\n
            Make the commands to clone the repositories of the students.\n
            Args:
                surname (str): [The surname of the student].\n
                course (str): [The course of the student].\n
                git (str): [The url of the git's repository].\n    
            """
            for frame in dfHandler.OrderListOfDFStudents:
                self.MakeCloneCommandsForDF(frame, dfHandler)
            
    def MakeCloneCommandsForDF(self, df: DataFrame, dfHandler: DFH)->None:
        """[summary]\n
        Make the commands to clone the repositories of the students.\n
        Args:
            df (DataFrame): [The DataFrame with the students information].\n
        """
        for i in df.index:
            crudeCourse = df[dfHandler.ConfigsJsonValues['Course']][i]
            courseStr = self.NormalizeCourse(self.FormatCourse(crudeCourse))
            surnameStr = df[dfHandler.ConfigsJsonValues['Surname']][i]
            nameStr = df[dfHandler.ConfigsJsonValues['Name']][i]
            message = f"Cloning {surnameStr}, {nameStr}'s repository from {crudeCourse}"
            command = f"git clone {self.NormalizeURL(df[dfHandler.ConfigsJsonValues['GitLink']][i])} {courseStr}//{self.FormatFullnameDate(surnameStr, nameStr)}"
            self.AddComand(command)
            self.CloningMessages = message

    def ExecuteCommands(self, cloneMessenger: CM)->None:
        """[summary]\n
        Execute the commands to clone the repositories of the students.\n
        Args:
            commandList (list): [The list of the commands to execute].\n
        """
        
        commandList = [x.strip() for x in self.Commands]
        messages = [x.strip() for x in self.CloningMessages]

        for command in commandList:
            cloneMessenger.SetMessage(messages[commandList.index(command)])
            cloneMessenger.PrintMessage()
            os.system(command)

    def CloneRepositories(self, DfH: DFH, )->None:
        """[summary]\n
        Open the file and get the data.\n
        """
        appInfo = f'{self.GetAppName()} - {self.GetAppVersion()}'
        self.Messenger.SetMessage(appInfo)
        self.Messenger.PrintMessage()

        try:
            #? Create git Clone commands
            self.MakeCloneCommands(DfH)

            #? Execute the commands
            self.ExecuteCommands(self.Messenger)
            
            # self.__Messenger.SetMessage('All Repositories have been cloned!')
            # self.__Messenger.PrintMessage()
        except Exception as e:
            self.Messenger.SetMessage(f'Exception: {e.args}')
            self.__Messenger.PrintMessage()
    
    #########? END METHODS #########
