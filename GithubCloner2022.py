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

import json
from GetData_Mod.DataManager import DataManager as DM

########## Start Basic Configuration ##########
filename = 'Github_Repositories.csv'
name = 'Github Repository Cloner'
version = '[V1.1.05]'
fileConfigName = 'apiInfo.json'
########## End Basic Configuration ##########

try:
    with open(fileConfigName, 'r') as APIFILE:
        JsonFile = json.load(APIFILE)[0]
        print(JsonFile)
        APIURL = f'{JsonFile["URL"]}/{JsonFile["USER"]}/{JsonFile["REPO"]}/commits/{JsonFile["BRANCH"]}'
        print(APIURL)

    manager = DM(filename, name, version, APIURL)
    manager.OpenFile()
except FileNotFoundError:
    print(f'File not found: {fileConfigName}')
