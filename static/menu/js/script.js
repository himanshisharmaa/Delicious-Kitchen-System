

function clickText(val_item){
    $('#search-input').val(val_item).submit;

    resultsBox.classList.add('not-visible');
}
var data={};
var text_add_summary='';
function updateQuantity(item_id, quantity) {

    // Update the data object with the new quantity
    item_name=document.getElementById('item_name_'+item_id).textContent;
    item_price=document.getElementById('item_price_'+item_id).textContent;
    item_image=document.getElementById('item_image_'+item_id).src;
    item_price=item_price.split('₹')[1];
    console.log(item_price[1])
    text_add_summary=`
        <tr data-item-id="${item_id}">
              <td>${item_name}</td>
              <td>${quantity}</td>
              <td>${item_price}</td>
            </tr>
    `


     if (Object.values(data).some(item => item.item_name === item_name)) {

        $('#order_body').find(`tr[data-item-id="${item_id}"]`).find('td:nth-child(2)').text(quantity);
    }  else {

        $('#order_body').append(text_add_summary);
    }
    data[item_id] = {'quantity':quantity,
            'item_name':item_name,
            'item_price':item_price,
            'item_image':item_image,
            };



    // Save the updated data to local storage
    localStorage.setItem('selectedItems', JSON.stringify(data));
    }
function decreaseQuantity(item_id) {
    var quantityInput = document.getElementById("quantity_div_"+item_id);
    var currentQuantity = parseInt(quantityInput.value);
    document.getElementById('add_cart_'+item_id).style.display='none';
    if (currentQuantity > 1) {
      quantityInput.value = currentQuantity - 1;
      updateQuantity(item_id,quantityInput.value );
    }
    else{
        document.getElementById('quantity_'+item_id).style.display='none';
        document.getElementById('add_cart_'+item_id).style.display='grid';
        document.getElementById('displayCart').style.display="none";

    }
//    data[item_id]= quantityInput.value
  }

  function increaseQuantity(item_id) {
    var quantityInput = document.getElementById("quantity_div_"+item_id);
    var currentQuantity = parseInt(quantityInput.value);
    
    quantityInput.value = currentQuantity + 1;
    updateQuantity(item_id, quantityInput.value);
//    data[item_id]= quantityInput.value
//    console.log(data)
  }
function add_to_cart(item_id){
   console.log(item_id);
  var menuDiv=document.getElementById('displayCart');
  var displayDiv=document.getElementById('addToCartText');
  var showDisplay=document.getElementById('showButton')
  if (showDisplay==null){

    hTag=document.createElement('h4');
    hTag.textContent="Your item has been added to cart!!!";
    hTag.style.textAlign = "center";
    hTag.style.color='white';

//
//    var divDisplay=document.createElement('button');
//
//    divDisplay.id="showButton";
//    divDisplay.type="button";
//    divDisplay.textContent="Proceed to CheckOut";
//    divDisplay.setAttribute('onclick','cartDetails();')
    menuDiv.style.display='block';
    displayDiv.style.display='block';

    $('#addToCartText').html(hTag);
//    menuDiv.append(divDisplay);
}
  var cart_num=document.getElementById("cartValue");
  console.log(cart_num);
  cart_num.textContent=parseInt(cart_num.textContent)+1;
  var cart=document.getElementById('add_cart_'+item_id);
  var quantity=document.getElementById('quantity_'+item_id);
  quantity.style.display="none";
  cart.style.display="none";
  if (quantity.style.display=="none"){
    cart.style.display="none";
    quantity.style.display="flex";
  }
//  data[item_id] = quantity.querySelector('input').value;
//  console.log("Data",document.getElementById('dataSelected'));
//  document.getElementById('dataSelected').value=data[item_id];
  updateQuantity(item_id,1);
}
function cartDetails(){
    // Redirect to the checkout page
    window.location.href = "/menu/cart/";

}

function setButtonClick(buttonName) {
        document.getElementById('closebutton').value = buttonName;
    }
$( function() {

    $( "#search-input" ).autocomplete({
      source:"search",
    });
  } );