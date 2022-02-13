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

import logging

class CloneMessenger:
    """_summary_
    Class to print messages in the console
    Returns:
        class: CloneMessenger
    """
    __message:str = ''

    def __init__(self, message:str) -> None:
        self.SetMessage(message)
    
    def SetMessage(self, message:str) -> None:
        """[_summary]
        Sets the message of the class
        Args:
            message (str): The message to be printed in the console
        """
        self.__message = message
    
    def GetMessage(self) -> str:
        """_summary_
        Gets the message of the class
        Returns:
            str: Message of the class to be printed in the console.
        """
        return self.__message
    
    def PrintMessage(self) -> None:
        """[summary]
        Creates a string of symbols of the same length of the message and
        prints them in the console.
        """
        symbols = self.GenerateSymbols()
        print(
            '\n',
            f'{symbols}\n', 
            f'{self.GetMessage()}\n', 
            f'{symbols}\n'
        )
    
    def GenerateSymbols(self) -> str:
        """[summary]
        Generates a string of symbols of the same length of the message of the class
        Returns:
            str: String of symbols of the same length of the message of the class
        """
        return ''.join(['#' for i in range(len(self.GetMessage()))])
    
