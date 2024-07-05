# Sri Lanka advanced level exam Z-score to subject API

## What is the purpose
---

#### The user is able to input the subjects, district and the z-score of the student and the API provides the relevent courses the student can apply

## Features
---

- Find the Courses
- Guess the Marks using Zscore 

##  How to setup
---
```bash
git clone https://github.com/Dileesha-abilash/Z_score_api.git

//change the distric subjects and zscore
python3 Course.py

// change the zscore and subject letters
python3 Marks_Guess.py

```

## structure of data file 
---
![d1](https://github.com/Dileesha-abilash/Z_score_api/assets/94125793/d6e3b978-c010-4e7f-bb6f-02b2db9aab33)
1. The `$` mark separates the possible combination sets
2. before the  `#` is mandatory subjects and after `#` have optional subjects ()


## Limitations 
---
- Dataset used to Guess the marks is way older ( 2011 - new syllabus ) .Stranded deviation and Mean is not release by Government So cant find the Recent Values for Calculations .
- We have only Data of Subjects in Science Steam (BIo/Maths) 
## Logical Errors 
---
- Some Courses require O/L Results.
- Relevancy of dataset used to calculate Guessed marks is often Failed-irrelevant (just created for fun 😁) 
### all the data obtain by 2022(2023) student_handbook_english.pdf
