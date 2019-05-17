# Startup Tracker

This simple small prject is simple made to log who has logged onto a ocmputer and when they have logged onto the computer. This script is supposed to be stored in C:\ and it will execute form there and create a text file called logOnLog.txt which stores which users have logged on and when.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install to get the software working on your system.
Some of these scripts will need third party modules form pip3.

First off we need to install python and git if it is not alreaqdy installed:
```
sudo apt-get install python3 git
```

If this is a windows machine you need to download Python3 from the Python website. You can download the files mentioned later from the Github website.

That should be all the setup done and finished.

### Installing

Now we are going to go through a step by step guide on how to install the applications.

We will download the scripts. (This saves the repository to your current directory.)

```
git clone https://github.com/Tom-2E0EEJ/Startup/blob/master/Source_Code/Startup.py
```

This is now the application downloaded.
You can also download the application from the website GUI and move it to C:\.
On linux you can move it to \etc .


## Running the applications

Running the application is simple and straight forward.
This is as simple as running any other python3 application for the command line.

an example of launching the pinger application is shown below.
```
sudo python3 Startup.py
```

or on windows you can just double click it and have it run.


## Deployment

They way to develop the application is to move the application to the C:\ you simple need to copy and paste it to C:\ in windows or in linux
'''
sudo cp Startup.py /etc
'''

And then setup your system to automatically execute the script on startup.



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Thomas Scott** - *Initial work* - [Tom-2E0EEJ](https://github.com/Tom-2E0EEJ)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who contributes any code for this project.
