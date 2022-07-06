

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:'+ productId, 'action:' + action);

        console.log('user: ' + user)
        if(user === 'AnonymousUser'){
            addCookieITem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }

    })

    function addCookieITem(productId, action){
        console.log('user not loggin')

        if(action == 'add'){
            if(cart[productId] == undefined){
                cart[productId] = {'quantity':1}
            }else{
                cart[productId]['quantity'] += 1
            }
        }

        if(action == 'remove'){
            cart[productId]['quantity'] -= 1

            if(cart[productId]['quantity'] <= 0){
                console.log('remove item')
                delete cart[productId]
            }
        }
        console.log(cart)

        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        location.reload()
    }


    function updateUserOrder(productId, action){
        console.log('User is logged in...')

        var url = 'update_item'

        fetch(url, {
            method: 'POST',
            headers: {
                'content-Type':'applicaion/json',
                'X-CSRFToken': csrftoken
            },
            body:JSON.stringify({'productId': productId, 'action': action})
        })
        .then((response)=>{
            return response.json()
        })

        .then((data)=>{
            console.log(data)
            location.reload()
        })
    }
}