# HBNB CLONE PROJECT
![Airbnb](https://cdn-eahjn.nitrocdn.com/ChEvwayTHZmZJUAdsUNMLXuXZdBprFoQ/assets/images/optimized/rev-82d6b35/www.spinxdigital.com/app/uploads/2022/11/image-airbnb.jpg)
## Description

HolbertonBnB is a comprehensive web application that emulates AirBnB's functionality by seamlessly integrating database storage, a robust back-end API, and an intuitive front-end interface. This project primarily focuses on the development of the back-end console component.

## Getting Started

To start the console, run the following command:
`./console.py`
## Usage

The console supports the following commands:

- `create`: Create new instances of specified classes.
- `destroy`: Obliterate objects based on class name and ID.
- `all`: Visualize representations of all objects or specific classes.
- `update`: Update object attributes to new values.
- `quit`: Gracefully exit the program.
- `Ctrl+D`: Swiftly bid farewell.

### Examples
```
(hbnb) create BaseModel
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) show BaseModel 1234-1234-1234
(hbnb) all BaseModel
(hbnb) update BaseModel 1234-1234-1234 name "New Name"
(hbnb) quit
```


### Interactive Mode
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
EOF  help  quit
(hbnb) quit
$
```
### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
EOF  help  quit
(hbnb)
$
```
## Testing

This project uses the `unittest` module for testing. Test files are located in the `tests/` directory, with the following conventions:

- File extension: `.py`
- File and folder names start with `test_`
- Test files are organized based on the corresponding source files (e.g., `tests/test_models/test_base.py` for `models/base.py`)

To run the tests, execute the following command:
```
python3 -m unittest discover tests
```
Alternatively, you can run tests for a specific file:
```
python3 -m unittest tests/test_models/test_base.py
```

## Authors

- Abdelhakim Joulal | `smoxhakim`
- Abdeljalil Ouafi  | `AbdeljalilOuafi`