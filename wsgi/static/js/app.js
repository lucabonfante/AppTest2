/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//author : lucabonfante

var APP = {
    aggiungiCoordinate: function () {
        $('#inviaCoordinate').on('click', function () {
            var longitude = $('#longitude').val();
            var latitude = $('#latitude').val();
            var date = new Date();
            $.ajax(
                    {
                        method: "POST",
                        url: "/insertPosition/",
                        contentType: "application/json",
                        crossDomain: true,
                        type: "json",
                        data: JSON.stringify({"longitude": longitude, "latitude": latitude, "date": date}),
                        dataType: "json",
                        success: function (data) {
                            APP.leggiPosizioni();
                            APP.maps(latitude, longitude);
                            console.info(data);
                        },
                        error: function () {
                            alert('errore');
                        }
                    });
        });

    },
    leggiPosizioni: function () {
        $.ajax(
                {
                    method: "POST",
                    url: "/readPositions/",
                    contentType: "application/json",
                    crossDomain: true,
                    type: "json",
                    dataType: "HTML",
                    success: function (result) {
                        $("#campoTextPositions").html(result);//html da stampare
                    },
                    error: function () {
                        $("#campoTextPositions").html("errore");
                    }
                });
    },
    eliminaPosition: function (codice) {
        $.ajax(
                {
                    method: "POST",
                    url: "/cleanPositions/",
                    contentType: "application/json",
                    crossDomain: true,
                    type: "json",
                    data: JSON.stringify({"pos": codice}),
                    dataType: "text",
                    success: function (data) {
                    },
                    error: function () {
                    }
                });

    },
    maps: function (latitude, longitude) {
        var myCenter = new google.maps.LatLng(43, 67);

        function initialize()
        {
            var mapProp = {
                center: myCenter,
                zoom: 5,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };

            var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

            var marker = new google.maps.Marker({
                position: myCenter,
            });

            marker.setMap(map);
        }

        google.maps.event.addDomListener(window, 'load', initialize);
    }

};
$(document).ready(function () {

    APP.aggiungiCoordinate();
    APP.leggiPosizioni();
    APP.eliminaPosition();
    APP.maps();
});