import * as readline from 'readline';

function processInputData(callback: (input: string) => void) {
  // Create readline interface
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  });

  // Listen for lines of input
  rl.on('line', (line) => {
    callback(line);
  });

  rl.on('close', () => {
    console.log('Input processing completed');
    process.exit(0);
  });
}

// Use the function
processInputData((input) => {
  console.log('Received input:', input);
});
