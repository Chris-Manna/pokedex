# Pokedex
Use this web application as a site to store and view your Pokemon. 

## Current State of the application
Right now this project uses Python3, Django, CSS, HTML, and a SQLite database. 

## How to run the project
- Download and install the code onto your computer

Use the following commands:
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py runserver` this will run the server locally
- navigate to your browser and use the local port as a way to access the content of the website

NOTES:
- There are some pokemon from each CSV that have the same ID but different Evolutions and so i chose to use the first version of the pokemon that appeared in the db to follow the thread of evolutions
- Python3
- Django 4.0.2

### The current features of the app as a user you can...
- Register for the application as a new user and log in as an existing user - there are two different versions of the app you'll see both as a logged in user and a logged out user.
- Upload a CSV file and thereby claim pokemon as part of your pokedex as a trainer. These pokemon then appear on the front page with all other pokemon. They also appear on your profile.
- Go to the main page to see what other monsters there are being trained by different trainers
- You can click on the trainer name on the pokemon card
- While on a trainer profile other than your own you can follow them. 
- When you navigate to a trainer profile you'll be able to see the trainer's following/follower ratio and the pokemon that they train.
- Notice each pokemon card has the specifications from the code challenge is represented, including...Weaknesses as represented by the pokemon that have those strength and Strengths  as represented by the pokemon that have the pokemone's strengths as weaknesses
- Names of the current pokemon's Evolutions in the form a DFS algorithm

### Lessons Learned: 
- Swap out Django for JavaScript, Vue, or React

### Next Steps for the application:
The next steps I'm going to take are in an effort to make the application more scalable and usable:
- Turn the SQLite database into an AWS backend and convert calls to the backend into REST API requests
- Replace django features with vanilla JS or Vue
- Deploy the project using a GitHub.io tool so that friends can enjoy it!
- Include the ability for users to comment
- If this were a full scale aerospace application:

### I would probably include...
AWS Cognito verification to verify the user is who they say they are
A separate full scale controller for users to be able to run aerospace algorithms without taking up resources
Use docker to package and ship the application so that it would work on your computer right out of the box as your computer may need to have the right version python (python3), Django.

_______

### On the main page you can...
- View information about all of the pokemon uploaded and viewable on cards.

Notice the navigator bar at the top:
<img width="526" alt="Screen Shot 2023-03-10 at 3 59 15 AM" src="https://user-images.githubusercontent.com/9891972/224310624-5fffa9c5-abe4-4430-a7ef-525000fe2652.png">

Use the paginator at the bottom to see pokemon on a different page
<img width="574" alt="Screen Shot 2023-03-10 at 4 04 48 AM" src="https://user-images.githubusercontent.com/9891972/224311770-5dcc12fb-e938-4baf-9918-fb37c70b3c01.png">


Navigate to your own user profile to...
- Add pokemon to your pokedex using a CSV file with all of the new monsters you want to train. See example: 
<img width="521" alt="Screen Shot 2023-03-10 at 3 55 56 AM" src="https://user-images.githubusercontent.com/9891972/224310095-f63ca007-342c-485c-8df4-88308b631ebe.png">

- view all of the monsters you train by clicking on your profile name. See Example: 
<img width="541" alt="Screen Shot 2023-03-10 at 3 57 08 AM" src="https://user-images.githubusercontent.com/9891972/224310268-11e5464c-6bee-43e9-a54f-7da0c35d4cd0.png">


Follow other trainers and have trainers follow you. 

Currently there are 12 users: 
- basic
<img width="1139" alt="Screen Shot 2023-03-10 at 3 52 00 AM" src="https://user-images.githubusercontent.com/9891972/224309210-11e604f5-4af3-4fd2-bef2-01161ce2d6d4.png">

- branched_evolution
<img width="1115" alt="Screen Shot 2023-03-10 at 3 51 10 AM" src="https://user-images.githubusercontent.com/9891972/224309016-f878960f-3241-40e3-8e00-e8845e4cc3a6.png">

- database
<img width="1122" alt="Screen Shot 2023-03-10 at 3 50 17 AM" src="https://user-images.githubusercontent.com/9891972/224308895-b1ebfde7-d7f9-41ae-ab62-f9de95ab82de.png">


- long_evolution
<img width="1058" alt="Screen Shot 2023-03-10 at 3 49 36 AM" src="https://user-images.githubusercontent.com/9891972/224308729-50b8fc49-bf34-4358-9588-d7fde73cd720.png">

- random_columns_names
<img width="1119" alt="Screen Shot 2023-03-10 at 3 48 53 AM" src="https://user-images.githubusercontent.com/9891972/224308557-67e930d4-4364-46f3-801a-5fcf8cd1879b.png">


- random_order_branches
<img width="1081" alt="Screen Shot 2023-03-10 at 3 48 11 AM" src="https://user-images.githubusercontent.com/9891972/224308426-3c4d7299-00a4-4dac-abd2-8ddf2d529d82.png">


- simple_evolution
<img width="1106" alt="Screen Shot 2023-03-10 at 3 53 45 AM" src="https://user-images.githubusercontent.com/9891972/224309549-eaae691b-ae11-4079-b31a-6e240b73d6e0.png">


- single_strength
<img width="1096" alt="Screen Shot 2023-03-10 at 3 46 49 AM" src="https://user-images.githubusercontent.com/9891972/224308185-1aa38470-dde9-4e6b-8a0a-4da79c7d86be.png">

- single_weakness
<img width="1090" alt="Screen Shot 2023-03-10 at 3 45 49 AM" src="https://user-images.githubusercontent.com/9891972/224308006-59c9b3cb-5135-4fe5-bee6-1728b83b5ae3.png">

- strength_against_many
<img width="1012" alt="Screen Shot 2023-03-10 at 3 32 02 AM" src="https://user-images.githubusercontent.com/9891972/224305498-64181cac-bf77-4b82-b102-965e2abd2caf.png">

- strong_against_self
<img width="1116" alt="Screen Shot 2023-03-10 at 3 30 27 AM" src="https://user-images.githubusercontent.com/9891972/224305177-1961590d-6016-4bc2-bab2-ee54e15b98ea.png">

- weakness_against_many
<img width="1143" alt="Screen Shot 2023-03-10 at 3 44 12 AM" src="https://user-images.githubusercontent.com/9891972/224307751-68c8a54b-43a0-48b5-9b58-c47542f606f4.png">


### Features coming soon: 
- The ability to search for a pokemon
- The ability to search for a trainer
- The ability to comment on trainers profiles
- The ability to comment on monster cards
- The ability to view "followers" and people you follow
- Turn this into a single page application
