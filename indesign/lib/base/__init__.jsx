#include "json.jsx"


$.range =function(num){
	output = [];
	var i = 0;
	
	for(i; i < num; i++){
		output.push(i)
		}
	
	return output
	}
app.addons.push('$.range');	

 
Application.prototype.growl = function (msg){
    var shScript = '/usr/local/bin/growlnotify' + 
        " -m '" + msg + "'" +
        " -a '" + '/Volumes' + String(this.fullName).replace(/%20/g, '\ ') + "'" +
        " -t " + this.name

    if(arguments[1] == true){
        shScript += ' -s ';
        }

    var asScript = 'do shell script "' + shScript + '"';
    this.doScript (asScript, 1095978087);
    };


app.addons.push('Application.prototype.growl');	


Application.prototype.exparrot = function(data){
	var output = "";
	var conn = new Socket;
	
	if (conn.open ("127.0.0.1:21569", 'utf-8')) {
		
		conn.write (JSON.stringify(data) + '\r\n');
		while (!conn.eof){
			output += conn.read(1048576*6);
			}
		conn.close();
		}	
	
	// return eval(output.replace(/^\{/, '({').replace(/}$/, '})'))
	
	return output.replace(/^\{/, '({').replace(/}$/, '})')
	}
app.addons.push('Application.prototype.exparrot');

Error.prototype.report = function(description){
	var output = [];
	var msg = [
		[				description],
		['File: ',		(!this.fileName ? '???' : decodeURI(this.fileName))],
		['Line: ',		(this.line || '???')],
		['Name: ',		this.name],
		['Message: ',	this.message]
		];
	
	output = msg.map(function(line){ return line.join(': ')})
	
	
	
	return output.join('\n')
	}
app.addons.push('Error.prototype.report');