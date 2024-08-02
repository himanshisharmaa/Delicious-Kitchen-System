
    // Retrieve the data object from localStorage
    var data = JSON.parse(localStorage.getItem('selectedItems')) || {};

    // Function to render items on the checkout page
    function renderCheckoutItems() {
        var checkoutItemsDiv = $('#products');
        // Clear any existing content
        checkoutItemsDiv.empty();
        var cart='';

        var count=0;
        var total_price=0;

        // Iterate over the items in the data object
        $.each(data, function(item_id, itemData) {
            var quantity = itemData.quantity;
            var item_name = itemData.item_name;
            var item_price = itemData.item_price;
            var item_image = itemData.item_image;
            // Create a new div element for each item
           count+=parseInt(quantity);
           total_price+= quantity*item_price
            console.log(count);
             cart+=`
                    <div id="product_${item_id}" class="product">

                      <img src=${item_image}>

                      <div class="product-info">

                        <h3 class="product-name">${item_name}</h3>

                        <h4  class="product-price">₹ ${item_price}</h4>
                        <p id="product_quantity_${item_id}" class="product-quantity">Qnt: ${quantity}</p>

                        <h4 id="product_price_${item_id}" class="product-offer">Total: ₹ ${item_price*quantity}</h4>
                        <button class="product-remove update-cart " type='button' onclick="removeDiv('${item_id}');">

                          <i class="fa fa-trash " aria-hidden="true"></i>
                          <span class="remove">Remove</span>
                       </button>



                      </div>

                    </div>
            `
            // Append the item div to the checkoutItemsDiv
            checkoutItemsDiv.html(cart);

        });

         $("#totalItemPrice").text( '₹ '+total_price);
        $("#cart_total").text(count);
        var totalCartPrice=(total_price+40+5+10);
        $("#totalPrice").text( '₹ '+totalCartPrice);
        $('#hiddenPrice').val(totalCartPrice);
    }


    // Call the renderCheckoutItems function when the page loads
    $(document).ready(function() {
        renderCheckoutItems();

    });
 function removeDiv(item_id){
    console.log(data);
        var total_price = parseInt($("#totalItemPrice").text().split('₹')[1]);
        var total_Cart_price = parseInt($("#totalPrice").text().split('₹')[1]);
        var total_quantity = parseInt($("#cart_total").text());
        var removed_price = parseInt($("#product_price_" + item_id).text().split('₹')[1]);
        var removed_quantity = parseInt($("#product_quantity_"+item_id).text().split(' ')[1]);
        console.log("quan"+total_quantity,removed_quantity);
        total_quantity -= removed_quantity;
        console.log(total_quantity);
        total_price -= removed_price;
        total_Cart_price-=removed_price;
        $("#product_"+item_id).remove();

        delete data[item_id];
        localStorage.setItem('selectedItems', JSON.stringify(data));
        $("#totalItemPrice").text('₹ ' + total_price);
        $("#totalPrice").text('₹ ' + total_Cart_price);
        $("#cart_total").text(total_quantity);
//        $('#hiddenPrice').val(total_Cart_price);
        var divEmpty='';
        if (total_quantity===0){
            divEmpty+=`
                    <div>
                        <h2>Cart is Empty!!!</h2>
                        <button class="btn" type="button"><a href="/menu/"> Go Back</a></button>
                    </div>
            `
           $('#products').html(divEmpty);
        }

    }

function changeAddress() {
    // Toggle visibility of address form
    var addressForm = document.getElementById("addressForm");
    if (addressForm.style.display === "none") {
        addressForm.style.display = "block";
    } else {
        addressForm.style.display = "none";
    }
}

function saveAddress() {
    // Get the new address input value
    var newAddress = document.getElementById("newAddressInput").value;

    // Update the current address text
    var currentAddress = document.getElementById("currentAddress");
    currentAddress.textContent = newAddress;

    // Hide the address form
    var addressForm = document.getElementById("addressForm");
    addressForm.style.display = "none";
}

