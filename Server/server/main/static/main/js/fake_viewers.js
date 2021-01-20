function updateFakeCurrentViewers(data, _, _) {
    $('.various-data').text(`Currently on this page: ${parseInt(data)} human(s)`);
}

let randomOrgFakeAjaxObject = {
    "type": "GET",
    "url": "http://www.random.org/integers/?num=1&min=1&max=10&col=5&base=10&format=plain&rnd=new",
    "success": updateFakeCurrentViewers
};