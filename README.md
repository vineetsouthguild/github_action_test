# GitHub Actions Learning Project 🚀

This project is designed to help you learn GitHub Actions with a practical Python application that includes automated testing, linting, and continuous integration.

## 📁 Project Structure

```
github_action/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions workflow file
├── src/
│   ├── __init__.py
│   └── calculator.py           # Main calculator module
├── tests/
│   ├── __init__.py
│   └── test_calculator.py      # Comprehensive test suite
├── main.py                     # Demo application
├── requirements.txt            # Python dependencies
├── pytest.ini                 # Pytest configuration
└── README.md                   # This file
```

## 🔧 What This Project Does

This project contains:

- **Calculator Module**: A simple calculator with basic math operations
- **Utility Functions**: Fibonacci, prime checking, and factorial functions
- **Comprehensive Tests**: Unit tests and integration tests using pytest
- **GitHub Actions Workflow**: Automated CI/CD pipeline

## 🤖 GitHub Actions Workflow Explained

The workflow file (`.github/workflows/ci.yml`) runs automatically when you:

- Push code to the `main` branch
- Create a pull request to the `main` branch

### Workflow Steps Breakdown:

1. **Checkout Code** (`actions/checkout@v4`)

   - Downloads your repository code to the GitHub runner
   - This is always the first step in any workflow

2. **Set up Python 3.11** (`actions/setup-python@v4`)

   - Installs Python 3.11 on the runner
   - Configures the Python environment

3. **Cache Dependencies** (`actions/cache@v3`)

   - Caches pip dependencies between runs
   - Speeds up subsequent workflow runs
   - Uses `requirements.txt` hash as cache key

4. **Install Dependencies**

   - Upgrades pip to latest version
   - Installs all packages from `requirements.txt`

5. **Lint with flake8**

   - Checks code style and quality
   - Finds syntax errors and undefined variables
   - Enforces Python coding standards

6. **Run Tests with pytest**

   - Executes all test files in the `tests/` directory
   - Shows verbose output and short tracebacks
   - Fails the workflow if any tests fail

7. **Generate Coverage Report**

   - Measures how much of your code is tested
   - Creates XML and terminal coverage reports

8. **Upload Coverage** (Optional)
   - Uploads coverage data to Codecov
   - Provides coverage tracking over time

## 🧪 Running Tests Locally

Before pushing to GitHub, you can test everything locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=term-missing

# Run linting
flake8 .

# Run the demo application
python main.py
```

## 📊 Test Coverage

The project includes comprehensive tests covering:

- ✅ All calculator operations (add, subtract, multiply, divide, power, square root)
- ✅ Error handling (division by zero, negative square roots)
- ✅ Utility functions (Fibonacci, prime checking, factorial)
- ✅ Edge cases and boundary conditions
- ✅ Integration tests

## 🚀 Getting Started

1. **Fork this repository** or **clone it locally**
2. **Make some changes** to the code (try adding a new function)
3. **Add tests** for your new functionality
4. **Push to the main branch** and watch GitHub Actions run!

## 🔄 How to Test the GitHub Actions Workflow

1. **Clone this repository to GitHub:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit: GitHub Actions learning project"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Watch the workflow run:**

   - Go to your GitHub repository
   - Click on the "Actions" tab
   - You'll see the "CI Pipeline" workflow running

3. **Make a change to test it:**
   - Edit `src/calculator.py` and add a new function
   - Add a test for it in `tests/test_calculator.py`
   - Commit and push your changes
   - Watch the workflow run again!

## 🎯 Learning Objectives

After working with this project, you'll understand:

- ✅ How GitHub Actions workflows are structured
- ✅ How to set up automated testing with Python and pytest
- ✅ How to use actions from the GitHub marketplace
- ✅ How to cache dependencies for faster builds
- ✅ How to generate and upload test coverage reports
- ✅ How continuous integration helps catch bugs early

## 🛠️ Try These Exercises

1. **Add a new math function** (like calculating GCD) and write tests for it
2. **Modify the workflow** to run on different Python versions (3.9, 3.10, 3.11)
3. **Add a new job** that builds documentation or runs security checks
4. **Create a release workflow** that publishes packages when you create a tag
5. **Add branch protection rules** to require the CI to pass before merging

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Testing Best Practices](https://docs.python.org/3/library/unittest.html)

---

Happy learning! 🎉 Don't forget to ⭐ star this repo if it helped you understand GitHub Actions!
