# Mental-Health-Chatbot

This repository contains code and data files for a chatbot designed to interact with users based on specific intents, as well as an order management system that manages customer order data. The chatbot is structured to respond to common greetings, farewells, and queries related to mental health, providing users with a therapeutic conversational experience. Additionally, an `order_data.xlsx` file is included to manage order details, allowing for order tracking, data analysis, and customer insights.

---

## Table of Contents

- [Overview](#overview)
- [Training Data](#training-data)
- [Strategies](#strategies)
- [Libraries Used](#libraries-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The project consists of two main components:

1. **Chatbot**: This conversational chatbot is designed to recognize intents and respond to users based on mental health-related patterns, offering personalized responses.
2. **Order Management System**: A data management component using `order_data.xlsx` to organize and analyze customer and order information, assisting in tracking orders and deriving insights.

---

## Training Data

### 1. Chatbot Training Data (`intents.json`)

The training data for the chatbot is organized into different tags, each representing an intent. For each intent, we have:
- **Tag**: Represents the category or intent, e.g., "greeting," "sad," "happy."
- **Patterns**: Common phrases or keywords users might type to invoke this intent, such as "Hi," "Hello," "Good morning."
- **Responses**: A set of predefined responses the chatbot will randomly select from when responding to the user.

Sample intents include:
- **Greeting**: Recognizes greetings from users and responds warmly.
- **Goodbye**: Recognizes farewells and offers a polite goodbye.
- **Mental Health**: Responds to feelings of sadness, stress, loneliness, and other emotions with supportive and empathetic messages.

### 2. Order Data (`order_data.xlsx`)

This file includes customer and order details such as:
- **Customer Information**: `id`, `first_name`, `last_name`, `email`, `gender`, `Phone_no`
- **Order Details**: `Product ID`, `Product Name`, `Scheduled Date`

These fields help in understanding customer demographics, tracking product popularity, and monitoring scheduled dates for various orders.

---

## Strategies

### Chatbot Strategies

The chatbot’s response strategies involve:
1. **Pattern Matching**: Each input is compared to patterns in the training data to detect the closest matching intent.
2. **Response Selection**: Based on the matched intent, a response is randomly chosen from a predefined list to ensure variety.
3. **Fallbacks for Unrecognized Inputs**: For unrecognized phrases, the chatbot has a default response to encourage users to clarify or continue the conversation.

### Order Management Strategies

1. **Data Aggregation**: Organizing and summarizing customer data, product preferences, and scheduling information to derive insights.
2. **Data Analysis**: Using Excel or data analysis libraries (e.g., `pandas`) to analyze trends, including the most popular products and customer demographics.
3. **Automation**: Creating scripts to automatically process order data and notify relevant departments about upcoming scheduled dates or order requirements.

---

## Libraries Used

This project uses several Python libraries for data processing, machine learning, and natural language processing:

- **pandas**: For handling and processing order data in Excel files.
- **NumPy**: For numerical operations and data handling.
- **NLTK / SpaCy**: For natural language processing, tokenizing user input, and preparing chatbot responses.
- **sklearn**: For clustering techniques, training models, and feature transformation.
- **Flask / FastAPI (Optional)**: To deploy the chatbot and order management APIs if a web-based interface is desired.

---

## Setup and Installation

**online App**:
- You can refer this [link for online App](https://mental-health-chatbot-monishar.streamlit.app/)

if you want to deploy it offline follow the below steps

  
1. **Clone the Repository**:
  Download the reposotory, extract, open the command prompt and paste the below command with the directory(Folder in which the files are present) of the app
   ```bash
   cd your/directory/path
   ```

3. **Install Required Libraries**:
   Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Install Required Libraries**:
   Install the dependencies using pip:
   ```bash
   streamlit run Mental_Helath_Chatbot.py
   ```
   Now you would have got a link in the cmd click on that link you will be directly taken to the app in the default browser

5. **Prepare Data**:
   - Ensure `intents.json` and `order_data.xlsx` files are in the root directory for the chatbot and order management system to function correctly.

---

## Usage

1. **Chatbot - Mental Health Gude**: Run the chatbot script to interact with it in a terminal or web interface. The bot will respond to greetings, general questions, and mental health queries.
3. **Order Management - Data**: Use the data analysis scripts provided to read and analyze `order_data.xlsx`. Custom scripts can be added to automate scheduling or analyze order trends.
4. **Order Management - Abilities**: If the user want to get the details about any order he or she can just enter the order_id of that partucualar order nothing front and back, the programme will check if the order is present in the `order_data.xlsx` if not found says 'Order Not found please contant the customer care' if found will show the order data.

---

## Contributing

We welcome contributions! Feel free to open issues, submit pull requests, or offer suggestions for improvements.

---

Feel free to reach out with any questions or suggestions on improving the chatbot’s functionalities or data processing strategies for order management.

---

