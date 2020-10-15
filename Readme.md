## Force Velocity ⚡️ [<img height="31" align="right" src="https://beta.deepnote.com/buttons/launch-in-deepnote-white.svg">](https://deepnote.com/project/fd05da77-5433-4d53-995a-78fb358e2927)

> Notebook for obtaining data and KPIs needed in Force Velocity Profiles (from instant velocity over time e.g. GPS, Radar) w/ Usain Bolt Example Data

![Bolt](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/Links/UsainBolt.jpeg)

## Getting Started

> Duplicate the project on **Deepnote** (See launch in Deepnote button at **top** of Readme), **or**, fork this repo to clone in a **local** Python environment e.g.

```bash
$ git clone git@github.com:githubusername/force_velocity_profile.git && cd force_velocity_profile
```

**Note:** For learning purposes, ***recreate*** this repository yourself as apposed to cloning or forking.

### ```Story```

> The methods used in this notebook for calculating Force Velocity Profile data and KPIs were inspired by this [post and excel template by JB Morin](https://jbmorin.net/2017/12/13/a-spreadsheet-for-sprint-acceleration-force-velocity-power-profiling/).

#### [```Speed Export Usain Bolt 120805.csv```](./data/Speed%20Export%20for%20Usain%20Bolt%20120805.csv)

This csv file contains Usain Bolt's ***velocity*** over the period of his 100m Final Race in London, 2012. You'll find it in the ```data``` folder. The data has recorded velocity at every 10th of a second (this would be similar to having a GPS device sampling at 10hz).

#### [```fvp.ipynb```](./fvp.ipynb)  

This is the notebook used for ***calculating*** and ***plotting*** Usain Bolt's Force Velocity Profile. The notebook can still run without the plots and output the FVP data with KPIs to a csv file within the ```fvp``` folder.

#### [```helpers.py```](helpers.py)

This is a ***Python Module*** containing some methods imported for use in the notebook. This was mainly done to keep the notebook clean, however, if in Deepnote, you can now hide code from a code cell and still display it's output (open command pallet on a notebook and search: hide), if you prefer that.

#### [```Usain Bolt FVP Stats 120805.csv```](./fvp/Usain%Bolt%FVP%Stats%120805.csv)

This is the result of a smooth run of the [```fvp.ipynb```](./fvp.ipynb) notebook. The KPIS will be simply be appened onto the end of the modeled FVP data (to avoid having that data separate, could alternatively store as JSON).

### ```Dependencies```

> If on **Deepnote**, please see the **```init.ipynb``` (environment tab)** to see how the project is setup. **If cloned locally**, install dependencies in ```Pipfile```. See [the docs](https://docs.pipenv.org/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install --user pipenv
# Run pipenv install (within cloned project directory)
$ pipenv install
```

> And **install** ```jupyter``` if you'd like to run the **notebook** version e.g.

```bash
$ pipenv install jupyter
```

### ```Running```

> To run the notebook simply open the ```fvp.ipynb``` file within your chosen Python environment (Jupyter/Deepnote). For a ***local*** development setup, do something like...

```bash
$ pipenv run jupyter notebook .
```

## Contributing

> See [contributing.md](./contributing.md)
