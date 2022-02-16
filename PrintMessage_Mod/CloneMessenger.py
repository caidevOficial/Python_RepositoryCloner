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

class CloneMessenger:
    """[summary]
    Class to print messages in the console. \n
    Returns:
        class: [CloneMessenger]. \n
    """
    # ?######? START ATTRIBUTES #######
    __message: str = ''
    # ?######? END ATTRIBUTES #######

    def __init__(self) -> None:
        pass

    def SetMessage(self, message: str) -> None:
        """[summary] \n
        Sets the message of the class. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.__message = message

    def GetMessage(self) -> str:
        """[summary] \n
        Gets the message of the class. \n
        Returns:
            str: Message of the class to be printed in the console. \n
        """
        return self.__message

    # ?###########? START METHODS ############

    def InitializeMessenger(self, message: str) -> None:
        """[summary] \n
        Initializes the class with a message. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.SetMessage(message)

    def PrintMessage(self) -> None:
        """[summary] \n
        Creates a string of symbols of the same length of the message and \n
        prints them in the console. \n
        """
        symbols = self.GenerateSymbols()
        print(
            ' \n',
            f'{symbols} \n',
            f'{self.GetMessage()} \n',
            f'{symbols} \n'
        )

    def GenerateSymbols(self) -> str:
        """[summary] \n
        Generates a string of symbols of the same length of the message of the class. \n
        Returns:
            str: String of symbols of the same length of the message of the class. \n
        """
        return ''.join(['#' for i in range(len(self.GetMessage()))])

    # ?###########? END METHODS ############
