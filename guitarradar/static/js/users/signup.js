
let buttonUsersSignup = $('#button_users_signup');
let labelPasswordsUsersSignup = $('#label_passwords_users_signup');
let labelPasswordLengthUsersSignup = $('#label_password_length_users_signup');
let labelUsernameLengthUsersSignup = $('#label_username_length_users_signup');
let username = $('#id_signup-username');
let email = $('#id_signup-email');
let password = $('#id_signup-password');
let rePassword = $('#id_signup-re_password');


function isPasswordLength() {
    if (password.val().length >= 8) {
        return true;
    } else {
        return false;
    }
}


function arePasswordsMatching() {
    if (password.val() === rePassword.val()) {
        return true;
    } else {
        return false;
    }
}


function areFieldsComplete() {
    if (username.val() != "" && email.val() != "" && password.val() != "" && rePassword.val() != "") {
        return true;
    } else {
        return false;
    }
}


function isUSernameLength() {
    if (username.val().length >= 3) {
        return true;
    } else {
        return false;
    }
}


function checkStates() {
    let fieldsComplete = areFieldsComplete();
    let passwordsMatch = arePasswordsMatching();
    let passwordsLength = isPasswordLength();
    let usernameLength = isUSernameLength();

    if (fieldsComplete && passwordsMatch && passwordsLength && usernameLength) {
        buttonUsersSignup.removeAttr('disabled');
    } else {
        buttonUsersSignup.attr('disabled', 'disabled');
    }

    if (passwordsMatch) {
        labelPasswordsUsersSignup.attr('style', 'color:red; display:none;');
    } else {
        labelPasswordsUsersSignup.attr('style', 'color:red;');
    }

    if (passwordsLength) {
        labelPasswordLengthUsersSignup.attr('style', 'color:red; display:none;');
    } else {
        labelPasswordLengthUsersSignup.attr('style', 'color:red;');
    }

    if (usernameLength) {
        labelUsernameLengthUsersSignup.attr('style', 'color:red; display:none;');
    } else {
        labelUsernameLengthUsersSignup.attr('style', 'color:red;');
    }
}


$('#id_signup-username').keyup(function(e) { checkStates(); });

$('#id_signup-email').keyup(function(e) { checkStates(); });

$('#id_signup-password').keyup(function(e) { checkStates(); });

$('#id_signup-re_password').keyup(function(e) { checkStates(); });
