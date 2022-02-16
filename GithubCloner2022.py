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

from GetData_Mod.DataManager import DataManager as DM

import pandas as pd
from DataFrameHandler_Mod.DFHandler import DataFrameHandler as DfH

##########? Start Basic Configuration ##########
filename = 'Github_Repositories.csv'
name = 'Github Repository Cloner'
version = '[V2.0.1]'
author = '[FacuFalcone - CaidevOficial]'
fileConfigName = 'API_Info.json'
##########? End Basic Configuration ##########

try:
    ##########? Start Initialization ##########
    JsonFile = pd.read_json(f"./{fileConfigName}", orient='records')
    JsonAPI = JsonFile['Github']
    JsonDFConfigs = JsonFile['DataFrame']['Fields']
    ##########? End Initialization ############

    ##########? Start Objects Instances ##########
    Handler = DfH()
    Manager = DM()
    ##########? End Objects Instances ##########

    ##########? Start DataManager Configuration ##########
    Manager.InitialConfig(name, version, author, JsonAPI)
    ##########? End DataManager Configuration ##########

    ##########? Start DataFrame Configuration ##########
    #* Reads the 'csv' File to get the dataframe
    df = pd.read_csv(filename)

    #* Sets the Main DF to the class to handle it
    Handler.MainDataFrame = df
    Handler.ConfigsJsonValues = JsonDFConfigs
    Handler.ConfigurateDataFrame(Handler.ConfigsJsonValues['Course'])
    ##########? End DataFrame Configuration ##########

    ##########? Start Initialize DataManager ########## 
    Manager.CloneRepositories(Handler)
    ###########? End Initialize DataManager ###########

except Exception as e:
    print(f'Exception: {e.args}')