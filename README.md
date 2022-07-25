
# Thats-My-IP API

That's-My-IP API is an API to fetch details of the given IP Address. It's main features are:

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Raghav67816/that-s-my-ip-api/blob/839c2c35aacfe4e9b1b25d492919a850782e8b67/LICENSE)

## Features

- Lightweight
- Lighting Fast
- User authentication (SignUp & Login)
- Request validation: Checks if request is sent by an authenticated user.
- Returns IP Address details as JSON Response
- Supports both IPv4 & IPv6 Addresses


## Development Environment

This API uses Python 3 packages listed in requirements.txt located in config directory of the project.
Using virtual environment is recommended. It also uses IP2Location LITE Database downloadable from https://bit.ly/3S1ilvG and MongoDB.

NOTE: You have to download D11 database. I have not included it here because of it's big size. However, after installing move that BIN file namely IP2LOCATION-LITE-DB11.IPV6.BIN to config directory.


## Demo

![Alt Text](https://github.com/Raghav67816/that-s-my-ip-api/blob/c383c62db1c727805d8aa7980f39395866b7941e/extras/demo.gif)

This is a short demo. Here we ask the endpoint to tell us about IP Address 8.8.8.8 (www.google.com). Detailed demo is available on youtube https://youtube.com/
## Installation

Clone this repository

```bash
    git clone https://github.com/Raghav67816/that-s-my-ip-api
    cd <repo-folder>
```

Now create virtual environment - Recommended. However, you can skip this step.

```bash
    pip install virtualenv
    virtualenv <env-name>
    pip install -r config\requirements.txt
```

Environment is ready now !
## Run Locally

Now our environment is ready, we can now run this API locally.
```bash
    cd <repo-folder>
    source <env-name>/Scripts/activate
    uvicorn api:app --reload
```

Congratulations ! Our local server is now running at localhost. Now, open your browser and open the url provided in the terminal.

## Authors

- [@Raghav67816](https://github.com/Raghav67816)


## License

This project is licensed under [MIT](https://choosealicense.com/licenses/mit/) License. Please view License file for more information.



## Support

For support, email at innovationinfinite8@gmail.com.


## Feedback

If you have any feedback, please reach out to me at innovationinfinite8@gmail.com. Your feedback will be highly appreciated.

