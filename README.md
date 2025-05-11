# COMS4170 Final Project - TriXposure

**Learn the exposure triangle the fast, interactive way.**

TriXposure is a Flask web‑app that teaches ISO, Shutter‑Speed and Aperture through short lessons and an auto‑graded quiz with 3 questions testing each section. 


## Project Layout
```text
TriXposure/
├── app.py                 # Flask entry‑point (runs both API and server‑side rendering)
│
├── src/                   # React + TypeScript source (if you want to rebuild the frontend)
│   ├── components/
│   └── …
│
├── templates/             
│   ├── base.html          # Shared layout – navbar, footer, Bootstrap/Tailwind imports
│   ├── iso.html           # Lesson page for ISO
│   ├── shutter.html       # Lesson page for Shutter Speed
│   ├── aperture.html      # Lesson page for Aperture
│   ├── quiz_base.html     # Generic quiz shell inherited by question pages
│   ├── quiz_home.html     # Quiz home page, transitioning from learning lesson to quiz section
│   ├── question1.html     # Quiz questions (1‑3)
│   ├── question2.html
│   ├── question3.html
│   └── review.html        # Review page in quiz section
│
├── static/                
│   ├── images/            # Illustrations for learning part and quiz photos
│   ├── data/
│   │   └── questions.json # Question/answer bank consumed by the quiz
│   └── react/             # Pre‑built Aurora animation for pages background
│       └── assets/        
│       └── index.html     
│
├── package.json           # Front‑end dependencies & npm scripts
├── package-lock.json      # Exact versions for reproducible builds
├── tsconfig.json          # TypeScript compiler settings for `/src`
├── node_modules/          # (auto‑generated) JS dependencies
│
└── README.md
```

## Requirements

- Python Python 3.8 or newer
- pip (Python package installer)

Install Flask with:
```bash
pip install flask
```

## Quick Start

```bash
# 1) Clone the repo
$ git clone https://github.com/Ry3n-Huang/TriXposure.git
$ cd TriXposure

# 2) Install dependencies
$ pip install flask

# 3) Fire up the server
$ python app.py   # visits http://127.0.0.1:5000/
```

## Browser Support
* For the best experience, open TriXposure in **Google Chrome**. 
* **Maximize** your browser window—some layouts may not render correctly on very small or mobile screens.
* Safari’s autoplay restrictions can block the looping hero video on the home page, leaving only a static background.

