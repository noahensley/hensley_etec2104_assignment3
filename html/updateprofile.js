"use strict";

function submit(){
    
let file = document.getElementById("ppic").files[0];

if(!file){
    console.log("No file!");
    return;
}
let R = new FileReader();
R.addEventListener("load", () => {
    let profilepic = btoa(R.result)
    let uname = document.getElementById("username").innerHTML;
    let fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let dob = document.getElementById("birthdate").value;
    // console.log("Info:",fname,lname,dob);
    let J = {
        userName: uname,
        firstName: fname,
        lastName: lname,
        birthDate: dob,
        pic: profilepic
    };
    fetch( "/updateprofile/.*",
        {   method: "POST",
            body: JSON.stringify(J)
        }
    ).then( (resp) => {
        resp.text().then( (J) => {
            console.log("Server said:",J);
            document.body.innerHTML = J
        });
    }).catch( (err) => {
        console.log("Uh oh",err);
    })
});
R.readAsBinaryString(file);
}
