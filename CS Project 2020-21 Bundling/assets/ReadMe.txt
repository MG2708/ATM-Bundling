INTRODUCTION TO PROJECT IDEA

The Project titled ATM Simulator is a software developed to understand the 
basic idea about the working of an ATM and understand the basic functions 
it is capable of doing. Using the freedom of programming, some features 
that are not usually performed by the real-world ATM Machine are included 
to make it more user-friendly, attractive, easy and fun to use.
balance.
The project provides the users to register themselves and perform the basic ATM tasks 
such as withdrawing money, depositing money in their account and checking the balance. 
The users can again login into the system using the details they had used while registering
and their balance is updated as per the last transaction in their last session 
This project is useful for those who want to understand what all functions scan be done 
using the ATM Machine. But, as mentioned earlier, few of the functions included in the project 
are not offered by some of the ATM Machines. This only gives a rough idea about working of ATM.

LOG IN CONDITIONS

The program uses Database hosted on a remote server and hence needs a PC with active network 
connection to maintain the record of Balance and Users. If active network connection is not available, the program will not work. 
Balance is set by default to be Rs. 0.00. 
On creating a new Account, it asks for Display Name and Pin. Display Name should be the Account 
Holder Name and Pin should be a 4-digit numeric pin. It gives an Account ID randomly which needs to 
be noted down for logging in next time.
After every transaction, the balance is stored in the MySQL Table against your Account ID. 
So, when you login next time (using that Account ID), your balance will be shown as the one it was after your last transaction.
Here, a local MySQL table is not used as the program has been developed with an intention to export 
it to users such that anyone without the need of downloading Python or MySQL can access the project and use it properly. 
So, please be patient
