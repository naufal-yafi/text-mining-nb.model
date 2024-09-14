# Text Mining: Naive Bayes

# Table of Content

- [Text Mining: Naive Bayes](#text-mining-naive-bayes)
- [Table of Content](#table-of-content)
  - [Libraries](#libraries)
  - [Software Required](#software-required)
  - [How to use this project](#how-to-use-this-project)
  - [Preprocessing Data](#preprocessing-data)
  - [Export model to PKL](#export-model-to-pkl)
  - [Running App](#running-app)

## Libraries

[[See all libraries use in this project](./requirements.txt)]

## Software Required

1. Jupyter Notebook
2. Python
3. Pip

## How to use this project

1. Create VENV

```sh
sh run -cv
```

2. Activate VENV

```sh
source active
```

3. Create Kernel

```sh
sh run -ck
```

4. Install All Libraries

```sh
sh run -i
```

5. Setup file .env

```sh
cp .env.example .env
```

Add field `BASE_DIR=`  
Example: /home/..user/text-mining or /home/..user/..your_folder/text-mining

## Preprocessing Data

```sh
sh run -p
```

## Export model to PKL

```sh
sh run -e
```

## Running App

1. Export model to PKL

```sh
sh run -e
```

2. Run server app

```sh
sh run -s
```
