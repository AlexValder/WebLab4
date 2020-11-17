//
// File for page look manipulation.
//

function setTheme(theme) {
    $('link[rel="stylesheet"]').attr('href', `css/${theme}-theme.css`);
}

let themeSwitcher = () => {
    if ($('link[rel="stylesheet"]').attr('href') === 'css/light-theme.css') {
        setTheme('dark');
        setCookie('theme', 'dark');
    } else {
        setTheme('light');
        setCookie('theme', 'light');
    }
};

let themeOnLoad = () => {
    if (getCookie('theme') === 'dark') {
        setTheme('dark');
    } else {
        setCookie('theme', 'light');
        setTheme('light');
    }
}