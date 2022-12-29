var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'https://aavpf6ktc3.execute-api.ap-south-1.amazonaws.com/test/getCount', true);

request.onload = function websiteVisits() {
  // Begin accessing JSON data here
  var data = this.response;
  console.log(data);
  document.getElementById('hh').innerHTML='Visits: '+data;

}

// Send request
request.send()