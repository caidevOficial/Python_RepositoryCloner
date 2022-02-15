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

from textwrap import indent
from numpy import ndarray
from pandas import DataFrame
import pandas as pd

class DataFrameHandler:

    ##### Attributes #####
    __configsJsonValues:dict = {}
    __commands = []
    __uniqueColumns:ndarray = []
    __mainDF:DataFrame = None
    __studentsDF = []
    __orderedListOfDFStudents:list = []
    ##### End Attributes #####

    def __init__(self) -> None:
        pass

    
    ##### Properties #####
    @property
    def OrderListOfDFStudents(self)->list:
        """[summary]
        Get the list of ordered dataframes
        Returns:
            [list]: [The list of ordered dataframes]
        """
        return self.__orderedListOfDFStudents

    @OrderListOfDFStudents.setter
    def OrderListOfDFStudents(self, df:DataFrame)->None:
        """[summary]
        Set the list of ordered dataframes
        Args:
            df (DataFrame): [The ordered dataframes]
        """
        self.__orderedListOfDFStudents.append(df)

    @property
    def ConfigsJsonValues(self)->dict:
        return self.__configsJsonValues
    
    @ConfigsJsonValues.setter
    def ConfigsJsonValues(self, value:dict)->None:
        self.__configsJsonValues = value

    @property
    def MainDataFrame(self)->DataFrame:
        """[summary]
        Get the main dataframe
        Returns:
            [DataFrame]: [The main dataframe]
        """
        return self.__mainDF

    @MainDataFrame.setter
    def MainDataFrame(self, df:DataFrame):
        """[summary]
        Set the main dataframe
        Args:
            df (DataFrame): [The dataframe to set]
        """
        self.__mainDF = df

    @property
    def UniqueColumns(self) -> ndarray:
        return self.__uniqueColumns
    
    @UniqueColumns.setter
    def UniqueColumns(self, uniqueColumns:ndarray):
        self.__uniqueColumns = uniqueColumns

    @property
    def Commands(self)->list:
        """[summary]
        Get the list of the commands
        Returns:
            [list]: [The list of the commands]
        """
        return self.__commands
    
    @Commands.setter
    def Commands(self, command:str)->None:
        """[summary]
        Set the command to the list of the commands
        Args:
            command (str): [The command to add]
        """
        self.__commands.append(command)

    @property
    def StudentsDF(self)->list:
        """[summary]
        Get the dataframe with the students
        Returns:
            [DataFrame]: [The dataframe with the students]
        """
        return self.__studentsDF
    
    @StudentsDF.setter
    def StudentsDF(self, df:DataFrame)->None:
        """[summary]
        Set the dataframe with the students
        Args:
            df (DataFrame): [The dataframe with the students]
        """
        self.__studentsDF.append(df)
    ##### End Properties #####
    
    ##### Methods #####
    def GetSpecificStudentsDF(self, df:DataFrame, column:str, value:str)->DataFrame:
        """[summary]
        Get the students that have the specified index value in the specified column.
        The DataFrame MUST be indexed by the 'value' column.
        Args:
            df (DataFrame): [The dataframe to filter]
            column (str): [The column to filter]
            value (str): [The value to filter]
        Returns:
            [DataFrame]: [The dataframe with the filtered students ordered by Course, Surname & Name]
        """
        specificDF: DataFrame = df[df[column] == value]
        orderedDF: DataFrame = self.OrderIndexedDFBy(
            specificDF, self.ConfigsJsonValues['Course'], 
            self.ConfigsJsonValues['Surname'], 
            self.ConfigsJsonValues['Name']
        )
        return orderedDF

    def GetListDFStudentsBy(self, df:DataFrame, column:str, columnValue:str):
        """[summary]
        Get the students that have the specified index value in the specified column.
        The DataFrame MUST be indexed by the 'value' column.
        Args:
            df (DataFrame): [The dataframe to filter]
            column (str): [The column to filter]
            value (list): [The values to filter]
        """
        #listCourses = []
        #listCourses.append(self.GetSpecificStudentsDF(df, column, columnValue))
        self.OrderListOfDFStudents = self.GetSpecificStudentsDF(df, column, columnValue)

    def OrderIndexedDFBy(self, df:DataFrame, firstField:str, secondField:str, thirdField:str)->DataFrame:
        """[summary]
        Order the dataframe by the specified fields
        Args:
            df (DataFrame): [The dataframe to order]
            firstField (str): [The first field to order]
            secondField (str): [The second field to order]
            thirdField (str): [The third field to order]
        Returns:
            [DataFrame]: [The dataframe ordered by the three fields in the specified order]
        """
        sortedDF = df.sort_values(by=[firstField, secondField, thirdField], ascending=[True, True, True])
        return sortedDF
    
    #* USED
    def ConfigUniqueValuesInColumn(self, column:str):
        """[summary]
        Get the unique values in the specified column and sort them in alphabetical order ASC.
        Args:
            column (str): [The column to filter]
        Returns:
            [list]: [The unique values in the specified column]
        """
        self.UniqueColumns = self.MainDataFrame[column].unique()
        self.UniqueColumns.sort()

    #* USED
    def CreateJsonOfEveryDF(self):
        for i in range(len(self.OrderListOfDFStudents)):
            frame:DataFrame = self.OrderListOfDFStudents[i]
            name = frame.at[frame.index.values[0], self.ConfigsJsonValues['Course']]
            filename:str = f'{name}.json'
            frame.to_json(f'{filename}', orient='table', indent=4, force_ascii=True)

    ##### End Methods #####

    #####* Main Method #####
    def ConfigurateDataFrame(self, columnValue:str)->None:
        #* Gets the unique values of the column 'columnValue' [Division]
        self.ConfigUniqueValuesInColumn(columnValue)
        #* For each unique value of the column 'columnValue' [Division]
        #* Creates a list of dataframes with the students that have the specified value in the column 'columnValue' [Division]
        for unique in self.UniqueColumns:
            self.GetListDFStudentsBy(self.MainDataFrame, columnValue, unique)
        self.CreateJsonOfEveryDF()
        
    #####* End Main Method #####
    
