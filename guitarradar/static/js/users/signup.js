
let buttonUsersSignup = $('#button_users_signup');
let labelPasswordsUsersSignup = $('#label_passwords_users_signup');
let labelPasswordLengthUsersSignup = $('#label_password_length_users_signup');


function checkPasswordLength() {
    let password = $('#id_signup-password').val();
    if (password.length < 8) {
        labelPasswordLengthUsersSignup.attr('style', 'color:red;');
        buttonUsersSignup.attr('disabled', 'disabled');
    } else {
        labelPasswordLengthUsersSignup.attr('style', 'color:red; display:none;');
        buttonUsersSignup.removeAttr('disabled');
    }
}


function checkForPasswordToMatch() {
    let password = $('#id_signup-password').val();
    let rePassword = $('#id_signup-re_password').val();
    if (password === rePassword) {
        labelPasswordsUsersSignup.attr('style', 'color:red; display:none;');
        buttonUsersSignup.removeAttr('disabled');
    } else {
        labelPasswordsUsersSignup.attr('style', 'color:red;');
        buttonUsersSignup.attr('disabled', 'disabled');
    }
}


function checkForButtonState() {
    let username = $('#id_signup-username').val();
    let email = $('#id_signup-email').val();
    let password = $('#id_signup-password').val();
    let rePassword = $('#id_signup-re_password').val();

    if (username != "" && email != "" && password != "" && rePassword != "" &&
        password === rePassword) {
        buttonUsersSignup.removeAttr('disabled');
    } else {
        buttonUsersSignup.attr('disabled', 'disabled');
    }
}


$('#id_signup-username').keyup(function(e) {
    checkForButtonState();
});

$('#id_signup-email').keyup(function(e) {
    checkForButtonState();
});

$('#id_signup-password').keyup(function(e) {
    checkForButtonState();
    checkForPasswordToMatch();
    checkPasswordLength();
});

$('#id_signup-re_password').keyup(function(e) {
    checkForButtonState();
    checkForPasswordToMatch();
    checkPasswordLength();
});
