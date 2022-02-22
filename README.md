<table align='center'>
    <tr>
        <td>
            <img alt="Universidad Tecnológica Nacional" src="https://github.com/caidevOficial/Logos/raw/master/Instituciones/logo-utn_black_white.png?raw=true" height="150px" />
        </td>
        <td>
            <img alt="Python Logo" src="https://github.com/devicons/devicon/raw/master/icons/python/python-original.svg?raw=true" height="160px" />
        </td>
    </tr>
    <tr>
        <td colspan=2 align='center'>
            <center>
                <img alt="Pandas Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png?raw=true" height="150px" />
            </center>
        </td>
    </tr>
</table>
</br>

<div align="center">
    <h3>Pisces♓ | Developer👨‍💻 | Python<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="28"/> | GCP <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg?raw=true" alt="GCP" width="30" height="30"> | Java <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="30" height="30"/> | C# <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="25" height="25"/> | Dreamer 💖 | Teacher👨‍🏫| A bit nerd🤓</h3>
    <br>
    <h3>📌 Programming Student & Assistant Professor at the <br>
    <strong>National Technological University [UTN]</strong> 👨‍💻</h3>
    <h3>📌 Backend programmer at <strong>Accenture</strong> 👨‍💻</h3>
</div>

![](https://hit.yhype.me/github/profile?user_id=12877139)

<p align="center">
    <img src="https://komarev.com/ghpvc/?username=caidevoficial&label=Profile%20views&color=0e75b6&style=plastic" alt="caidevoficial" />
</p>

<p align="center">
    <a href="https://github.com/CaidevOficial">
        <img src="https://github-profile-trophy.vercel.app/?username=caidevoficial&theme=nord&column=7" alt="caidevoficial" />
    </a>
</p>
<br><br><br>

---

<br>




<table align='center'>
    <theader>
        <th><h2><center>Watch this little video Demo [for version without Pie Chart] on 🎥</center></h2></th>
    </theader>
    <tbody>
        <tr>
        <td>
            <a href="https://lnkd.in/e-m4ThfQ" target="_blank">
                <center>
                    <img alt='Youtube Logo' src='./Media/YT_Logo.png' width=350/>
                </center>
            </a>
        </td>
    </tr>
    </tbody>
</table>

<br><br><br>

# Repository Cloner
The program it allows you to clone repositories from github in bulk and store them in specific directories from a csv file.
Aditionally it saves the data of every student & course into a json with the name of the course.

All this is possible by the use of [Pandas library](https://pandas.pydata.org/docs/index.html) and dataframes to manipulate the data, sorting and filtering the courses, students and repositories to get a list of dataframes, one for each course with all the students data sorted by course, surname and name.

At the end of the execution, the program will download the files of every student and save them in the directory of the course that they belong to.

like this:

<table align='center'>
    <theader>
        <th>Courses & students directories</th>
    </theader>
    <tbody>
        <tr>
            <td>
                <img alt='Directories Image' src='./Media/Directories_tree.png' height=250px>
            </td>
        </tr>
    </tbody>
</table>

And the JSON generates with the data of the students and courses will be like this:

```json
{
    "schema":{
        "fields":[
            {
                "name":"index",
                "type":"integer"
            },
            {
                "name":"Marca temporal",
                "type":"string"
            },
            {
                "name":"Nombre\/s",
                "type":"string"
            },
            {
                "name":"Apellido\/s",
                "type":"string"
            },
            {
                "name":"Divisi\u00f3n",
                "type":"string"
            },
            {
                "name":"DNI \/ Legajo",
                "type":"integer"
            },
            {
                "name":"E-Mail",
                "type":"string"
            },
            {
                "name":"Link al repositorio",
                "type":"string"
            }
        ],
        "primaryKey":[
            "index"
        ],
        "pandas_version":"1.4.0"
    },
    "data":[
        {
            "index":5,
            "Marca temporal":"2022\/02\/13 10:26:52 p.\u00a0m. GMT-3",
            "Nombre\/s":"Artemisa",
            "Apellido\/s":"Grecian God",
            "Divisi\u00f3n":"1G - Professor 1 - Helper 1",
            "DNI \/ Legajo":444444,
            "E-Mail":"zeus@ray.com",
            "Link al repositorio":"https:\/\/github.com\/caidevOficial\/Python_IEEE_Team14293.git"
        },
        {
            "index":3,
            "Marca temporal":"2022\/02\/13 10:26:52 p.\u00a0m. GMT-3",
            "Nombre\/s":"Zeus",
            "Apellido\/s":"Grecian God",
            "Divisi\u00f3n":"1G - Professor 1 - Helper 1",
            "DNI \/ Legajo":444444,
            "E-Mail":"zeus@ray.com",
            "Link al repositorio":"https:\/\/github.com\/caidevOficial\/Python_IEEE_Team14293.git"
        },
        {
            "index":4,
            "Marca temporal":"2022\/02\/13 10:26:52 p.\u00a0m. GMT-3",
            "Nombre\/s":"Mercury",
            "Apellido\/s":"Romane God",
            "Divisi\u00f3n":"1G - Professor 1 - Helper 1",
            "DNI \/ Legajo":222222,
            "E-Mail":"neptune@notplanet.com",
            "Link al repositorio":"https:\/\/github.com\/caidevOficial\/SPD2022_TPS.git"
        },
        {
            "index":0,
            "Marca temporal":"2022\/02\/13 10:26:52 p.\u00a0m. GMT-3",
            "Nombre\/s":"Neptune",
            "Apellido\/s":"Romane God",
            "Divisi\u00f3n":"1G - Professor 1 - Helper 1",
            "DNI \/ Legajo":222222,
            "E-Mail":"neptune@notplanet.com",
            "Link al repositorio":"https:\/\/github.com\/caidevOficial\/SPD2022_TPS.git"
        }
    ]
}
```
<br><br><br>

---

<br><br><br>
# Console Messages
Meanwhile the program is cloning the repositories, the console will show messages like showns below:

<table align='center'>
    <theader>
        <th><center>Console Messages</center></th>
    </theader>
    <tbody>
        <tr>
            <td>
                <img alt='Console Messages Image' src='./Media/Messages.png'>
            </td>
        </tr>
    </tbody>
</table>

When finish, you look a final message (with the elapsed time of the execution) like this:

<table align='center'>
    <theader>
        <th><center>Console Final Message</center></th>
    </theader>
    <tbody>
        <tr>
            <td>
                <img alt='Console Messages Image' src='./Media/FinalMessage.png'>
            </td>
        </tr>
    </tbody>
</table>

At the end of the execution, the program will download the files of every student and save them in the directory of the course that they belong to. Additionally, the program will generate a JSON with the data of the students and courses and it will generate a Pie Chart with the percentage of students that have downloaded the repositories...

Like the image below:

<table align='center'>
    <theader>
        <th><center>Example Pie Chart</center></th>
    </theader>
    <tbody>
        <tr>
            <td>
                <img alt='Example Pie Chart' src='./Media/pieChart.png'>
            </td>
        </tr>
    </tbody>
</table>


<br><br><br>

---

<br><br><br>
### File format
* 1st Column: Date time. [it isn't used yet.]
* 2nd Column: Student Name
* 3rd Column: Student Surname
* 4th Column: Student Division
* 5th Column: Student ID. [it isn't used yet.]
* 6th Column: Student E-mail. [it isn't used yet.]
* 7th Column: Repository Name to download (It could skip the '.git' part)

Like this:

```
"Marca temporal","Nombre/s","Apellido/s","División","DNI / Legajo","E-Mail","Link al repositorio"
"2022/02/13 10:26:52 p. m. GMT-3","Neptune","Romane God","1G - Professor 1 - Helper 1","222222","neptune@notplanet.com","https://github.com/caidevOficial/SPD2022_TPS.git"
"2022/02/13 10:26:52 p. m. GMT-3","Poseidon","Grecian God","1F - Professor 2 - Helper 2","333333","poseidon@sea.com","https://github.com/caidevOficial/Python_ITBA_IEEE.git"
"2022/02/13 10:26:52 p. m. GMT-3","Hades","Grecian God","1F - Professor 2 - Helper 2","111111","Hades@underworld.com","https://github.com/caidevOficial/CaidevOficial.git"
```
<br><br><br>

---

<br><br><br>
# Configuration
In order to use this Cloner, you should configure the file [API_Info.json](./Modules/API_Info.json) with your Github API's information as shown below.

```json
[
    "Github": {
        "URL": "https://api.github.com/repos",
        "USER": "YOUR_GITHUB_USER",
        "REPO": "YOUR_REPOSITORY_NAME",
        "BRANCH": "THE_PRINCIPAL_BRANCH_NAME"
    },
    "DataFrame": {
        "Fields": {
            "Date": "First_Datetime_Field_To_Delete",
            "Name": "Name_For_Column_Of_Names",
            "Surname": "Name_For_Column_Of_Surnames",
            "Course": "Name_For_Column_Of_Courses",
            "ID": "Name_For_Column_Of_Students_ID",
            "Email": "Name_For_Column_Of_Emails",
            "GitLink": "Name_For_Column_Of_Links_To_Repositories"
        }
    },
    "Files": {
        "Dir_Plots_img": "./DIR_FOR_PLOTS_IMAGES",
        "Dir_Cloned_Repos": "./DIR_FOR_CLONED_REPOSITORIES",
    }
]
```

for example:

```json
[
    {
        "URL": "https://api.github.com/repos",
        "USER": "CaidevOficial",
        "REPO": "Python_RepositoryCloner",
        "BRANCH": "main"
    },
    "DataFrame": {
        "Fields": {
            "Date": "Marca temporal",
            "Name": "Nombre/s",
            "Surname": "Apellido/s",
            "Course": "División",
            "ID": "DNI / Legajo",
            "Email": "E-Mail",
            "GitLink": "Link al repositorio"
        }
    },
    "Files": {
        "Dir_Plots_img": "./Plot_Images",
        "Dir_Cloned_Repos": "./Repositories"
    }
]
```

Then the code will make the link like:

```
https://api.github.com/repos/CaidevOficial/Python_RepositoryCloner/commits/main
```

This way the program will take the 'Date' of the last commit of the branch 'main' and will use it to create the folder with the name of the repository. Obviously, the repository <strong>MUST BE PUBLIC</strong>, otherwise the program won't be able to access its API.

Regarding the 'DataFrame' Key, al the keys inside are configured to use them with a 'csv' file with at least theses columns. [Could have more columns, but it's not necessary for us.]

Finally, respect the 'Files' Key, where you can configure the directory where the plots will be saved and the directory where the cloned repositories will be saved.

For our example, the columns of the csv file are:

<table>
    <thead>
        <th>Marca Temporal</th><th>Nombre/s</th><th>Apellido/s</th><th>División</th><th>DNI / Legajo</th><th>E-Mail</th><th>Link al repositorio</th>
    </thead>
    <tbody>
        <tr>
            <td align='center'>
                <h3>2022/02/13 10:26:52 p. m. GMT-3</h3>
            </td>
            <td align='center'>
                <h3>Poseidon</h3>
            </td>
            <td align='center'>
                <h3>Grecian God</h3>
            </td>
            <td align='center'>
                <h3>1F</h3>
            </td>
            <td align='center'>
                <h3>123456789</h3>
            </td>
            <td align='center'>
                <h3>poseidon@grecianGod.olympus</h3>
            </td>
            <td align='center'>
                <h3>https://github.com/caidevOficial/CaidevOficial.git</h3>
            </td>
        </tr>
    </tbody>
</table>
<br><br><br>

---

<br><br><br>
<table align='center'>
    <tr align='center'>
        <h2 align='center'>Technologies used. 📌</h2>
        <td>
            <a href="https://www.python.org/downloads/"><img alt="Pyhton Logo" src="https://github.com/caidevOficial/Logos/blob/master/Lenguajes/py_logo1_1.png?raw=true" width="50px" height="50px" /></a>
        </td>
        <td><center>Python</center></td>
    </tr>
    <tr align='center'>
        <td>
            <a href="https://pandas.pydata.org/"><img alt="Pandas Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png?raw=true" height="50px" /></a>
        </td>
        <td><center>Pandas</center></td>
    </tr>
    <tr align='center'>
        <td>
            <a href="https://numpy.org/"><img alt="NumPy Logo" src="https://caidevoficial.github.io/FF_Resume/media/icons/numpy/numpy_logo.svg?raw=true" height="50px" /></a>
        </td>
        <td><center>Numpy</center></td>
    </tr>
        <tr align='center'>
        <td>
            <a href="https://matplotlib.org/"><img alt="MatPlotLib Logo" src="https://matplotlib.org/_static/logo2_compressed.svg?raw=true" height="50px" /></a>
        </td>
        <td><center>MatPlotLib</center></td>
    </tr>
    <tr align='center'>
        <td>
            <a href="https://code.visualstudio.com/"><img alt="VSCode Logo" src="https://github.com/caidevOficial/Logos/blob/master/Lenguajes/visual-studio-code.svg?raw=true" height="50px" /></a>
        </td>
        <td><center>VSCode</center></td>
    </tr>
</table>
<br><br><br>

---

<br><br><br>
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
<br><br><br>

---

<br><br><br>
<table align='center'>
  <theader>
  <th><h2 align='center'>Where to find me: 🌎</h2></th>
    <tr align='center'>
      <td>
        <img class="circular" alt="Facu" src="https://avatars1.githubusercontent.com/u/12877139?s=400&u=d369ee24466653d9bbeeb9654930e3ff1c67b76a&v=4" width="80px" height="80px" />
      </td>
    </tr>
    <th><center>🤴 Facu Falcone - Junior Developer</center></th>
    </theader>
    <tbody>
    <tr align='center'>
      <td>
        <a href="https://github.com/caidevOficial/">
          <img alt="GitHub" src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" width="125px" height="30px" />
        </a>
      </td>
    </tr>
    <tr align='center'>
      <td>
          <a href="https://www.linkedin.com/in/facundo-falcone/">
            <img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" width="125px" height="30px" />
          </a>
      </td>
    </tr>
    <tr align='center'>
      <td>
        <a href="https://cafecito.app/caidevoficial/">
          <img alt='Invitame un café en cafecito.app' srcset='https://cdn.cafecito.app/imgs/buttons/button_5.png 1x, https://cdn.cafecito.app/imgs/buttons/button_5_2x.png 2x, https://cdn.cafecito.app/imgs/buttons/button_5_3.75x.png 3.75x' src='https://cdn.cafecito.app/imgs/buttons/button_5.png' width="125px" height="30px" />
        </a>
      </td>
    </tr>
    <tr align='center'>
      <td>
        <a href='https://ko-fi.com/P5P74JBOH' target='_blank'>
          <img width="125px" height="30px" style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' />
        </a>
      </td>
    </tr>
  </tbody>
</table>
