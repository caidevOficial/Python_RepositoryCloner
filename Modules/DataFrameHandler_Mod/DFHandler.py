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

from numpy import ndarray
from pandas import DataFrame


class DataFrameHandler:
    """[summary] \n
    Class in charge of configurate and handle all the dataframe operations. \n
    Returns:
        class: [DataFrameHandler]. \n
    """
    # ?####? Attributes #####
    __configsJsonValues: dict = {}
    __commands = []
    __uniqueColumns: ndarray = []
    __mainDF: DataFrame = None
    __studentsDF = []
    __orderedListOfDFStudents: list = []
    # ?####? End Attributes #####

    def __init__(self) -> None:
        pass

    # ?####? Properties #####

    @property
    def OrderListOfDFStudents(self) -> list:
        """[summary] \n
        Get the list of ordered dataframes. \n
        Returns:
            [list]: [The list of ordered dataframes]. \n
        """
        return self.__orderedListOfDFStudents

    @OrderListOfDFStudents.setter
    def OrderListOfDFStudents(self, df: DataFrame) -> None:
        """[summary] \n
        Set the list of ordered dataframes. \n
        Args:
            df (DataFrame): [The ordered dataframes]. \n
        """
        self.__orderedListOfDFStudents.append(df)

    @property
    def ConfigsJsonValues(self) -> dict:
        """[summary] \n
        Get the configs of the json. \n
        Returns:
            [dict]: [The configs of the json]. \n
        """
        return self.__configsJsonValues

    @ConfigsJsonValues.setter
    def ConfigsJsonValues(self, value: dict) -> None:
        """[summary] \n
        Set the configs of the json. \n
        Args:
            value (dict): [The configs of the json]. \n
        """
        self.__configsJsonValues = value

    @property
    def MainDataFrame(self) -> DataFrame:
        """[summary] \n
        Get the main dataframe. \n
        Returns:
            [DataFrame]: [The main dataframe]. \n
        """
        return self.__mainDF

    @MainDataFrame.setter
    def MainDataFrame(self, df: DataFrame):
        """[summary] \n
        Set the main dataframe. \n
        Args:
            df (DataFrame): [The dataframe to set]. \n
        """
        self.__mainDF = df

    @property
    def UniqueColumns(self) -> ndarray:
        """[summary] \n
        Get the unique values of the column 'columnValue' [Division]. \n
        Returns:
            [ndarray]: [The unique values of the column 'columnValue' [Division]]. \n
        """
        return self.__uniqueColumns

    @UniqueColumns.setter
    def UniqueColumns(self, uniqueColumns: ndarray):
        """[summary] \n
        Set the unique values of the column 'columnValue' [Division]. \n
        Args:
            uniqueColumns (ndarray): [The unique values of the column 'columnValue' [Division]]. \n
        """
        self.__uniqueColumns = uniqueColumns

    @property
    def Commands(self) -> list:
        """[summary] \n
        Get the list of the commands. \n
        Returns:
            [list]: [The list of the commands]. \n
        """
        return self.__commands

    @Commands.setter
    def Commands(self, command: str) -> None:
        """[summary] \n
        Sets a command inside the list of the commands. \n
        Args:
            command (str): [The command to add]. \n
        """
        self.__commands.append(command)

    @property
    def StudentsDF(self) -> list:
        """[summary] \n
        Get the dataframe with the students. \n
        Returns:
            [DataFrame]: [The dataframe with the students]. \n
        """
        return self.__studentsDF

    @StudentsDF.setter
    def StudentsDF(self, df: DataFrame) -> None:
        """[summary] \n
        Set the dataframe with the students. \n
        Args:
            df (DataFrame): [The dataframe with the students]. \n
        """
        self.__studentsDF.append(df)

    # ?####? End Properties #####

    # ?####? Methods #####

    def GetSpecificStudentsDF(self, df: DataFrame, column: str, value: str) -> DataFrame:
        """[summary] \n
        Get the students that have the specified index value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            df (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            value (str): [The value to filter]. \n
        Returns:
            [DataFrame]: [The dataframe with the filtered students ordered by Course, Surname & Name]. \n
        """
        specificDF: DataFrame = df[df[column] == value]
        orderedDF: DataFrame = self.OrderIndexedDFBy(
            specificDF, self.ConfigsJsonValues['Course'],
            self.ConfigsJsonValues['Surname'],
            self.ConfigsJsonValues['Name']
        )
        return orderedDF

    def CreateListDFStudentsBy(self, df: DataFrame, column: str, columnValue: str):
        """[summary] \n
        Creates a list of the students that have the specified index value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            df (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            value (list): [The values to filter]. \n
        """
        self.OrderListOfDFStudents = self.GetSpecificStudentsDF(
            df, column, columnValue)

    def OrderIndexedDFBy(self, df: DataFrame, firstField: str, secondField: str, thirdField: str) -> DataFrame:
        """[summary] \n
        Order the dataframe by the specified fields. \n
        Args:
            df (DataFrame): [The dataframe to order]. \n
            firstField (str): [The first field to order]. \n
            secondField (str): [The second field to order]. \n
            thirdField (str): [The third field to order]. \n
        Returns:
            [DataFrame]: [The dataframe ordered by the three fields in the specified order]. \n
        """
        sortedDF = df.sort_values(
            by=[firstField, secondField, thirdField], ascending=[True, True, True])
        return sortedDF

    def ConfigUniqueValuesInColumn(self, column: str):
        """[summary] \n
        Get the unique values in the specified column and sort them in alphabetical order ASC. \n
        Args:
            column (str): [The column to filter]. \n
        Returns:
            [list]: [The unique values in the specified column]. \n
        """
        self.UniqueColumns = self.MainDataFrame[column].unique()
        self.UniqueColumns.sort()

    def CreateJsonOfEveryDF(self):
        """[summary] \n
        Create a json file for every dataframe. \n
        """

        for i in range(len(self.OrderListOfDFStudents)):
            frame: DataFrame = self.OrderListOfDFStudents[i]
            name = frame.at[frame.index.values[0],
                            self.ConfigsJsonValues['Course']]
            filename: str = f'{name}.json'
            frame.to_json(f'{filename}', orient='table',
                          indent=4, force_ascii=True)

    # ?####? End Methods #####

    # *####* Main Method #####

    def ConfigurateDataFrame(self, columnValue: str) -> None:
        """[summary] \n
        Configurate the dataframe with the specified column value. \n
        Args:
            columnValue (str): [The column value to configurate]. \n
        """

        # *# Gets the unique values of the column 'columnValue' [Division]
        self.ConfigUniqueValuesInColumn(columnValue)
        # *# For each unique value of the column 'columnValue' [Division]
        # *# Creates a list of dataframes with the students that have the
        # *# specified value in the column 'columnValue' [Division]
        for unique in self.UniqueColumns:
            self.CreateListDFStudentsBy(
                self.MainDataFrame, columnValue, unique)
        self.CreateJsonOfEveryDF()

    # *####* End Main Method #####
