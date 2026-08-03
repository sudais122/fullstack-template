# Full Stack MERN Template

A reusable full-stack template built with the MERN stack.

## Tech Stack

### Frontend

* React
* Vite
* React Router
* 
* Tailwind CSS

### Backend

* Node.js
* Express.js
* MongoDB
* Mongoose
* JWT Authentication
* Cookie Parser
* Multer
* Cloudinary
* CORS

## 📁 Project Structure

```text
fullstack-template/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── middleware/
│   │   ├── db/
│   │   ├── utils/
│   │   └── index.js
│   │
│   ├── public/
│   ├── .env.example
│   └── package.json
│
├── .prettierrc
├── .prettierignore
├── .gitignore
├── package.json
└── README.md
```

## ⚙️ Installation

Clone or scaffold the project:

```bash
npx degit yourusername/fullstack-template my-project
```

Move into the project:

```bash
cd my-project
```

Install backend dependencies:

```bash
cd backend
npm install
```

Install frontend dependencies:

```bash
cd ../frontend
npm install
```

## 🔑 Environment Variables

Create a `.env` file inside the `backend` folder.

```bash
cp .env.example .env
```

Update the values with your own credentials.

## ▶️ Running the Project

Start the backend:

```bash
cd backend
npm run dev
```

Start the frontend:

```bash
cd frontend
npm run dev
```

## 🎨 Formatting

From the project root:

```bash
npm run format
```

To check formatting:

```bash
npm run check-format
```

## 📄 License

This project is available under the ISC License.
