
// In the first few sections, we do all the coding here.
// Later, you'll see how to organize your code into separate
// files and modules.

////////////////////////////////////////////////////////////////////////////////////
//Constructor essentially for the new backbone object 
// var Song = Backbone.Model.extend({
//     initialize: function() {
//         console.log("A new song has been created.");
//     }
// });

// //Creating a new object
// var song = new Song();

////////////////////////////////////////////////////////////////////////////////////
// var Song = Backbone.Model.extend();
// var song = new Song();

// song.set("title", "Blue in Green");
// song.set({
//     artist: "Miles Davis",
//     publishYear: 1959
// })

////////////////////////////////////////////////////////////////////////////////////

//Can also initialize this way with a json object:
//This will appear in the attributes section of the model.
// var song = new Song({
//     title: "Blue in Green",
//     artist: "Miles Davis",
//     publishYear: 1959
// });

// //Can convert to json object with:
// song.toJSON();

// //Can retrieve attributes by saying:
// song.get("title"); //note you have to have the quotes

// //clear by doing:
// song.unset("title");

// //or clear all vars with:
// song.clear();

// //Check if song has something:
// song.has("title"); //should return false

////////////////////////////////////////////////////////////////////////////////////

//Sometimes we'll want to make some default values in the model.

// var Song = Backbone.Model.extend({
//     defaults: {
//         genre: "Jazz"
//     }
// });

////////////////////////////////////////////////////////////////////////////////////

//If we need to ensure that the model contains something, we use validation
var Song = Backbone.Model.extend({
    validate: function(attrs) {
        if (!attrs.title) {
            return "Title is required";
        }
    }
})

var song = new Song(); //won't throw an error but will not be valid.

//to check if valid:
song.isValid();

////////////////////////////////////////////////////////////////////////////////////

//Inheritance