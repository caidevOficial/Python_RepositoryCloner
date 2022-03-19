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
    __configs_json_values: dict = {}
    __commands = []
    __unique_columns: ndarray = []
    __main_df: DataFrame = None
    __students_df = []
    __ordered_list_of_df_students: list = []
    # ?####? End Attributes #####

    def __init__(self) -> None:
        pass

    # ?####? PROPERTIES - Getters #####

    @property
    def OrderListOfDFStudents(self) -> list:
        """[summary] \n
        Get the list of ordered dataframes. \n
        Returns:
            [list]: [The list of ordered dataframes]. \n
        """
        return self.__ordered_list_of_df_students

    @property
    def ConfigsJsonValues(self) -> dict:
        """[summary] \n
        Get the configs of the json. \n
        Returns:
            [dict]: [The configs of the json]. \n
        """
        return self.__configs_json_values

    @property
    def MainDataFrame(self) -> DataFrame:
        """[summary] \n
        Get the main dataframe. \n
        Returns:
            [DataFrame]: [The main dataframe]. \n
        """
        return self.__main_df

    @property
    def UniqueColumns(self) -> ndarray:
        """[summary] \n
        Get the unique values of the column 'columnValue' [Division]. \n
        Returns:
            [ndarray]: [The unique values of the column 'columnValue' [Division]]. \n
        """
        return self.__unique_columns

    @property
    def Commands(self) -> list:
        """[summary] \n
        Get the list of the commands. \n
        Returns:
            [list]: [The list of the commands]. \n
        """
        return self.__commands

    @property
    def StudentsDF(self) -> list:
        """[summary] \n
        Get the dataframe with the students. \n
        Returns:
            [DataFrame]: [The dataframe with the students]. \n
        """
        return self.__students_df

    # ?####? End PROPERTIES - GETTERS #####

    # ?####? PROPERTIES - Setters #####

    @OrderListOfDFStudents.setter
    def OrderListOfDFStudents(self, frame: DataFrame) -> None:
        """[summary] \n
        Set the list of ordered dataframes. \n
        Args:
            frame (DataFrame): [The ordered dataframes]. \n
        """
        self.__ordered_list_of_df_students.append(frame.reset_index(drop=True))

    @ConfigsJsonValues.setter
    def ConfigsJsonValues(self, value: dict) -> None:
        """[summary] \n
        Set the configs of the json. \n
        Args:
            value (dict): [The configs of the json]. \n
        """
        self.__configs_json_values = value

    @MainDataFrame.setter
    def MainDataFrame(self, frame: DataFrame):
        """[summary] \n
        Set the main dataframe. \n
        Args:
            frame (DataFrame): [The dataframe to set]. \n
        """
        self.__main_df = frame

    @UniqueColumns.setter
    def UniqueColumns(self, unique_columns: ndarray):
        """[summary] \n
        Set the unique values of the column 'columnValue' [Division]. \n
        Args:
            unique_columns (ndarray): [The unique values of the column 'columnValue' [Division]]. \n
        """
        self.__unique_columns = unique_columns

    @Commands.setter
    def Commands(self, command: str) -> None:
        """[summary] \n
        Sets a command inside the list of the commands. \n
        Args:
            command (str): [The command to add]. \n
        """
        self.__commands.append(command)

    @StudentsDF.setter
    def StudentsDF(self, frame: DataFrame) -> None:
        """[summary] \n
        Set the dataframe with the students. \n
        Args:
            frame (DataFrame): [The dataframe with the students]. \n
        """
        self.__students_df.append(frame)

    # ?####? End PROPERTIES - SETTERS #####

    # ?####? METHODS #####

    def OrderIndexedDFBy(self, frame: DataFrame, first_field: str, second_field: str, third_field: str) -> DataFrame:
        """[summary] \n
        Order the dataframe by the specified fields. \n
        Args:
            frame (DataFrame): [The dataframe to order]. \n
            first_field (str): [The first field to order]. \n
            second_field (str): [The second field to order]. \n
            third_field (str): [The third field to order]. \n
        Returns:
            [DataFrame]: [The dataframe ordered by the three fields in the specified order]. \n
        """
        sorted_df = frame.sort_values(
            by=[first_field, second_field, third_field], ascending=[True, True, True])
        return sorted_df

    def GetSpecificStudentsDF(self, frame: DataFrame, column: str, value: str) -> DataFrame:
        """[summary] \n
        Get the students that have the specified index value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            frame (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            value (str): [The value to filter]. \n
        Returns:
            [DataFrame]: [The dataframe with the filtered students \n
            ordered by Course, Surname & Name]. \n
        """
        specific_df: DataFrame = frame[frame[column] == value]
        ordered_data_frame: DataFrame = self.OrderIndexedDFBy(
            specific_df, self.ConfigsJsonValues['Course'],
            self.ConfigsJsonValues['Surname'],
            self.ConfigsJsonValues['Name']
        )
        return ordered_data_frame

    def CreateListDFStudentsBy(self, frame: DataFrame, column: str, column_value: str):
        """[summary] \n
        Creates a list of the students that have the specified index \n
        value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            frame (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            column_value (list): [The values to filter]. \n
        """
        self.OrderListOfDFStudents = self.GetSpecificStudentsDF(
            frame, column, column_value)

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

    def createJSONofDF(self, frame: DataFrame, name: str):
        """[summary] \n
        Create a json file for the specified dataframe. \n
        Args:
            frame (DataFrame): [The dataframe to create the json file]. \n
            name (str): [The name of the json file]. \n
        """
        frame.to_json(f'{name}.json', orient='records',
                   indent=4, force_ascii=True)

    def createJsonOfEveryDF(self):
        """[summary] \n
        Create a json file for every dataframe. \n
        """
        for students_df in self.OrderListOfDFStudents:
            name = students_df.at[students_df.index.values[0],
                            self.ConfigsJsonValues['Course']]
            filename: str = f'{name}.json'
            self.createJSONofDF(students_df, filename)

    # ?####? End METHODS #####

    # *####* MAIN METHOD #####

    def ConfigurateDataFrame(self, column_value: str) -> None:
        """[summary] \n
        Configurate the dataframe with the specified column value. \n
        Args:
            column_value (str): [The column value to configurate]. \n
        """

        # *# Gets the unique values of the column 'column_value' [Division]
        self.ConfigUniqueValuesInColumn(column_value)
        # *# For each unique value of the column 'column_value' [Division]
        # *# Creates a list of dataframes with the students that have the
        # *# specified value in the column 'column_value' [Division]
        for unique in self.UniqueColumns:
            self.CreateListDFStudentsBy(
                self.MainDataFrame, column_value, unique
            )
        self.createJsonOfEveryDF()

    # *####* END MAIN METHOD #####
