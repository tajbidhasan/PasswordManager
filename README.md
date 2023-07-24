

 <h1>Password Manager GUI Application</h1>
    <p>This code is a simple password manager application built using the Tkinter library in Python. 
    The application provides a graphical user interface (GUI) that allows users to store and retrieve their website 
    login credentials (website, email/username, and password) securely. The password generator feature also enables users to create strong and random passwords for their accounts.</p>
    <h2 align="center">Video Demo</h2>
    <p align="center">
        <a href="https://youtu.be/4XFKmoh0mMo">
            <img src="https://img.youtube.com/vi/4XFKmoh0mMo/0.jpg" alt="Video">
        </a>
    </p>
<h2>Features:</h2>
<ul>
    <li><strong>Password Generator:</strong> The application includes a password generator function that creates strong and random passwords consisting of letters (both lowercase and uppercase), numbers, and symbols. The generated password can be copied and used for various accounts.</li>
    <li><strong>Save Passwords:</strong> Users can input the website, email/username, and password into the designated input fields and click the "Add" button to save their login credentials. The data is stored in a JSON file named "data.json" in the same directory as the application.</li>
    <li><strong>Search Passwords:</strong> Users can search for their saved passwords by entering the website's name and clicking the "Search" button. If the website's data is present in the JSON file, the application will display the corresponding email/username and password.</li>
</ul>


<h2>Usage:</h2>
<ul>
    <li>Upon running the application, the main window will open, featuring input fields for website, email/username, and password.</li>
    <li>To generate a random password, click the "Generate Password" button, and the generated password will be displayed in the password input field.</li>
    <li>To save login credentials, enter the website, email/username, and password in their respective input fields and click the "Add" button.</li>
    <li>To search for a saved password, enter the website's name in the website input field and click the "Search" button. If the website's data is present, the email/username and password will be displayed in a pop-up message.</li>
</ul>

<h2>Note:</h2>
<ul>
    <li>If the "data.json" file is not present initially, the application will create it when saving the first set of login credentials.</li>
    <li>The application assumes that users have read and write permissions for the current directory to interact with the "data.json" file.</li>
</ul>

<h2>Additional Considerations:</h2>
<ul>
    <li>For security reasons, it is essential to encrypt the password data before saving it to the file. The current implementation stores passwords in plain text, which is not recommended for a production-level application.</li>
    <li>It's advisable to add error handling and validation to ensure that users enter the required information correctly.</li>
    <li>To enhance the password manager's functionality, additional features such as editing or deleting saved passwords can be implemented.</li>
    <li>Consider integrating a master password mechanism to protect access to the application and its saved data.</li>
    <li>This application is intended for educational purposes and personal use. For real-world applications, it is recommended to use established and secure password manager software that employs strong encryption algorithms and follows industry best practices.</li>
</ul>

<p>Overall, this Password Manager GUI application is a simple implementation to showcase the use of Tkinter in building user-friendly interfaces for password management.</p>
