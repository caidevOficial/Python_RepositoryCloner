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
from PrintMessage_Mod.CloneMessenger import CloneMessenger as CM
from DataFrameHandler_Mod.DFHandler import DataFrameHandler as DFH

import pandas as pd
from pandas import DataFrame


class DataManager:
    #!TODO: Implement Pandas
    """[summary]
    Class in charge of the file management to read and process the 
    data of the students in order to clone their repositorys.
    Returns:
        [class]: [DataManager]
    """
    __configAPIURL = ''
    __name = ''
    __version = ''
    __commands: list = []
    __Messenger: CM = None
    __studentsInfo: DataFrame = DataFrame()

    def __init__(self):
        pass

    def InitialConfig(self, name:str, version:str, APIURL:dict):
        #self.SetFilename(fileName)
        self.SetAppName(name)
        self.SetAppVersion(version)
        self.SetAPIURL(APIURL)

    #* SETTERS

    def SetFilename(self, fileName:str)->None:
        """[summary]
        Set the name of the file to read
        Args:
            fileName (str): [The name of the file to read]
        """
        self.fileName = fileName
    
    def SetAppName(self, name:str)->None:
        """[summary]
        Set the name of the file
        Args:
            name (str): [The name of the file]
        """
        self.__name = name
    
    def SetAppVersion(self, version:str)->None:
        """[summary]
        Set the version of the file
        Args:
            version (str): [The version of the file]
        """
        self.__version = version

    def SetAPIURL(self, api:dict)->None:
        """[summary]
        Set the URL of the API
        Args:
            api (str): [The URL of the API]
            "URL": "https://api.github.com/repos",
            "USER": "CaidevOficial",
            "REPO": "Python_Udemy_DataManipulation",
            "BRANCH": "main"
        """
        self.__configAPIURL = f'{api["URL"]}/{api["USER"]}/{api["REPO"]}/{api["BRANCH"]}'

    def AddComand(self, command:str)->None:
        """[summary]
        Add a command to the list of the commands
        Args:
            command (str): [The command to add]
        """
        self.__commands.append(command)

    def SetStudentsDF(self, students: DataFrame)->None:
        """[summary]
        Sets the dataframe of students to work with.
        Args:
            students (DataFrame): The dataframe of students to work
        """
        self.__studentsInfo = students

    #* GETTERS

    def GetCommands(self)->list:
        """[summary]
        Get the commands to clone the repositories of the students
        Returns:
            list: [The list of the commands to execute]
        """
        return self.__commands
    
    @property
    def Commands(self):
        """[summary]
        Get the commands to clone the repositories of the students
        Returns:
            list: [The list of the commands to execute]
        """
        return self.__commands
    
    @Commands.setter
    def Commands(self, commands:list):
        """[summary]
        Set the commands to clone the repositories of the students
        Args:
            commands (list): [The list of the commands to execute]
        """
        self.__commands = commands

    def GetAppName(self)->str:
        """[summary]
        Get the name of the application
        Returns:
            str: [The name of the application]
        """
        return self.__name
    
    def GetAppVersion(self)->str:
        """[summary]
        Get the version of the application
        Returns:
            str: [The version of the application]
        """
        return self.__version

    def GetFilename(self)->str:
        """[summary]
        Get the name of the file
        Returns:
            str: [The name of the file]
        """
        return self.fileName

    def GetAPIURL(self)->str:
        """[summary]
        Get the URL of the API
        Returns:
            str: [The URL of the API]
        """
        return self.__configAPIURL

    def GetDate(self, api:str)->str:
        """[summary]
        Get the date from the API
        Args:
            api (str): [The link of the API to consume]
        Returns:
            str: [The date formatted without the dashes]
        """
        date = requests.get(api)
        date = date.json()["commit"]["author"]["date"]
        date = date[:10]
        return date.replace("-","")

    def GetStudentsDF(self)->DataFrame:
        """[summary]
        Gets the Students DataFrame of the class to work with.
        Returns:
            DataFrame: The Actual DataFrame of the students
        """
        return self.__studentsInfo

    def NormalizeURL(self, url:str)->str:
        """[summary]
        Normalize the URLs of the git's repositorys of the students, 
        adding the .git at the end if it is not already there
        Args:
            url (str): [The crudal url of the git's repository]
        Returns:
            str: [The normalized url]
        """
        if not ".git" in url:
            url = url.replace('\n','')
            url = f'{url}.git'
        return url.replace("\\n","")

    def NormalizeCourse(self, course:str)->str:
        """[summary]
        Normalize the course name, removing the spaces.
        Args:
            course (str): [The course name]
        Returns:
            str: [The normalized course name]
        """
        return course.replace(' - ', '-').replace(" ","_")

    def FormatFullnameDate(self, surname:str, name:str)->str:
        """[summary]
        Format the surname of the student, removing the spaces and replacing them with _
        Args:
            surname (str): [The surname of the student]
            name (str): [The name of the student]
            date (str): [The date of the student]
            Returns:
                str: [The formatted Fullname like this: surname_name_date]
        """
        surname = surname.replace(",","_").replace(" ","").replace("\n","")
        name = name.replace(",","_").replace(" ","").replace("\n","")
        
        return f'{surname}_{name}_{self.GetDate(self.GetAPIURL())}'
    
    def FormatCourse(self, fieldList:str)->str:
        """[summary]
        Format the course of the student, removing the line jumps and replacing them with _
        Args:
            fieldList (str): [The field of the course. It is the second field of the csv file]
        Returns:
            str: [The formatted course]
        """
        return self.NormalizeCourse(fieldList[3].replace("\n",""))
        
    # def MakeCloneCommands(self, surname:str, course:str, git:str)->None:
    #     """[summary]
    #     Make the commands to clone the repositories of the students
    #     Args:
    #         surname (str): [The surname of the student]
    #         course (str): [The course of the student]
    #         git (str): [The url of the git's repository]    
    #     """
    #     command = f'git clone {git} {course}//{surname}'
    #     self.AddComand(command)
    
    #def MakeCloneCommands(self, dfHandler:DataFrame, surname:str, name:str, course:str, git:str)->None:
    def MakeCloneCommands(self, dfHandler: DFH, df: DataFrame, configJsonFields: dict)->None:
            """[summary]
            Make the commands to clone the repositories of the students
            Args:
                surname (str): [The surname of the student]
                course (str): [The course of the student]
                git (str): [The url of the git's repository]    
            """
            for index, row in dfHandler.iterrows():
                courseStr = self.NormalizeCourse(self.FormatCourse(row[configJsonFields['Course']]))
                surnameStr = row[configJsonFields['Surname']]
                nameStr = row[configJsonFields['Name']]
                command = f"git clone {self.NormalizeURL(row[configJsonFields['GitLink']])} {courseStr}//{self.FormatFullnameDate(surnameStr, nameStr)}"
                self.AddComand(command)
            
            

    def ExecuteCommands(self)->None:
        """[summary]
        Execute the commands to clone the repositories of the students
        Args:
            commandList (list): [The list of the commands to execute]
        """
        commandList = [x.strip() for x in self.Commands]
        for command in commandList:
            os.system(command)

    #!TODO: Implement Pandas
    def OpenFile(self)->None:
        """[summary]
        Open the file and get the data
        """
        #file = pd.read_csv(self.fileName)
        appInfo = f'{self.GetAppName()} - {self.GetAppVersion()}'
        self.__Messenger = CM(appInfo)
        self.__Messenger.PrintMessage()

        try:
            with open(self.GetFilename(), 'r') as f:
                lines:list = f.readlines()[1::]
                for line in lines:
                    fieldList = line.split(',')
                    fieldList = [x.strip().replace('"', '') for x in fieldList]

                    if len(fieldList)>=6:
                        message = f'Cloning repository of {fieldList[2]}, {fieldList[1]}'
                        self.__Messenger = CM(message)
                        studentGitUrl = fieldList[6]
                        api = self.GetAPIURL()
                        date = self.GetDate(api)

                        self.__Messenger.PrintMessage()

                        self.MakeCloneCommands(
                            self.FormatSurname(fieldList, date), 
                            self.FormatCourse(fieldList), 
                            self.NormalizeURL(studentGitUrl)
                        )
                        self.ExecuteCommands(self.GetCommands())
            self.__Messenger.SetMessage('All Repositories have been cloned!')
            self.__Messenger.PrintMessage()
        except Exception as e:
            self.__Messenger = CM(e)
            self.__Messenger.PrintMessage()
    
    #def DoMagic(self, dfHandler: DFH):


