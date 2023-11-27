<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Number guessing game</title>
    <style>
    html {
      font-family: sans-serif;
    }
    body {
      width: 50%;
      max-width: 800px;
      min-width: 480px;
      margin: 0 auto;
    }
	img {
	  width: 200px;
	  height: 250px;
	}
    .lastResult {
      color: white;
      padding: 3px;
    }
   </style>
  </head>
  <body>
  <h1>看图猜猜价格</h1>
  <p>请根据图片中的物品，试着猜出它的价格是多少，精确到多少角就可以了。请在下方给出你的正确答案，确定后，请按下确定按钮。
  <b>注意，每一张图片，你只有三次机会。</b></p>
  <img src="./img/01shouji.jpg">
  <div class="form">
    <label for="guessField">请输入你猜的价格: </label><input type="text" id="guessField" class="guessField">
    <input type="submit" value="确定" class="guessSubmit">
  </div>

  <div class="resultParas">
    <p class="guesses"></p>
    <p class="lastResult"></p>
    <p class="lowOrHi"></p>
  </div>
  <script src="js/jquery.js"></script>
  <script>
  //添加变量保存我们的数据
  let realPrice = 1999;
  const guesses = document.querySelector('.guesses');
  const lastResult = document. querySelector('.lastResult'); 
  const lowOrHi = document.querySelector('.lowOrHi');

  const guessSubmit = document.querySelector('.guessSubmit');
  const guessField = document.querySelector('.guessField');

  let guessCount = 1; 
  let resetButton;  
  
  //检测价格函数
  function checkGuess() {
  //alert('I am a placeholder');
  let userGuess = Number(guessField.value);
  
  if (guessCount === 1) {
    guesses.textContent = '之前你猜过:';
  }
  guesses.textContent += userGuess + ' ';
  if (userGuess === realPrice) {
    lastResult.textContent = '祝贺你猜对了!';
    lastResult.style.backgroundColor = 'green';
    lowOrHi.textContent = '';
    setGameOver();
  } else if (guessCount === 3) {
    lastResult.textContent = '!!!本轮游戏结束!!!';
    setGameOver();
  } else {
    lastResult.textContent = '对不起，你猜错了!';
    lastResult.style.backgroundColor = 'red';
    if(userGuess < realPrice) {
      lowOrHi.textContent = '你猜低了!';
    } else if(userGuess > realPrice) {
      lowOrHi.textContent = '你猜高了!';
    }
  }
    guessCount++;
    guessField.value = '';
    guessField.focus();
  }
  
  guessSubmit.addEventListener('click', checkGuess);
  function setGameOver() {
     guessField.disabled = true;
     guessSubmit.disabled = true;
     resetButton = document.createElement('button');
     resetButton.textContent = '开始一轮新游戏';
     document.body.appendChild(resetButton);
     resetButton.addEventListener('click', resetGame);
  }
  function resetGame() {
     guessCount = 1;
     const resetParas = document.querySelectorAll('.resultParas p');
     for (let i = 0 ; i < resetParas.length ; i++) {
       resetParas[i].textContent = '';
     }
     resetButton.parentNode.removeChild(resetButton);
     guessField.disabled = false;
     guessSubmit.disabled = false;
     guessField.value = '';
     guessField.focus();
     lastResult.style.backgroundColor = 'white';
  }
  let resetParas = document.querySelectorAll('.resultParas p');
  for (let i = 0 ; i < resetParas.length ; i++) {
     resetParas[i].textContent = '';
  }
  </script>
  </body>
</html>