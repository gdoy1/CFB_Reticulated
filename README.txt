Project: 
-Updating a dashboard containing items prescribed from a primary care trust 
-Decsription: We were provided with a skeleton dashboard and a dataset from which information on the dashboard would be presented.

How to install and run project: We downloaded the database https://www.dropbox.com/s/76cawm3bmnwdtza/abxdb.db?dl=0 and
then cloned the following  repo https://github.com/IAM-lab/MIE-skeleton from git and into a folder. The run.py file can be used to run/serve the dashboard. The abxdb.db contains the prescribing data. 

Problem it solves: The abxdb.db database contains a mass amount of information regarding the prescribed items. The dashboard has been updated to pull and present key information

Features:

How to use the Dashboard: The dashboard can be accessed to gather specific information from the prescribing data;
-total items
-top prescribed item
-average ACT cost
-number of unique items

How to contribute to the project: After downloading the database contaning the prescribing data and cloning the repo, the files of interest include controllers.py in the database folder, controllers.py in the views folder.
and the index.html file found in the templates/dashboard folder. Editing these scripts to enable communication between the three will update/ make changes to the dashboard 



