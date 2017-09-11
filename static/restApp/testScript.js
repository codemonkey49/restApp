

function test()
{
    document.getElementByID("demo").innerHTML = "sup, i hope this worked";
}

function httpGet(url)
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open( "GET", url, false ); // false for synchronous request
    xmlhttp.send( null );
    return xmlhttp.responseText;
    //document.getElementById("demo").innerHTML = xmlHttp.responseText;
}
function httpPost(url)
{
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.open("PUT",url,false);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send();

}
function retrievePeople(instanceID)
{   
    url="http://nari.housing.wwu.edu/~smithe65/rest/people/"+instanceID;
    document.getElementById("demo").innerHTML=httpGet(url);
}
function updateScore(personPk,points,add)
{
    var url="http://nari.housing.wwu.edu/~smithe65/rest/score/"+personPk+"?points="+points+"&add="+add
    httpPost(url);    
}
