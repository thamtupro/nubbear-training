const express = require("express");
const cors = require("cors");
const app = express();
const productsRoute = require("./routes/products");

app.use(cors());
app.use(express.json());
app.use("/api/products", productsRoute);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
