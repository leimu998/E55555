<?php
// 连接到 MySQL 数据库
$servername = "localhost";
$username = "Sunny";
$password = "LY2000414QWE";
$dbname = "photo share";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

// 从表单数据中获取用户名和密码
$username = $_POST["username"];
$password = $_POST["password"];

// 查询用户表中是否存在该用户
$sql = "SELECT * FROM users WHERE username='$username'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    // 验证密码是否正确
    if ($password == $row["password"]) {
        // 将用户信息存储在 session 中
        session_start();
        $_SESSION["username"] = $username;

        // 跳转到主页
        header("Location: index.php");
        
    } else {
        // 密码错误，显示错误消息
        echo "密码错误，请重新输入。";
    }
} else {
    // 用户名不存在，显示错误消息
    echo "该用户名不存在，请重新输入。";
}

$conn->close();
?>
