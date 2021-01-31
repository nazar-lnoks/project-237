var icon = document.getElementById('userIcon');
var list = document.getElementById('profileList');

list.style.display = 'none';

icon.addEventListener('click', function(){
    if(list.style.display === 'none'){
        list.style.display = 'block';
    } else {
        list.style.display = 'none';
    }
})