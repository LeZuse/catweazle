Array.prototype.each  = function(func){	for (var i = 0; i < this.length; i++){		func(this[i], i);		}	}app.addons.push('Array.prototype.each');