"use strict";

function submit(){
    let fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let dob = document.getElementById("birthdate").value;
    console.log("Info:",fname,lname,dob);
    let J = {
        firstName: fname,
        lastName: lname,
        birthDate: dob,
    };
    fetch( "/updateprofile/.*",
        {   method: "POST",
            body: JSON.stringify(J)
        }
    ).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
        });
    }).catch( (err) => {
        console.log("Uh oh",err);
    })
}
