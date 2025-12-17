<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/transition-zero/.github/raw/main/profile/img/logo-dark.png">
  <img alt="TransitionZero Logo" width="1000px" src="https://github.com/transition-zero/.github/raw/main/profile/img/logo-light.png">
  <a href="https://www.transitionzero.org/"></a>
</picture>

# Software Engineer Assessment

Thank you for your interest in working with TransitionZero!

This assessment has been developed to assess your basic Python software engineering skills, your knowledge of API frameworks, and your use of version control. We will carry out the assessment as a live coding interview.

We know taking tests is stressful - thanks for taking this one. You're going to do great!


## Instructions

_Scenario:_ Imagine that you and your colleagues at TransitionZero have decided you want to keep track of the books that you have read. You're going to build a data service that catalogues books and their authors.
    
The tasks will be shared with you during the live coding interview. You will be able to ask your interviewer questions and google anything you need to refresh your memory on, but we will ask you not to use AI for this exercise.

You may set up the application on your machine ahead of the interview if you wish, following the setup instructions below.

### Setup

**1. Clone this repository** to a development environment of your choice, and create and activate a virtual environment.
    
**2. Install this repo** in your virtual environment by running `make install`.

**3. Spin up a containerised postgres instance.** Run `make db` to launch a local instance of the database with the settings specified in the `.env` file.

**4. Load data into your database.** Run `make load_data` to build the database and load the data contained in `bin/tz_reads.csv`.
