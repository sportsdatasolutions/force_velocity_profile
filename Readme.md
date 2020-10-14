## Force Velocity ⚡️ [<img height="31" align="right" src="https://beta.deepnote.com/buttons/launch-in-deepnote-white.svg">](https://deepnote.com/project/fd05da77-5433-4d53-995a-78fb358e2927)

> Notebook for obtaining data and KPIs needed in Force Velocity Profiles (from instant velocity over time e.g. GPS, Radar) w/ Usain Bolt Example Data

![Bolt](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/Links/UsainBolt.jpeg)

## Getting Started

> ***Fork*** this repo and clone your own fork locally or on Deepnote. See instruction below to install dependencies and run the program.

**Note:** For learning purposes, ***recreate*** this repository yourself as apposed to cloning or forking.

### ```Story```

> The methods used in this notebook for calculating Force Velocity Profile data and KPIs were inspired by this [post and excel template by JB Morin](https://jbmorin.net/2017/12/13/a-spreadsheet-for-sprint-acceleration-force-velocity-power-profiling/).

#### [```Speed Export Usain Bolt 120805.csv```](./data/Speed%20Export%20for%20Usain%20Bolt%20120805.csv)

This csv file contains Usain Bolt's ***velocity*** over the period of his 100m Final Race in London, 2012. You'll find it in the ```data``` folder. The data has recorded velocity at every 10th of a second (this would be similar to having a GPS device sampling at 10hz).

#### [```fvp.ipynb```](./fvp.ipynb)  

This is the notebook used for ***calculating*** and ***plotting*** Usaing Bolt's Force Velocity Profile. The notebook will still run without the plots (if you'd just like to format the data to visualise else where), but, even better, you may even want to create a ***script version*** (```.py```) of the notebook to run ***without*** Jupyter or Deepnote (Github Actions > Cloud Storage > BI/WebApp?).

#### [```helpers.py```](helpers.py)

This is a ***Python Module*** containing some methods imported for use in the notebook.

#### [```Usain Bolt FVP Stats 120805.csv```](./fvp/Usain%Bolt%FVP%Stats%120805.csv)

This is the result of a smooth run of the [```fvp.ipynb```](./fvp.ipynb) notebook. The FVP KPIS will be simply be appened onto the end of the modeled FVP data (to avoid having that data separate, could alternatively store as JSON).

### ```Dependencies```

> **If cloned locally**, install dependencies in ```Pipfile```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install pipenv
# Run pipenv install (within cloned project directory)
$ pipenv install
```

### ```Running```

> To run the notebook simply open the ```fvp.ipynb``` file within your chosen Python environment (Jupyter/Deepnote). For a ***local*** development setup, do something like...

```bash
$ pipenv run jupyter notebook .
```

## Contributing

> See [contributing.md](./contributing.md)
