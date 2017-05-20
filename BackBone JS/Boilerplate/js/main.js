
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
var Song = Backbone.Model.extend();
// var song = new Song();

// song.set("title", "Blue in Green");
// song.set({
//     artist: "Miles Davis",
//     publishYear: 1959
// })

////////////////////////////////////////////////////////////////////////////////////

//Can also initialize this way with a json object:
//This will appear in the attributes section of the model.
var song = new Song({
    title: "Blue in Green",
    artist: "Miles Davis",
    publishYear: 1959
});

////////////////////////////////////////////////////////////////////////////////////