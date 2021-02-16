
**The goal of today's recap is to go over the process of converting a training notebook into a training package.**

## Let's start by generating a new taxifare package

``` bash
packgenlite taxifare
```

Since we want to be able to test and use our package in the **taxifare/notebooks/usage.ipynb** notebook as it is being built, we will install it using the `-e` flag...

``` bash
cd taxifare
pip install -e .
```

## Have a look at the training notebook

Let's run the **taxifare/notebooks/boilerplate.ipynb** notebook and see how it works.

## Decompose it into elements for our package

Now we will go through all the cells one by one and progressively move the code into our package.

We may adopt the following structure for the code of the package:

```
taxifare
├── __init__.py
├── data.py
├── metrics.py
├── mlflow.py
├── model.py
├── pipeline.py
├── trainer.py
└── transformers
    ├── distance_transformer.py
    └── utils.py
```

## Usage notebook

The goal is to refactor the code of the training notebook into the package so that the usage notebook can be run without errors.

You may progressively run the cells of the usage notebook in order to both see way the output of your package is. And in order to see the definitive output once the refactor is over.

## First step: Trainer class

The first step is to run without getting errors the **Trainer using our package** cell.

The package should be able to:
- Load some number of rows from the taxifare dataset
- Use a holdout
- Create a `Pipeline` containing the data cleaning and preprocessing
- Train a `RandomForestRegressor`
- Evaluate the performance
- Save the trained model to disk
- Save the parameters and metrics of the run to https://mlflow.lewagon.co

## Second step: ParamTrainer class

The second step is to run without getting errors the **Trainer with params and gridsearch** cell.

We want our package to be able to:
- Train on a combination of models and pipeline hyperparameters
- Use a `GridSearch` on our pipeline
