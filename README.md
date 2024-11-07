# Research Paper Repository

A platform created for the DPS R.K. Puram Hackathon, allowing users to share, categorize, and interact with research papers within a like-minded community. Built with Django, this platform enables users to upload, comment on, and discuss research papers.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **Paper Upload**: Users can upload their research papers in PDF format.
- **Commenting**: Engage with other researchers by commenting on their work.
- **Discussion & Chat**: Users can chat with other researchers to facilitate discussions and collaborations.
- **Categorization**: Papers can be categorized by topic, making them easy to discover.
- **Community Building**: Designed to foster a collaborative and engaging research community.

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python 3.x** installed
- **Django**: Install Django via pip:
  ```bash
  pip install django
  ```

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/research-paper-repo.git
   cd research-paper-repo
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

All file uploads are securely stored on the server you’re hosting. Users do not need any separate setup for file storage.

- **Sign Up / Log In**: Create an account to access the platform.
- **Upload Papers**: Log in to upload your research papers in PDF format.
- **Browse and Discuss**: Browse papers by category, and engage with others by commenting and chatting.
- **Collaboration**: Use the chat feature to connect with researchers who share your interests.

[Run the website on incognito for best performance.]
---

### Credits

This project was created by Dhairya Sibal and Shloak Gupta for the DPS R.K. Puram Hackathon.
