import sys

def input_taker() -> tuple:
    """
    This function takes the input as an console argument from the user.
    First argument is the path of the log file.
    Second argument is the log level.(Not mandatory)
    """
    log_level = None

    if len(sys.argv) == 2:
        file_path = sys.argv[1]

    elif len(sys.argv) == 3:
        file_path = sys.argv[1]
        log_level = sys.argv[2].upper()
        
        if log_level not in ["INFO", "DEBUG", "ERROR", "WARNING"]:
            print("Please provide the correct log level. It should be one of Info, Debug, Error or Warning.")
            return sys.exit(1)

    else:
        print(
            "Please provide the path of the log file(as a first argument) and log level(if needed) as a second argument."
        )
        return sys.exit(1)

    return file_path, log_level


def load_logs(file_path: str) -> list:
    """
    This function reads the log file and returns a list of log lines.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found. Please provide the correct path.")
        return sys.exit(1)


def parse_log_line(line: str) -> dict:
    """
    Parses a single log line and returns a dictionary with the keys date, time, log_level and log_message.
    """
    parsed_line = {"date": None, "time": None, "log_level": None, "log_message": None}

    parsed_line["date"] = line.split()[0]
    parsed_line["time"] = line.split()[1]
    parsed_line["log_level"] = line.split()[2]
    parsed_line["log_message"] = " ".join(line.split()[3:])

    return parsed_line


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters the logs by the given log level.
    """
    filtered_logs = []
    filtered_logs = filter(lambda log: log["log_level"] == level, logs)
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of logs for each log level.
    """
    log_count = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    for log in logs:
        log_count[log["log_level"]] += 1
    return log_count


def display_log_counts(counts: dict):
    """
    Displays the log counts.
    """
    print("{:<17} | {:<10}".format("Log level", "Quantity"))
    print("------------------|----------")  # Line of dashes
    for level, count in counts.items():
        print("{:<17} | {:<10}".format(level, count))
    print("\n")

def display_one_type_logs(logs: list, level: str):
    print(f"Details of logs for the '{level}' level:")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['log_message']}")


def main():
    file_path, log_level = input_taker()
    lines = load_logs(file_path)
    parsed_lines = []
    
    for line in lines:
        parsed_line = parse_log_line(line)
        parsed_lines.append(parsed_line)
        
        
    display_log_counts(count_logs_by_level(parsed_lines))
    
    if log_level:
        display_one_type_logs(filter_logs_by_level(parsed_lines, log_level), log_level)
            
    


if __name__ == "__main__":
    main()
