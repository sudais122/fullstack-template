import path from "path";
import { fileURLToPath } from "url";
import dotenv from "dotenv";
import { app } from "./app.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// dot.env config
dotenv.config({
  path: path.join(__dirname, "../.env"),
});

const PORT = process.env.PORT || 8000;

const startServer = async () => {
  try {
    // await connectDB();
    // console.log("Database connected successfully");

    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
  } catch (error) {
    console.error("Failed to start server:", error);
    process.exit(1);
  }
};

startServer();
