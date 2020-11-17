//
// File for page look manipulation.
//

function setTheme(theme) {
    $('link[rel="stylesheet"]').attr('href', `css/${theme}-theme.css`);
}