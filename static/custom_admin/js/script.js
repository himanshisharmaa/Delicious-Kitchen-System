var item_type=['Steamed Momos','Fried Momos','Malai Momos','Kurkure Momos','Dragon Momos',
'Schezwan Momos','Manchurian Momos','Tandoori Momos','Noodles','Appetizers',
'Delicious Mania','Fried Rice','Pasta','Soups','Classic Fries','Burgers',
'Chinese Rolls','Kathi Roll','Tandoori Roll','Tandoori Chaap','Tandoori Paneer',
'Tandoori Mushroom','Breads','Classic Shakes','Mocktails(coolers)','Cold Coffee','Desserts','Yebo Specials']


var options=document.getElementById('item_type')

for(let i =0;i<item_type.length;i++){
    var option = document.createElement('option');
    option.value = item_type[i];
    option.textContent = item_type[i];
    options.appendChild(option);
    }


