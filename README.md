# Zip Cracker
A Python script that attempts to crack password-protected ZIP files using a wordlist.

```
                  _                                  _                
                 (_)                                | |               
            ____ _  _ __     ___  _ __  __ _   ___  | | __ ___  _ __  
            |_  /| || '_ \   / __|| '__|/ _` | / __|| |/ // _ \| '__| 
             / / | || |_) | | (__ | |  | (_| || (__ |   <|  __/| |    
            /___||_|| .__/   \___||_|   \__,_| \___||_|\_\\___||_|    
                    | |                                               
                    |_|             
```

 The script utilizes multithreading to speed up the cracking process and provides a progress bar to visualize the progress.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## Overview

This script is designed to help users recover access to their own password-protected ZIP files by trying a list of common passwords. It uses the `zipfile` module to handle ZIP files and `concurrent.futures` for multithreading, making it efficient for larger password lists.

## Features

- Multithreaded password cracking for faster execution.
- Progress bar to visualize the cracking process.
- Handles common exceptions gracefully.
- Easy to use with a simple command-line interface.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/njeru-codes/zip-cracker.git
   cd zip-cracker
   ```
