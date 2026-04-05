# Database Schema and Architecture Documentation

This document provides a comprehensive overview of the database schema and architecture for the Flask Project.

## Database Overview
The application uses a relational database to manage its data. The schema is designed to accommodate a variety of features and functionalities for the users.

### Entities
1. **Users**  
   - **id** (Primary Key)  
   - **username** (Unique)  
   - **email** (Unique)  
   - **password_hash**  
   - **created_at**  
   - **updated_at**  

2. **Posts**  
   - **id** (Primary Key)  
   - **user_id** (Foreign Key to Users)  
   - **title**  
   - **content**  
   - **created_at**  
   - **updated_at**  

3. **Comments**  
   - **id** (Primary Key)  
   - **post_id** (Foreign Key to Posts)  
   - **user_id** (Foreign Key to Users)  
   - **content**  
   - **created_at**  

4. **Likes**  
   - **id** (Primary Key)  
   - **post_id** (Foreign Key to Posts)  
   - **user_id** (Foreign Key to Users)  
   - **created_at**  

### Relationships
- A User can have many Posts.
- A Post can have many Comments.
- A User can like many Posts.

### Database Diagram
(Include or reference a diagram of the schema)

## Schema Creation
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW() 
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(id),
    user_id INT REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(id),
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);
``` 

## Considerations
- Ensure proper indexing for performance.
- Regular backups to prevent data loss.
- Proper normalization to reduce redundancy.

This documentation should evolve as the application develops further.