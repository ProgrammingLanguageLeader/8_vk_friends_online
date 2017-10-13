# Watcher of Friends Online

A small script that enables you to watch list of your VK online friends, without visiting the site.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to use

### Preparing
Before you run the script, you have to set **_ONLINE_WATCHER_VK_ID_** environment variable.

### Example

A launching on Linux
```bash
$ python vk_friends_online.py
Login: <your login>
Password: <your password>
These friends are currently online:
Harry Potter
Severus Snape
```

The launching on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
