document.addEventListener("touchstart", function(){}, true);

$(function() {
    'use strict';

    // data
    var reflectionData = {};

    var dataSplash = $('.page-content').attr('data-splash');
    var dataRedirect = $('.page-content').attr('data-redirect');
    if(dataSplash>0){
        $('.loading-mask').addClass('stop-loading');
        setTimeout(function(){
            goToPage(dataRedirect);
        },dataSplash);
    }
    $("#submit-form").submit(function(event) {
        var dataRedirect = $(this).attr('data-redirect');
        goToPage(dataRedirect);
        event.preventDefault();
        return false;
    });

    $("#main-stack").on('submit', '#reflection-form', function(event) {
        // $('.loading-mask').removeClass('stop-loading');
        event.preventDefault();
        
        var dataRedirect = $(this).data('redirect'),
            dataSubmit = $(this).data('submit');

        var date = new Date();
        var dateFormatted = date.toISOString().substring(0,10);
        
        var data ={
            date:dateFormatted,
            exerciseType: 2,
            
        };

        if (dataSubmit){
            $.ajax({
                method: "POST",
                url: '/api/doExercise',
                data: data,

                success: function(response){
                    goToPage(dataRedirect);
                },
                error: function (request, status, error) {
                    console.log(request.responseText);
                    alert(error + ". Please refresh the page and try again.");
                }
            });
            return;
        }
        else if (dataRedirect){
            goToPage(dataRedirect);
            return;
        }
    
        var dataInject = $(this).attr('data-inject');
        var $body = $('.page-content#main-stack');
        var $form = $('#reflection-form');

        var step = $form.data('step');
        console.log(step);

        switch(step){
            case 'high-point':
                reflectionData.highpoint = $('.input-form[name=high-point]').val();
                break;
            case 'low-point':
                reflectionData.lowpoint = $('.input-form[name=low-point]').val();
                break;
            case 'causes':
                var active = $('.bubble-block.active');
                var active_causes = [];
                for (var i = active.length - 1; i >= 0; i--) {
                    active_causes[i] = $(active[i]).text();
                }
                reflectionData.causes = active_causes;
                console.log(reflectionData);
                break;
            case 'better':

                var happy = $('.better-face').data('face') == 'happy';
                reflectionData.better = happy;
                console.log(reflectionData);
                break;
            default:
                break;
        }

        $.ajax({
            method: "GET",
            url: dataInject,
            // send data

            success: function(response){
                replaceContent($body, response);
                // $body.html(newBody);
            },
            error: function (request, status, error) {
                console.log(request.responseText);
                alert(error + ". Please refresh the page and try again.");
            }
        });
    });

    if (navigator.userAgent.match(/Mobi/)) {
        $('.mobile-wrapper').width('100%');
    }
    $('#grid-1-column').on('click', function(){
        $('.portfolio-gallery').find('.portfolio-item')
            .removeClass('grid-1-column grid-2-columns grid-3-columns')
            .addClass('grid-1-column');
        $('.options-new .small-button').removeClass('selected');
        $(this).addClass('selected');

        return false;
    });
    $('#grid-2-columns').on('click', function(){
        $('.portfolio-gallery').find('.portfolio-item')
            .removeClass('grid-1-column grid-2-columns grid-3-columns')
            .addClass('grid-2-columns');
        $('.options-new .small-button').removeClass('selected');
        $(this).addClass('selected');

        return false;
    });
    $('#grid-3-columns').on('click', function(){
        $('.portfolio-gallery').find('.portfolio-item')
            .removeClass('grid-1-column grid-2-columns grid-3-columns')
            .addClass('grid-3-columns');
        $('.options-new .small-button').removeClass('selected');
        $(this).addClass('selected');

        return false;
    });
    $('input:radio.radio-bullet', '.w-form').change( function(){
        var name = $(this).attr('name');
        $('input:radio[name="'+ name +'"]').each(function( index ) {
          $(this).prev('.radio-bullet-replacement').removeClass('checked');
        });
        if ($(this).is(':checked')) {
            $(this).prev('.radio-bullet-replacement').addClass('checked');
        }else{
            $(this).prev('.radio-bullet-replacement').removeClass('checked');
        }
    });
    $('input:checkbox.checkbox-input', '.w-form').change( function(){
        if ($(this).is(':checked')) {
            $(this).prev('.checkbox-handle').addClass('checked');
            $(this).next('.checkbox-label').addClass('checked');
        }else{
            $(this).prev('.checkbox-handle').removeClass('checked');
            $(this).next('.checkbox-label').removeClass('checked');
        }
    });
    // Loading Pages
    $('.loading-mask').addClass('stop-loading');
    $('[data-load="1"]').on('click',  function(e){
        $('.loading-mask').removeClass('stop-loading');
        e.preventDefault();
        var hrefPage = $(this).attr('href');
        setTimeout(function(){
            goToPage(hrefPage);
        },10);
        return false;
    });
    var goToPage = function(hrefPage){
        document.location = hrefPage;
    };

    var replaceContent = function($body, newContent){
        $body.html('');
        $body.html(newContent);        
    };

    window.onpopstate = function(e){
        $('.loading-mask').addClass('stop-loading');
    };

    $('.mood-btn').on('click', function(e) {
        var faceId = $(this).data('face-id');
        var date = new Date();
        var dateFormatted = date.toISOString().substring(0,10);
        var rating = {
            date:dateFormatted,
            score: faceId*20,
            faceID: faceId,
        };
        console.log(rating);
        $.ajax({
            method: "POST",
            url: '/api/setRating',
            data: JSON.stringify(rating),

            success: function(response){
                goToPage('/reflection1');
            },
            error: function (request, status, error) {
                console.log(request.responseText);
                alert(error + ". Please refresh the page and try again.");
            }
        });
    });

    $('#main-stack').on('click', '.bubble-block', function(e){
        $(this).toggleClass('active');
    });

    $('#main-stack').on('click', '.better-face ', function(e){
        $(this).addClass('active');
    });

});

