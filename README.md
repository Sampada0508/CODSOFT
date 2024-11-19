<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chefie - Your Recipe Chatbot</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600;700&display=swap");

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
        }

        /* Background Color Animation with 6 shades */
        @keyframes backgroundTransition {
            0% , 100% {
                background: linear-gradient(90deg, #1d4e89, #133b63, #2a5985, #1f4e6f, #294f75, #123b57);
            }
            20% {
                background: linear-gradient(90deg, #294f75, #1a3f5f, #23597b, #182e49, #113c56, #1d5275);
            }
            40% {
                background: linear-gradient(90deg, #23597b, #1f517a, #2b688b, #1c3d5e, #183453, #153545);
            }
            60% {
                background: linear-gradient(90deg, #2b688b, #103d4a, #1b4e6a, #163f5c, #1e4b6f, #2a5677);
            }
            80% {
                background: linear-gradient(90deg, #1b4e6a, #295e74, #1a3b55, #224f70, #172c3e, #1d4e5c);
            }
            100% {
                background: linear-gradient(90deg, #1d4e89, #133b63, #2a5985, #1f4e6f, #294f75, #123b57);
            }
            
        }

        body {
            animation: backgroundTransition 5s ease infinite;
            background: linear-gradient(90deg, #1d4e89, #133b63, #2a5985, #1f4e6f, #294f75, #123b57);
            font-family: Arial, sans-serif;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-size: 400% 400%;
            overflow: hidden;
            flex-direction: column;
            color: #ffffff;
        }

        .header {
            text-align: center;
            background: linear-gradient(90deg, #143559, #1c3d69);
            color: #fff;
            padding: 1rem 2rem;
            width: 50%;
            margin: 0 auto;
            box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
            font-style: italic;
            font-size: 1.8rem;
            text-transform: uppercase;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1rem;
        }

        .header h1 {
            font-size: 2rem;
            font-weight: 600;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.6);
            margin: 0;
        }

        .header img {
            height: 40px;
            width: 40px;
            border-radius: 50%;
            filter: invert(100%);
        }

        .container {
            background-color: #ffffff;
            width: 60%;
            padding: 2rem;
            margin: 3rem auto;
            border-radius: 8px;
            box-shadow: 4px 8px 16px rgba(0, 0, 0, 0.4);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 80vh;
        }

        #chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
            border-bottom: 1px solid #ddd;
        }

        .chat-message {
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
        }

        .chat-message.bot {
            justify-content: flex-start;
        }

        .chat-message.user {
            justify-content: flex-end;
        }

        .chat-message p {
            max-width: 80%;
            padding: 0.8rem 1rem;
            border-radius: 8px;
            font-size: 0.95rem;
            line-height: 1.4;
        }

        .chat-message.bot p {
            background-color: #143559;
            color: #ffffff;
            border-radius: 8px 8px 8px 0;
        }

        .chat-message.user p {
            background-color: #1c3d69;
            color: #ffffff;
            border-radius: 8px 8px 0 8px;
        }

        .chat-message img {
            max-width: 40%;
            margin-top: 1rem;
            border-radius: 8px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
            margin-top: 0.5rem;
        }

        .input-container {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .input-container input {
            flex: 1;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .input-container button {
            padding: 0.8rem 1rem;
            background-color: #143559;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .input-container button:hover {
            background-color: #1c3d69;
        }

        footer p {
            text-align: center;
            color: rgb(224, 219, 219);
            font-size: 0.8rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <header class="header">
        <img src="https://img.icons8.com/ios/452/chef-hat.png" alt="Chef Icon">
        <h1>Welcome to Chefie's World</h1>
    </header>

    <div class="container">
        <div id="chat-area">
            <div class="chat-message bot">
                <p>Hi there! 👋 I'm Chefie, your recipe assistant. What recipe are you looking for today?</p>
            </div>
        </div>
        <div class="input-container">
            <input type="text" id="user-input" placeholder="Type your recipe here..." autofocus>
            <button id="send-btn">Send</button>
        </div>
    </div>

    <footer>
        <p>Created By Sampada N S</p>
    </footer>

    <script>
        let chatArea = document.getElementById("chat-area");
        let sendBtn = document.getElementById("send-btn");
        let userInput = document.getElementById("user-input");

        const apiBaseUrl = "https://www.themealdb.com/api/json/v1/1/search.php?s=";

        const hardcodedRecipes = {
            "rasmalai": {
                name: "Rasmalai",
                image: "https://spicesnflavors.com/wp-content/uploads/2020/10/rasmalai-1-720x960.jpg",
                ingredients: [
                    "500g ricotta cheese",
                    "1 cup milk",
                    "1/2 cup sugar",
                    "1/2 tsp cardamom powder",
                    "Saffron strands",
                    "Almonds, chopped"
                ],
                instructions: `
                    1. Boil the milk and reduce it to half.
                    2. Add sugar, cardamom powder, and saffron to the milk.
                    3. Prepare ricotta cheese balls and soak them in the milk.
                    4. Garnish with almonds and serve chilled.
                `
            },
            "dosa": {
                name: "Dosa",
                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTf8ZlCKTNhV3Xg4NuPq8MaZpcRJMAcWm5ABuoFVUHyqpkyZzdJq5txI0Y4E6IeOv2iezo&usqp=CAU",
                ingredients: [
                    "1 cup rice",
                    "1/4 cup urad dal",
                    "1/2 tsp fenugreek seeds",
                    "Water",
                    "Salt"
                ],
                instructions: `
                    1. Soak rice and urad dal overnight.
                    2. Grind into a smooth batter and ferment for 8 hours.
                    3. Heat a pan, pour a thin layer of batter, and cook on both sides.
                    4. Serve with chutney or sambar.
                `
            },
            "idli": {
                name: "Idli",
                image: "https://artofpalate.com/wp-content/uploads/2016/08/idli-with-rice-flour.jpg",
                ingredients: [
                    "1 cup rice",
                    "1/4 cup urad dal",
                    "1/4 tsp fenugreek seeds",
                    "Water",
                    "Salt"
                ],
                instructions: `
                    1. Soak rice and urad dal overnight.
                    2. Grind into a smooth batter and ferment for 8 hours.
                    3. Steam the batter in idli molds for 10-15 minutes.
                    4. Serve with chutney and sambar.
                `
            }
            
                   
                
               
        };

        // Function to create chat messages
        function createChatMessage(sender, message, image = null) {
            let messageDiv = document.createElement("div");
            messageDiv.classList.add("chat-message", sender);
            let messageContent = document.createElement("p");
            messageContent.innerHTML = message;
            messageDiv.appendChild(messageContent);

            if (image) {
                let imgElement = document.createElement("img");
                imgElement.src = image;
                messageDiv.appendChild(imgElement);
            }

            chatArea.appendChild(messageDiv);
            chatArea.scrollTop = chatArea.scrollHeight;
        }

        // Function to fetch recipes
        function fetchRecipe(recipeName) {
            // Check for hardcoded recipes
            if (hardcodedRecipes[recipeName.toLowerCase()]) {
                const recipe = hardcodedRecipes[recipeName.toLowerCase()];
                const mealDetails = `
                    <b>HERE'S WHAT I FOUND FOR "${recipe.name}":</b><br><br>
                    <b>INGREDIENTS:</b><br> ${recipe.ingredients.join(", ")}<br><br>
                    <b>INSTRUCTIONS:</b><br>${recipe.instructions}
                `;
                createChatMessage("bot", mealDetails, recipe.image);
            } else {
                // If not hardcoded, fetch from API
                fetch(apiBaseUrl + recipeName)
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.meals) {
                            let meal = data.meals[0];
                            let ingredients = [];
                            let count = 1;

                            for (let key in meal) {
                                if (key.startsWith("strIngredient") && meal[key]) {
                                    let ingredient = meal[key];
                                    let measure = meal["strMeasure" + count];
                                    ingredients.push(`${measure} ${ingredient}`);
                                    count++;
                                }
                            }

                            let mealDetails = `
                                <b>HERE'S WHAT I FOUND FOR "${meal.strMeal}":</b><br><br>
                                <b>CUISINE:</b> ${meal.strArea}<br><br>
                                <b>INGREDIENTS:</b><br> ${ingredients.join(", ")}<br><br>
                                <b>INSTRUCTIONS:</b><br>${meal.strInstructions}
                            `;
                            createChatMessage("bot", mealDetails, meal.strMealThumb);
                        } else {
                            createChatMessage("bot", "Sorry, I couldn't find that recipe. Try searching for something else.");
                        }
                    })
                    .catch(() => {
                        createChatMessage("bot", "Oops! Something went wrong. Please try again.");
                    });
            }
        }

        sendBtn.addEventListener("click", () => {
            let userMessage = userInput.value.trim();
            if (userMessage) {
                createChatMessage("user", userMessage);
                createChatMessage("bot", "Let me find that for you...");
                fetchRecipe(userMessage);
                userInput.value = "";
            }
        });

        userInput.addEventListener("keyup", (e) => {
            if (e.key === "Enter") {
                sendBtn.click();
            }
        });
    </script>
</body>
</html>
