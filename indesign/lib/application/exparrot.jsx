Application.prototype.exparrot = function(data){	var output = "";	var conn = new Socket;		if (conn.open ("127.0.0.1:21569", 'utf-8')) {				conn.write (JSON.stringify(data) + '\r\n');		while (!conn.eof){			output += conn.read(1048576*6);			}		conn.close();		}			// return eval(output.replace(/^\{/, '({').replace(/}$/, '})'))		return output.replace(/^\{/, '({').replace(/}$/, '})')	}