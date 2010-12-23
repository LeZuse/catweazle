// placeholder

function callback(event){
    var doc = event.target
    
    var print_preferences = doc.printPreferences
    
    
    for (i in print_preferences){
        
        try{
            app.info('%s: %s'.format(i, print_preferences[i]))
            }
        catch(e){}
        }
    }