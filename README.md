# EverQuest Raid Log Taker - README

This guide will help you set up and run the Python script that extracts player information from your EverQuest logs and saves it to a separate file.

## What This Script Does

This script:
- Reads your EverQuest log file
- Finds the most recent player list (who's online)
- Saves this information to a separate file with a timestamp
- Shows you how many players are in your zone
- Displays a cool "XANAX LOVES YOU!!" message
- Automatically closes after 7 seconds

## Installation Instructions

### Step 1: Install Python

1. Check if you already have Python installed:
   - Press `Win + R` on your keyboard
   - Type `cmd` and press Enter
   - In the black window that appears, type `python --version` and press Enter
   - If you see something like "Python 3.x.x", you already have Python and can skip to Step 2

2. If Python is not installed:
   - Go to [python.org/downloads](https://python.org/downloads)
   - Click the big "Download Python" button (get the latest version)
   - Run the downloaded file
   - **IMPORTANT**: Check the box that says "Add Python to PATH" at the bottom of the installer
   - Click "Install Now"
   - Wait for installation to complete and click "Close"

### Step 2: Download the Script

1. Create a folder where you want to keep the script (e.g., `C:\LogsTaken`)
2. Copy the Python script to this folder
3. Rename the file to something easy to remember like `takelogs.py`

### Step 3: Edit the Script for Your Computer

1. Right-click on the `takelogs.py` file
2. Select "Edit with Notepad" or just "Edit"
3. Look for these lines (they're near the bottom):
   ```python
   log_file_path = 'D:\\TAKPv22HD\\eqlog_Xanax_pq.proj.txt'
   output_dir = 'E:\\FormerGlorySite\\Logs'
   ```

4. Change these to match your own paths:
   - `log_file_path`: This should point to your EverQuest log file
   - `output_dir`: This is where you want the extracted logs to be saved

5. For example:
   ```python
   log_file_path = 'C:\\EverQuest\\Logs\\eqlog_YourCharacter_YourServer.txt'
   output_dir = 'C:\\EQLogger\\SavedLogs'
   ```

6. **IMPORTANT**: Always use double backslashes (`\\`) in file paths, not single ones

7. Save the file (File > Save or press Ctrl+S)

### Step 4: Create a Shortcut (Optional but Recommended)

1. Right-click on the `takelogs.py` file
2. Select "Create shortcut"
3. Move the shortcut to your desktop or somewhere easy to access

## Before Running the Script

Step 1: Enable Logging in EverQuest

Before the script can extract player information, you need to make sure EverQuest is saving logs:

    Enable logging in one of these ways:

        Edit your eqclient.ini file and set Log=TRUE

        OR simply type /logs on in the game chat and press ENTER

    Verify logging is enabled - you should see a message in-game confirming logs are on

Step 2: Generate the Player List in EverQuest

    While playing EverQuest, type /who guild and press ENTER

    This command will write the list of guild members in your current zone to your log file

    The script will extract this information when run


## Running the Script

### Method 1: Direct Double-Click

1. Simply double-click the `takelogs.py` file or its shortcut
2. A command window will appear showing:
   - Information about the log file being processed
   - The number of players in your current zone
   - The "XANAX LOVES YOU!!" ASCII art
   - A 7-second countdown before closing

### Method 2: Command Prompt (If Double-Click Doesn't Work)

1. Right-click in the folder where your script is located while holding Shift
2. Select "Open command window here" or "Open PowerShell window here"
3. Type `python takelogs.py` and press Enter
4. The script will run and show the same information as Method 1

## What to Expect When It Runs

When the script runs successfully:
1. A black command window will open
2. You'll see log processing messages
3. You'll see a line showing how many players are in your zone
4. The "XANAX LOVES YOU!!" ASCII art will display
5. The window will show where the log was saved
6. A 7-second countdown will begin before the window closes

## Troubleshooting

If the script doesn't work:
- Make sure Python is installed correctly
- Check that you've edited the file paths correctly (with double backslashes)
- Ensure your log file exists at the specified location
- Make sure you have permission to write to the output directory

## Need Help?

If you continue to have issues:
- Take a screenshot of any error messages
- Check that your EverQuest log file is being created properly
- Make sure you're using the correct character name in the log file path

This script will help you track who's playing EverQuest without having to manually copy the information!
