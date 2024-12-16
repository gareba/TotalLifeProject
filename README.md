Hello there! Welcome to my Take Home Project!

Due to time constraints I was only able to implement the specifications for Part 1. However, I do have some experience with front end development in similar contexts to this that I am more than happy to discuss during my review. 

flaskWork.py is the main file for the server, and I have extracted various helper functions to other Python files in this repo.
Dependencies: python, sqlite3, requests
To run the server, all one needs to do is have this repo downloaded and run 

```shell script
python flaskWork.py
```

Requirements
1. ERDiagram.jpg in this repo is a drawing I made to visualize and design my SQLite dataBase. I initialized the tables using DBBrowser.
2. Endpoints are implemented in various python files organized by table. See CRUDclinicians.py, CRUDpatients.py, and CRUDappointments.py for more. 
3. The SQLite Database is included in part1DB.db Additionally, I have included my DBBrowser project file for convienience.
4. Validation for requests is handled in flaskWork.py before requests are passed to the helper functions in the CRUD python helper files
5. See NPITEST.py for my usage of the NPI resgistry api

Please don't hesistate to reach out if you have any questions, thank you!

Code made by github user gareba, remote repo can be found at github.com/gareba/TotalLifeProject
Resources Consulted:
    https://www.youtube.com/watch?v=zsYIw6RXjfM
    https://www.youtube.com/watch?v=hpc5jyVpUpw&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY
    