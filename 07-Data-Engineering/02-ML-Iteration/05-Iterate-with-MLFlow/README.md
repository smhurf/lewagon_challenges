# Iterate with MlFlow

Now that we have built a simple model and tracked the results with MLflow, we want to make it better! The ultimate goal is having a model that makes more accurate predictions on the test set, hence getting a RMSE as low as possible.

**So what can we do?**

There are many different things that make models better:
- build and try to use different or more features
- test with different estimators (linear, non linear, etc..)
- tune hyperparameters

In this series of exercise, you will get hands on using the [MLFlow Tracking Api](https://www.mlflow.org/docs/latest/tracking.html) in order to experiment with different features, models and parameters.

We now have a good workflow to make model improvements and it is very important to track all our different experiments. We want to be able to save all our different training runs and compare their performance

This is what MLFlow tracking is about.

## Summary
1. [Try different models](#part2)
2. [Features engineering](#part3)

## Prerequisites
Before carrying on make sure you understood:
- the structure of the `Trainer()` class from ex1 is clear, if not please reach out to one of your TA's
- the way to log a metric and a parameter on [wagon_hosted_mlflow server](https://mlflow.lewagon.co/#/experiments/0)
- how to pass random number of parameters to a class or functions (`**kwargs`), and how to access them
- you might need to `pip install category_encoders memoized_property psutil xgboost pygeohash`

We are going to modify the `trainer.py` in order to push the training parameters and metrics to **MLflow**.

Please add the following method to your trainer (and fill its content):

``` python
    def save_model(self):
        """Save the model into a .joblib format"""

    # mlflow methods
```

Do not forget to add and import for the `joblib` package and to call the `save_model` method in your `if main` block of code (`if __name__ == "__main__":`)

👉 We will call the `save_model()` method in order to push data to MLflow, keep it in mind for later
👉 Once you're happy with your model's performance, you will submit your best model’s predictions to kaggle

Last thing, we suggested here a package structure to organize your code and your run, feel free to tweak is as you like if need be.
## 0. Define your experiment name
You will all continue to log your run results and parameters on the same MLFLOW instance hosted on le wagon server.  Make sure, you will have your own global `EXPERIMENT_NAME` variable defined inside `trainer.py` as follows:
```python
EXPERIMENT_NAME = "[Country][City][github]TaxiFareModel"
```

## 1. Try different models <a name=part2></a>
- Think about the different estimators that you know that can be used to solve prediction problems
- Implement a short script that will loop through all estimators, train the model and evaluate it on a validation set.
👉 Here you might need to tweek `TaxiFareModel` package
- View results with on [wagon_hosted_mlflow server](https://mlflow.lewagon.co/#/experiments/0)

And last advice, while building your pipeline, run it on small datasample

## 2. Features engineering and selection <a name=part3></a>
**Now it is time to be creative!**

You just tried different models, and you now see that some estimators may be more powerful than others. Another area where you can experiment is about `features engineering`.

- Try different combinations of features (by removing or adding some) and track the runs.
💡`direction`, `manhattan distance`, `euclidian distance`, `geohash`
- Use some "context knowledge" to generate new features that you think might be explaining the fares.
 👉 For example: we know that taxis apply a fixed amount for airport transfers
- Try different methods for removing outliers
- Look at how the size of the training set helps to reduce the RMSE on the validation set

### 💡 Suggested method to track influence of Feature Engineering:
You will use the benefits of Pipelines integrated into our custom class.
Start with one additional feature: `distance_to_center`(go back to data-challenges/07-Data-Engineering/02-ML-Iteration/01-Kaggle-Taxi-Fare notebook to find complete feature engineering options):

1. Implement a Custom Transformer class inside encoders.py called `DistanceToCenter`, which returns a `distance_to_center` column
2. Add a feature engineering block `feateng_block` variable to your `set_pipeline()` method which holds all the available pre-processing pipelines (now including distance_to_center)
3. Update the params being fed to the `Trainer()` class at the start of a run to specify which pipelines within the block to use in the final pipeline for that particular run
4. launch 2 new runs, one with the `distance_to_center` being used during training and one without, then compare their scores
5. Once you understand the process, add as many features as you want and analyse the impact on performances from different combinations
Bonus - Use [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html) transfomer to generate new features from distance.
