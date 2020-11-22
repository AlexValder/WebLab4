//
// File for cookie manipulation.
//

function setCookie(name, value) {

    let expDate = new Date();
    expDate.setTime(expDate.getTime() + (7*24*60*60*1000));


    let str = `${name}=${value};expires=${expDate.toUTCString()};samesite=lax;path=/`;
    document.cookie = str;
}

function deleteCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;`;
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}