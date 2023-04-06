$(document).ready(function () {
    $('#search-form').on('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        $.ajax({
            url: this.action,
            method: this.method,
            data: new URLSearchParams(formData),
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function (data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    // Show an alert or update the page based on the response
                    alert(data.domain_found ? 'Domain found in database.' : 'Domain not found in database.');
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown);
            }
        });
    });
});