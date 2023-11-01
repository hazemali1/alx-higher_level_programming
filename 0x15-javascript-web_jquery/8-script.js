$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: function (data) {
		$.each(data.results, function (index, ti){
			$("UL#list_movies").append('<li>' + ti.title + '</li>');
		});
	}
});
