document.addEventListener("DOMContentLoaded", function () {
    const backendUrl = "https://hotel-booking-system-r5u2.onrender.com";

    // Signup
    async function signup() {
        const email = document.getElementById("signup-email").value;
        const username = document.getElementById("signup-username").value;
        const password = document.getElementById("signup-password").value;

        if (!email || !username || !password) {
            alert("Please fill in all signup fields.");
            return;
        }

        try {
            const response = await fetch(`${backendUrl}/signup`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include",
                body: JSON.stringify({ email, username, password }),
            });

            if (!response.ok) {
                const data = await response.json();
                alert("Signup failed: " + data.message);
            } else {
                alert("Signup successful!");
            }
        } catch (error) {
            console.error("Signup Error:", error);
            alert("Signup failed: Network error");
        }
    }

    // Login
    async function login() {
        const email = document.getElementById("login-email").value;
        const password = document.getElementById("login-password").value;

        if (!email || !password) {
            alert("Please fill in all login fields.");
            return;
        }

        try {
            const response = await fetch(`${backendUrl}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include",
                body: JSON.stringify({ email, password }),
            });

            if (!response.ok) {
                const data = await response.json();
                alert("Login failed: " + data.message);
            } else {
                alert("Login successful!");
            }
        } catch (error) {
            console.error("Login Error:", error);
            alert("Login failed: Network error");
        }
    }

    // Load Hotels
    async function getHotels() {
        try {
            const response = await fetch(`${backendUrl}/hotels`, {
                method: "GET",
                credentials: "include",
            });

            const data = await response.json();

            const hotelList = document.getElementById("hotel-list");
            hotelList.innerHTML = "";

            if (response.ok) {
                data.hotels.forEach(hotel => {
                    const li = document.createElement("li");
                    li.textContent = `${hotel.name} - ${hotel.location}`;
                    hotelList.appendChild(li);
                });
            } else {
                alert("Failed to fetch hotels: " + data.message);
            }
        } catch (error) {
            console.error("Fetch Hotels Error:", error);
            alert("Could not fetch hotels.");
        }
    }

    // Event listeners
    document.getElementById("signup-button").addEventListener("click", signup);
    document.getElementById("login-button").addEventListener("click", login);

    // Expose getHotels to global for button onclick
    window.getHotels = getHotels;
});
