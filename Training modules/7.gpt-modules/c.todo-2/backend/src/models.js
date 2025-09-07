const { Sequelize, DataTypes } = require("sequelize");

// ⚠️ Sau này sẽ chuyển sang PostgreSQL → chỉ cần đổi dialect + driver
const sequelize = new Sequelize("todo_db", "root", "password", {
  host: "localhost",
  dialect: "mysql"
});

const Todo = sequelize.define("Todo", {
  title: { type: DataTypes.STRING, allowNull: false },
  completed: { type: DataTypes.BOOLEAN, defaultValue: false }
});

module.exports = { sequelize, Todo };
