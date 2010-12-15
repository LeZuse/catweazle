(function(){

var a = {
        LOGGING: true,
        LOGGING_INFO: true,
        LOGGING_DEBUG: true,
        LOGGING_WARNING: true,
        LOGGING_ERROR: true,
        LOGGING_CRITICAL: true,



    menu: {    "n": {name: 'Maintenance menu',
            'c': ['check for updates', function(){ app.info('checking for updates ...') }], 
            'u': ['update database', 'update_database']}}
    }            
return a
}());