# 🚀 API Integration & JSON Handling

A beginner-friendly web project demonstrating **API integration, JSON data handling, asynchronous JavaScript, and dynamic DOM manipulation**.

This project fetches user data from a public REST API and dynamically displays the information in responsive user cards.

## 🌐 Live Demo

Add your deployed project link here:

`https://your-username.github.io/api-integration-json-handling/`

## 📌 Features

* 🔗 REST API Integration
* 📦 JSON Data Handling
* ⚡ Fetch API
* ⏳ Async/Await
* 🔄 Dynamic Data Rendering
* 🛡️ Error Handling
* 📱 Responsive User Cards
* 🔍 Console-based JSON inspection
* 🎨 Clean and simple UI

## 🛠️ Technologies Used

* HTML5
* CSS3
* JavaScript
* REST API
* JSON
* Fetch API
* Git & GitHub

## 🔌 API Used

This project uses the **JSONPlaceholder** public API.

API Endpoint:

`https://jsonplaceholder.typicode.com/users`

The API provides sample user information such as:

* Name
* Username
* Email
* Phone
* City
* Company

## 📂 Project Structure

```text
API Integration JSON Handling/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

## ⚙️ How It Works

The application follows this basic flow:

```text
User clicks "Load Users"
          ↓
       fetch()
          ↓
      API Request
          ↓
     JSON Response
          ↓
    response.json()
          ↓
 JavaScript Array/Object
          ↓
    DOM Manipulation
          ↓
   User Cards Displayed
```

## 📖 Key Concepts

### Fetch API

The `fetch()` method is used to request data from the REST API.

```javascript
const response = await fetch(
    "https://jsonplaceholder.typicode.com/users"
);
```

### JSON Handling

The API response is converted into JavaScript data using:

```javascript
const users = await response.json();
```

### Dynamic Rendering

User information is dynamically displayed using JavaScript:

```javascript
users.forEach(user => {
    // Create and display user card
});
```

### Nested JSON

The project also demonstrates accessing nested JSON properties:

```javascript
user.address.city
```

and:

```javascript
user.company.name
```

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/api-integration-json-handling.git
```

### 2. Open the project

```bash
cd api-integration-json-handling
```

### 3. Open in VS Code

```bash
code .
```

### 4. Run the project

Open `index.html` using **Live Server** in VS Code.

Click the **Load Users** button to fetch and display API data.

## 🧪 Error Handling

The project uses `try...catch` to handle API errors:

```javascript
try {
    // API request
} catch (error) {
    console.error("API Error:", error);
}
```

This helps prevent the application from failing silently when an API request encounters an error.

## 🎯 Learning Objectives

Through this project, I learned:

* How REST APIs work
* How to fetch data using JavaScript
* How to handle JSON responses
* How to use async/await
* How to work with arrays and objects
* How to access nested JSON data
* How to dynamically create HTML elements
* How to handle API errors
* How to integrate external APIs into frontend applications

## 🔮 Future Improvements

* 🔍 Add user search functionality
* 📊 Add filtering and sorting
* 📄 Add pagination
* 🌙 Add dark mode
* 📱 Improve mobile UI
* 🔄 Add refresh functionality
* 💾 Add local storage support

## 👨‍💻 Author

**Ayush Singh**

B.Tech Computer Science & Engineering Student

### 🔗 Connect With Me

* GitHub: `https://github.com/rajputayushsingh`
* LinkedIn: Add your LinkedIn profile link here

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📄 License

This project is created for **learning and educational purposes**.
