# **0x00. AirBnB clone - The console**
>In this repository, Sebastian Carvajal and I implemented the AirBnB clone - version1.

## Project's description: 
>This is the first step towards building a full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

>Steps:
* Create a parent class (called **BaseModel**) to take care of the initialization, serialization and deserialization of the future instances.
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all the classes and storage engine.
* Create the command interpreter.

>Our child classes from BaseModel:
* User
* State
* City
* Place
* Amenity
* Review

>And our class for the engine:
* FileStorage

## Serialization-deserialization's flow:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

>For this first step, we have to write in a file all our objects/instances created/updated in our command interpreter and restore them when we start it. We can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure as the one above.

## Command Interpreter:
> The console allow us to create the data model, manage objects and store and persist objects to a file (JSON file). Some examples:
* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes of an object.
* Destroy an object.

>The first piece is to manipulate the storage system. This storage engine will give us an abstraction between “Our objects” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored. This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

>The console will be a tool to validate this storage engine.

## First approach to the project:
<img src="https://github.com/jhojanperlaza/holbertonschool-AirBnB_clone/blob/master/AirBnBv1.png?raw=true" alt="Stage1-AirBnB_clone_project"/>

### How to start it:
>**AirBnB$ ./console.py** """interactive mode"""

(hbnb) help

Documented commands (type help < topic >):
__________________________________________
EOF     all     create     destroy     help     quit     show     update

(hbnb) 

(hbnb) quit

>**AirBnB$ echo "help" | ./console.py** """non-interactive mode"""
(hbnb)

Documented commands (type help < topic >):
__________________________________________
EOF     all     create     destroy     help     quit     show     update

(hbnb) 

AirBnB$

### How to use it:
>This is the command's list:
* **help** - Shows information about the console or its commands - Usage: help or help create
* **EOF** - Exits the console
* **quit** - Exits the console
* **create** - Creates an instance - Usage: create Class
* **show** - Prints the string representation of an instance - Usage: show Class id
* **destroy** - Deletes an intance - Usage: destroy Class id
* **all** - Prints all string representation of all instance - Usage: all or all Class
* **update** - Updates an instance - Usage: update Class id attribute value

### Examples:
**Create:**

>(hbnb) create BaseModel

929fab0f-efb4-4eb7-9cfa-27c57cd167df

>(hbnb) create User

5aa4eec2-ce66-4415-ba41-28c3207a68b6

>(hbnb) create Place

63514b83-af33-4038-9c66-256fefc35165

**show:**
>(hbnb) create User

0e100f94-884d-4d6e-b1ac-73ccff8ee8e6

>(hbnb) show User 0e100f94-884d-4d6e-b1ac-73ccff8ee8e6

[User] (0e100f94-884d-4d6e-b1ac-73ccff8ee8e6) {'id': '0e100f94-884d-4d6e-b1ac-73ccff8ee8e6', 'created_at': datetime.datetime(2022, 7, 6, 15, 43, 19, 809060), 'updated_at': datetime.datetime(2022, 7, 6, 15, 43, 19, 809092)}

**destroy:**
>(hbnb) create Place

9fd1f506-9cc7-4ba8-9b2f-d6bda9bbcddb

>(hbnb) destroy Place 9fd1f506-9cc7-4ba8-9b2f-d6bda9bbcddb

>(hbnb) show Place 9fd1f506-9cc7-4ba8-9b2f-d6bda9bbcddb

** no instance found **

**all:**
>(hbnb) create BaseModel

bf876ce4-ecc9-4185-8d22-88c23cbe4f28

>(hbnb) create BaseModel

61691f4f-f58c-4b58-8618-14472c984061

>(hbnb) create User

81fc9995-016a-4f47-85ef-62bb73ce5e1c

>(hbnb) all

["[BaseModel] (bf876ce4-ecc9-4185-8d22-88c23cbe4f28) {'id': 'bf876ce4-ecc9-4185-8d22-88c23cbe4f28', 'created_at': datetime.datetime(2022, 7, 6, 15, 49, 15, 483376), 'updated_at': datetime.datetime(2022, 7, 6, 15, 49, 15, 483395)}", "[BaseModel] (61691f4f-f58c-4b58-8618-14472c984061) {'id': '61691f4f-f58c-4b58-8618-14472c984061', 'created_at': datetime.datetime(2022, 7, 6, 15, 49, 31, 624055), 'updated_at': datetime.datetime(2022, 7, 6, 15, 49, 31, 624070)}", "[User] (81fc9995-016a-4f47-85ef-62bb73ce5e1c) {'id': '81fc9995-016a-4f47-85ef-62bb73ce5e1c', 'created_at': datetime.datetime(2022, 7, 6, 15, 49, 36, 876947), 'updated_at': datetime.datetime(2022, 7, 6, 15, 49, 36, 877007)}"]

**update:**
>(hbnb) create BaseModel

101da88b-e3f4-4bb0-813d-cbb5febd2f68

>(hbnb) show BaseModel 101da88b-e3f4-4bb0-813d-cbb5febd2f68

[BaseModel] (101da88b-e3f4-4bb0-813d-cbb5febd2f68) {'id': '101da88b-e3f4-4bb0-813d-cbb5febd2f68', 'created_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196636), 'updated_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196652)}

>(hbnb) update BaseModel 101da88b-e3f4-4bb0-813d-cbb5febd2f68 name "Sebas"

>(hbnb) show BaseModel 101da88b-e3f4-4bb0-813d-cbb5febd2f68

[BaseModel] (101da88b-e3f4-4bb0-813d-cbb5febd2f68) {'id': '101da88b-e3f4-4bb0-813d-cbb5febd2f68', 'created_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196636), 'updated_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196652), 'name': 'Sebas'}

>(hbnb) update BaseModel 101da88b-e3f4-4bb0-813d-cbb5febd2f68 name "Jhojan"

>(hbnb) show BaseModel 101da88b-e3f4-4bb0-813d-cbb5febd2f68

[BaseModel] (101da88b-e3f4-4bb0-813d-cbb5febd2f68) {'id': '101da88b-e3f4-4bb0-813d-cbb5febd2f68', 'created_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196636), 'updated_at': datetime.datetime(2022, 7, 6, 15, 52, 53, 196652), 'name': 'Jhojan'}



## How can you report an error or solve a question?
> You can contact to authors sending a message through github accounts or an email to Jhojan Perlaza <4739@holbertonschool.com> or to Sebastian Carvajal <4574@holbertonschool.com>