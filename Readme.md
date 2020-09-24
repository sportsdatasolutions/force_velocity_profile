## Force Velocity ⚡️ 

> Notebook for obtaining data and KPIs needed in Force Velocity Profiles (from instant velocity over time e.g. GPS, Radar) w/ Usain Bolt Example Data

### Getting Started

> ***Fork*** this repo and clone your own fork locally or on Deepnote. See instruction below to install dependencies and run the program.

**Note:** For learning purposes, ***recreate*** this repository yourself as apposed to cloning or forking.

#### ```User Story```

> The methods used in this notebook for calculating Force Velocity Profile data and KPIs were inspired by this [post and excel template by JB Morin](https://jbmorin.net/2017/12/13/a-spreadsheet-for-sprint-acceleration-force-velocity-power-profiling/).

##### ```[Speed Export Usain Bolt 120805.csv](./data/Speed Export Usain Bolt 120805.csv)```

This csv file contains Usain Bolt's ***velocity*** over the period of his 100m Final Race in London, 2012. You'll find it in the ```data``` folder. The data has recorded velocity at every 10th of a second (this would be similar to having a GPS device sampling at 10hz).

##### ```[fvp.ipynb](./fvp.ipynb)```

This is the notebook used for ***calculating*** and ***plotting*** Usaing Bolt's Force Velocity Profile. The notebook will still run without the plots (if you'd just like to format the data to visualise else where), but, even better, you may even want to create a ***script version*** (```.py```) of the notebook to run ***without*** Jupyter or Deepnote (Github Actions > Cloud Storage > BI/WebApp?).

##### ```[helpers.py](helpers.py)```

This is a ***Python Module*** containing some methods imported for use in the notebook.

##### ```[Usain Bolt FVP Stats 120805.csv](Usain Bolt FVP Stats 120805.csv)```

This is the result of a smooth run of the ```[fvp.ipynb](./fvp.ipynb)``` notebook. The FVP KPIS will be simply be appened onto the end of the modeled FVP data (to avoid having that data separate, could alternatively store as JSON).

#### ```Dependencies```

> **If cloned locally**, install dependencies in ```Pipfile```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install pipenv
# Run pipenv install (within cloned project directory)
$ pipenv install
```

> **If cloned in Deepnote**, ***replace*** the code in ```init.ipyb``` (via Environment Tab) ***with code below***, and ***restart*** the ***machine***.

```bash
%%bash
# Make sure we change into the project directory, if you have placed your project in the deepnote root directory comment out the line below.
cd force_velocity_profile
# If your project has a 'Pipfile' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f Pipfile
  then
    sed -i '/jedi/d;/jupyter/d;' Pipfile
    pip install pipenv
    pipenv install
  else echo "There's no Pipfile, so nothing to install. This is the case with most projects."
fi
```

#### ```Run```

> To run the notebook simply open the ```fvp.ipynb``` file within your Python environment of choice. For ***Deepnote*** or ***Colab*** simply import the project and open ```fvp.ipynb``` or for a ***local*** development setup, do something like...

```bash
$ pipenv run jupyter notebook .
```

### [Contributing](./contributing.md)