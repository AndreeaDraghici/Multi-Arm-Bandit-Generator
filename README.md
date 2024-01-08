## Overview

The Random Input Generator is a simple Python tool designed to generate random input files for[ Multi-Arm Bandit
Agent ](https://github.com/AndreeaDraghici/Multi-Arm-Bandit-Agent) simulations. This tool is useful for creating diverse
sets of input parameters for testing and experimentation with
Multi-Arm Bandit algorithms.

## Usage

### Installation

### Step 1: Install Python

1. _**Download Python:**_
   Visit the official Python website [Python](https://www.python.org/downloads/) and download the 3.10 version of Python for
   your operating system (Windows, macOS, or Linux).


2. _**Install Python:**_
   Follow the installation instructions provided on the Python website to install Python on your machine. Make sure to
   check the option that adds Python to your system PATH during installation.

### Step 2: Install PyCharm

1. **_Download PyCharm:_** Visit the official [PyCharm](https://www.jetbrains.com/pycharm/download/) website and download
   the version of PyCharm
   Community Edition, which is free to use.


2. **_Install PyCharm:_**
   Follow the installation instructions provided on the PyCharm website to install PyCharm on your machine.

### Step 3: Clone the Repository

**Open Terminal/Command Prompt:**
Open your terminal or command prompt on your machine.

**Clone the repository to your local machine:**

Run the following commands:

``git clone <https://github.com/AndreeaDraghici/Multi-Arm-Bandit-Generator.git>``

`cd <Multi-Arm-Bandit-Generator>`

### Step 4: Install Dependencies

Make sure to install the required dependencies. Run the following command in the terminal to install the required
dependencies:

`pip install -r requirements.txt`

### Step 5: Configure Logging

Ensure that the logging configuration file (logging_config.yml) is set up according to your preferences. This file is
used to configure logging in the tool.

### Step 6: Run the Generator

Open the Python file containing the code in PyCharm. To generate random input files, instantiate the _RandomInputGenerator_ class and call the _generate_inputs_ method. By
default, the tool generates 10 input files, each containing random values for the number of arms, total iterations, and
epsilon. Run the script to generate random input files.

![img.png](img.png)


###  Step 7: Check Output
_**Check Output:**_
Verify that the generated input files are saved in the 'input' directory.

**Note:**
If you encounter any issues during installation or execution, check for error messages and consult the documentation or
online resources for troubleshooting.

## Input File Format

Each input file (input{i}.txt) follows the format:

`{num_arms}`

`{num_iterations}`

`{epsilon}`

* num_arms: Random number of arms (between 5 and 15).

* num_iterations: Random number of iterations (between 1500 and 50000).

* epsilon: Random epsilon value (between 0.1 and 0.5).

## History

Version 1.0.0 - Initial version of tool