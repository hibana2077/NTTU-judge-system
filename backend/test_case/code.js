const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (num) => {
    for (let i = 0; i < num; i++) {
        rl.question('', (input) => {
            const [a, b] = input.split(' ');
            console.log(parseInt(a) + parseInt(b));
        });
    }
    rl.close();
});
