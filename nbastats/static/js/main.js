
// document.getElementById('player-1').onclick = function() {

// };


// var $playerOne = $('#player-1');
// var $playerTwo = $('#player-2');
// var $playerOneStat = $('#player-1-stat');
// var $playerTwoStat = $('#player-2-stat');

// $playerOne.on('change', function() {
//     changeSelected();
// })

// // Changes all PRIVACY OPTIONS to the selected value from the dropdown menu
// function changeSelected(target, value) {
//     // $.ajax -> GET ID of player /nbaplayer/$id
    
    
//     target.val(value.val());
// }

jQuery.ajax({
    url: "/nbastats/players",
}).done(function( data ) {
    console.log(data);
});

