![py version](https://img.shields.io/badge/python3-v_3.12.5-blue) ![pip version](https://img.shields.io/badge/pip3-v_24.2-blue) ![os](https://img.shields.io/badge/alpine_linux-v_3.17.0-blue)

# Text Mining: Naive Bayes

This repository is an implementation of `text mining` to classify texts into **Kurikulum**, **Kesiswaan** or **Prasarana** categories using the `Multinomial Naive Bayes` algorithm.

# How to use this project:

## 1. Setup

- Create VENV
  ```sh
  sh run -cv
  ```
- Activate VENV  
  1. Linux/MacOS:
      ```sh
      source active
      ```
  2. Windows (cmd):
      ```sh
      venv\Scripts\activate.bat
      ```
  3.  Windows (powershell):
      ```sh
      venv\Scripts\Activate.ps1
      ```
- Create kernel (optional)
  ```sh
  sh run -ck
  ```
- Install all libraries
  ```sh
  sh run -i
  ```
- Setup custom package
  ```sh
  pip install -e .
  ```
- Setup environment variable  
  Field value variable on `.env`
  ```sh
  cp .env.example .env
  ```

## 2. Preprocessing Data

```sh
sh run -p
```

## 3. Creating Model

```sh
sh run -e
```

## 4. Running App

```sh
sh run -s
```
