

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

//MAKING THE PASSWORD LISY
const nums = ['1','2','3','4','5','6','7','8','9','0'];
const lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'];
const uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'];
const symbols = ['@','#','$','%','&','.','-','_'];

const everyChar =  nums.concat(lowercase, uppercase, symbols);


//MAKING THE PASSWORD
function make_password(use){
    var new_password = '';

    for (let i=0; i<= 15; i++){
        let random_num = Math.floor(Math.random()*66);
        new_password = new_password.concat(everyChar[random_num]);
    }

    console.log("Password: "+new_password);
};


//ACTUAL SCRIPT
// var loop = 'Y';
while (loop === 'Y'){
    readline.question('What is this password for? ', use => {
        make_password(use);
        readline.question('Do you want to continue? Y/N: '), loop =>{
            readline.close()
        }
        readline.close();
    });
}
