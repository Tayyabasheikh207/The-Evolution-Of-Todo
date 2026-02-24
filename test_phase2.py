"""
Comprehensive test suite for Phase 2 Todo Web Application
Tests backend API endpoints, authentication, and todo operations
"""

import requests
import json
from typing import Optional

# Configuration
BASE_URL = "http://localhost:8001"
AUTH_URL = f"{BASE_URL}/auth"
TODOS_URL = f"{BASE_URL}/todos"

# Test data
TEST_USER_1 = {
    "email": "testuser1@example.com",
    "password": "password123"
}

TEST_USER_2 = {
    "email": "testuser2@example.com",
    "password": "password456"
}

TEST_TODO = {
    "content": "Test Todo Item - This is a test todo"
}

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_test(test_name: str):
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}Testing: {test_name}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

def print_success(message: str):
    print(f"{Colors.GREEN}[PASS] {message}{Colors.END}")

def print_error(message: str):
    print(f"{Colors.RED}[FAIL] {message}{Colors.END}")

def print_info(message: str):
    print(f"{Colors.YELLOW}[INFO] {message}{Colors.END}")

class TestResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def add_pass(self):
        self.passed += 1

    def add_fail(self, error: str):
        self.failed += 1
        self.errors.append(error)

    def print_summary(self):
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}TEST SUMMARY{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}Passed: {self.passed}{Colors.END}")
        print(f"{Colors.RED}Failed: {self.failed}{Colors.END}")

        if self.errors:
            print(f"\n{Colors.RED}Errors:{Colors.END}")
            for i, error in enumerate(self.errors, 1):
                print(f"{Colors.RED}{i}. {error}{Colors.END}")

        total = self.passed + self.failed
        if total > 0:
            success_rate = (self.passed / total) * 100
            print(f"\n{Colors.BLUE}Success Rate: {success_rate:.1f}%{Colors.END}")

results = TestResults()

def test_health_check():
    """Test if the API is running"""
    print_test("Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print_success("API is running")
            print_info(f"Response: {response.json()}")
            results.add_pass()
            return True
        else:
            print_error(f"Health check failed with status {response.status_code}")
            results.add_fail("Health check failed")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to API. Is the server running?")
        print_info("Start the server with: cd backend && uvicorn src.api.main:app --reload")
        results.add_fail("API not running")
        return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Health check error: {str(e)}")
        return False

def test_signup(user_data: dict) -> Optional[dict]:
    """Test user signup"""
    print_test(f"User Signup - {user_data['email']}")
    try:
        response = requests.post(
            f"{AUTH_URL}/signup",
            json=user_data,
            timeout=5
        )

        if response.status_code == 200:
            user = response.json()
            print_success(f"User created successfully")
            print_info(f"User ID: {user.get('id')}")
            print_info(f"Email: {user.get('email')}")
            results.add_pass()
            return user
        elif response.status_code == 409:
            print_info("User already exists (this is okay for testing)")
            results.add_pass()
            return None
        else:
            print_error(f"Signup failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Signup failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Signup error: {str(e)}")
        return None

def test_signin(user_data: dict) -> Optional[str]:
    """Test user signin and return token"""
    print_test(f"User Signin - {user_data['email']}")
    try:
        response = requests.post(
            f"{AUTH_URL}/signin",
            json=user_data,
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            print_success("Signin successful")
            print_info(f"Token received: {token[:20]}...")
            print_info(f"User: {data.get('user')}")
            results.add_pass()
            return token
        else:
            print_error(f"Signin failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Signin failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Signin error: {str(e)}")
        return None

def test_create_todo(token: str, todo_data: dict) -> Optional[dict]:
    """Test creating a todo"""
    print_test("Create Todo")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            f"{TODOS_URL}/",
            json=todo_data,
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            todo = response.json()
            print_success("Todo created successfully")
            print_info(f"Todo ID: {todo.get('id')}")
            print_info(f"Content: {todo.get('content')}")
            print_info(f"Completed: {todo.get('completed')}")
            results.add_pass()
            return todo
        else:
            print_error(f"Create todo failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Create todo failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Create todo error: {str(e)}")
        return None

def test_get_todos(token: str) -> Optional[list]:
    """Test getting all todos"""
    print_test("Get All Todos")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{TODOS_URL}/",
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            todos = response.json()
            print_success(f"Retrieved {len(todos)} todos")
            for i, todo in enumerate(todos, 1):
                print_info(f"{i}. {todo.get('content')} - Completed: {todo.get('completed')}")
            results.add_pass()
            return todos
        else:
            print_error(f"Get todos failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Get todos failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Get todos error: {str(e)}")
        return None

def test_toggle_todo(token: str, todo_id: str):
    """Test toggling todo completion"""
    print_test("Toggle Todo Completion")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.patch(
            f"{TODOS_URL}/{todo_id}/toggle-complete",
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            todo = response.json()
            print_success("Todo toggled successfully")
            print_info(f"New completion status: {todo.get('completed')}")
            results.add_pass()
            return todo
        else:
            print_error(f"Toggle todo failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Toggle todo failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Toggle todo error: {str(e)}")
        return None

def test_update_todo(token: str, todo_id: str, update_data: dict):
    """Test updating a todo"""
    print_test("Update Todo")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.put(
            f"{TODOS_URL}/{todo_id}",
            json=update_data,
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            todo = response.json()
            print_success("Todo updated successfully")
            print_info(f"New content: {todo.get('content')}")
            results.add_pass()
            return todo
        else:
            print_error(f"Update todo failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Update todo failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Update todo error: {str(e)}")
        return None

def test_delete_todo(token: str, todo_id: str):
    """Test deleting a todo"""
    print_test("Delete Todo")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(
            f"{TODOS_URL}/{todo_id}",
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            print_success("Todo deleted successfully")
            results.add_pass()
            return True
        else:
            print_error(f"Delete todo failed with status {response.status_code}")
            print_error(f"Response: {response.text}")
            results.add_fail(f"Delete todo failed: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Delete todo error: {str(e)}")
        return False

def test_unauthorized_access():
    """Test that unauthorized access is blocked"""
    print_test("Unauthorized Access Protection")
    try:
        response = requests.get(f"{TODOS_URL}/", timeout=5)

        if response.status_code == 401 or response.status_code == 403:
            print_success("Unauthorized access properly blocked")
            results.add_pass()
            return True
        else:
            print_error(f"Unauthorized access not blocked! Status: {response.status_code}")
            results.add_fail("Unauthorized access not blocked")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        results.add_fail(f"Unauthorized test error: {str(e)}")
        return False

def run_all_tests():
    """Run all tests in sequence"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}PHASE 2 TODO WEB APP - COMPREHENSIVE TEST SUITE{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

    # Test 1: Health check
    if not test_health_check():
        print_error("\nServer is not running. Please start the server first.")
        print_info("Run: cd backend && uvicorn src.api.main:app --reload")
        return

    # Test 2: Unauthorized access
    test_unauthorized_access()

    # Test 3: User signup
    test_signup(TEST_USER_1)

    # Test 4: User signin
    token = test_signin(TEST_USER_1)
    if not token:
        print_error("\nCannot continue without authentication token")
        results.print_summary()
        return

    # Test 5: Create todo
    todo = test_create_todo(token, TEST_TODO)
    if not todo:
        print_error("\nCannot continue without a todo")
        results.print_summary()
        return

    todo_id = todo.get('id')

    # Test 6: Get all todos
    test_get_todos(token)

    # Test 7: Toggle todo completion
    test_toggle_todo(token, todo_id)

    # Test 8: Update todo
    update_data = {
        "content": "Updated Test Todo - This todo has been updated"
    }
    test_update_todo(token, todo_id, update_data)

    # Test 9: Get todos again to verify update
    test_get_todos(token)

    # Test 10: Delete todo
    test_delete_todo(token, todo_id)

    # Test 11: Verify deletion
    todos = test_get_todos(token)

    # Print final summary
    results.print_summary()

    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.GREEN}[SUCCESS] Testing complete!{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

if __name__ == "__main__":
    run_all_tests()
