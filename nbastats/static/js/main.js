
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
}).done(function( data ){
    
    for (var i = 0; i < data.length; i++){
        $('#player-one').append($('<option />').val(data[i].id).html(data[i].name));
        $('#player-two').append($('<option />').val(data[i].id).html(data[i].name));
    }
    
    // PLAYER ONE HANDLERS
    $('#player-one').on('change', function(){
        console.log($(this).val());
        
        jQuery.ajax({
            url: '/nbastats/players/' + $(this).val()
        }).done(function( player ){
            console.log(player);
            
            $('#one-name').html(player.name);
            $('#one-team').html(player.team);
            $('#one-pos').html(player.position);
            $('#one-gp').html(player.game_played);
            $('#one-min').html(player.min_per_game);
            $('#one-fg').html(player.field_goal_percent);
            $('#one-ft').html(player.free_throw_percent);
            $('#one-threem').html(player.three_made);
            $('#one-threeper').html(player.three_percent);
            $('#one-threepg').html(player.three_per_game);
            $('#one-pts').html(player.pts_per_game);
            $('#one-oreb').html(player.o_reb_per_game);
            $('#one-dreb').html(player.d_reb_per_game);
            $('#one-reb').html(player.reb_per_game);
            $('#one-ast').html(player.ast_per_game);
            $('#one-stl').html(player.steals_per_game);
            $('#one-blk').html(player.blocks_per_game);
            $('#one-to').html(player.to_per_game);
            $('#one-pf').html(player.fouls_per_game);
            $('#one-tech').html(player.tot_tech);
            $('#one-pmr').html(player.plus_minus_rating);
            
        })
        
    })
    
    // PLAYER TWO HANDLERS
    $('#player-two').on('change', function() {
        jQuery.ajax({
            url: '/nbastats/players/' + $(this).val()
        }).done(function( player ){
            console.log(player);
            
            $('#two-name').html(player.name);
            $('#two-team').html(player.team);
            $('#two-pos').html(player.position);
            $('#two-gp').html(player.game_played);
            $('#two-min').html(player.min_per_game);
            $('#two-fg').html(player.field_goal_percent);
            $('#two-ft').html(player.free_throw_percent);
            $('#two-threem').html(player.three_made);
            $('#two-threeper').html(player.three_percent);
            $('#two-threepg').html(player.three_per_game);
            $('#two-pts').html(player.pts_per_game);
            $('#two-oreb').html(player.o_reb_per_game);
            $('#two-dreb').html(player.d_reb_per_game);
            $('#two-reb').html(player.reb_per_game);
            $('#two-ast').html(player.ast_per_game);
            $('#two-stl').html(player.steals_per_game);
            $('#two-blk').html(player.blocks_per_game);
            $('#two-to').html(player.to_per_game);
            $('#two-pf').html(player.fouls_per_game);
            $('#two-tech').html(player.tot_tech);
            $('#two-pmr').html(player.plus_minus_rating);
            
        })
    })

})

var numbers = ['one', 'two', 'three', 'four', 'five'];

jQuery.ajax({
    url: "/nbastats/players/points"
}).done(function( points ){
    for (var i = 0; i < points.length; i++){
        console.log('points: ', points[i]);
        console.log($('#ppg-table'));
        
        $('#ppg-name-' + numbers[i]).html(points[i].name)
        $('#ppg-num-' + numbers[i]).html(points[i].pts_per_game);
    }

})

jQuery.ajax({
    url: "/nbastats/players/rebounds"
}).done(function( rebounds ){
    for (var i = 0; i < rebounds.length; i++){
        console.log('rebounds: ', rebounds[i]);
        
        $('#rpg-name-' + numbers[i]).html(rebounds[i].name)
        $('#rpg-num-' + numbers[i]).html(rebounds[i].reb_per_game);
    }

})

jQuery.ajax({
    url: "/nbastats/players/assists"
}).done(function( assists ){
    for (var i = 0; i < assists.length; i++){
        console.log('assists: ', assists[i]);
        
        $('#apg-name-' + numbers[i]).html(assists[i].name)
        $('#apg-num-' + numbers[i]).html(assists[i].ast_per_game);
    }

})

jQuery.ajax({
    url: "/nbastats/players/plus_minus_rating"
}).done(function( plus_minus_rating ){
    for (var i = 0; i < plus_minus_rating.length; i++){
        console.log('plus_minus_rating:', plus_minus_rating[i]);
        
        $('#pmr-name-' + numbers[i]).html(plus_minus_rating[i].name)
        $('#pmr-num-' + numbers[i]).html(plus_minus_rating[i].plus_minus_rating);
    }

})