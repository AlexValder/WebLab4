

let tab; // заголовок вкладки
let tabContent; // блок содержащий контент вкладки

function hideTabsContent(index) {
    for (let j = index; j < tabContent.length; ++j) {
        $(tabContent[j]).removeClass('show').addClass("hide");
        $(tab[j]).removeClass('active');
    }
}

function showTabsContent(index){
    if ($(tabContent[index]).hasClass('hide')) {
        hideTabsContent(0);
        $(tab[index]).addClass('active');
        $(tabContent[index]).removeClass('hide').addClass('show');
    }
}

