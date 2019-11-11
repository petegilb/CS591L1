var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});


const display = function (dealer, player) {
  let dealerStr = 'Dealer: ' + dealer.join(', ');
  let playerStr = 'Player: ' + player.join(', ');
  console.log(dealerStr);
  console.log(playerStr);
};

const clear = function () {
  console.clear();
};

const readBoolean = function () {
  console.log('Receive another card? Y/N:');
  return new Promise(function (resolve) {
    rl.on('line', function (line) {
      resolve(line.toLowerCase() === 'y');
    });
  });
};

const stop = function () {
  rl.close();
}

module.exports = {
  display: display,
  clear: clear,
  readBoolean: readBoolean,
  stop: stop
};

// for testing purposes
async function main() {
  // display some hands
  display(['6', 'X'], ['11', '8']);

  // read decision as promise and await for it to resolve
  const bool = await readBoolean();

  // Clear screen and display some other hand
  if (bool) {
    clear();
    display(['6', 'X'], ['11', '8', '9']);
    console.log('you lost!');
  }

  // Stop
  stop();
}
if (require.main === module) {
  main();
}


