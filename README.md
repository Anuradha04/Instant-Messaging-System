# Instant-Messaging-System

A simple message management system using Python and MySQL. This script allows you to create, add, search, and delete messages from a MySQL database.

## Prerequisites

- Python 3.x
- MySQL database

## Installation

1. **Install MySQL Connector:**
   ```sh
   pip install mysql-connector-python
   ```

2. **Set Up MySQL Database:**
   - Create a database named `service`.
   - Create a user with the following credentials:
   - Input your password for root in place of password in the code.
     ```sql
     CREATE USER 'root'@'localhost' IDENTIFIED BY 'password'; 
     GRANT ALL PRIVILEGES ON service.* TO 'root'@'localhost';
     ```

## Usage
1. **Update Database Connection in the Script:**
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="password",
       database="service"
   )
   ```

2. **Run the Script:**
   ```sh
   python instantmsg.py
   ```

## Project Details

- **Instant Messaging System**
  - Developed an Instant Messaging system for managing and storing user messages, enabling message filtering, retrieval, and deletion functionalities with a user-friendly interface.
  - Enhanced the system by integrating MySQL database functionality, creating message storage, retrieval, and deletion operations, and improving message management efficiency with a structured database schema.

---
