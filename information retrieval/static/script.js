function search() {
    var keyword = $('#keyword').val();
    $.get('/search', { keyword: keyword }, function(data) {
        displayResults(data);
    });
}

function displayResults(results) {
    var resultsDiv = $('#results');
    resultsDiv.empty();
    if (results.length === 0) {
        resultsDiv.append('<p>No results found.</p>');
    } else {
        results.forEach(function(result) {
            resultsDiv.append('<p><a href="#" onclick="playVideo(\'' + result.video + '\', \'' + result.timestamp + '\')">' + result.video + ' - ' + result.timestamp + '</a></p>');
        });
    }
}

function playVideo(video, timestamp) {
    // Your code to play the video at the specified timestamp
    console.log('Playing video:', video, 'at timestamp:', timestamp);
}
function search() {
    var keyword = $('#keyword').val();
    $.get('/search', { keyword: keyword }, function(data) {
        displayResults(data);
    });
}

function displayResults(results) {
    var resultsDiv = $('#results');
    resultsDiv.empty();
    if (results.length === 0) {
        resultsDiv.append('<p>No results found.</p>');
    } else {
        results.forEach(function(result) {
            resultsDiv.append('<p><a href="#" onclick="playVideo(\'' + result.video + '\', \'' + result.timestamp + '\')">' + result.video + ' - ' + result.timestamp + '</a></p>');
        });
    }
}

function playVideo(video, timestamp) {
    var videoContainer = $('#video-container');
    videoContainer.empty();
    videoContainer.append('<video controls><source src="' + video + '" type="video/mp4"></video>');
    // Optionally, seek to the specified timestamp
}

$(document).ready(function() {
    $('#searchButton').click(function() {
        var keyword = $('#keywordInput').val();
        $.ajax({
            url: '/search',
            method: 'GET',
            data: { 'keyword': keyword },
            success: function(data) {
                displayResults(data);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });

    function displayResults(results) {
        $('#results').empty();
        results.forEach(function(result) {
            $('#results').append('<p>' + result + '</p>');
        });
    }
});

