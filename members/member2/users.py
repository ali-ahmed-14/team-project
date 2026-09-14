import json
import os


class UserManager:
    """
    Manages library users and stores their data in a JSON file.
    """

    def __init__(self, data_file="users_data.json"):
        self.data_file = os.path.join(
            os.path.dirname(__file__),
            data_file
        )

        self.users = self.load_users()

    # ---------------------------------------------------------
    # File Operations
    # ---------------------------------------------------------

    def load_users(self):
        """
        Load users from the JSON file.

        Returns:
            list: List of users.
        """
        if not os.path.exists(self.data_file):
            return []

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                return []

        except (json.JSONDecodeError, OSError):
            return []

    def save_users(self):
        """
        Save all users to the JSON file.
        """
        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(
                    self.users,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError as error:
            print(f"Error saving users: {error}")

    # ---------------------------------------------------------
    # ID Generation
    # ---------------------------------------------------------

    def generate_user_id(self):
        """
        Generate a new unique user ID.

        Returns:
            int: New user ID.
        """
        if not self.users:
            return 1

        return max(user["id"] for user in self.users) + 1

    # ---------------------------------------------------------
    # Create User
    # ---------------------------------------------------------

    def add_user(self, name, email, phone):
        """
        Add a new user to the library.

        Args:
            name (str): User's full name.
            email (str): User's email.
            phone (str): User's phone number.

        Returns:
            dict: Created user.
        """

        name = name.strip()
        email = email.strip()
        phone = phone.strip()

        if not name:
            raise ValueError("User name cannot be empty.")

        if not email:
            raise ValueError("Email cannot be empty.")

        if self.find_user_by_email(email):
            raise ValueError("A user with this email already exists.")

        user = {
            "id": self.generate_user_id(),
            "name": name,
            "email": email,
            "phone": phone
        }

        self.users.append(user)
        self.save_users()

        return user

    # ---------------------------------------------------------
    # Get Users
    # ---------------------------------------------------------

    def get_all_users(self):
        """
        Return all users.

        Returns:
            list: All users.
        """
        return self.users

    # ---------------------------------------------------------
    # Find User
    # ---------------------------------------------------------

    def find_user_by_id(self, user_id):
        """
        Find a user by ID.

        Args:
            user_id (int): User ID.

        Returns:
            dict or None: User if found.
        """

        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            return None

        for user in self.users:
            if user["id"] == user_id:
                return user

        return None

    def find_user_by_email(self, email):
        """
        Find a user by email.

        Args:
            email (str): User email.

        Returns:
            dict or None: User if found.
        """

        email = email.strip().lower()

        for user in self.users:
            if user["email"].lower() == email:
                return user

        return None

    # ---------------------------------------------------------
    # Update User
    # ---------------------------------------------------------

    def update_user(self, user_id, name=None, email=None, phone=None):
        """
        Update an existing user's information.

        Args:
            user_id (int): User ID.
            name (str): New name.
            email (str): New email.
            phone (str): New phone.

        Returns:
            dict or None: Updated user.
        """

        user = self.find_user_by_id(user_id)

        if user is None:
            return None

        if name is not None:
            name = name.strip()

            if not name:
                raise ValueError("User name cannot be empty.")

            user["name"] = name

        if email is not None:
            email = email.strip()

            existing_user = self.find_user_by_email(email)

            if existing_user and existing_user["id"] != user["id"]:
                raise ValueError(
                    "Another user already uses this email."
                )

            user["email"] = email

        if phone is not None:
            user["phone"] = phone.strip()

        self.save_users()

        return user

    # ---------------------------------------------------------
    # Delete User
    # ---------------------------------------------------------

    def delete_user(self, user_id):
        """
        Delete a user by ID.

        Args:
            user_id (int): User ID.

        Returns:
            bool: True if deleted, otherwise False.
        """

        user = self.find_user_by_id(user_id)

        if user is None:
            return False

        self.users.remove(user)
        self.save_users()

        return True

    # ---------------------------------------------------------
    # Search Users
    # ---------------------------------------------------------

    def search_users(self, keyword):
        """
        Search users by name, email, or phone.

        Args:
            keyword (str): Search keyword.

        Returns:
            list: Matching users.
        """

        keyword = keyword.strip().lower()

        return [
            user
            for user in self.users
            if keyword in user["name"].lower()
            or keyword in user["email"].lower()
            or keyword in user["phone"].lower()
        ]


# -------------------------------------------------------------
# Testing
# -------------------------------------------------------------

if __name__ == "__main__":

    manager = UserManager()

    print("=== Library User Management ===")

    print("\nCurrent Users:")
    for user in manager.get_all_users():
        print(user)

    print("\nAdding a test user...")

    try:
        new_user = manager.add_user(
            "Ahmed Ali",
            "ahmed@example.com",
            "777123456"
        )

        print("User added successfully:")
        print(new_user)

    except ValueError as error:
        print(f"Error: {error}")

    print("\nAll Users:")

    for user in manager.get_all_users():
        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Email: {user['email']} | "
            f"Phone: {user['phone']}"
        )
