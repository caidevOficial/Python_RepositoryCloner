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

import pandas as pd
from DataFrameHandler_Mod.DFHandler import DataFrameHandler as DfH

##########? Start Basic Configuration ##########
filename = 'Github_Repositories.csv'
name = 'Github Repository Cloner'
version = '[V1.1.04]'
fileConfigName = 'API_Info.json'
##########? End Basic Configuration ##########



try:
    JsonFile = pd.read_json(f"./{fileConfigName}", orient='records')
    JsonAPI = JsonFile['Github']
    JsonDFConfigs = JsonFile['DataFrame']['Fields']
    
    Handler = DfH()
    Manager = DM()
    Manager.InitialConfig(name, version, JsonAPI)


    ########## Start DataFrame Configuration ##########
    #* Reads the 'csv' File to get the dataframe
    df = pd.read_csv(filename)

    #? SETTINGS OF DATAFRAMEHANDLER
    #* Sets the Main DF to the class to handle it
    Handler.MainDataFrame = df
    Handler.ConfigsJsonValues = JsonDFConfigs
    Handler.ConfigurateDataFrame(Handler.ConfigsJsonValues['Course'])

    ########## TEST UNIQUE VALUES ########## #* TEST PASSED
    print('UNIQUE VALUES\n')
    for unique in Handler.UniqueColumns:
        print(unique)
    ########## End TEST UNIQUE VALUES ##########

    ########## TEST LIST OF STUDENTS ########## #* TEST PASSED
    print('\nLIST OF STUDENTS\n')
    studList = Handler.OrderListOfDFStudents
    print(studList)
    ########## END TEST LIST OF STUDENTS ##########

except Exception as e:
    #print(f'File not found: {fileConfigName}')
    print(f'Error: {e}')

# try:
#     with open(fileConfigName, 'r') as APIFILE:
#         JsonFile = pd.read_json(APIFILE)["Github"]
#         print(JsonFile)
#         APIURL = f'{JsonFile["URL"]}/{JsonFile["USER"]}/{JsonFile["REPO"]}/commits/{JsonFile["BRANCH"]}'
#         print(APIURL)

#     manager = DM(filename, name, version, APIURL)
#     manager.OpenFile()
# except FileNotFoundError:
#     print(f'File not found: {fileConfigName}')
