$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#input').val(),
				},
			type : 'POST',
			url : '/convertor'
		})
			}

		});

		event.preventDefault();

	});

});
