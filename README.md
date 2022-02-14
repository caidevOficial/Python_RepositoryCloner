# Repository Cloner
It allows you to clone repositories from github in bulk and store them in specific directories from a csv file.

### File format
* 1st Column: Date time. [it isn't used yet.]
* 2nd Column: Student Name
* 3rd Column: Student Surname
* 4th Column: Student Division
* 5th Column: Student ID. [it isn't used yet.]
* 6th Column: Student E-mail. [it isn't used yet.]
* 7th Column: Repository Name to download (It could skip the '.git' part)


# Configuration
In order to use this Cloner, you should configure the file [apiInfo.json](apiInfo.json) with your Github API's information as shown below.

```json
[
    {
        "URL": "https://api.github.com/repos",
        "USER": "Your_Github_User",
        "REPO": "Your_Repository_To_Get_The_Date_Of_Last_Commit",
        "BRANCH": "The_Branch_Of_The_Last_Commit_lowercase"
    }
]
```

for example:

```json
[
    {
        "URL": "https://api.github.com/repos",
        "USER": "CaidevOficial",
        "REPO": "Python_Udemy_DataManipulation",
        "BRANCH": "main"
    }
]
```

Then the code will make the link like:

```
https://api.github.com/repos/CaidevOficial/Python_Udemy_DataManipulation/commits/main
```

This way the program will take the 'Date' of the last commit of the branch 'main' and will use it to create the folder with the name of the repository. Obviously, the repository <strong>MUST BE PUBLIC</strong>, otherwise the program won't be able to access its API.


<table>
    <theader>
        <tr>
            <th colspan=2>
                <center><strong>LICENSE</strong></center>
            </th>
        </tr>
        <tr>
            <th colspan=2>
                <center>Git Repository Cloner 2022</center>
            </th>
        </tr>
        <tr>
            <th>
                <center>License</center>
            </th>
            <th>
                <center>Author</center>
            </th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
                <center>[GNU General Public License V3]</center>
            </td>
            <td>
                <center>[Facundo Falcone - CaidevOficial]</center>
            </td>
        </tr>
        <tr>
            <td colspan=2>
                <center>
                    This program is free software: you can redistribute it and/or modify
                    it under the terms of the GNU General Public License as published by
                    the Free Software Foundation, either version 3 of the License, or
                    (at your option) any later version.
                    This program is distributed in the hope that it will be useful,
                    but WITHOUT ANY WARRANTY; without even the implied warranty of
                    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
                    GNU General Public License for more details.
                    You should have received a copy of the GNU General Public License
                    along with this program.
                    If not, see <a href='https://www.gnu.org/licenses/'>GNU Licenses</a>.
                </center>
            </td>
        </tr>
    </tbody>
</table>
