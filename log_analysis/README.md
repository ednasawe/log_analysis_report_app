# The Logs Analysis


This is a Logs Analysis project is a reporting tool that
is used to print out reports in plain text format based
on the database dta provided.
The project uses *POstgreSQL and Python* to answer the following questions and then reporting them:

1. What are the most popular three articles of all time? - 
This will present a sorted list of articles, with the most popular articles being at the top of the list

2. Who are the most popular article authors of all time? - 
this results will present a sorted list of the most popular authors of all times.

3. On which days did more than 1% of requests lead to errors? - THis reporting results will present all the days that had more than 1% requests that resulted in an HTTP error.

## Getting started

THe project uses Python and PostgreSQL database with the following files:

* log.py* - The main python script that manages the queries and then generates content contained in the output.txt file.
* output.txt* - THe file conatins the output data when the queries in log.py is run.

## Requirements

* *VirtualBox* - If you do not have it, [download it from here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

* *Vagrant* - If you do not have it, [download it from here](https://www.vagrantup.com/downloads.html)

* *Python 3* - You can download it from, [here](https://www.python.org/download/releases/3.0/)

## How to Run

* Step 1:

Download or clone from github `fullstack-nandegree-vm repository`

Change the directory to fullstack-nandegree-vm repository\vagrant

You can find newsdata.sql in the vagrant directory inside fullstack-nandegree-vm repository, IF NOT

[Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Unzip the zip file to reveal `newsdata.sql`


* Step 2: 

Setup your virtual environment by starting and log in using:
`vagrant init` which will create a Vagrantfile
`vagrant up` 
Then `vagrant ssh`
cd to the cd/vagrant
Open the directory you've cloned 


* Step 3:

Clone this log_analysis repository using:
```
git clone {REPOSITORY_CLONE_URL}
```

Or download the repo as a zipped file to your desktop


* Step 4:

From your virtual environment terminal, switch to `/vagrant`
Then run the command below to load data
```
psql -d newsname -f newsdata.sql
```

Create the views for the database by:
```
$ psql -d newsname -f views.sql
```

You can check the database details:

``` psql -d newsname ``` 
- To open the psql database newsname

```\dt``` 
- To view the database schema, name of the database,type of database, and the owner of the database. 

```\du``` 
- To view the users, users' roles, attributes, and access privileges

```\l```  
- To view the lists of the databases available and owner.


* Step 5:

Switch back to `/log-analysis` directory then,
Run the log_analysis python script to generate
the output using the command:

```
python3 log.py
``` 
The output will appear in the _output.txt_ file


### How to Contribute

Contributions are welcomes. If you find any typos, errors, or additional resources. First, fork this repository. Please follow the contribution guidlines.

* You can Fork the project.
* Clone the repository 
* Or download the zip file to make changes.

$ git clone {REPOSITORY_CLONE_URL}
$ cd to the directory


## License

The contents of this repository are covered under the *MIT License.*

#### by Edna Sawe
