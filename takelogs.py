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
    
    Parameters:
    - log_file_path: Path to the log file.
    
    Returns:
    - The last block of player information as a string.
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

def save_block(block, output_file_path):
    """
    Saves the block to a file.
    
    Parameters:
    - block: The block of text to save.
    - output_file_path: Path to the output file.
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
        
        with open(output_file_path, 'w') as file:
            file.write(block)
    
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
        # Generate a filename based on the current datetime
        now = datetime.now()
        filename = now.strftime('%Y-%m-%d_%H-%M-%S.txt')
        output_file_path = os.path.join(output_dir, filename)
        
        save_block(block, output_file_path)
        print(f"Saved block to {output_file_path}")
    else:
        print("No player information found.")
    
    # Add countdown before exit
    countdown_exit()

if __name__ == "__main__":
    main()
