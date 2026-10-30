# SQL-Connector

A small command-line Python project that connects to a MySQL database (via XAMPP), lets users **sign up and log in**, and includes a **number-guessing game** whose scores are saved in the database.

## Features

- Automatically starts and stops XAMPP (Windows and Linux)
- Creates a database and a table if you don't have one yet
- Sign up / log in with a username and password
- Passwords are hashed with `bcrypt` and hidden while typing
- Parameterized SQL queries (protection against SQL injection)
- Number-guessing game: fewer guesses = higher score
- Score is saved per user and can be viewed any time
- Leaderboard of all users, built with `rich`

## Requirements

- Python 3.8+
- [XAMPP](https://www.apachefriends.org/) installed in the default location
- Python packages:

```bash
pip install mysql-connector-python rich bcrypt
```

> `platform`, `random`, `os`, `time` and `getpass` are part of Python's standard library, so they don't need to be installed.

## How to run

1. Install XAMPP in the default directory.
2. Install the packages above.
3. Run the script:

```bash
python sql.py
```

On Linux, the script uses `sudo` to start and stop XAMPP, so it may ask for your password.

## Usage

After logging in, type one of these commands:

| Command  | What it does                    |
|----------|---------------------------------|
| `game`   | Play the number-guessing game   |
| `score`  | Show your total score           |
| `users`  | Show the leaderboard            |
| `exit`   | Close the program and stop XAMPP |

### Scoring

| Number of guesses | Score |
|-------------------|-------|
| 1                 | 10    |
| 2 to 5            | 5     |
| 6 to 10           | 2     |
| more than 10      | 0     |

## Database

The table is created with these columns:

| Column       | Type         | Description            |
|--------------|--------------|------------------------|
| `User`       | VARCHAR(20)  | Username               |
| `password`   | VARCHAR(255) | bcrypt hash of the password |
| `score_hads` | INT(3)       | Total game score       |

You can manage the data in phpMyAdmin at `http://localhost/phpmyadmin` (default user `root`, empty password).

## Roadmap

- [ ] `qrcode` command
- [ ] Move database settings to a `.env` file
- [ ] Use a dedicated MySQL user instead of `root`
- [ ] More games
- [ ] Split the code into multiple modules

## Notes

This is a learning project. The default XAMPP `root` user without a password is only suitable for local development, never for a real server.

## License

Add a license of your choice (for example MIT) via GitHub's **Add file ← Create new file ← LICENSE**.
