# CFB_Reticulated

## About the Project

This project took a skeleton dashboard and updated the dashboard to include information on the prescribing data collected from a primary care trust.
The dataset was downloaded and key information was pulled to be displayed on the dashboard with edits to the code of several scripts made to ensure this is carried out.

Key information pulled extends to include...

## The Database

The abxdb.db database contains a mass amount of information regarding the prescribed items. The subset of the database and the relation between the two tables can be seen below. The dashboard makes key information from this database easy to view, this means the user will not have to spend time searching the database.

![image](/DB_diagram.png)

## Built With

Major frameworks/libraries used to build this project;

#### SQL
##### Python flask

## Installation

First the database should be downloaded from https://www.dropbox.com/s/76cawm3bmnwdtza/abxdb.db?dl=0 and saved in the same folder that the github repository needed for this project will be cloned to.
Next, the following repo should be cloned into that folder https://github.com/IAM-lab/MIE-skeleton. The run.py file can be used to run/serve the dashboard. The abxdb.db contains the prescribing data.


## Usage

The dashboard can be accessed to gather specific information from the prescribing data by running unning the run.py file and accessing the dashboard using the following the url http://127.0.0.1:5000/dashboard/home/


![image](/imgD.png)

### Features:

The dashboard comes with an 'About' feature that enables users to gather some information about the project

Other features include the boxes shown containing key information, these include;

#### Total items prescribed
#### Prescribed item
#### Average ACT cost
#### Number of unique items

Perecntage bars show the infection treatment drug of all infection treatments as a percentage

A creatinine calculator has also been implemented for the user

## How to contribute
After downloading the database contaning the prescribing data and cloning the repo, the files of interest include controllers.py in the database folder, controllers.py in the views folder,
and the index.html file found in the templates/dashboard folder. Editing these scripts to enable communication between the three will update/ make changes to the dashboard 
So if you have any suggestions that might make our project better, please follow the instructions above and create a pull request through git to get started!
