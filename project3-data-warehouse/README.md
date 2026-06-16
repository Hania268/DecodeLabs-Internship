# Project 3: The Data Warehouse 🗄️

## Overview
Provisioned a managed MySQL database on AWS RDS and created a structured Interns table with full data persistence.

## Tools Used
- AWS RDS (MySQL)
- MySQL Workbench
- Python + PyMySQL (Bonus)

## What I Did
- Created RDS MySQL instance (Free Tier) in AWS
- Configured Security Group with Port 3306
- Created `Interns` table with PRIMARY KEY, UNIQUE, NOT NULL constraints
- Inserted 5+ dummy records using INSERT INTO
- Verified data with SELECT query
- Connected via Python script using PyMySQL (Bonus)

## SQL Used
```sql
CREATE TABLE Interns (
    InternID   INT          PRIMARY KEY,
    FirstName  VARCHAR(50)  NOT NULL,
    LastName   VARCHAR(50)  NOT NULL,
    Role       VARCHAR(100) NOT NULL,
    Email      VARCHAR(100) UNIQUE NOT NULL
);
```
## Bonus
- Python script connected to RDS and fetched all records programmatically
