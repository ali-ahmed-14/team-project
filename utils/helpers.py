import json
import os
from datetime import datetime


def get_data_path(filename):
    """
    Return the absolute path of a data file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        str: Absolute file path.
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(project_root, filename)


def load_json(filename, default=None):
    """
    Load data from a JSON file.

    Args:
        filename (str): Path of the JSON file.
        default: Value returned if the file does not exist
                 or contains invalid data.

    Returns:
        Loaded JSON data or default value.
    """
    if default is None:
        default = []

    if not os.path.exists(filename):
        return default

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return default


def save_json(filename, data):
    """
    Save data to a JSON file.

    Args:
        filename (str): Path of the JSON file.
        data: Data to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        directory = os.path.dirname(filename)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except OSError as error:
        print(f"Error saving data: {error}")
        return False


def generate_id(items):
    """
    Generate a unique integer ID.

    Args:
        items (list): List of dictionaries containing an 'id' key.

    Returns:
        int: New unique ID.
    """
    if not items:
        return 1

    ids = [
        item["id"]
        for item in items
        if isinstance(item, dict)
        and isinstance(item.get("id"), int)
    ]

    if not ids:
        return 1

    return max(ids) + 1


def find_by_id(items, item_id):
    """
    Find an item by its ID.

    Args:
        items (list): List of dictionaries.
        item_id (int): ID to search for.

    Returns:
        dict or None: Matching item.
    """
    try:
        item_id = int(item_id)
    except (ValueError, TypeError):
        return None

    for item in items:
        if item.get("id") == item_id:
            return item

    return None


def search_items(items, keyword, fields):
    """
    Search items using multiple fields.

    Args:
        items (list): List of dictionaries.
        keyword (str): Search keyword.
        fields (list): Fields to search in.

    Returns:
        list: Matching items.
    """
    keyword = str(keyword).strip().lower()

    if not keyword:
        return items

    results = []

    for item in items:
        for field in fields:
            value = item.get(field, "")

            if keyword in str(value).lower():
                results.append(item)
                break

    return results


def get_current_datetime():
    """
    Return the current date and time.

    Returns:
        str: Current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_date():
    """
    Return the current date.

    Returns:
        str: Current date.
    """
    return datetime.now().strftime("%Y-%m-%d")


def is_valid_email(email):
    """
    Basic email validation.

    Args:
        email (str): Email address.

    Returns:
        bool: True if the email format is valid.
    """
    email = str(email).strip()

    return (
        "@" in email
        and "." in email.split("@")[-1]
        and " " not in email
    )


def is_empty(value):
    """
    Check whether a value is empty.

    Args:
        value: Value to check.

    Returns:
        bool: True if empty, otherwise False.
    """
    return value is None or str(value).strip() == ""


def print_separator(length=60):
    """
    Print a separator line.

    Args:
        length (int): Number of characters.
    """
    print("-" * length)


def print_title(title):
    """
    Print a formatted title.

    Args:
        title (str): Title text.
    """
    print_separator()
    print(title.center(60))
    print_separator()


def confirm_action(message="Are you sure?"):
    """
    Ask the user to confirm an action.

    Args:
        message (str): Confirmation message.

    Returns:
        bool: True if confirmed.
    """
    answer = input(f"{message} (y/n): ").strip().lower()

    return answer in ("y", "yes")
