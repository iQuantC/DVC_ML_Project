# Machine Learning project with DVC (Data Version Control)
This project uses the Iris dataset to demonstrate a basic ML pipeline with DVC for data and model versioning.


## Requirements
1. DVC:             To track data, model, and pipeline stages
2. Git:             For version control
3. Scikit-learn:    To train a model
4. Pandas and Joblib


## Set up Environment

### Create and Activate Virtual ENV
```sh
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Initialize Git & DVC
```sh
git init
```
```sh
dvc init
```

### Download & Add Dataset to Data directory
```sh
mkdir data
```

```sh
wget -O data/iris.csv https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
```

### Add Iris dataset with DVC tracking

```sh
dvc add data/iris.csv
```

### Track the changes with git
```sh
git add data/iris.csv.dvc 
```

```sh
git commit -m "Add Iris dataset with DVC tracking"
```


## Create DVC Pipeline

### Data Preparation Step
```sh
dvc stage add -n prepare \
  -d src/prepare.py -d data/iris.csv \
  -o data/X_train.csv -o data/X_test.csv -o data/y_train.csv -o data/y_test.csv \
  python src/prepare.py
```

### Model Training Step
```sh
dvc stage add -n train \
  -d src/train.py -d data/X_train.csv -d data/y_train.csv \
  -o model/model.joblib \
  python src/train.py
```

### Evaluate Trained Model
```sh
dvc stage add -n evaluate \
  -d src/evaluate.py -d model/model.joblib -d data/X_test.csv -d data/y_test.csv \
  -M metrics.json \
  python src/evaluate.py
```

### Commit Changes
```sh
git add dvc.yaml 
```
```sh
git commit -m "Add DVC pipeline stages for prepare, train, evaluate"
```


### Run the Full Pipeline
```sh
dvc repro
```

If Pipeline is successful, run the command:
```sh
git add dvc.lock
```

### Visualize Metrics
```sh
dvc metrics show
```

Optional:
```sh
dvc metrics diff --targets metrics.json
```


## Use Makefile to Automate the entire DVC Pipeline

### Install make
```sh
sudo apt install make -y
```

```sh
cd <directory with Makefile>
```

### Run Any of the Tasks in the DVC Pipeline
```sh
make install     # installs dependencies
make run         # runs the DVC pipeline
make metrics     # shows metrics from metrics.json
```



## Deploy the Trained Model w/ Gradio + Joblib

```sh
pip install gradio
```
Already installed earlier in requirements.txt

```sh
python app/gradio_app.py
```

On your browser, open:
```sh
http://localhost:7860
```

## Now, Let's Simulate Data Change

### Take Backup & Modify the Original Dataset
```sh
cp data/iris.csv data/iris.csv.bak
```

Append a fake row (synthetic)
```sh
echo "4.4,5.6,2.9,1.8,synthetic_class" >> data/iris.csv
echo "4.0,5.0,2.0,1.0,synthetic_class" >> data/iris.csv
```
Check iris.csv to see modification

### Track the Data Change with DVC
```sh
dvc add data/iris.csv
```

### Commit changes
```sh
git add data/iris.csv.dvc
git commit -m "Modified iris dataset with synthetic sample"
```

### Re-run Pipeline
```sh
dvc repro
```

### Track Changes with Git
```sh
git add model/model.joblib dvc.lock metrics.json
git commit -m "Retrained model with updated data"
```

### Run Experiments without committing
```sh
dvc exp run
```

### List experiments
```sh
dvc exp show
```
q to Exit


### Save the best one & commit it
```sh
dvc exp apply <exp_id>
```
```sh
git add .
git commit -m "Applied best model experiment"
```

## Let Simulate Rollback 

### Run New Experience & Apply Best Experiment
```sh
dvc exp run
```
```sh
dvc exp show
```
```sh
dvc exp apply <exp_id>
git add .
git commit -m "Applied better model from experiment"
```

### Get Git Logs and Checkout Old Commit
```sh
git log --oneline
```

### Copy the commit hash you want to roll back to:
```sh
git checkout <old_commit_hash>
```

### Roll back all DVC-tracked files (data/model/metrics)
```sh
dvc checkout
```

