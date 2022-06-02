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

import datetime
import logging
import pandas as pd

from Modules.DataFrameHandler_Mod.df_handler import DataFrameHandler as DfH
from Modules.DataManager_Mod.data_manager import DataManager as DM
from Modules.DirectoryManager_Mod.dir_manager import DirectoryManager as DirM
from Modules.Formatter_Mod.Formatter import Formatter as FMT
from Modules.PlotManager_Mod.plot_manager import PlotManager as Plot
from Modules.PrintMessage_Mod.clone_messenger import CloneMessenger as CM

# ?######### Start Basic Configuration ##########
FILENAME: str = 'Github_Repositories.csv'
NAME: str = 'Github Repository Cloner'
VERSION: str = '[V2.2.1.11]'
AUTHOR: str = '[FacuFalcone - CaidevOficial]'
FILE_CONFIG_NAME: str = 'Modules/API_Info.json'
# ?######### End Basic Configuration ##########

# INFO -> 10
# DEBUG -> 20
# WARNING -> 30
# ERROR -> 40
# CRITICAL -> 50

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        start_time = datetime.datetime.now()
    # ?#########? Start Initialization ##########
        logging.debug('Reading Json with configurations...')
        JsonFile = pd.read_json(f"./{FILE_CONFIG_NAME}", orient='records')
        JsonAPI = JsonFile['Github']
        JsonDFConfigs = JsonFile['DataFrame']['Fields']
        JsonDirConfigs = JsonFile['Files']
    # ?#########? End Initialization ############

    # ?#########? Start Objects Instances ##########
        Handler = DfH()
        Manager = DM()
        Messenger = CM()
        Timer = FMT()
        Plotter = Plot()
        DirManager = DirM()
    # ?#########? End Objects Instances ##########

    # ?#########? Start Directory Creation ##########
        logging.debug('Creating directories to save files...')
        DirManager.PathToCreate = JsonDirConfigs['Dir_Plots_img']
        DirManager.createDirIfNoExist()

        DirManager.PathToCreate = JsonDirConfigs['Dir_Cloned_Repos']
        DirManager.createDirIfNoExist()

        DirManager.PathToCreate = JsonDirConfigs['Dir_Statistics']
        DirManager.createDirIfNoExist()
    # ?#########? End Directory Creation ##########

    # ?#########? Start DataManager Configuration ##########
        logging.debug('Initializing Data Manager...')
        Manager.InitialConfig(NAME, VERSION, AUTHOR, JsonAPI, JsonDirConfigs['Dir_Cloned_Repos'])
    # ?#########? End DataManager Configuration ##########

    # ?#########? Start DataFrame Configuration ##########
        # *# Reads the 'csv' File to get the dataframe
        logging.debug('Reading CSV with students info...')
        df = pd.read_csv(FILENAME)
        
        # *# Sets the Main DF to the class to handle it
        logging.debug('Configuring main dataframe with student information...')
        Handler.ConfigsJsonValues = JsonDFConfigs
        Handler.MainDataFrame = Handler.FormatDF(df, JsonDFConfigs)
        Handler.ConfigurateDataFrame(
            Handler.ConfigsJsonValues['Course'], 
            JsonDirConfigs['Dir_Statistics']
        )
    # ?#########? End DataFrame Configuration ##########

    # ?#########? Start Initialize DataManager ##########
        logging.debug('Cloning Repositories...')
        Manager.CloneRepositories(Handler)
    # ?##########? End Initialize DataManager ###########

    # ?#########? Start PlotManager Configuration ##########
        logging.debug('Creating Plot...')
        Plotter.initialize(Handler, 'Cloned Repositories', JsonDirConfigs['Dir_Plots_img'])

    # ?#########? Start Timer Config ##########
        Timer.CrudeTime = start_time
    # ?#########? End Timer Config ##########

    # ?#########? Start Print Message ##########
        Messenger.Message = f"Elapsed Time: {Timer.FormattedTimeStr}"
        Messenger.PrintMessage()

        Messenger.Message = f"Thanks for using {NAME} {VERSION} by {AUTHOR}! ♥"
        Messenger.PrintMessage()

        Messenger.Message = "Creating Pie Chart..."
        Messenger.PrintMessage()
        Plotter.createPieChart()

        Messenger.Message = "Success! All task done. Press a key to close the app"
        Messenger.PrintMessage()
    # ?#########? End Print Message ##########
    except Exception as e:
        print(f'Exception: {e.args}')
    finally:
        end = input()
