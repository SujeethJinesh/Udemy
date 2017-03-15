console.log('Starting app.');

const fs = require('fs'); //tells node that we want to use the module
const os = require('os');
const notes = require('./notes.js');

var user = os.userInfo();

//console.log(user);

//to call it we use fs.appendFile
fs.appendFile('greetings.txt', `Hello ${user.username}! You are ${notes.age}`); //pass in file name and data

//this will cause errors so we can fix it two ways
/*
fs.appendFile('greetings.txt', 'Hello world!', function (err) {
	if (err) {
		console.log('Unable to write to file');
	}
});

fs.appendFileSync('greetings.txt', 'Hello world!');
*/