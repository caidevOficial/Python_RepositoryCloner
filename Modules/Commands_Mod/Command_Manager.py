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

class Command:
    """[Summary]\n
    Class in charge to handle the command and directories to clone\n
    The repositories of the students.
    
        Returns:\n
        class: [Command]\n
    """

    __main_directory = ''
    __sub_directory = ''
    __full_command = ''

    def __init__(self) -> None:
        pass

    @property
    def Main_Directory(self)-> str:
        return self.__main_directory

    @property
    def Sub_Directory(self)-> str:
        return self.__sub_directory

    @property
    def Full_Command(self)-> str:
        return self.__full_command
    
    @Main_Directory.setter
    def Main_Directory(self, dir: str) -> None:
        self.__main_directory = dir
    
    @Sub_Directory.setter
    def Main_Directory(self, sub_dir: str) -> None:
        self.__sub_directory = sub_dir
    
    @Full_Command.setter
    def Main_Directory(self, cmd: str) -> None:
        self.__full_command = cmd
    
    
    
    
    
    

        
    
