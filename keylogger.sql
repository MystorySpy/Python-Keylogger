CREATE DATABASE IF NOT EXISTS keylogger;
USE keylogger;

CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `key` VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Keylogger SQL Setup
-- This script creates the database and table, and inserts minimal sample data for demonstration.

INSERT INTO logs (`key`) VALUES ('a');
INSERT INTO logs (`key`) VALUES ('A');
INSERT INTO logs (`key`) VALUES ('1');
INSERT INTO logs (`key`) VALUES ('!');
INSERT INTO logs (`key`) VALUES (' ');
INSERT INTO logs (`key`) VALUES ('[enter]');
