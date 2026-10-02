async function fetchUsers() {

    const userContainer = document.getElementById("userContainer");
    const loading = document.getElementById("loading");

    userContainer.innerHTML = "";
    loading.innerText = "Loading...";

    try {

        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users"
        );

        if (!response.ok) {
            throw new Error("Failed to fetch data");
        }

        const users = await response.json();

        console.log("JSON Data:", users);

        loading.innerText = "";

        users.forEach(user => {

            const card = document.createElement("div");

            card.classList.add("card");

            card.innerHTML = `
                <h2>${user.name}</h2>

                <p><strong>Username:</strong> ${user.username}</p>

                <p><strong>Email:</strong> ${user.email}</p>

                <p><strong>Phone:</strong> ${user.phone}</p>

                <p><strong>City:</strong> ${user.address.city}</p>

                <p><strong>Company:</strong> ${user.company.name}</p>
            `;

            userContainer.appendChild(card);
        });

    } catch (error) {

        loading.innerText = "Error: " + error.message;

        console.error("API Error:", error);
    }
}