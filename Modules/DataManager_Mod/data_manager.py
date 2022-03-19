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

from Modules.DataFrameHandler_Mod.df_handler import DataFrameHandler as DFH
from Modules.PrintMessage_Mod.clone_messenger import CloneMessenger as CM
from Modules.Commands_Mod.command_manager import Command as CMD
from pandas import DataFrame


class DataManager:
    """[summary] \n
    Class in charge of the file management to read and process the  \n
    data of the students in order to clone their repositorys. \n
    Returns:
        [class]: [DataManager]. \n
    """
    # ?########? START ATTRIBUTES #########
    __mainDir: str = ''
    __configAPIURL = ''
    __APIResponse = None
    __APIDate = None
    __name = ''
    __version = ''
    __author = ''
    __studentsInfo: DataFrame = DataFrame()
    __Messenger: CM = CM()
    __commands: list[CMD] = []
    __cloningMessages: list[str] = []
    # ?#######? END ATTRIBUTES #########

    def __init__(self):
        pass

    # ?########? PROPERTIES - GET #########

    @property
    def AppAuthor(self) -> str:
        """[summary] \n
        Get the author of the application. \n
        Returns:
            str: [The author of the application]. \n
        """
        return self.__author

    @property
    def Messenger(self) -> CM:
        """[summary] \n
        Get the Messenger of the class. \n
        Returns:
            CM: [The Messenger of the class]. \n
        """
        return self.__Messenger

    @property
    def Commands(self):
        """[summary] \n
        Get the commands to clone the repositories of the students. \n
        Returns:
            list: [The list of the commands to execute]. \n
        """
        return self.__commands

    @property
    def APIResponse(self) -> str:
        """[summary] \n
        Get the API Response. \n
        Returns:
            str: [The API Response]. \n
        """
        return self.__APIResponse

    @property
    def AppName(self) -> str:
        """[summary] \n
        Set the name of the file. \n
        Args:
            name (str): [The name of the file]. \n
        """
        return self.__name

    @property
    def AppVersion(self) -> str:
        """[summary] \n
        Get the version of the application. \n
        Returns:
            str: [The version of the application]. \n
        """
        return self.__version

    @property
    def APIURL(self) -> str:
        """[summary] \n
        Get the URL of the API. \n
        Returns:
            str: [The URL of the API]. \n
        """
        return self.__configAPIURL

    @property
    def StudensDF(self) -> DataFrame:
        """[summary] \n
        Get the dataframe with the students information. \n
        Returns:
            DataFrame: [The dataframe with the students information]. \n
        """
        return self.__studentsInfo

    @property
    def CloningMessages(self) -> list:
        """[summary]  \n
        Get the list of the cloning messages. \n
        Returns:
            list: [The list of the cloning messages]. \n
        """
        return self.__cloningMessages

    @property
    def APIDate(self) -> str:
        """[summary] \n
        Get the date of the API. \n
        Returns:
            str: [The date of the API]. \n
        """
        return self.__APIDate

    @property
    def MainDir(self) -> str:
        """[summary] \n
        Get the main directory to save the downloaded repositories. \n
        Returns:
            str: [The main directory to save the downloaded repositories]. \n
        """
        return self.__mainDir

    # ?########? END PROPERTIES - GET #########

    # ?########? START PROPERTIES - SET #########

    @AppAuthor.setter
    def AppAuthor(self, author: str) -> None:
        """[summary] \n
        Set the author of the application. \n
        Args:
            author (str): [The author of the application]. \n
        """
        self.__author = author

    @Commands.setter
    def Commands(self, commands: list[CMD]):
        """[summary] \n
        Set the commands to clone the repositories of the students. \n
        Args:
            commands (list): [The list of the commands to execute]. \n
        """
        self.__commands = commands

    @APIResponse.setter
    def APIResponse(self, APILink: str):
        """[summary] \n
        Set the API Response by sending a request trough the API link. \n
        Args:
            APILink (str): [The Link of the API]. \n
        """
        self.__APIResponse = requests.get(APILink)

    @AppName.setter
    def AppName(self, name: str) -> None:
        """[summary] \n
        Set the name of the file. \n
        Args:
            name (str): [The name of the file]. \n
        """
        self.__name = name

    @AppVersion.setter
    def AppVersion(self, version: str) -> None:
        """[summary] \n
        Set the version of the file. \n
        Args:
            version (str): [The version of the file]. \n
        """
        self.__version = version

    @APIURL.setter
    def APIURL(self, url: dict) -> None:
        """[summary] \n
        Set the URL of the API. \n
        Args: \n
            url (dict): [The json with all the fields of the API url.] \n
            "URL": "https://api.github.com/repos", \n
            "USER": "Your_Github_User", \n
            "REPO": "Your_Repository", \n
            "BRANCH": "Your_Principal_Branch"  \n
            Example: "https://api.github.com/repos/Your_Github_User/Your_Repository/commits/Your_Principal_Branch". \n
        """
        self.__configAPIURL = f'{url["URL"]}/{url["USER"]}/{url["REPO"]}/commits/{url["BRANCH"]}'

    @StudensDF.setter
    def StudensDF(self, studentsInfo: DataFrame) -> None:
        """[summary] \n
        Set the dataframe of students to work with. \n
        Args:
            studentsInfo (DataFrame): The dataframe of students to work. \n
        """
        self.__studentsInfo = studentsInfo

    @CloningMessages.setter
    def CloningMessages(self, cloningMessage: str):
        """[summary] \n
        Adds a message to the cloning messages. \n
        Args:
            cloningMessage (str): [The message to add]. \n
        """
        self.__cloningMessages.append(cloningMessage)

    @APIDate.setter
    def APIDate(self, APIResponse: str):
        """[summary] \n
        Set the date of the API. \n
        Args:
            APIResponse (str): [The response of the API Setted]. \n
        """
        date = APIResponse.json()["commit"]["author"]["date"]
        date = date[:10]
        self.__APIDate = date.replace("-", "")

    @MainDir.setter
    def MainDir(self, mainDir: str) -> None:
        """[summary] \n
        Set the main directory to save the downloaded repositories. \n
        Args:
            mainDir (str): [The main directory to save the downloaded repositories]. \n
        """
        self.__mainDir = mainDir.strip()

    # ?#######? END PROPERTIES - SET #########

    # ?########? METHODS #########

    def InitialConfig(self, name: str, version: str, author: str, APIURL: dict, mainDir: str):
        """[summary] \n
        Initialize the config of the class, Also sets the API response \n
        and the date of the API. \n
        Args:
            name (str): [The name of the program]. \n
            version (str): [The version of the program]. \n
            author (str): [The author of the program]. \n
            APIURL (dict): [The API URL of the program]. \n
            mainDir (str): [The main directory to clone repositories]. \n
        """
        self.AppName = name
        self.AppVersion = version
        self.AppAuthor = author
        self.APIURL = APIURL
        self.APIResponse = self.APIURL
        self.APIDate = self.APIResponse
        self.MainDir = mainDir

    def AddComand(self, command: CMD) -> None:
        """[summary] \n
        Add a command to the list of the commands. \n
        Args:
            command (str): [The command to add]. \n
        """
        self.__commands.append(command)

    def NormalizeURL(self, url: str) -> str:
        """[summary] \n
        Normalize the URLs of the git's repositorys of the students, \n
        adding the .git at the end if it is not already there. \n
        Args:
            url (str): [The crudal url of the git's repository]. \n
        Returns:
            str: [The normalized url]. \n
        """
        if ".git" not in url:
            url = url.replace('\n', '.git')
        return url.replace("\n", "")

    def NormalizeCourse(self, course: str) -> str:
        """[summary] \n
        Normalize the course name, removing the spaces. \n
        Args:
            course (str): [The course name]. \n
        Returns:
            str: [The normalized course name]. \n
        """
        return course.replace(' - ', '-').replace(" ", "_")

    def FormatFullnameDate(self, surname: str, name: str) -> str:
        """[summary] \n
        Format the surname of the student, removing the spaces and replacing them with '_' \n
        Args:
            surname (str): [The surname of the student]. \n
            name (str): [The name of the student]. \n
            date (str): [The date of the student]. \n
            Returns:
                str: [The formatted Fullname like this: surname_name_date]. \n
        """
        surname = surname.replace(",", "_").replace(" ", "").replace(" \n", "")
        name = name.replace(",", "_").replace(" ", "").replace(" \n", "")
        return f'{surname}_{name}_{self.APIDate}'

    def FormatCourse(self, fieldList: str) -> str:
        """[summary] \n
        Format the course of the student, removing the line jumps and replacing them with '_' \n
        Args:
            fieldList (str): [The field of the course. It is the second field of the csv file]. \n
        Returns:
            str: [The formatted course]. \n
        """
        return self.NormalizeCourse(fieldList.replace(" \n", ""))

    def MakeCloneCommands(self, dfHandler: DFH) -> None:
        """[summary] \n
            Make the commands to clone the repositories of the students. \n
            Args:
                surname (str): [The surname of the student]. \n
                course (str): [The course of the student]. \n
                git (str): [The url of the git's repository]. \n
            """
        for frame in dfHandler.OrderListOfDFStudents:
            self.MakeCloneCommandsForDF(frame, dfHandler)

    def CreateSingleCommand(self, courseStr: str, normalizedFullname: str, normalizedURL: str) -> None:
        """[summary]\n
        Create a single command to clone the repository of the student,\n
        then add it to the list of the commands.

        Args:
            courseStr (str): [The course of the student].\n
            normalizedFullname (str): [The normalized fullname of the student].\n
            normalizedURL (str): [The normalized url of the git's repository of the student].\n
        """
        single_command = CMD()
        single_command.Main_Directory = f'{self.MainDir}'
        single_command.Sub_Directory = f'{courseStr}/{normalizedFullname}'
        single_command.Full_Command = f'git clone {normalizedURL} {single_command.Main_Directory}/{single_command.Sub_Directory}'
        self.AddComand(single_command)

    def MakeCloneCommandsForDF(self, df: DataFrame, dfHandler: DFH) -> None:
        """[summary] \n
        Make the commands to clone the repositories of the students. \n
        Args:
            df (DataFrame): [The DataFrame with the students information]. \n
        """
        # *## Deletes the first column [Date]
        df = df.drop(columns=dfHandler.ConfigsJsonValues['Date'], inplace=False, axis=1)
        # df = df.applymap(lambda x: str(x).strip())
        for i in df.index:
            crudeCourse = df[dfHandler.ConfigsJsonValues['Course']][i]
            courseStr = self.NormalizeCourse(self.FormatCourse(crudeCourse))
            surnameStr = df[dfHandler.ConfigsJsonValues['Surname']][i]
            nameStr = df[dfHandler.ConfigsJsonValues['Name']][i]
            message = f"Cloning the repository of: {surnameStr}, {nameStr} from {crudeCourse}"
            normalizedURL = self.NormalizeURL(
                df[dfHandler.ConfigsJsonValues['GitLink']][i])
            normalizedFullname = self.FormatFullnameDate(surnameStr, nameStr)
            self.CreateSingleCommand(courseStr, normalizedFullname, normalizedURL)
            self.CloningMessages = message

    def ExecuteCommands(self, cloneMessenger: CM) -> None:
        """[summary] \n
        Execute the commands to clone the repositories of the students. \n
        Args:
            commandList (list): [The list of the commands to execute]. \n
        """
        commandList = [x.Full_Command.strip() for x in self.Commands]
        messages = [x.strip() for x in self.CloningMessages]

        for command in commandList:
            cloneMessenger.Message = messages[commandList.index(command)]
            cloneMessenger.PrintMessage()
            os.system(command)

    def CloneRepositories(self, DfH: DFH, ) -> None:
        """[summary] \n
        Open the file and get the data. \n
        """
        appInfo = f'{self.AppName} - {self.AppVersion} by {self.AppAuthor}'
        self.Messenger.Message = appInfo
        self.Messenger.PrintMessage()
        try:
            # ?## Create git Clone commands
            self.MakeCloneCommands(DfH)

            # ?## Execute the commands
            self.ExecuteCommands(self.Messenger)

            self.Messenger.Message = 'All Repositories have been cloned!'
            self.Messenger.PrintMessage()

        except Exception as e:
            self.Messenger.Message = f'Exception: {e.args}'
            self.Messenger.PrintMessage()

    # ?########? END METHODS #########
