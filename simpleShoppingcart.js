// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

/* Create an array named products which you will use to add all of your product object literals that you create in the next step. */
const products = [];
/* Create 3 or more product objects using object literal notation 
   Each product should include five properties
   - name: name of product (string)
   - price: price of product (number)
   - quantity: quantity in cart should start at zero (number)
   - productId: unique id for the product (number)
   - image: picture of product (url string)
*/

let totalPaid = 20;
let cherry = {
  name :"Cherry",
  price : 5 , 
  quantity : 0,
  productId : 1,
  image :"cherry.jpg"

} ;
let orange = {
  name :"Orange",
  price : 7 , 
  quantity : 0,
  productId : 2,
  image :"orange.jpg"

} ;
let strawberry = {
  name :"Strawberry",
  price : 3 , 
  quantity : 0,
  productId : 3,
  image :"strawberry.jpg"

} ;

products.splice(0, 0, cherry , orange, strawberry);
/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/

/* Declare an empty array named cart to hold the items in the cart */
const cart = [];
/* Create a function named addProductToCart that takes in the product productId as an argument
  - addProductToCart should get the correct product based on the productId
  - addProductToCart should then increase the product's quantity
  - if the product is not already in the cart, add it to the cart
*/
function addProductToCart(productid){
    addedObject = indexing(productid);
    
    if (cart.includes(addedObject)){
        
        addedObject["quantity"] +=1;
                
     }
    else {
        cart.splice(products.indexOf(addedObject), 0,addedObject);
        addedObject["quantity"] +=1;
     }

    };


/* Create a function named increaseQuantity that takes in the productId as an argument
  - increaseQuantity should get the correct product based on the productId
  - increaseQuantity should then increase the product's quantity
*/
function increaseQuantity(productid){
    
    increasedObject = indexing(productid);
    increasedObject["quantity"] +=1
  };


/* Create a function named decreaseQuantity that takes in the productId as an argument
  - decreaseQuantity should get the correct product based on the productId
  - decreaseQuantity should decrease the quantity of the product
  - if the function decreases the quantity to 0, the product is removed from the cart
*/
function decreaseQuantity(productid){
    decreasedObject = indexing(productid);
    if(decreasedObject["quantity"] === 1){
        cart.splice(cart.indexOf(decreasedObject), 1);
        }
    else {
        decreasedObject["quantity"] -=1
        }
    };
  
   
  
function removeProductFromCart(productid){
    deletedObject = indexing(productid);
    deletedObject["quantity"] = 0;
    cart.splice(cart.indexOf(deletedObject), 1);
        
};
function indexing(productid){
    for (i = 0; i < products.length; i++){
        if (products[i]["productId"] === productid){
            return products[i];
        }
    };
};

function emptyCart(){
    
    for (i = 0; i < products.length; i++){
        if (cart.includes(products[i])){
            products[i]["quantity"] = 0 ;
            removeProductFromCart(products[i]["productId"]);
            
        }
    };
};

function cartTotal(){
    let cartTotal = 0 ;
    cart.forEach(function callback(value){ 
        
        
        
        cartTotal += value["price"] * value["quantity"];
        
    });
    return cartTotal ; 
};

function pay(amount){ 
    totalPaid += amount ; 
    return totalPaid - cartTotal() ; 
};














