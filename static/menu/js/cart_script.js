// Retrieve the data object from localStorage.
var data = JSON.parse(localStorage.getItem('selectedItems')) || {};

function normalizeItemImage(imageUrl) {
    if (!imageUrl) {
        return '';
    }

    try {
        var parsedUrl = new URL(imageUrl, window.location.origin);
        if (parsedUrl.hostname === 'localhost' || parsedUrl.hostname === '127.0.0.1') {
            return window.location.origin + parsedUrl.pathname;
        }
    } catch (error) {
        return imageUrl;
    }

    return imageUrl;
}

function getAmountFromText(selector) {
    return parseInt($(selector).text().replace(/[^0-9]/g, ''), 10) || 0;
}

function renderEmptyCart() {
    $('#products').html(`
        <div>
            <h2>Cart is Empty!!!</h2>
            <button class="btn" type="button"><a href="/menu/">Go Back</a></button>
        </div>
    `);
}

// Function to render items on the checkout page.
function renderCheckoutItems() {
    var checkoutItemsDiv = $('#products');
    checkoutItemsDiv.empty();

    var cart = '';
    var count = 0;
    var total_price = 0;

    $.each(data, function(item_id, itemData) {
        var quantity = parseInt(itemData.quantity, 10) || 0;
        var item_name = itemData.item_name;
        var item_price = parseInt(itemData.item_price, 10) || 0;
        var item_image = normalizeItemImage(itemData.item_image);

        itemData.item_image = item_image;
        count += quantity;
        total_price += quantity * item_price;

        cart += `
            <div id="product_${item_id}" class="product">
                <img src="${item_image}" alt="${item_name}">
                <div class="product-info">
                    <h3 class="product-name">${item_name}</h3>
                    <h4 class="product-price">Rs. ${item_price}</h4>
                    <p id="product_quantity_${item_id}" class="product-quantity">Qnt: ${quantity}</p>
                    <h4 id="product_price_${item_id}" class="product-offer">Total: Rs. ${item_price * quantity}</h4>
                    <button class="product-remove update-cart" type="button" onclick="removeDiv('${item_id}');">
                        <i class="fa fa-trash" aria-hidden="true"></i>
                        <span class="remove">Remove</span>
                    </button>
                </div>
            </div>
        `;
    });

    if (count === 0) {
        renderEmptyCart();
    } else {
        checkoutItemsDiv.html(cart);
    }

    localStorage.setItem('selectedItems', JSON.stringify(data));
    $("#totalItemPrice").text('Rs. ' + total_price);
    $("#cart_total").text(count);

    var totalCartPrice = total_price + 40 + 5 + 10;
    $("#totalPrice").text('Rs. ' + totalCartPrice);
    $('#hiddenPrice').val(totalCartPrice);
}

$(document).ready(function() {
    renderCheckoutItems();
});

function removeDiv(item_id) {
    var total_price = getAmountFromText("#totalItemPrice");
    var total_Cart_price = getAmountFromText("#totalPrice");
    var total_quantity = parseInt($("#cart_total").text(), 10) || 0;
    var removed_price = getAmountFromText("#product_price_" + item_id);
    var removed_quantity = parseInt($("#product_quantity_" + item_id).text().split(' ')[1], 10) || 0;

    total_quantity -= removed_quantity;
    total_price -= removed_price;
    total_Cart_price -= removed_price;
    $("#product_" + item_id).remove();

    delete data[item_id];
    localStorage.setItem('selectedItems', JSON.stringify(data));
    $("#totalItemPrice").text('Rs. ' + total_price);
    $("#totalPrice").text('Rs. ' + total_Cart_price);
    $("#cart_total").text(total_quantity);
    $('#hiddenPrice').val(total_Cart_price);

    if (total_quantity === 0) {
        renderEmptyCart();
    }
}

function changeAddress() {
    var addressForm = document.getElementById("addressForm");
    if (addressForm.style.display === "none") {
        addressForm.style.display = "block";
    } else {
        addressForm.style.display = "none";
    }
}

function saveAddress() {
    var newAddress = document.getElementById("newAddressInput").value;
    var currentAddress = document.getElementById("currentAddress");
    currentAddress.textContent = newAddress;

    var addressForm = document.getElementById("addressForm");
    addressForm.style.display = "none";
}
