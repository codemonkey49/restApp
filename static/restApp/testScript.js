function test()
{
    document.getElementById("demo").innerHTML = "sup, i hope this worked";
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
    var data=httpGet(url);
    document.getElementById("demo").innerHTML=data;
}
function updateScore(personPk,points,add)
{
    var url="http://nari.housing.wwu.edu/~smithe65/rest/score/"+personPk+"?points="+points+"&add="+add
    httpPost(url);    
}
function makeTable()
{
    var table= document.getElementById("scoreBoard");
    var row=table.inserRow("newRow");
    var cell1=row.insertCell(0);
    var cell2=row.insertCell(1);
    var cell3=row.insertCell(3);

    cell1.innerHTML="first cell";
    cell2.innerHTML="second cell";
    cell3.innerHTML="third cell";
}
function saveCanvas(){
    var dataURL=document.getElementById("myCanvas").toDataURL("image/png");
    document.getElementById("imageField").value=dataURL;
    $('#canvasForm').submit();
}

$(document).ready(function() {
    $("#tableBtn").click(function(event){
    alert("fixed it");
    });
});



