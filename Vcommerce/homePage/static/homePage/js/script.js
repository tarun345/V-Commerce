function voice_command(){
    window.open('voice_command', '_blank')
}

function openMenu(){
    document.querySelector(".sidebar").classList.add("open")
}

function closeMenu(){
    document.querySelector(".sidebar").classList.remove("open")
}

function searchProduct(){
    location.href='{% url"search_products" %}'
}

function addToCart(id){
    var productId = id 
    console.log('productId:', productId)
    console.log('user:', user)
    if(user=="AnonymousUser"){
        console.log("user not logged in")
    }
    else{
        console.log("user logged in")
    }
}