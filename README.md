![Logo of the project](https://i.ytimg.com/vi/2G1d3q8MlsI/maxresdefault.jpg)

# P &middot;  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> Python App that connects Arduino to Cloud

A client app that talks to Ardunio over serial port, gets an array of data from multiple sensors and store that into firebase database.

## Requirements
- Python 3.x
- Linux (Raspbian)

## Stack
- [Firebase](https://firebase.google.com/) Store and sync data with our NoSQL cloud database. 
- [Arduino](https://www.arduino.cc/)  A popular tool for IoT product development 
- [Raspberry Pi](https://www.raspberrypi.org/) A small and affordable computer that you can use to learn programming


## Getting started

Clone the repo and install dependencies: 

Open the directory, create and activate a virtual environment:
```
$ cd path2project
$ virtualenv venv
$ source venv/bin/activate
```

Run the app:
```
$ python src/main.py
```

## Todo

- Add Documentation
- Add comments
- Seprate credentials and api key in seperate json file


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
