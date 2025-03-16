import os
import re
from datetime import datetime
import logging
import time
import sys

# Set up logging to console instead of file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_last_block(log_file_path):
    """
    Extracts the last block of player information from the log file.
    """
    try:
        logging.info(f"Attempting to read log file: {log_file_path}")
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
        
        # Regular expression to match the start and end of a block
        start_pattern = r'\[.*\] Players on EverQuest:'
        end_pattern = r'There are \d+ players in .*'
        
        # Find all blocks
        blocks = []
        current_block = []
        in_block = False
        
        logging.info("Processing log lines...")
        for line in reversed(lines):
            if re.search(end_pattern, line):
                current_block.append(line.strip())
                in_block = True
            elif in_block:
                current_block.append(line.strip())
                if re.search(start_pattern, line):
                    blocks.append('\n'.join(reversed(current_block)))
                    current_block = []
                    in_block = False
        
        # Return the last block found
        if blocks:
            logging.info("Found a block of player information.")
            return blocks[0]
        else:
            logging.warning("No blocks found in the log file.")
            return ""
    
    except Exception as e:
        logging.error(f"Error extracting block: {e}")
        return ""

def get_player_count(block):
    """
    Extract the player count from the block.
    """
    lines = block.split('\n')
    if lines:
        last_line = lines[-1]
        match = re.search(r'There are (\d+) players', last_line)
        if match:
            return match.group(1)
    return "unknown"

def extract_player_names(block):
    """
    Extract just the player names from the block.
    """
    lines = block.split('\n')
    player_names = []
    
    # Skip the header and footer lines
    if len(lines) >= 3:
        player_lines = lines[2:-1]  # Skip first two and last line
        
        for line in player_lines:
            # Handle different formats
            if 'AFK' in line and '[ANONYMOUS]' in line:
                match = re.search(r'AFK\s+\[ANONYMOUS\]\s+(\w+)', line)
                if match:
                    player_names.append(match.group(1))
            elif '[ANONYMOUS]' in line:
                match = re.search(r'\[ANONYMOUS\]\s+(\w+)', line)
                if match:
                    player_names.append(match.group(1))
            elif 'AFK' in line:
                match = re.search(r'AFK\s+\[\d+.*?\]\s+(\w+)', line)
                if match:
                    player_names.append(match.group(1))
            else:
                match = re.search(r'\][\s]+(\w+)[\s]+\(', line)
                if match:
                    player_names.append(match.group(1))
    
    return player_names

def save_block(block, output_file_path):
    """
    Saves the block to a file.
    """
    try:
        logging.info(f"Saving block to file: {output_file_path}")
        
        # Extract the last line of the block to log
        lines = block.split('\n')
        if lines:  # Check if there are lines
            last_line = lines[-1]
            logging.info(f"Block saved successfully to {output_file_path}")
            print("\n=====================")
            print("Results...")
            print(f"{last_line}")
            print("Xanax loves you!!")
            print("=====================\n")
        else:
            logging.warning(f"No lines found in block saved to {output_file_path}")
        
        # Extract just the player names
        player_names = extract_player_names(block)
        
        # Write only the player names to the file
        with open(output_file_path, 'w') as file:
            file.write('\n'.join(player_names))
    
    except Exception as e:
        logging.error(f"Error saving block to file: {e}")

def countdown_exit():
    """
    Display a countdown and exit the script.
    """
    print("\nScript execution complete.")
    for i in range(7, 0, -1):
        print(f"Closing in {i} seconds...", end="\r")
        time.sleep(1)
    print("Goodbye!                    ")

def is_block_from_today(block):
    """
    Check if the log block is from today.
    
    Returns:
        tuple: (bool, str) - Whether the block is from today and the timestamp string
    """
    try:
        lines = block.split('\n')
        if not lines:
            return False, "No lines found in block"
        
        # Extract timestamp from the first line
        first_line = lines[0]
        match = re.search(r'\[(.*?)\]', first_line)
        
        if not match:
            return False, "No timestamp found in block"
        
        timestamp_str = match.group(1)
        
        # EverQuest logs typically use format like: [Wed Mar 16 20:45:30 2025]
        # Try to parse this timestamp
        try:
            # Try multiple date formats since EQ logs can vary
            for fmt in [
                "%a %b %d %H:%M:%S %Y",  # Wed Mar 16 20:45:30 2025
                "%a %b %d %H:%M:%S",     # Wed Mar 16 20:45:30 (no year)
                "%m-%d-%Y %H:%M:%S"      # 03-16-2025 20:45:30
            ]:
                try:
                    if "%Y" not in fmt:
                        # If format doesn't include year, add current year
                        current_year = datetime.now().year
                        parsed_time = datetime.strptime(f"{timestamp_str} {current_year}", f"{fmt} %Y")
                    else:
                        parsed_time = datetime.strptime(timestamp_str, fmt)
                    
                    # Compare date part only
                    today = datetime.now().date()
                    log_date = parsed_time.date()
                    
                    return log_date == today, timestamp_str
                except ValueError:
                    continue
            
            # If we're here, none of the formats worked
            return False, f"Could not parse timestamp: {timestamp_str}"
            
        except Exception as e:
            return False, f"Error parsing timestamp: {e}"
    
    except Exception as e:
        return False, f"Error checking block date: {e}"

def main():
    log_file_path = 'D:\\TAKPv22HD\\eqlog_Xanax_pq.proj.txt'  # Update this path
    output_dir = 'E:\\FormerGlorySite\\Logs'  # Update this path
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            logging.info(f"Created output directory: {output_dir}")
        except Exception as e:
            logging.error(f"Failed to create output directory: {e}")
    
    # Run just once instead of in a loop
    logging.info("Checking for new log block...")
    block = extract_last_block(log_file_path)
    
    if block:
        # Check if the block is from today
        is_today, timestamp = is_block_from_today(block)
        
        if is_today:
            # Extract the player count for the filename
            player_count = get_player_count(block)
            
            # Generate a filename based on the current datetime and player count
            now = datetime.now()
            filename = now.strftime('%Y-%m-%d_%H-%M-%S') + f"_{player_count}-Players.txt"
            output_file_path = os.path.join(output_dir, filename)
            
            save_block(block, output_file_path)
            print(f"Saved block to {output_file_path}")
        else:
            # Log and inform the user that the data is not from today
            logging.warning(f"Found log block with timestamp [{timestamp}] is not from today. No file saved.")
            print("\n=====================")
            print("Results...")
            print(f"Found player data from [{timestamp}] which is not from today.")
            print("Please run '/who guild' in EverQuest to generate fresh data.")
            print("Xanax loves you!!")
            print("=====================\n")
    else:
        print("No player information found.")
    
    # Add countdown before exit
    countdown_exit()

if __name__ == "__main__":
    main()
