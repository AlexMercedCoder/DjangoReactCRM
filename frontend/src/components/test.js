function apitest () {fetch('http://localhost:8000/api/actor/?format=json')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson));
  });}

  apitest ();