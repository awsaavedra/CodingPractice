/*
Make a function that looks through a list (first argument) 
and returns an array of all objects that have equivalent 
property values (second argument).
*/

function where(collection, source) {
  var arr = [];
  var len = collection.length;
	for( var i = 0; i < len; i++){
		if( collection[i].last == source.last){
			arr.push(collection[i]);
		}
	}
	return arr;
}

console.log(where([{ first: 'Romeo', last: 'Montague' }, 
{ first: 'Mercutio', last: null }, 
{ first: 'Tybalt', last: 'Capulet' }], { last: 'Capulet' }));
