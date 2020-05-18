# Stonks

- [Stonks](#stonks)
  - [Requirements](#requirements)
    - [Setting Up Your Virtual Environment](#setting-up-your-virtual-environment)
      - [Windows](#windows)
      - [Unix](#unix)
  - [Quick Start](#quick-start)

## Requirements

- Python 3.6 or newer

### Setting Up Your Virtual Environment

More information can be found in the official [Python Docs](https://docs.python.org/3/library/venv.html).

#### Windows

```cmd
REM make sure you have a compatible version of python installed
C:\> python --version
Python 3.7.7

REM create a virtual environment named 'venv' in the current directory
C:\> python -m venv venv

REM activate it
C:\> venv\Scripts\activate.bat

REM now we can pip install without explicitly using python to invoke pip
(venv) C:\> python --version
Python 3.7.7
```

#### Unix

```bash
# make sure you have a compatible version of python installed
$ python3 --version
Python 3.7.7

# create a virtual environment named 'venv' in the current directory
$ python3 -m venv venv

# activate it
$ source venv/bin/activate

# now we can pip install without explicitly using python to invoke pip
# note we're just using python here
(venv) $ python --version
Python 3.7.7
```

## Quick Start

1. Clone the repository:

    ```bash
    $ git clone https://github.com/Jeff457/stonks.git
    ```

1. Install the dependencies:

    ```bash
    $ cd stonks/
    # activate your virtual environment
    $ source ~/venv/bin/activate
    # install the dependencies
    (venv) $ pip install -r requirements.txt
    ```

1. Run the app:

    ```bash
    (venv) $ python stonks/app.py
    The phrase 'SPY' was mentioned 15 times today in WallStreetBets
    ```
