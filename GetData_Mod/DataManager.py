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
#import pandas as pd
#from pandas import DataFrame as df
from PrintMessage_Mod.CloneMessenger import CloneMessenger as CM


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
    #__studentsInfo: pd.DataFrame = pd.DataFrame()

    def __init__(self, fileName:str, name:str, version:str, APIURL:str):
        self.SetFilename(fileName)
        self.SetAppName(name)
        self.SetAppVersion(version)
        self.SetAPIURL(APIURL)

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

    def SetAPIURL(self, api:str)->None:
        """[summary]
        Set the URL of the API
        Args:
            api (str): [The URL of the API]
        """
        self.__configAPIURL = api

    def AddComand(self, command:str)->None:
        """[summary]
        Add a command to the list of the commands
        Args:
            command (str): [The command to add]
        """
        self.__commands.append(command)

    def GetCommands(self)->list:
        """[summary]
        Get the commands to clone the repositories of the students
        Returns:
            list: [The list of the commands to execute]
        """
        return self.__commands

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
                lines:list = f.readlines()
                for line in lines:
                    fieldList = line.split(';')
                    fieldList = [x.strip() for x in fieldList]

                    if len(fieldList)>=4:
                        message = f'Cloning repository of {fieldList[0]}'
                        self.__Messenger = CM(message)
                        studentGitUrl = fieldList[4]
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

    def FormatSurname(self, fieldList:list, date)->str:
        """[summary]
        Format the surname of the student, removing the spaces and replacing them with _
        Args:
            fieldList (list): [The list of the fields of the student]
            date (str): [The date of the student]
            Returns:
                str: [The formatted surname]
        """
        surname = fieldList[0].replace(",","_").replace(" ","").replace("\n","")
        return f'{surname}_{date}'
    
    def FormatCourse(self, fieldList:str)->str:
        """[summary]
        Format the course of the student, removing the line jumps and replacing them with _
        Args:
            fieldList (str): [The field of the course. It is the second field of the csv file]
        Returns:
            str: [The formatted course]
        """
        return fieldList[1].replace("\n","")
        
    def MakeCloneCommands(self, surname:str, course:str, git:str)->None:
        """[summary]
        Make the commands to clone the repositories of the students
        Args:
            surname (str): [The surname of the student]
            course (str): [The course of the student]
            git (str): [The url of the git's repository]    
        """
        command = f'git clone {git} {course}//{surname}'
        self.AddComand(command)

    def ExecuteCommands(self, commandList:list)->None:
        """[summary]
        Execute the commands to clone the repositories of the students
        Args:
            commandList (list): [The list of the commands to execute]
        """
        commandList = [x.strip() for x in commandList]
        for command in commandList:
            os.system(command)
