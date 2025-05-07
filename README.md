# Facebook Phisher - Phishing Page for Facebook Login

This repository contains a phishing page for Facebook login, designed as a way to learn and experiment with web-based attacks in a controlled environment. **Do not use for illegal activities.**

The repository includes HTML, CSS, and Python files that set up a phishing page designed to look like Facebook's login page. It uses Python's Flask web framework to simulate login requests.

---

## Repository Structure

```plaintext
FacebookPhisher/
├── FacebookLogin/                 # Contains the login page HTML template and related scripts
├── LoginPage/                     # HTML for login form and phishing page structure
├── templates/                     # Contains additional HTML templates used for phishing
├── .gitattributes                 # Git configuration file
├── .gitignore                     # Ignores unnecessary files from Git repository
├── LICENSE                        # License for the repository
├── README.md                      # This file
├── manage.py                      # Python script to run the Flask server and handle requests
```

---

## Description of Files

- **FacebookLogin/**: This folder contains the HTML and CSS code for simulating the Facebook login page. It mimics the look and feel of the real login page, intended to deceive users.

- **LoginPage/**: This directory holds the main login page HTML file and other related resources for creating the phishing form.

- **templates/**: This folder contains additional HTML templates and forms that are used in the phishing attack, such as pages for capturing user data.

- **.gitattributes**: Git configuration file that controls how Git treats specific files and directories in the repository.

- **.gitignore**: A list of files and directories that should be ignored by Git version control, ensuring temporary or unnecessary files aren’t committed.

- **LICENSE**: The license under which the repository is shared. Always be sure to check the license before using or contributing.

- **README.md**: This file, providing an overview of the repository and its components.

- **manage.py**: A Python script that sets up a simple server with Flask to simulate the login process and capture the input data provided by the user.

---

## How to Use

### **1. Clone the Repository**

To use the phishing page, clone this repository to your local machine:

```bash
git clone https://github.com/senani-derradji/FacebookPhisher.git
```

### **2. Install Dependencies**

Make sure you have Python installed. You also need to install the required dependencies for the project. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

### **3. Run the Server**

Once the dependencies are installed, you can start the Flask server using the following command:

```bash
python manage.py
```

The server will start running on `http://127.0.0.1:5000/` by default, where you can see the phishing page.

### **4. Customize the Page (Optional)**

You can edit the HTML files inside the `FacebookLogin/` and `LoginPage/` directories to further customize the phishing page if desired. Modify the CSS and JavaScript to match the look of a real Facebook login page.

### **5. Capture User Input**

Any input submitted on the login page is captured and stored by the Flask backend. You can modify the backend code to handle the captured data as needed.

---

## Important Disclaimer

This repository is **for educational purposes only**. 

- Do not use this phishing page to engage in illegal activities.
- Use it only in a controlled and ethical environment to learn more about web-based attacks and phishing techniques.
- Respect others' privacy and never use this for malicious purposes.

---

## Requirements

- Python 3.x
- Flask web framework
- Basic knowledge of HTML, CSS, and Python
- Make sure to configure the server to avoid unnecessary exposure to public networks

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to fork this repository and contribute by creating a pull request. Always be sure to test the changes thoroughly before submitting.

---

## Warning ⚠️

> **This is a phishing tool, use responsibly. Always ensure that your usage of this repository complies with legal and ethical guidelines.**
> 
> **This project is intended for educational purposes only.**

---

**Happy coding and stay secure! 🕶️**
