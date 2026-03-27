import logging
import schedule
import time
from analytics_worker import tasks

# Set up logging to display messages in the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_tasks():
    """Run all tasks in the analytics-worker project."""
    for task in tasks.get_all_tasks():
        try:
            task.run()
        except Exception as e:
            logging.error(f"Task {task.name} failed: {e}")

def main():
    """Schedule tasks to run at regular intervals."""
    schedule.every(1).minutes.do(run_tasks)  # Run tasks every 1 minute

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()