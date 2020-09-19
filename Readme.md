## Force Velocity Profiles

> Script for obtaining data and KPIs needed in Force Velocity Profiles (from instant velocity over time e.g. GPS Devise)

### Getting Started

For learning purposes, ***recreate*** this repository yourself as apposed to cloning or forking. The methods used for calculating Force Velocity Profile data and KPIs were inspired by this [post and excel template by JB Morin](https://jbmorin.net/2017/12/13/a-spreadsheet-for-sprint-acceleration-force-velocity-power-profiling/).

#### ```dependencies```

> Check the [Pipfile](./Pipfile).

#### ```boltfvp.csv```

> This csv file apparently contains Usain Bolt's velocity (from a radar gun) over a 5 second period. The data is 5 seconds long, as this is the recommended timespan for a FVP in a sprint, and sampled at 10Hz, to mimic that of a GPS devise sampling at 10Hz. The only additional data we need from Bolt are his mass and height, and we're good to go!

#### ```fvp.ipynb``` or ```fvp.py```

> There are the two identical python scripts. One is an interactive notebook (```fvp.ipynb```) and the other is simply a script (```fvp.py```). This is so you can run the FVP solution in the Python environment of your choice.

#### ```helpers.py```

> This is a python module containing some methods used in the main FVP script.

#### ```User Story```

> The FVP script takes in veclocity over time data in csv format (see ```boltfvp.csv```),
>
> Models Speed, Acceleration, Force and Power off Velocity and Time,
>
> Calculates Key PFV KPIs and appends them to the main data frame,
>
> Writes this data to a new csv file called ```boltfvp_stats.csv```.

#### ```Run```

> To run the script simply open the ```fvp.ipynb``` file or ```fvp.py``` file within your Python environment of choice. For ***Deepnote*** or ***Colab*** simply import the project and open ```fvp.ipynb``` or for a ***local*** development setup, do something like...

```bash
# with jupyter
$ jupyter notebook fvp.ipynb
# with python
$ python fvp.py
# or with pipenv
$ pipenv run jupyter notebook fvp.ipynb
$ pipenv run python fvp.py
```

-----

### [Contributing](./contributing.md)
