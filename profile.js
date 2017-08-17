<body>
Accounts.onCreateUser(function(options, user) {
    if (! options.profile) options.profile = {};
    options.profile.artist = true;
    options.profile.reputation = 100;
    options.profile.someObject = {a: [], b: {}};

    user.profile = options.profile;
    return user;
});
