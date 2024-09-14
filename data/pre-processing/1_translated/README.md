# Translated CSV

I used [Google Spreadsheets](https://docs.google.com/spreadsheets/u/0/) to translate all the csv rows.

Formula:

```sh
=GOOGLETRANSLATE(column; "en"; "id")
```

Example:

```sh
=GOOGLETRANSLATE(B2; "en"; "id")
```
