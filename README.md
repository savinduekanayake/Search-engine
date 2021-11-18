# Search Engine - Ministers

![parliment](https://user-images.githubusercontent.com/47809365/142301933-49477a6e-2c0f-457a-b139-f154275c7ab9.JPG)


## Parliment Ministers search engine using Sinhala language

* `search by name` : ජී. එල්. පීරිස් මහතා
* `search by party` : ශ්‍රී ලංකා පොදුජන පෙරමුණනේ මන්නීවරුන්
* `search by district` : මාතර දිස්ික්කය ිපයෝජනය කරන මන්නීවරු
* `search by related subject` : අධ්යාපනයට සම්බන්ධ මන්ත්රීවරු
* `search by overall rank` : හොදම 10 මන්නීවරුන්
* `search by participated_in_parliament` : 5 වාරගනනක් පාර්ලිමේන්තුවට සහබාගීවුන මන්නීවරුන්
* `search by bio` : මාතර දිස්ික්කපයන්න ශ්‍රී ලංකා පොදුජන පෙරමුණ ෙක්ෂය යටපත්

## Quickstart

* Download the repo
* Run the activate.bat file in the IR/Scripts folder.
* Run the docker-compose.yml file in the IR folder.
* Run upload_crawled_data.py file in IR/app folder to create index.
* Finally go to the IR/app folder and run the file using 'flask run'.
* Visit http://localhost:5000 and search by entering relevant queries in Sinhala language.


## Data

Dataset contains the all the parliment ministers scraped from this [website](http://www.manthri.lk/si/politicians). 

* Name
* Gender
* Birthday
* Age
* Education
* Position
* Party
* District
* Overall rank
* No. of time participated in parliment
* Related subjects
* Terms in parliment
* Biography
* Contact informations

## Directory Structure

* `crawler` - contains the scrapped ministers coprus and the scrapping code.
* `IR` - contain all the project files.
* `IR/Scripts` - contain the relavent envirenment files and scripts.
* `IR/docker-compose.yml` - contain the docker file.
* `IR/app` - contain both backend and frontend of the Search Engine.
* `IR/app/templates` - contains the User interface templates.
* `IR/app/data` - contains the dataset.
* `app.py` - contains the code to run the search engine server.


