[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gTEh4MXp)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16227139)
# Data Visualization - Fall 2024 - Final Project

# Due date: December 16th 2024 by 11:59pm

> [!IMPORTANT]  
> Please read this thoroughly, and reach out with any questions!

## Introduction

The final project for the semester will simulate use of data management and visualization techniques we have covered so far in a professional setting.

> [!IMPORTANT]
> <b>The goal of the project is to choose a topic and accompanying dataset, extract original insights from the topic at hand, visualize the results with plots (like in a scientific report), creating a Dashboard (or a set on mini-dashboards) to illustrates the main conclusions, and produce a professional report in a Jupyter notebook.</b>

We want to identify some set of rich data either from a live source or from a scientific publication, and provide the viewer with a means to explore the data and perhaps a means to compute some statistics or measures on the data. You will need to verify your data source and ensure that there is enough data to work with. *Enough* is subjective, and so do not hesitate to reach out with questions. Remember that data analysis may have unexpected, or unremarkable, conclusions. If your results are not what you expect, not exciting, or otherwise useless, *that is ok*. The point of this project is to tell a story, and sometimes stories are boring.

> [!IMPORTANT]  
> Individuals and groups must inform me of their team by October 4th<br><br> Teams must work with me on a topic and data source by October 14th<br>&emsp; - The sooner you get started working on a topic and data after October 4th the better<br>&emsp;&emsp; - I will try not to reject any topics, but there must be sufficient supporting data<br><br> If you are in a group of 3, I would expect to see about 3x the level of work than an individual.<br><br> I will also require each student to fill out a survey about each of their teammates work that they've done.<br><br> If an individual scores poorly on the surveys from teammates, they will get penalized a maximum of 25% per each negative survey. <br><br> DO NOT let your team down!

> [!NOTE]  
> If there are libraries/modules you wish to use that are not available in our cloud environment, please let me know as soon as possible and I will get them added.

## Deliverables

> [!IMPORTANT]  
> All 3 of the following deliverables are required!

**Project Abstract**: Write one paragraph in a README file specifying the concept you are going to be analyzing, where you can get data about that problem, what techniques you think you might be able to apply to it, and what insights you plan to attempt to extract from it. The project abstract is due the same day as the project itself, but it is highly recommended to review your topic idea with your instructor first. Sending via email or discussing in office hours are both acceptable.

**Project Notebook**: This is the main artifact of the final project. It should be a professionally written report on the data, your methods, and the insights you gained from it, including any data management techniques you used to extract those insights and visualizations which display them. The main points must be expressed using a Dashboard.

**Project Modules and OOP**: Rather than developing large chunks of code in your Jupyter notebook, you are required to implement complex functions in their own modules and call these modules from your notebook. You are also required to implement an amount of Object-Oriented Programming (OOP) as per the Grading Rubric. There should be a minimal amount of code in your Jupyter notebook because the project should be presented as a formal analysis of whatever topic you decide to cover.

> [!WARNING]
> You are expected to site references, sources, and and more. Failure to properly site the work of others is considered plagiarism. While you will undoubtedly seek the internet for help with your code, your submission must be your own original code and not just a mashup of the work of others. Using ChatGPT and/or other AI tools to assist in your project is strictly prohibited. <br><br> All deliverables shall be provided by **11:59pm on Dec 16th**. Please submit via GitHub but note that no points will be deducted for an improper git submission for this project. Git submission mechanics were assessed in the beginning of the semester. The goal of this assignment is to assess your ability to extract original insights to tell a data driven story that is entirely your own.

> [!CAUTION]
> <b>Any violations of our "ChatGPT & AI Technologies" or "University Policies on Academic Integrity" laid out in our Syllabus will result in the Final Project getting a maximum score of 0.</b>

## Requirements

The following project requirements on format, technical depth, insight, software, technical communication, and use of techniques from class shall be adhered to.

### Format

> [!IMPORTANT]  
> The project Notebook deliverable shall be written as a professional report in the following format. Each bullet should be a top level section in your notebook.

**Introduction**: Write 1-2 paragraphs introducing the topic and dataset you are studying. Review the rest of the sections of the notebook. Explain what techniques you will be applying and why you are applying them. Employ a visual to show the problem or dataset you are studying at a glace.

**Motivation**: Write a paragraph explaining why you are studying this topic and why the reader should care about the insights you gain from it. There are many topics to be analyzed in the world. Explain why yours matters!

**Methods**: Explain the methods you are using to study your topic or dataset. Include a subsection for each method you employed. Explain why you chose each method. Write at least a short paragraph for each method used.

**Main Results**: Present the main results here as a Dashboard or set of Dashboards. Be sure to employ at least three techniques from class (see the grading rubric). Include a subsection for each main result that include the visualizations of the result and a short paragraph explaining each.

**Conclusion**: Summarize your findings and contributions in a paragraph here.

### Technical Communication

Project notebooks shall showcase professional technical communication skills. Project notebooks shall be divided into well structured sections and shall use markdown to specify headings for each section. Project notebooks shall use LaTeX within markdown to typeset equations. Project notebooks shall be written in full sentences and well-constructed paragraphs (3-10 sentences per paragraph). Writing shall guide readers through the material by narrating where they are in the document and explaining where they are going next.

### Use of Techniques from Class

### Mandatory 5
> [!IMPORTANT] 
> <b>Project notebooks must have the following 5 techniques that we've learned:</b>

1. DataFrame operations, including cleaning data techniques
2. Software Hygiene (black)
3. OOP and Python Modules
4. Use of holoviews and hvplot to generate data observations throughout the report
<br>&emsp;&emsp;- You may use a different library for plotting
5. Panel Dashboard(s) for main result (see grading rubric, no Dashboard = minus **10 points**)
<br>&emsp;&emsp;- If using plotly, you may use Dash for your dashboard
<br>&emsp;&emsp;- This Dashboard will serve to also provide the use of interactive plots to explore data

### Mandatory 2, choose from 9
> [!IMPORTANT] 
> <b>Project notebooks must include at least 2 of the following techniques that we've learned:</b>

* a) Use of histograms to represent distributions and use of combined scatter and histograms to represent joint and marginal distributions, and using clustering to visualize groups of data
* b) Complete Case Analysis and use of machine learning models to impute and score missing data
* c) Visualizations of cleaning data and machine learning accuracy
* d) Representation of multivariate data using colors, markers, 3D plots, and interactive plots
* e) Correlation and fitting techniques
* f) Use of mathematical transforms to extract insights from data (Fourier or other)
* g) Use of principal component analysis to reduce high dimensional data to a low dimensional space for visualization
* h) Use of geopy to obtain geographic data, use of geopandas and geoviews to plot shapes and lines on a map
* i) Use of pymap3d to handle coordinate conversions when working with geographic data


# Grading Rubric
> [!IMPORTANT] 
> The following grading rubic is important in its entirety. Please read carefully!

The project will be graded out of 100 points.

## Originality (10%)
> [!IMPORTANT]  
> Originality (20%)

The following criteria will be used to assess the originality of a project.

### Choice of Topic and Dataset
Project notebooks shall represent an analysis of a topic of interest to the student's field of choice and explain why it is of interest to this community. Notebooks lacking explanation of why a problem is of interest will lose a maximum of **5 points**.

### Original Steps to Visualize the Topic

Project notebooks shall go beyond simply calling available functions from one or two popular libraries and shall instead take original steps to analyze the topic by combining tools from many libraries in unique ways. Notebooks that use < 2 tools to perform straightforward analysis (e.g., simply generate some default plots) will lose a maximum of **5 points**.

### Original Insights and Code

The insights shall be exposited in an original manner. Each insight should be explained in an original manner, in your own words. Use analogies and other explanatory devices to help the reader see the insights you have extracted from the data and take action on them. All code and writing must be the student's own work.

<br><br>
## Software Hygiene (20%)
> [!IMPORTANT]  
> Software Hygiene (20%)

### Use of Modules

Any functions longer than 20 lines of code shall be implemented in importable modules. If any functions greater than 20 lines of code implemented within project notebooks, **5 points** will be deducted.

### High Quality Documentation

All project deliverables shall provide high quality documentation. All functions shall have docstrings. Use comments, but do not comment every line of code. Write code that is self-explanatory and does not need a comment for every line. Ensure the notebook reads like a professional report. Notebooks and modules without high quality documentation will lose **5 points**.

### Descriptive Variable and Function Names

Variable names shall be descriptive nouns. Function names shall be descriptive verbs. One letter variable names shall not be used. Variables which store measured quantities shall include the units of the measured quantities in their names. Poor quality variable names will lose **5 points**.

### Use of a Style Guide

Project notebooks shall be styled with `black`. Running `black` once before submission is sufficient. Projects clearly unstyled will lose **2 points**.

### Dead Code

Project notebooks shall contain no commented out or dead code. Notebooks with dead code with lose **2 points**.

### Quality of Commit Messages

Write high quality commit messages using the guidance learned in class. A good commit message should read `"When applied, this commit will...[insert your message here]"`. Poor quality commit messages will lose **1 points**.

<br><br>
## Data Management and Visualization Professionalism (70%)
> [!IMPORTANT]  
> Data Management and Visualization Professionalism (70%)

### This is broken down into 3 parts:

### 1. Project Format and Cleanliness (15%)
* Notebooks shall adhere to the [project format](#format). Notebooks that do not will lose **5 points**.
* Notebook shall use full sentences and paragraphs. Writing that is not in full sentences and paragraphs will lose **5 points**.
* Notebooks shall use a spell checker. Numerous spelling errors (> 5) will lose **2 points**.
* Notebooks shall be written in clear expository tone. Do not use an exploratory tone, e.g., do not write "here we try X, it didn't work, so instead let's try Y". Exploratory tone is encouraged in exploratory notes, but this project will produce a final deliverable! Exploratory tone will result in a **2 point** deduction.
* Do not forget to make the goal of each notebook section clear to the reader. Failure to narrate where the reader is in the notebook will result in a **1 point** deduction.

### 2. Object-Oriented Programming (5%)
* Use of OOP is a must. You must have at least 1 class defined that has > 3 methods. A project without any OOP will result in a **5 point** deduction.

### 3. Telling a data-driven story and using a Dashboard (50%)
* Notebooks shall act as presentations, written and designed such that a user with no knowledge of your project topic should be able to understand the material and make clear conclusions. **10 points**
* Data visualizations must make sense and have clear and effective insights **20 points**
* The Dashboard works and highlights key results about the data. **20 points**
> [!CAUTION]
> No Dashboard at all results in a **20 point** deduction!

> [!WARNING]  
> If the Dashboard is not working, I must be informed at least 1 week prior to final project submission so we can try to fix it.<br>&emsp;- We can try to fix it the weekend before, but there is no guarantee.<br>&emsp;&emsp; - A non-working Dashboard will result in a maximum of a **10 point** deduction. <br>&emsp;&emsp;&emsp; - If we've discussed it and tried to fix it, it will be at maximum a **5 point** deduction


### Examples from Previous Students

* Taylor Swift Album Release Effects on Spotify - live data from Spotify's data API was recorded for the weeks leading up to and after the release of Taylor Swift's album *Red (Taylor's Version)*
* Steam Player Behaviors - live data from Steam's data API was recorded hourly for a select number of games for the months of October and November to show behavioral patterns of gamers
* Magic the Gathering Rules Complexity - dataset of all cards was used to attempt to show how the complexity of the game has increased over the years by associating rules complexity with the word counts for every card.
* COVID-19 Pandemic Spread - COVID-19 infection rates for counties across the USA from mid 2020 through mid 2021 were interatively visualized to show the fluctuations of infection hotspots
