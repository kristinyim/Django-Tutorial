var city;
function initialize() {
	$.get("http://ipinfo.io", function(response) {
    	console.log(response.city, response.country);
    	city = response.city;
    	document.getElementById("city").value = city;
	}, "jsonp");
}
function getData() {
document.getElementById("results").innerHTML="Loading...";
jQuery.ajax({
            url: "http://api.reimaginebanking.com/enterprise/merchants?key=1252b146fef896dd827f3fa7d59a4f31",
            type: "GET",

            contentType: 'application/json; charset=utf-8',
            success: function(resultData) {
                //here is your json.
                  // process it
                  document.getElementById("results").innerHTML="";
                  console.log(resultData);
				//var json = { items: ['item 1', 'item 2', 'item 3'] };
				console.log(resultData.results);
				$(resultData.results).each(function(index, item) {
					//var obj = jQuery.parseJSON(item.address);
					console.log(item.address.city);
					if(item.address.city==city && item.name.includes(document.getElementById("name").value) && item.address["street name"] != undefined) {
						//ul.append(
        					//$(document.getElementById("results").appendChild("hi");
        					//document.createElement('li').text(item.name))
    					//);
    					var myDiv = document.getElementById("results");
    					var aTag = document.createElement("a");
    					//aTag.setAttribute('href', "yourlink.html");
    					aTag.setAttribute('style', "color:white");
    					aTag.setAttribute('onmouseover', 'this.style.textDecoration = "underline"');
    					aTag.setAttribute('onmouseout', 'this.style.textDecoration = "none"');
    					var param = 'processNewBusinessPage(\''+item.name+'\', \''+item.address.city+'\', \''+item.address.state+'\', \''+item.address["street name"]+'\', \''+item.address["street number"]+'\', \''+item.address.zip+'\')';
    					//console.log(item.address.street_name);
    					aTag.setAttribute('onclick', param);
    					aTag.innerHTML = "<li class = 'list-unstyled'>"+item.name+"</li>";
    					//element.appendChild(document.createTextNode(item.name));

    					myDiv.appendChild(aTag);
					}
    				
			});

            },
            error : function(jqXHR, textStatus, errorThrown) {
            },

            timeout: 120000,
        });
}

function processNewBusinessPage(name, city, state, street_name, street_number, zip) {
	alert("Printing: "+name+city+state+street_name+street_number+zip);
}
