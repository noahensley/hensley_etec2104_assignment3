"use strict";

function submit(){
    
let file = document.getElementById("ppic").files[0];
let pfp = document.getElementById("ppicinput");

if(!file){
    console.log("No file!");
    pfp.classList.add("error-input");
    return;
}
else
    pfp.classList.remove("error-input");

let R = new FileReader();
R.addEventListener("load", () => {

    let fNameInput, lNameInput, dobInput
    let profilepic, uname, fname, lname, dob;

    // ChatGPT also made these for me
    let namePatt = /^[a-zA-Z\s]+$/;
    let dobPatt = /^\d{4}-\d{2}-\d{2}$/;
    
    try {
        profilepic = btoa(R.result)

        uname = document.getElementById("username").innerHTML;
        fNameInput = document.getElementById("fname");
        fname = fNameInput.value;
        lNameInput = document.getElementById("lname");
        lname = lNameInput.value;
        dobInput = document.getElementById("birthdate");
        dob = dobInput.value;
    }
    catch (e) {
        console.log("Error recieving user input.", e)
    }

    // ChatGPT helped me with classList add/remove
    if (namePatt.test(fname)) {
        fNameInput.classList.remove("error-input");
        console.log("Valid first name.");
    } else {
        fNameInput.classList.add("error-input");
        console.log("Invalid first name.");
        return;
    }
    
    if (namePatt.test(lname)) {
        lNameInput.classList.remove("error-input")
        console.log("Valid last name.");
    } else {
        lNameInput.classList.add("error-input")
        console.log("Invalid last name.");
        return;
    }

    if (dobPatt.test(dob)) {
        dobInput.classList.remove("error-input")
        console.log("Valid DOB.");
    } else {
        dobInput.classList.add("error-input")
        console.log("Invalid DOB.");
        return;
    }

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
            // console.log("Server said:",J);
            document.body.innerHTML = J
        });
    }).catch( (err) => {
        console.log("Uh oh",err);
    })
});
R.readAsBinaryString(file);
}
