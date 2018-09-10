# Software Development Project - Proposal

Project Management Data Processing Software

# Purpose
The purpose of the proposed software is to address an ineffective and inefficient data processing functionality gap between project management software and cost data in corporate ERP. There is currently no quick data processing tool which serves as ‘cost integrator’ between Oracle Primavera P6, a  powerful, high functioning schedule and earned value software, and the institutional Oracle ERP. The proposed software will address the labor intensive cost integration process and provide a new web based user interface for review of full integrated project management data.

# Pain point
The in use cost integration tool has not been upgraded since the 1990’s and requires dedicated employees to manually enter data every month. The process entails replicating schedule activities from the schedule software into the cost integration software at the begin of a project or after any approved configuration management approval. On a monthly basis cost data from an ERP system is then matched  to the appropriate schedule data by charge codes. The data is then dissimentied to project managers via PDF in a static, hard to read table. The end result is an expensive, slow, and out date presentation of project management schedule and cost data which I near impossible to manipulate for further analysis.

# Scope of project
A simple software program to take time phased data schedule from Oracle Primavera P6 and process basic earned value data metrics. The processed data will be used to generate graphical representations of project data for example, project s-curves.  All the processed data will then be accessible via a web application which allows the user different views of the project data. The conceptual fullstack system design consists of four components: Data processing software, SQL Database, an API and a User Interface. 
 
# Fullstack conceptual components:       

Data processing software
Python software package to process schedule data from a CSV output file, Python programming will utilize Pandas, Numpy, and Matplot to process and visualize data.
     
SQL Database for data storage and processing
The processed data from the data output file software will be stored in a SQL database. The use of a SQL database is            required to allow historical access to prior month data as well as allow the user interface access to different level of dataset analysis.
           
Application Program Interface
An API to fully integrate the three major components of the software program.  The API will serve as the connection for the data processing software to the SQL database storage.  The API will also serve as the connection for the SQL database to the web based user interface.

User Interface
The user interface(UI) is a web based application which allows users (project personal) to access the data sets produced by the data processing software.  The UI will be written in HTML5/CSS/JavaScript. The application will provide the user access to a portfolio projects, filter data from selected project/projects and allow for easy graphical visualization of the selected data.
