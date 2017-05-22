
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
// var Song = Backbone.Model.extend({
//     validate: function(attrs) {
//         if (!attrs.title) {
//             return "Title is required";
//         }
//     }
// })

// var song = new Song(); //won't throw an error but will not be valid.

// //to check if valid:
// song.isValid();

////////////////////////////////////////////////////////////////////////////////////

//Inheritance

// var Animal = Backbone.Model.extend({
//     walk: function() {
//         console.log("Animal walking...");
//     }
// });

// var Dog = Animal.extend({
//     walk: function() {
//         //If we want the super one/upper class one
//         Animal.prototype.walk(); // works like a static method
//         Animal.prototype.walk.apply(this); //this is to apply it to this.
//         console.log("Dog walking...");
//     }
// });

// var dog = new Dog();

// dog.walk();

////////////////////////////////////////////////////////////////////////////////////

//Collections

// var Song = Backbone.Model.extend();

// var Songs = Backbone.Collection.extend({
//     model: Song
// })

// var songs = new Songs([
//     new Song({title: "Song 1"}),
//     new Song({title: "Song 2"}),
//     new Song({title: "Song 3"}),    
// ]);

// songs.add(new Song({title: "Song 1"}));

// //All collections have a length and models property

// //indexing
// songs.at(0)

// //getting a particular one
// songs.get("c1")

// //removing
// songs.remove(songs.at(0))

// //length
// songs.length

// ////////////////////////////////////////////////////////////////////////////////////

// //Adding to a collections

// songs.add(new Song({title: "Song 1", genre: "Jazz", downloads: 110}), {at: 0}); //push to certain indexing

// //orrrr you can do:

// songs.push(new Song({title: "Song 2", genre: "Jazz", downloads: 90}))

// //finding objects

// var jazzSongs = songs.where({genre: "Jazz"}) //Returns a collection

// var firstJazzSong = songs.findWhere({genre: "Jazz"})

// console.log("Jazz Songs", jazzSongs);

// console.log("First Jazz Songs", firstJazzSong);

// //Can filter further
// var filteredSongs = songs.where({genre: "Jazz", title: "Song 2"});
// console.log("Filtered Songs", filteredSongs);

// //If we want to filter by download numbers or something like that
// var topDownloads = songs.filter(function(song) {
//     return song.get("downloads") > 100;
// })

// console.log("Top Downloads", topDownloads);

// //Iterating through collection.
// songs.each(function(song) {
//     console.log(song);
// })


