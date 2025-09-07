const express = require("express");
const router = express.Router();
const products = require("../data/fake-products.json");

router.get("/", (req, res) => {
  res.json(products);
});

module.exports = router;
